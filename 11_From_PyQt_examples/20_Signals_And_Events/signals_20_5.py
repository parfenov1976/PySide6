"""
Пользовательские сигналы

Можно создавать свои собственные, пользовательские сигналы. Для этого следует определить
в классе какой-либо атрибут класса (не обычный!) и присвоить ему результат, возвращенный
функцией Signal() из модуля QtCore. Формат функции:
Signal([<Тип 1>, <Тип 2>,. . ., <Тип N>][, name=None])
Можно указать типы значений, передаваемых сигналу (например: bool или int):
mysignal1 = QtCore.Signal(int)
mysignal2 = QtCore.Signal(int, str)
При использовании типа данных С++ его имя необходимо указать в виде строки:
mysignalЗ = QtCore.Signal("QDate")
Если сигнал не принимает параметров, типы не указываются.
Параметр name задает имя создаваемого сигнала. Если он не указан, имя сигнала совпадет с
именем атрибута класса, в котором он хранится. Пример:
mysignal4 = QtCore.Signal(int, name="mySignal")
Можно создать несколько одноименных сигналов, принимающих разные параметры (перегруженный
сигнал). В этом случае типы передаваемых значений указываются внутри квадратных скобок.
Вот пример сигнала, передающего данные типа int или str:
mysignal5 = QtCore.Signal([int], [str])

Вместо конкретного типа принимаемого сигналом параметра можно указать тип QVariant из
модуля QtCore. В этом случае сигналу допускается передавать значение любого типа. Пример:
mysignal = QtCore.pyqtSignal(QtCore.QVariant)
self.mysignal.emit(20)
self.mysignal.emit("Привет!")
self.mysignal.emit([l, "2"])
"""

import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import Signal

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса виджета кнопки QPushButton, класс базового пустого виджета QWidget

Импорт из модуля PySide6.QtCore класса сигнала Signal
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения
    """
    mysignal = Signal(int, int)  # создание пользовательского сигнала

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Пользовательские сигналы')  # присвоение заголовка главному окну
        self.resize(300, 300)  # установка исходного размера окна
        self.btn1 = QPushButton('Нажми меня')  # создание виджета кнопки
        self.btn2 = QPushButton('Кнопка 2')  # создание виджета кнопки
        self.vbox = QVBoxLayout()  # создание слоя для виджетов
        self.vbox.addWidget(self.btn1)  # добавление виджета на слой
        self.vbox.addWidget(self.btn2)  # добавление виджета на слой
        self.container = QWidget()  # создание контейнера для слоев
        self.container.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера для слоев в главном окне приложения
        self.btn1.clicked.connect(self.on_clicked_btn1)  # создание сигнала и привязка обработчика
        self.btn2.clicked.connect(self.on_clicked_btn2)  # создание сигнала и привязка обработчика
        self.mysignal.connect(self.on_mysignal)  # создание сигнала и привязка обработчика

    def on_clicked_btn1(self) -> None:
        """
        Обработчик сигнала на нажатие кнопки 1
        """
        print('Нажата кнопка 1')
        self.btn2.clicked[bool].emit(False)  # генерируем сигнал нажатия 2-ой кнопки
        self.mysignal.emit(10, 20)  # генерируем пользовательский сигнал

    @staticmethod
    def on_clicked_btn2() -> None:
        """
        Обработчик сигнала на нажатие кнопки 2
        """
        print('Нажата кнопка 2')

    @staticmethod
    def on_mysignal(x: int, y: int) -> None:
        print('Обработан пользовательский сигнал mysignal1()')
        print(f'x = {x}, y = {y}')


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()