"""
Пример использования виджета слоев с расположением виджетов по сетке.
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса слоев QGridLayout, класса пустого, базового виджета QWidget
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""
from layout_colorwidget import Color  # импорт класса пользовательского виджета цвета из модуля


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от родительского класса главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктов главного окна приложения.
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.layout = QGridLayout()  # создание экземпляра виджета слоев с расположением виджетов по сетке
        self.layout.addWidget(Color('red'), 0, 0)  # добавление виджета в ячейку (номер столбца, номер строки)
        self.layout.addWidget(Color('green'), 1, 0)
        self.layout.addWidget(Color('blue'), 1, 1)
        self.layout.addWidget(Color('purple'), 2, 1)
        self.widget = QWidget()  # создание контейнера для слоя из класса пустого виджета
        self.widget.setLayout(self.layout)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(self.widget)  # размещение контейнера слоя в главном окне приложения


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
