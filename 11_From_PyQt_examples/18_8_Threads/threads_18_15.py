"""
Пример многопоточного приложения - обмен сигналами между потоками
"""

import sys

from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import (QThread,
                            Signal,
                            Qt,
                            )

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication,
класса ярлыка QLabel, класса главных окон QMainWindow, класса кнопок QPushButton,
класса контейнера с вертикальным расположение виджетов QVBoxLayout,
класса виджета кнопки QPushButton, класса слоев с вертикальной организацией виджетов QVBoxLayout,

Импорт из модуля PySide6.QtCore класса потоков QThread, класса набора аттрибутов и настроек Qt,
класс сигналов Signal
"""


class Thread1(QThread):
    """
    Класс потока 1 от супер класса потоков
    """
    signal_1 = Signal(int)  # создание сигнала, принимающего целое число

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор потока 1
        :param parent: None
        """
        QThread.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.count = 0  # создание счетчика сигналов

    def run(self) -> None:
        """
        Метод, содержащий код для выполнения в отдельном потоке
        :return: None
        """
        self.exit()  # запуск цикла обработки сигнала в отдельном потоке

    def on_start(self) -> None:
        """
        Обработчик сигнала на нажатие кнопки генерации сигнала
        :return: None
        """
        self.count += 1  # увеличение счетчика сигналов
        self.signal_1.emit(self.count)  # генерация сигнала с передачей значения счетчика сигналов


class Thread2(QThread):
    """
    Класс потока 2 от супер класса потоков
    """
    signal_2 = Signal(str)  # создание сигнала, принимающего строку

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор потока 2
        :param parent: None
        """
        QThread.__init__(self, parent)  # явный вызов конструктора родительского класса

    def run(self):
        """
        Метод, содержащий код для выполнения в отдельном потоке
        :return: None
        """
        self.exec()  # запуск цикла обработки сигналов в отдельном потоке

    def on_change(self, i: int) -> None:
        """
        Метод, обработчик сигнала, принимающий сигнал из потока 1
        :param i: int - значение счетчика из 1-го потока
        :return: None
        """
        i += 10  # увеличение счетчика сигналов
        self.signal_2.emit(f'{i}')  # генерация сигнала с передачей строки со значением переменной i


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: None
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Многопоточное приложение с обменом сигналами между потоками')
        # установка заголовка главного окна приложения
        self.label = QLabel('Нажмите кнопку')  # создание ярлыка с надписью
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # установка флага выравнивания для ярлыка
        self.button = QPushButton('Сгенерировать сигнал')
        self.vbox = QVBoxLayout()  # создание слоя для виджетов с вертикальной организацией
        self.vbox.addWidget(self.label)  # размещение ярлыка в слое
        self.vbox.addWidget(self.button)  # размещение кнопки в слое
        self.widget = QWidget()  # создание контейнера для слоев с виджетами
        self.widget.setLayout(self.vbox)  # размещение слоя в контейнере
        self.setCentralWidget(self.widget)  # размещение контейнера со слоями в главном окне приложения
        self.thread1 = Thread1()  # создание экземпляра потока 1
        self.thread2 = Thread2()  # создание экземпляра потока 1
        self.thread1.start()  # запуск потока 1 на выполнение
        self.thread2.start()  # запуск потока 2 на выполнение
        self.button.clicked.connect(self.thread1.on_start)  # назначение обработчика сигналу на нажатие
        # кнопки генерации сигнала
        self.thread1.signal_1.connect(self.thread2.on_change)  # назначение обработчика сигналу из потока 1
        self.thread2.signal_2.connect(self.on_thread2_signal_2)  # назначение обработчика сигналу из потока 2

    def on_thread2_signal_2(self, s: str) -> None:
        """
        Обработчик сигнала из потока 2
        :param s: str - строка, передаваемая сигналом из потока 2
        :return: None
        """
        self.label.setText(s)  # вывод строки из сигнала на ярлык


if __name__ == '__main__':  # проверка условия запуска модуля предотвращает запуск кода после условия при
    # импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий (основного потока) главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.resize(300, 70)  # установка размеров окна по умолчанию
    window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
