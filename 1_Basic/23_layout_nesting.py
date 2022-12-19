"""
Пример использования виджетов слоев c вложениями друг в друга.
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, классов слоев QVBoxLayout и QHBoxLayout, класса пустого, базового виджета QWidget
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
        self.layout1 = QHBoxLayout()  # создание экземпляра класса слоя, на первом слое размести остальные два
        self.layout2 = QVBoxLayout()
        self.layout3 = QVBoxLayout()
        self.layout1.setContentsMargins(0, 0, 0, 0)
        self.layout1.setSpacing(20)
        self.layout2.addWidget(Color('red'))  # добавление пользовательского виджета цвета на слой
        self.layout2.addWidget(Color('blue'))
        self.layout2.addWidget(Color('green'))
        self.layout1.addLayout(self.layout2)  # размещение слоя 2 на слое 1
        self.layout1.addWidget(Color('green'))
        self.layout3.addWidget(Color('red'))
        self.layout3.addWidget(Color('purple'))
        self.layout1.addLayout(self.layout3)  # размещение слоя 3 на слое 1
        self.widget = QWidget()  # создание экземпляра пустого виджета, контейнера для слоя
        self.widget.setLayout(self.layout1)  # добавление виджета слоя в контейнер, добавлять нужно только базовый слой
        self.setCentralWidget(self.widget)  # размещение виджета контейнера слоя в главном окне приложения


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
