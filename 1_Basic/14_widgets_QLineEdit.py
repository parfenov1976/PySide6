#!/usr/bin/env python3
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета редактируемого однострочного текстового поля QLineEdit. 
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс основного окна приложения от супер класса виджета основного окна
    """
    def __init__(self) -> None:
        """
        Конструктов основного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.widget = QLineEdit()  # создание экземпляра класса виджета однострочного редактируемого текстового поля
        self.widget.setMaxLength(10)  # установка максимального размера текста в поле в знакоместах
        self.widget.setPlaceholderText('Enter your text')  # установка текста, который отображается в пустом поле
        # self.widget.setReadOnly(True)  # делает поле не редактируемым
        self.widget.returnPressed.connect(self.return_pressed)  # создание сигнала на нажатие клавиши Ввод
        self.widget.selectionChanged.connect(self.selection_changed)  # создание сигнала на выделение текста
        # в текстовом поле
        self.widget.textChanged.connect(self.text_changed)  # создание сигнала об изменении текста в поле
        # данный сигнал отправляется при любом изменении текста, а не только при редактировании пользователем
        self.widget.textEdited.connect(self.text_edited)  # создание сигнала о выполнении редактирования текста в поле
        # данный сигнал отправляется только тогда, когда текст редактируется пользователем
        self.setCentralWidget(self.widget)  # размещение виджета внутри главного окна приложения
        # self.widget.setInputMask('aaa.000.000.000;*')  # маска ввода с заполнением пустых мест

    def return_pressed(self) -> None:
        """
        Метод ресивер (слот) для принятия сигнала от виджета на нажатие клавиши Ввод.
        :return: None
        """
        print('Return pressed')
        self.centralWidget().setText('BOOM!')  # размещение в середине главного окна текста

    def selection_changed(self) -> None:
        """
        Метод ресивер (слот) для принятия сигнала от виджета на выделение текста в поле.
        :return: None
        """
        print('Selection changed')
        print(self.centralWidget().selectedText())  # вызов метода для получения выделенного текста

    @staticmethod
    def text_changed(s: str) -> None:
        """
        Метод ресивер (слот) сигнала об изменении текста из виджета текстового поля.
        :param s: текст, передаваемый сигналом из виджета.
        :return: None
        """
        print('Текст changed...')
        print(s)

    @staticmethod
    def text_edited(s: str) -> None:
        """
        Метод ресивер (слот) сигнала о редактировании текста из виджета текстового поля.
        :param s: текст, передаваемый сигналом из виджета.
        :return: None
        """
        print('Text edited...')
        print(s)


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # Метод вывода главного окна приложения на экран. По умолчанию окно скрыто.
    app.exec()  # запуск основного цикла событий главного окна приложений


if __name__ == '__main__':  # данная конструкция не позволяет запускаться коду верхнего уровня
    # при импортировании данного файла как модуля
    main()  # запуск кода верхнего уровня
