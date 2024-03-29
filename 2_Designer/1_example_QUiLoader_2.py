"""
Пример использования UI файла из Qt Designer для загрузки в код при помощи QUiLoader
из пакета PySide6.QtUiTools. Пример с пользовательской функцией настройки главного окна.
"""
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt из модуля PySide6.QtCore содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication.
Работа с классом основного окна QMainWindow зашита в код UI файла.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

loader = QUiLoader()  # создание экземпляра класса загрузчика интерфейса


def mainwindow_setup(w: QUiLoader) -> None:
    """
    Функция настройки главного окна приложения
    :param w: экземпляр главного окна приложения
    :return: None
    """
    w.setWindowTitle('MainWindow Title')


def main():
    """
    Функция запуска кода приложения верхнего уровня
    :return:
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = loader.load('1_mainwindow.ui', None)  # загрузка файла интерфейса и создание главного окна приложения
    mainwindow_setup(window)
    window.show()  # метод показа окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня приложения при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уроня приложения
