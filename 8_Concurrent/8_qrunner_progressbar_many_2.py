"""
Пример использования много поточности для обеспечения работы полосы индикатора прогресса
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков
Также понадобиться класс декоратора Slot и класс сигнала Signal
В данном примере рассмотрено отслеживание прогресса нескольких рабочих потоков
и отображение его на одном индикаторе прогресса. Устранено проблема рывков
индикатора по мере завершения отдельных рабочих потоков.
"""
import sys
import time
import random
import uuid

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
Модуль uuid библиотека для создания уникальных идентификаторов.
Модуль random библиотек для генерации случайностей.
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
    progress = Signal(str, int)  # создание сигнала для передачи данных о прогрессе
    finished = Signal(str)  # создание сигнала для отслеживания завершения рабочего потока


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
        self.job_id = uuid.uuid4().hex  # генерация случайного уникального идентификатора
        self.signals = WorkerSignals()  # создаем экземпляр класса сигналов

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код, который необходимо выполнить помещаем в метод с именем run()
        """
        total_n = 1000  # установка количества интервалов для эмуляции какого либо процесса
        delay = random.random() / 100  # генерация случайной величины задержки
        for n in range(total_n):  # запуск цикла определения степени выполнения
            progress_pc = int(100 * float(n + 1) / total_n)  # определение процента выполнения задания
            self.signals.progress.emit(self.job_id, progress_pc)  # передача сигналу идентификатора
            # рабочего потока и процента его завершения
            time.sleep(delay)  # установка задержки для эмуляции нагрузки
        self.signals.finished.emit(self.job_id)  # передача сигнала о завершении рабочего потока и его идентификатора


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
        self.status = QLabel('0 workers')  # создание экземпляра ярлыка для индикации количества
        # активных рабочих потоков
        layout.addWidget(self.progress)  # размещение индикатора прогресса в слое для виджетов
        layout.addWidget(button)  # размещение кнопки в слое для виджетов
        layout.addWidget(self.status)  # размещение индикатора количества рабочих потоков
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя с виджетами
        self.worker_progress = {}  # создание словаря для хранения данных по рабочим потокам
        self.setCentralWidget(container)  # размещение контейнера со слоями в главном окне приложения
        self.timer = QTimer()  # создание экземпляра таймера
        self.timer.setInterval(100)  # установка длительности интервала в миллисекундах
        self.timer.timeout.connect(self.refresh_progress)  # создание сигнала на истечение интервала таймера
        self.timer.start()  # запуска таймера

    def execute(self) -> None:
        """
        Метод ресивер (слот), запускающий эмуляцию выполнения кода по нажатию кнопки
        :return: None
        """
        worker = Worker()  # создаем экземпляр рабочего потока
        worker.signals.progress.connect(self.update_progress)  # создание сигнала на изменение
        # прогресса выполнения с привязкой метода ресивера
        worker.signals.finished.connect(self.cleanup)  # создание сигнала на завершение рабочего потока
        # и привязка метода ресивера
        self.threadpool.start(worker)  # запуск рабочего потока на исполнение

    def cleanup(self, job_id: uuid) -> None:
        """
        Метода ресивер (слот) для удаления из словаря рабочих
        потоков завершенного рабочего потока
        :param job_id: uuid - уникальный идентификатор рабочего потока
        :return: None
        """
        if all(v == 100 for v in self.worker_progress.values()):  # проверка завершения всех рабочих потоков из словаря
            self.worker_progress.clear()  # если все рабочие потоки завершены словарь очищается
            self.refresh_progress()  # вызов метода обновления индикатора прогресса
    def update_progress(self, job_id: uuid, progress: int) -> None:
        """
        Метод ресивер (слот) обновляющий индикатор прогресс по сигналу рабочего потока
        :param progress: int значение прогресса конкретного рабочего потока
        :param job_id: uuid идентификатор рабочего потока
        :return:
        """
        self.worker_progress[job_id] = progress  # обновление процента выполнения конкретного рабочего потока

    def calculate_progress(self) -> int:
        """
        Метод для расчета прогресса по всем рабочи потокам
        :return:
        """
        if not self.worker_progress:  # проверка пустоты словаря рабочих потоков
            return 0
        return sum(v for v in self.worker_progress.values()) / len(self.worker_progress)
        # подсчет среднего значения прогресса для всех потоков

    def refresh_progress(self) -> None:
        """
        Метод ресивер (слот),
        :return:
        """
        progress = self.calculate_progress()  # обновление прогресса по всем рабочим потокам
        print(self.worker_progress)
        self.progress.setValue(progress)  # установка значения выполнения на индикаторе прогресса
        self.status.setText(f'{len(self.worker_progress)} рабочих потоков')
        # обновление индикатора количества запущенных рабочих потоков


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
