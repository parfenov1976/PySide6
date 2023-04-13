"""
Пример использования много поточности для решения проблемы с "зависанием" при длительном выполнении инструкций.
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков
Также понадобиться класс декоратора Slot
"""
import sys
import time

from PySide6.QtWidgets import (QApplication,
                               QVBoxLayout,
                               QLabel,
                               QMainWindow,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool

"""
Модуль time с библиотеками для работы со временем.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета ярлыка QLabel, класса виджета
кнопки QPushButton, класса базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса таймера для измерения времени QTimer, класс контейнера для
исполняемого кода QRunnable, класс менеджера потоков QThreadPool, класс декоратора Slot.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class Worker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода
    """

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код, который необходимо выполнить помещаем в метод с именем run()
        """
        print('Thread start')
        time.sleep(5)
        print('Thread complete')


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self):
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса

        self.threadpool = QThreadPool()  # создание экземпляра класса менеджера потоков
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()}')  # запрос и вывод
        # максимального количества потоков

        self.counter = 0  # создание аттрибута счетчика с присвоением начального значения
        layout = QVBoxLayout()  # создание экземпляра слоев для размещения виджетов
        self.label = QLabel('Start')  # создание ярлыка с надписью
        button = QPushButton('DANGER!!!')  # создание кнопки с надписью
        button.pressed.connect(self.oh_no)  # создание сигнала с привязкой метода ресивера
        layout.addWidget(self.label)  # размещение ярлыка в слое для виджетов
        layout.addWidget(button)  # размещение кнопки в слое для виджетов
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(container)  # размещение контейнера со слоями в главном окне приложения
        self.timer = QTimer()  # создание экземпляра класса таймера
        self.timer.setInterval(1000)  # установка интервала таймера в милли секундах
        self.timer.timeout.connect(self.recurring_timer)  # создание сигнала на истечение интервала
        # с привязкой ресивера
        self.timer.start()  # запуск таймера, по истечении интервала таймер перезапускается автоматически

    def oh_no(self) -> None:
        """
        Метод ресивер (слот) на нажатие кнопки
        :return: None
        """
        worker = Worker()
        self.threadpool.start(worker)

    def recurring_timer(self) -> None:
        """
        Метод ресивер (слот) на истечение таймера
        :return:
        """
        self.counter += 1
        self.label.setText(f'Counter: {self.counter}')


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
