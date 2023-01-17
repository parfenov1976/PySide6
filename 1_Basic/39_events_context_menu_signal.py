"""
Пример реализации контекстного меню с помощью создания сигнала от виджета контекстного меню.
"""
import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt из модуля PySide6.QtCore содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля PySide6.QtGui класса эффектов действия QAction.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса ярлыка QLabel, класса базового пустого виджета QWidget (данный класс 
импортирован, чтобы работало документирование, сами ручки работает и без этого импорта).
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса виджета главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Context menu app')
        self.label = QLabel('Context menu app window')
        self.setCentralWidget(self.label)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos: QPoint) -> None:
        """
        Метод обработчик событий PySide6.QMainWindow.contextMenuEvent, отрабатывающий по правому клику мышки или
        по кнопке вызова контекстного меню
        :param pos: tuple - координаты точки вызова контекстного меню
        :return: None
        """
        context = QMenu(self)  # создание экземпляра класса виджета контекстного меню
        context.addAction(QAction('Test 1', self))  # создание пункта контекстного меню
        context.addAction(QAction('Test 2', self))
        context.addAction(QAction('Test 3', self))
        context.exec(self.mapToGlobal(pos))  # запуск цикла событий контекстного меню c


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # методы вывода главного окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла событий главного окна приложения


if __name__ == '__main__':  # эта конструкция предотвращает запуск кода верхнего уроня приложения
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
