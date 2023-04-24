"""
Пример использования много поточности для обеспечения работы полосы индикатора прогресса
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков
Также понадобиться класс декоратора Slot и класс сигнала Signal
В данном файле рассмотрен пример постановки рабочего потока на паузу.
"""
import sys
import time

from PySide6.QtWidgets import (QApplication,
                               QHBoxLayout,
                               QMainWindow,
                               QProgressBar,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtCore import QRunnable, Slot, QThreadPool, Signal, QObject

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с горизонтальной организацией QHBoxLayout, класса виджета кнопки QPushButton,
класса индикатора прогресса QProgressBar, класса базового виджета QWidget.
Импорт из модуля PySide6.QtCore класса таймера для измерения времени QTimer, класс контейнера для
исполняемого кода QRunnable, класс менеджера потоков QThreadPool, класс декоратора Slot,
класс сигнала Signal, класс базового объекта QObject.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class WorkerKilledException(Exception):
    """
    Подкласс исключения для остановки рабочего потока от супер-класса исключений
    """
    pass


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    progress индикатор прогресса от 0 до 100
    """
    progress = Signal(int)


class JobRunner(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами
    и результатов работы.
    """
    signals = WorkerSignals()  # создание экземпляра класса сигналов рабочего потока

    def __init__(self, iterations: int = 5) -> None:
        """
        Конструктор рабочего потока
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.is_killed = False  # создаем аттрибут для флага завершения рабочего потока
        self.is_paused = False  # создаем аттрибут для флага паузы в выполнении рабочего потока

    @Slot()  # данный декоратор помечает метод как слот
    def run(self) -> None:
        """
        Код, который необходимо выполнить помещаем в метод с именем run()
        """
        for n in range(100):  # запуск цикла определения степени выполнения
            self.signals.progress.emit(n + 1)  # передача определенного процента сигналу
            time.sleep(0.1)  # установка задержки для эмуляции нагрузки
            while self.is_paused:  # запуск цикла с проверкой флага паузы
                time.sleep(0)  # установка таймера на остановку, 0 позволяет исключить блокировку потока частыми
                # проверкам, питон при 0 просто ожидает условия для выхода из цикла, но сам цикл при этом не гоняет
            if self.is_killed:  # проверка флага завершения рабочего потока
                return  # возврат из кода рабочего потока

    def pause(self) -> None:
        """
        Метод установка флага паузы в Истина
        :return: None
        """
        self.is_paused = True

    def resume(self) -> None:
        """
        Метод установка флага паузы в Ложь
        :return: None
        """
        self.is_paused = False

    def kill(self) -> None:
        """
        Метод, устанавливающий флаг завершения рабочего потока на "истина"
        для обеспечения условия для выполнения кода завершения потока
        :return: None
        """
        self.is_killed = True


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
        layout = QHBoxLayout()  # создание экземпляра слоев для размещения виджетов
        self.status = self.statusBar()  # создание панели статуса на главном окне
        self.progress = QProgressBar()  # создание экземпляра класса индикатора прогресса
        self.status.addPermanentWidget(self.progress)  # размещение индикатора прогресса в панели статуса
        button_stop = QPushButton('Стоп')  # создание кнопки с надписью
        button_pause = QPushButton('Пауза')
        button_resume = QPushButton('Продолжить')
        layout.addWidget(button_stop)  # размещение кнопки в слое для виджетов
        layout.addWidget(button_pause)
        layout.addWidget(button_resume)
        container = QWidget()  # создание контейнера для слоев с виджетами
        container.setLayout(layout)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(container)  # размещение контейнера со слоями в главном окне приложения
        self.runner = JobRunner()  # создание экземпляра рабочего потока
        self.runner.signals.progress.connect(self.update_progress)  # создание сигнала на обновление
        # индикатора прогресса с привязкой метода его обновления
        self.threadpool.start(self.runner)  # запуск рабочего потока на выполнение
        button_stop.pressed.connect(self.runner.kill)  # создание сигнала с привязкой метода ресивера
        button_pause.pressed.connect(self.runner.pause)
        button_resume.pressed.connect(self.runner.resume)

    def update_progress(self, progress: int) -> None:
        """
        Метод ресивер (слот) обновляющий индикатор прогресс по сигналу рабочего потока
        :param progress: int - значение величины индикатора прогресса
        :return: None
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
