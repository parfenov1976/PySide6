"""
Пример использований встроенного в PySide6 класса QProcess для запуска внешних процессов.
Для этого используем класс из модуля PySide6.QtCore:
QProcess - класс для запуска внешних процессов
"""
import sys
import re

from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPlainTextEdit,
                               QProgressBar,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )

from PySide6.QtCore import QProcess

"""
Модуль re для работы с регулярными выражениями.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс виджета индикатора прогресса QProgressBar, класс виджета многострочного редактируемого
текстового поля QPlainTextEdit, класс базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса для запуска внешних процессов и управления ими QProcess.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

STATES = {
    QProcess.NotRunning: "Not running",
    QProcess.Starting: "Starting...",
    QProcess.Running: "Running..."
}

progress_re = re.compile('Total complete: (\d+)%')


def simple_percent_parser(output: str) -> int:
    """
    Функция для извлечения значения процента выполнения из строки статуса
    :param output:
    """
    m = progress_re.search(output)  # поиск в строке статуса процента выполнения
    if m:
        pc_complete = m.group(1)  # извлечение процента из матч объекта и запись в переменную
        return int(pc_complete)  # возврат процента выполнения в виде целого чиста


def extract_vars(l):
    """
    Функция, извлекающая из строки результатов равенства и преобразующая их в элементы словаря
    и формирующая словарь результатов работы внешнего процесса
    :param l: строка результатов работы внешнего процесса
    """
    data = {}  # создание словаря для результатов
    for s in l.split():  # рзбиение строки проход по результатам разбиения
        if '=' in s:  # проверка, что подстрока является равенством
            name, value = s.split('=')  # разбиение равенства на подстроки
            data[name] = value  # запись ключа и значения в словарь результатов
    return data


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.p = None  # создание аттрибута для хранения ссылки на внешний процесс
        layout = QVBoxLayout()  # создание экземпляра класса слоев для виджетов
        self.text = QPlainTextEdit()  # создание экземпляра класса многострочного
        # редактируемого текстового поля.
        self.progress = QProgressBar()  # создание экземпляра виджета индикатора прогресса

        btn_run = QPushButton('Execut')  # создание кнопки с надписью
        btn_run.clicked.connect(self.start)  # создание сигнала на нажатие кнопки запуска процесса
        # с привязкой ресивера
        layout.addWidget(self.text)  # добавление виджета на слой
        layout.addWidget(self.progress)  # добавление виджета на слой
        layout.addWidget(btn_run)  # добавление виджета на слой
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение слоя в контейнера
        self.setCentralWidget(container)  # размещение контейнера в главном окне приложения

    def start(self) -> None:
        """
        Метода, запускающий процесс
        """
        if self.p is not None:
            return
        self.p = QProcess()  # создание экземпляра класса для запуска внешних процессов
        self.p.readyReadStandardOutput.connect(self.handle_stdout)  # создание сигнала с выводом
        # с привязкой метода ресивера
        self.p.readyReadStandardError.connect(self.handle_stderr)  # создание сигнала об ошибке
        # с привязкой метода ресивера
        self.p.stateChanged.connect(self.handle_state)  # создание сигнала на изменение состояния
        # процесса с привязкой метода ресивра для обработки
        self.p.finished.connect(self.cleanup)  # создание сигнала на завершение процесса и привязка метода очистки
        self.p.start('python', ['dummy_script.py'])  # запуск внешнего процесса

    def handle_stderr(self) -> None:
        """
        Метод ресивер - обработчик стандартных ошибок
        """
        result = bytes(self.p.readAllStandardError()).decode("utf8")  # декодирование вывода с ошибкой из процесса
        progress = simple_percent_parser(result)  # извлечение из сообщения об ошибке процента выполнения
        self.progress.setValue(progress)  # установка значения на индикаторе прогресса выполнения

    def handle_stdout(self) -> None:
        """
        Метод ресивер - обработчик стандартного вывода из процесса
        """
        result = bytes(self.p.readAllStandardOutput()).decode("utf8")  # декодирование строки вывода из процесса
        data = extract_vars(result)  # извлечение результатов работ из строки вывода
        self.text.appendPlainText(str(data))  # запись результатов в тестовое поле

    def handle_state(self, state) -> None:
        """
        Метод ресивер - обработчик вывода состояния процесса
        """
        self.statusBar().showMessage(STATES[state])  # установка статуса процесса в стоке
        # состояния главного окна приложения

    def cleanup(self) -> None:
        """
        Метод ресивер - обработчик сигнала завершения выполнения процесса
        """
        self.p = None  # сброс аттрибута состояния


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла событий приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window.show()  # установка видимости главного окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
