"""
Пример использования много поточности при запуске любых функций,
передаваемых рабочему потоку в качестве аргумента.
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков.
Также понадобиться класс декоратора Slot и класс сигнала Signal
В данном примере для функции добавлена возможность получать
объекты сигналов рабочего потока и передавать им данные в процессе
своего выполнения (callback).
"""
import sys
import time
import traceback

from PySide6.QtWidgets import (QApplication,
                               QLabel,
                               QVBoxLayout,
                               QMainWindow,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject, QTimer

"""
Модуль time для работы со временем.
Модуль traceback для работы с трассировками стека программы.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс однострочного текстового поля ярлыка QLabel, класса базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса таймера для измерения времени QTimer, класс контейнера для
исполняемого кода QRunnable, класс менеджера потоков QThreadPool, класс декоратора Slot,
класс сигнала Signal, класс базового объекта QObject, класс таймера для измерения времени QTimer. 
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


# def execute_this_fn(signals: Signal) -> str:
#     """
#     Функция, которую нужно передать рабочему потоку на выполнение
#     :param signals: Signal - объект сигналов рабочего потока
#     :return: str - сообщение об окончании выполнения кода функции
#     """
#     for i in range(0, 5):  # цикл, эмулирующий вычислительную нагрузку
#         time.sleep(1)  # остановка выполнения на 1 секунду
#         signals.progress.emit(i * 100 / 4)
#     return 'Done.'

def execute_this_fn(**kwargs) -> str:
    """
    Функция, которую нужно передать рабочему потоку на выполнение
    :return: str - сообщение об окончании выполнения кода функции
    """
    for i in range(0, 5):  # цикл, эмулирующий вычислительную нагрузку
        time.sleep(1)  # остановка выполнения на 1 секунду
        kwargs['signals'].progress.emit(i * 100 / 4)
    return 'Done.'


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    Перечень поддерживаемых сигналов:
    finished - без данных, сигнал о завершении исполнения кода функции
    error - кортеж типа (extype, value, traceback.format_exc()) с сообщением об ошибке и трассировкой
    result - объект с возвращаемыми данными любыми, полученными в результате работы кода функции
    """
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами c
    результатами работы.
    """

    def __init__(self, fn, *args, **kwargs) -> None:
        """
        Конструктор рабочего потока.
        :param fn: функция для выполнения
        :param args: аргументы для выполняемой функции
        :param args: ключевые аргументы для выполняемой функции
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.fn = fn  # сохранение объекта функции для выполнения в аттрибуте рабочего потока
        self.args = args  # сохранение аргументов для функции в аттрибуте рабочего потока
        self.kwargs = kwargs  # сохранение ключевых аргументов для функции в аттрибуте рабочего потока
        self.signals = WorkerSignals()  # создание экземпляра класса сигналов рабочего потока
        kwargs['signals'] = self.signals  # создание ключевого аргумента для передачи объекта
        # сигналов рабочего потока

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код рабочего потока для запуска функции с передачей ей аргументов
        """
        try:
            result = self.fn(*self.args, **self.kwargs)  # вызов функции с аргументами
            # и сохранение результатов ее работы
        except:
            traceback.print_exc()  # вывод информации об ошибке
            exctype, value = sys.exc_info()[:2]  # извлечение параметров из стека программы
            self.signals.error.emit((exctype, value, traceback.format_exc()))  # возврат сигнала с сообщением об ошибке
        else:
            self.signals.result.emit(result)  # возврат результата работы функции
        finally:
            self.signals.finished.emit()  # возврат сигнала о завершении выполнения функции


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.counter = 0  # счетчик количества выполненных функций
        layout = QVBoxLayout()  # создание экземпляра слоев для размещения виджетов
        self.label = QLabel('Start')  # создание ярлыка с надписью
        button = QPushButton('DANGER!')  # создание кнопки с надписью
        button.pressed.connect(self.oh_no)  # создание сигнала на нажатие кнопки с привязкой метода ресивера
        layout.addWidget(self.label)  # размещение текстового поля в слое для виджетов
        layout.addWidget(button)  # размещение кнопки в слое для виджетов
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя для виджетов
        self.setCentralWidget(container)  # размещение контейнера в главном окне приложения
        self.threadpool = QThreadPool()  # создание экземпляра класса менеджера потоков
        print(f'Multithreading with maximum {self.threadpool.maxThreadCount()}')
        # вывод максимального количества доступных потоков
        self.timer = QTimer()  # создание экземпляра таймера
        self.timer.setInterval(1000)  # установка интервала таймера
        self.timer.timeout.connect(self.recurring_timer)  # создание сигнала о завершении таймера
        # с привязкой метода ресивера
        self.timer.start()  # запуска таймера

    @staticmethod
    def progress_fn(n: int) -> None:
        """
        Метод для вывода хода выполнения функции
        :param n: int - процент выполнения
        :return: None
        """
        print(f'{n}% done')

    @staticmethod
    def print_output(s: str) -> None:
        """
        Метод для вывода сообщений в консоль
        :param s: str - текст сообщения
        :return: None
        """
        print(s)  # вывод сообщения

    @staticmethod
    def thread_complete() -> None:
        """
        Метода для вывода сообщения о завершении работы потока
        :return: None
        """
        print('THREAD COMPLETE!')  # вывод сообщения о завершении рабочего потока

    def oh_no(self) -> None:
        """
        Функция ресивер (слот), запускающая функцию на выполнение в рабочем потоке
        :return: None
        """
        worker = Worker(execute_this_fn)  # создание экземпляра рабочего потока с передачей ему функции для исполнения
        # также при этом можно передать аргументы для функции Worker(execute_this_fn, *args, **kwargs)
        worker.signals.result.connect(self.print_output)  # создание сигнала на получение результатов работы
        # функции и их вывода через привязанный метод ресивер
        worker.signals.finished.connect(self.thread_complete)  # создание сигнала на завершение и привязка
        # метода ресивер, выводящего сообщение о завершении рабочего потока
        worker.signals.progress.connect(self.progress_fn)  # создание сигнала для отображения хода выполнения
        # с привязкой метода ресивера, выводящего прогресс выполнения
        self.threadpool.start(worker)  # запуск рабочего потока на выполнение

    def recurring_timer(self) -> None:
        """
        Метод ресивер (слот) для подсчета количества отработанных интервалов таймера
        :return: None
        """
        self.counter += 1  # увеличение счетчика на работы таймера
        self.label.setText(f'Counter: {self.counter}')  # обновление текста ярлыка


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
