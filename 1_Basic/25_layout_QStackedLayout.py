"""
Пример использования виджета стэка слоев QStackedLayout
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, классов стэка слоев QStackedLayout и базового виджета QWidget
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""
from layout_colorwidget import Color  # импорт класса пользовательского виджета цвета из модуля


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный запуск конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.layout = QStackedLayout()  # создание экземпляра виджета стэка слоев
        self.layout.addWidget(Color('red'))  # помещение в стэк слоев экземпляра пользовательского класса цвета
        self.layout.addWidget(Color('blue'))
        self.layout.addWidget(Color('green'))
        self.layout.addWidget(Color('yellow'))
        self.layout.setCurrentIndex(2)  # установка индекса виджета, которые будет показан на верхнем видимом слое
        # индекс указывается в порядке добавления виджетов в стэк слоев
        """
        Также можно указать текущий виджет с помощью self.layout.setCurrentWidget(self.widget)
        передав в метод непосредственно сам виджет
        """
        self.widget = QWidget()  # создание контейнера для размещения слоя
        self.widget.setLayout(self.layout)  # размещение в контейнере слоя
        self.setCentralWidget(self.widget)  # размещение контейнера, содержащего слой, в главном окне приложения


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # Создание экземпляра класса основного цикла событий приложения.
    window = MainWindow()  # Создание главного окна приложения.
    window.show()  # Метод вывода главного окна приложения (по умолчанию окно спрятано).
    app.exec()  # Запуск основного цикла событий главного окна приложения.


if __name__ == '__main__':  # Данное условие предотвращает запуск кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня
