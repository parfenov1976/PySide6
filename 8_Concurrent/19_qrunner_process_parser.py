"""
Пример использования много поточности при запуске внешнего процесса.
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков.
Также понадобиться класс декоратора Slot и класс сигнала Signal
В данном примере внешний процесс запускается с помощью встроенной библиотеки python subprocess.
Добавлен парсер для перехвата и обработки результатов.
"""
import subprocess
import sys
import re

from PySide6.QtWidgets import (QApplication,
                               QPlainTextEdit,
                               QVBoxLayout,
                               QMainWindow,
                               QPushButton,
                               QWidget,
                               QProgressBar
                               )
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject

"""
Модуль re для работы с регулярными выражениями.
Модуль subprocess для работы с внешними процессами.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс виджета многострочного редактируемого текстового поля QLineEdit, класс базового виджета QWidget,
класс виджета индикатора прогресса QProgressBar.
Импорт из модуля PySide6.QtCore класс контейнера для исполняемого кода QRunnable,
класс менеджера потоков QThreadPool, класс декоратора Slot, класс сигнала Signal, класс базового объекта QObject
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

progress_re = re.compile('Total complete: (\d+)%')  # регулярное выражение для формирования вывода прогресса выполнения


def simple_percent_parser(output: str) -> int:
    """
    Функция для извлечения из строк результата
    :param output: str - строка с выводом из внешнего процесса
    :return: int - процент выполнения задачи внешним процессом
    """
    m = progress_re.search(output)  # извлечение из строки процента выполнения
    if m:  # проверка наличия процента выполнения
        pc_complete = m.group(1)  # передача процента выполнения из match объекта в переменную
        return int(pc_complete)  # преобразование текста в целое число и возврат его из функции


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    Перечень поддерживаемых сигналов:
    result - словарь с результатом работы кода
    progress - процент выполнения задачи
    """
    result = Signal(str)
    progress = Signal(int)


class SubProcessWorker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода внешнего процесса.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами c
    результатами работы.
    """

    def __init__(self, command, parser=None) -> None:
        """
        Конструктор рабочего потока.
        :param command: команда для запуска во внешнем процессе
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.signals = WorkerSignals()  # создание экземпляра класса сигналов рабочего потока
        self.command = command  # сохранение команд для исполнения в аттрибуте рабочего потока
        self.parser = parser  # сохранение ссылки на функцию обработчик
        # результатов работы внешнего процесса

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код рабочего потока для запуска функции с передачей ей аргументов
        """
        result = []  # создание списка для результатов
        with subprocess.Popen(  # запуск подпроцесса с Popen позволяет получить доступ к его исходящему потоку данных
                self.command,
                bufsize=1,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # использование стандартного вывода для вывода стандартных ошибок
                universal_newlines=True,
        ) as proc:
            while proc.poll() is None:
                data = proc.stdout.readline()  # читаем строку из внешнего процесса или ожидаем ее
                result.append(data)  # добавляем прочтенную строку в список с результатами
                if self.parser:  # передача собранных данных парсеру
                    value = self.parser(data)
                    if value:
                        self.signals.progress.emit(value)  # передача данных для сигнала о прогрессе выполнения
        output = "".join(result)  # сборка списка результатов в строку
        self.signals.result.emit(output)  # передача результатов работы внешнего процесса
        # объекту сигналов рабочего потока


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        layout = QVBoxLayout()  # создание экземпляра слоев для размещения виджетов
        self.text = QPlainTextEdit()  # создание экземпляра виджета многострочного редактируемого текстового поля
        self.progress = QProgressBar()  # создание экземпляра класса виджета индикатора прогресса
        self.progress.setRange(0, 100)  # установка диапазона отображения
        self.progress.setValue(0)  # установка начального значения
        btn_run = QPushButton('Execute!')  # создание кнопки с надписью
        btn_run.clicked.connect(self.start)  # создание сигнала на нажатие кнопки с привязкой метода ресивера
        layout.addWidget(self.text)  # размещение текстового поля в слое
        layout.addWidget(self.progress)  # размещение индикатора прогресса в слое для виджетов
        layout.addWidget(btn_run)  # размещение кнопки в слое для виджетов
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя для виджетов
        self.setCentralWidget(container)  # размещение контейнера в главном окне приложения
        self.threadpool = QThreadPool()  # создание экземпляра класса менеджера потоков
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()}')
        # вывод максимального количества доступных потоков

    def start(self) -> None:
        """
        Метод ресивер (слот) на нажатие кнопки запуска выполнения внешнего процесса
        :return: None
        """
        self.runner = SubProcessWorker('python dummy_script.py', parser=simple_percent_parser)
        # создание экземпляра рабочего потока для запуска кода внешнего процесса dummy_script.py с передачей ссылки
        # на функцию обработчик результатов работы внешнего процесса simple_percent_parser
        self.runner.signals.result.connect(self.result)  # создание сигнала на получение результата с привязкой ресивера
        self.runner.signals.progress.connect(self.progress.setValue)  # установка процента выполнения
        self.threadpool.start(self.runner)  # запуск рабочего потока

    def result(self, s: str) -> None:
        """
        Метод ресивер (слот) на завершение выполнения кода внешнего процесса
        :return: None
        """
        self.text.appendPlainText(s)


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла событий приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # установка видимости главного окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
