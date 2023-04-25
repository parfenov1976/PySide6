"""
Пример использования много поточности для обеспечения работы полосы индикатора прогресса
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков
Также понадобиться класс декоратора Slot и класс сигнала Signal
В данном файле рассмотрен пример использованию отдельного рабочего потока для обращения
к удаленным серверам и сохранения исходящего с серверов дампа данных в системе логирования.
"""
import sys
import requests

from PySide6.QtWidgets import (QApplication,
                               QLabel,
                               QVBoxLayout,
                               QMainWindow,
                               QPlainTextEdit,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject, QTimer

"""
Модуль request для работы с запросам по интернету.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс однострочного текстового поля ярлыка QLabel, класс виджета многострочного редактируемого,
текстового поля QPlainTextEdit класса базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса таймера для измерения времени QTimer, класс контейнера для
исполняемого кода QRunnable, класс менеджера потоков QThreadPool, класс декоратора Slot,
класс сигнала Signal, класс базового объекта QObject, класс таймера для измерения времени QTimer. 
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    data - кортеж данных вида (идентификатор, данные)
    """
    data = Signal(tuple)


class Worker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами
    и результатов работы.
    """

    def __init__(self, id: int, url: str) -> None:
        """
        Конструктор рабочего потока.
        :param id: Идентификатор рабочего потока.
        :param url: str - Строка запроса к удаленному серверу.
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.id = id  # создание аттрибута для хранения идентификатора рабочего потока
        self.url = url  # создание аттрибута для хранения запроса
        self.signals = WorkerSignals()  # создание экземпляра класса сигналов рабочего потока

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код, который необходимо выполнить помещаем в метод с именем run()
        """
        r = requests.get(self.url)  # отправка запроса на удаленные сервер и сохранение ответа в переменную r
        for line in r.text.splitlines():  # извлечение из ответа сервера отдельных строк
            self.signals.data.emit((self.id, line))  # передача кортежа данных объекту сигналов рабочего потока


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.urls = [  # сохранение списка запросов в аттрибуте главного окна приложения
            "https://www.pythonguis.com/",
            "https://www.mfitzp.com/",
            "https://www.google.com",
            "https://www.udemy.com/create-simple-gui-applicationswith-python-and-qt / ",
        ]
        layout = QVBoxLayout()  # создание экземпляра слоев для размещения виджетов
        self.text = QPlainTextEdit()  # создание экземпляра класса виджета многострочного
        # редактируемого текстового поля
        self.text.setReadOnly(True)  # установка запрета на запись в текстовое поле
        button = QPushButton('Послать запрос')  # создание кнопки с надписью
        button.pressed.connect(self.execute)  # создание сигнала на нажатие кнопки с привязкой метода ресивера
        layout.addWidget(self.text)  # размещение текстового поля в слое для виджетов
        layout.addWidget(button)  # размещение кнопки в слое для виджетов
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя для виджетов
        self.setCentralWidget(container)  # размещение контейнера в главном окне приложения
        self.threadpool = QThreadPool()  # создание экземпляра класса менеджера потоков
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()}')
        # вывод максимального количества доступных потоков

    def execute(self) -> None:
        """
        Метод ресивер (слот) на нажатие кнопки, запускающий рабочие потоки,
        передающие запросы удаленным серверам и собирающим данные их ответов
        :return: None
        """
        for n, url in enumerate(self.urls):  # цикл создания и запуска рабочих потоков
            worker = Worker(n, url)  # создание экземпляра рабочего потока
            worker.signals.data.connect(self.display_output)  # создание сигнала на получение ответа
            # от сервера и привязка метода ресивера для отображения ответа сервера
            self.threadpool.start(worker)  # запуска рабочего потока на исполнение

    def display_output(self, data: tuple) -> None:
        """
        Метод ресивер (слот) принимающий сигнал о поступлении ответа от сервера и выводящий его в текстовое поле
        :param data: tuple - данные ответа от сервера для отображения
        :return: None
        """
        id, s = data
        self.text.appendPlainText(f'WORKER {id}: {s}')


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
