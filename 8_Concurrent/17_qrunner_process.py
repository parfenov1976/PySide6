"""
Пример использования много поточности при запуске внешнего процесса.
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков.
Также понадобиться класс декоратора Slot и класс сигнала Signal
В данном примере внешний процесс запускается с помощью встроенной библиотеки python subprocess.
"""
import subprocess
import sys
import time
import traceback
import uuid
from collections import namedtuple


from PySide6.QtWidgets import (QApplication,
                               QPlainTextEdit,
                               QVBoxLayout,
                               QMainWindow,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject, QTimer, Qt

"""
Модуль subprocess для работы с внешними процессами
Модуль uuid библиотека для создания уникальных идентификаторов
Библиотека namedtuple из модуля collections для создания подкласса кортежа с именами (по аналогии со словарями)
Модуль time для работы со временем.
Модуль traceback для работы с трассировками стека программы.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс виджета многострочного редактируемого текстового поля QPlainTextEdit, класс базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса таймера для измерения времени QTimer, класс контейнера для
исполняемого кода QRunnable, класс менеджера потоков QThreadPool, класс декоратора Slot,
класс сигнала Signal, класс базового объекта QObject, класс таймера для измерения времени QTimer.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    Перечень поддерживаемых сигналов:
    finished - без данных, сигнал о завершении исполнения кода функции
    result - текстовая строка с результатом работы кода
    """
    finished = Signal()
    result = Signal(str)


class SubProcessWorker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода внешнего процесса.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами c
    результатами работы.
    """

    def __init__(self, command) -> None:
        """
        Конструктор рабочего потока.
        :param command: команда для запуска во внешнем процессе
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.signals = WorkerSignals()  # создание экземпляра класса сигналов рабочего потока
        self.command = command  # сохранение команд для исполнения в аттрибуте рабочего потока

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код рабочего потока для запуска функции с передачей ей аргументов
        """
        output = subprocess.getoutput(self.command)  # запуск команд внешнего процесса и сохранение
        # результатов в переменной
        self.signals.result.emit(output)  # передача результатов работы внешнего процесса
        # объекту сигналов рабочего потока
        self.signals.finished.emit()  # сообщение о завершении работы внешнего процесса
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
        self.text = QPlainTextEdit()  # создание экземпляра редактируемого многострочного текстового поля
        btn_run = QPushButton('Execute!')  # создание кнопки с надписью
        btn_run.clicked.connect(self.start)  # создание сигнала на нажатие кнопки с привязкой метода ресивера
        layout.addWidget(self.text)  # размещение текстового поля в слое для виджетов
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
        self.runner = SubProcessWorker('python dummy_script.py')  # создание экземпляра рабочего потока для
        # запуска кода внешнего процесса
        self.runner.signals.result.connect(self.result)  # создание сигнала на получение результата с привязкой ресивера
        self.threadpool.start(self.runner)  # запуск рабочего потока

    def result(self, s: str) -> None:
        """
        Метод ресивер (слот) на завершение выполнения кода внешнего процесса
        :return: None
        """
        self.text.appendPlainText(s)  # добавление результатов работы кода внешнего процесса
        # в многострочное текстовое поле


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