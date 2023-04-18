"""
Пример использования много поточности для обеспечения работы полосы индикатора прогресса
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков
Также понадобиться класс декоратора Slot и класс сигнала Signal
"""
import sys
import time

from PySide6.QtWidgets import (QApplication,
                               QVBoxLayout,
                               QLabel,
                               QMainWindow,
                               QProgressBar,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool, Signal, QObject

"""
Модуль time с библиотеками для работы со временем.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета ярлыка QLabel, класса виджета
кнопки QPushButton, класса индикатора прогресса QProgressBar, класса базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса таймера для измерения времени QTimer, класс контейнера для
исполняемого кода QRunnable, класс менеджера потоков QThreadPool, класс декоратора Slot,
класс сигнала Signal, класс базового объекта QObject.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    progress индикатор прогресса от 0 до 100
    """
    progress = Signal(int)


class Worker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами
    и результатов работы.
    """

    def __init__(self, iterations: int = 5) -> None:
        """
        Конструктор рабочего потока
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.signals = WorkerSignals()  # создаем экземпляр класса сигналов

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код, который необходимо выполнить помещаем в метод с именем run()
        """
        total_n = 1000  # установка количества интервалов для эмуляции какого либо процесса
        for n in range(total_n):  # запуск цикла определения степени выполнения
            progress_pc = int(100 * float(n + 1) / total_n)  # определение процента выполнения задания
            self.signals.progress.emit(progress_pc)  # передача определенного процента сигналу
            time.sleep(0.01)  # установка задержки для эмуляции нагрузки

class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса

        self.threadpool = QThreadPool()  # создание экземпляра класса менеджера потоков
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()}')  # запрос и вывод
        # максимального количества потоков

        layout = QVBoxLayout()  # создание экземпляра слоев для размещения виджетов
        self.progress = QProgressBar()  # создание экземпляра класса индикатора прогресса
        button = QPushButton('МАХМУД, ПОДЖИГАЙ!!!')  # создание кнопки с надписью
        button.pressed.connect(self.execute)  # создание сигнала с привязкой метода ресивера
        layout.addWidget(self.progress)  # размещение индикатора прогресса в слое для виджетов
        layout.addWidget(button)  # размещение кнопки в слое для виджетов
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(container)  # размещение контейнера со слоями в главном окне приложения


    def execute(self) -> None:
        """
        Метод ресивер (слот), запускающий эмуляцию выполнения кода по нажатию кнопки
        :return: None
        """
        worker = Worker()  # создаем экземпляр рабочего потока
        worker.signals.progress.connect(self.update_progress)  # создание сигнала на изменение
        # прогресса выполнения с привязкой метода ресивера
        self.threadpool.start(worker)  # запуск рабочего потока на исполнение

    def update_progress(self, progress: int) -> None:
        """
        Метод ресивер (слот) обновляющий индикатор прогресс по сигналу рабочего потока
        :param progress:
        :return:
        """
        self.progress.setValue(progress)  # обновление значения индикатора прогресса


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
