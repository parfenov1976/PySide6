#!/usr/bin/env python3
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtCore PySide6 класса аттрибутов для настройки и управления виджетами Qt.
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса чекбокса QCheckBox/ 
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс QMainWindow для создания и настройки главного окна приложения
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.widget = QCheckBox('This is a checkbox')  # создание экземпляра класс виджета чекбокса
        self.widget.setCheckState(Qt.Checked)  # установка галки по умолчанию
        # self.widget.setCheckState(Qt.PartiallyChecked)  # разрешение третьего состояния - частично включен
        # self.widget.setTristate(True)  # разрешение третьего состояния - частично включен, 2-ой вариант
        self.widget.stateChanged.connect(self.show_state)  # создание сигнала об изменении состояния и привязка ресивера
        self.setCentralWidget(self.widget)  # размещение виджета чекбокса в главном окне приложения

    @staticmethod
    def show_state(signal: int) -> None:
        """
        Ресивер сигнала - слот и метод для вывода кодов состояния чекбокса.
        :param signal: Сигнал из виджета чекбокса об изменении его состояния.
        :return: None
        """
        print(signal == Qt.Checked.value)  # проверка сигнала и состояния установленной галки
        print(signal, Qt.Checked.value)  # вывод сигнала


def main() -> None:
    """
    Функция запуска кода верхнего уровня.
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.
    app.exec()  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен.


if __name__ == '__main__':  # данное условие предотвращает запуск кода верхнего уровня модуля при его импортировании
    main()  # вызов функции запуска кода верхнего уровня
