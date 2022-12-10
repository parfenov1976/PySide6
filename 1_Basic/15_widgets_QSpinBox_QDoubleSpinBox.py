#!/usr/bin/env python3
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox
from PySide6.QtWidgets import QVBoxLayout, QWidget

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета спинбокса (поле изменения численного содержимого со стрелочкам) 
QSpinBox, QDoubleSpinBox.
Дополнительно импортируем класс слоев для размещения виджетов QVBoxLayout и базовый класс виджета QWidget.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс основного окна приложения, созданный от супер класса основного окна.
    """

    def __init__(self):
        """
        Конструктор основного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.widget = QSpinBox()  # создание экземпляра виджета спинбокса для целых чисел
        self.widget2 = QDoubleSpinBox()  # создание экземпляра виджета спинбокса для чисел с плавающей точкой
        self.widget.setMinimum(-10)  # установка минимального значения спинбокса
        self.widget.setMaximum(3)  # установка максимального значения спинбокса
        self.widget2.setRange(-10, 10)  # можно установить сразу диапазон значений спинбокса
        # стартовое значение по умолчанию равно 0
        self.widget.setValue(-6)  # стартовое значение можно задать так
        self.widget.setPrefix('$')  # установка значка, который будет показываться перед числом
        self.widget.setSuffix('c')  # установка значка, который будет показываться после числа
        self.widget2.setPrefix('N=')  # установка значка, который будет показываться перед числом
        self.widget2.setSuffix(' кН')  # установка значка, который будет показываться после числа
        self.widget.setSingleStep(3)  # установка шага изменения значения в спинбоксе (для дробных числе можно
        # установить дробный шаг)
        self.widget2.setSingleStep(.1)
        self.widget.valueChanged.connect(self.value_changed)  # Создание сигнала на изменение значения в спинбоксе
        # и привязка ресивера. Данный сигнал передает только число (без префикса и суффикса).
        self.widget.textChanged.connect(self.value_changed_str)  # Создание сигнала на изменение содержимого спинбокса
        # и привязка метода ресивера. Данный сигнал передает содержимое спинбокса как строку с префиксом и суффиксом.
        self.widget2.valueChanged.connect(self.value_changed)
        self.widget2.textChanged.connect(self.value_changed_str)
        self.layout = QVBoxLayout()  # создание слоя для размещения виджетов
        self.layout.addWidget(self.widget)  # добавление виджета на слой для их размещения
        self.layout.addWidget(self.widget2)  # добавление виджета на слой для их размещения
        self.widget3 = QWidget()  # создание контейнера для хранения слоя из класса базового виджета
        self.widget3.setLayout(self.layout)  # размещение слоя в контейнере
        self.setCentralWidget(self.widget3)  # размещение контейнера в главном окне приложения

    @staticmethod
    def value_changed(i: int or float) -> None:
        """
        Метод ресивер (слот) для приема сигнала от виджета.
        :param i: число целое или с плавающей точкой.
        :return: None
        """
        print(i)

    @staticmethod
    def value_changed_str(s: str) -> None:
        """
        Метод ресивер (слот) для приема сигнала от виджета
        :param s: строка.
        :return: None
        """
        print(s)


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # метод вывода главного окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла событий главного окна приложения


if __name__ == '__main__':  # конструкция для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода приложения верхнего уровня
