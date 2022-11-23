#!/usr/bin/env python3
"""
Пример использования виджета выпадающего списка QComboBox
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtCore PySide6 класса аттрибутов для настройки и управления виджетами Qt.
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса выпадающего списка QComboBox/ 
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # Явный запуск конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.widget = QComboBox()  # создание экземпляра класса выпадающего списка
        self.widget.addItems(['One', 'Two', 'Three'])  # создание пунктов выпадающего списка
        self.widget.currentIndexChanged.connect(self.index_changed)  # создание сигнала об изменении индекса
        # пункта списка с привязкой ресивера (слота)
        self.widget.currentTextChanged.connect(self.text_changed)  # создание сигнала об изменении текста
        # пункта списка с привязкой ресивера (слота)
        self.widget.setEditable(True)  # позволяет строку выпадающего списка сделать редактируемой
        # При этом, через сигнал будет передаваться набранный текст после каждого нажатия клавиши.
        # (индекс передаваться не будет, т.к. для этого нужно выбирать пункт из выпадающего списка)
        # набранный текст может добавляться в выпадающий список в зависимости от флага вставки
        # self.widget.setInsertPolicy(QComboBox.NoInsert)  # вставки нет
        # self.widget.setInsertPolicy(QComboBox.InsertAtTop)  # вставка в начало списка
        # self.widget.setInsertPolicy(QComboBox.InsertAtCurrent)  # замена текущего пункта
        # self.widget.setInsertPolicy(QComboBox.InsertAtBottom)  # вставка в конец списка
        self.widget.setInsertPolicy(QComboBox.InsertAfterCurrent)  # вставка после текущего пункта списка
        # self.widget.setInsertPolicy(QComboBox.InsertBeforeCurrent)  # вставка перед текущим пунктом списка
        # self.widget.setInsertPolicy(QComboBox.InsertAlphabetically)  # вставка в алфавитном порядке
        self.widget.setMaxCount(10)  # установка максимального количества пунктов в выпадающем списке
        self.setCentralWidget(self.widget)  # размещение виджета выпадающего списка в главном окне приложения

    @staticmethod
    def index_changed(i: int) -> None:
        """
        Ресивер (слот) для получения сигнала от виджета и вывода его значения.
        :param i: int - индекс выбранного пункта выпадающего списка.
        :return: None
        """
        print(i)

    @staticmethod
    def text_changed(s: str) -> None:
        """
        Ресивер (слот) для получения сигнала от виджета и вывода его значения.
        :param s: str - наименование пункта выпадающего списка.
        :return: None
        """
        print(s)


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня.
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # Метод вывода главного окна приложения. По умолчанию окно скрыто.
    app.exec()  # запуск основного цикла событий главного окна приложения
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен.


if __name__ == '__main__':  # данное условие предотвращает запуск кода верхнего уровня модуля при его импортировании
    main()  # вызов функции запуска кода верхнего уровня
