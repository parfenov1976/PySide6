"""
Пример использования виджета вкладок QTabWidget.
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QTabWidget)


"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета вкладок QTabWidget.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""
from layout_colorwidget import Color  # импорт класса пользовательского виджета цвета из модуля


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения с наследованием от супер класс главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.tabs = QTabWidget()  # создание экземпляра виджета вкладок
        self.tabs.setTabPosition(QTabWidget.West)  # задает размещение кнопок переключения вкладок
        self.tabs.setMovable(True)  # разрешает перемещение кнопок вкладок
        self.tabs.setDocumentMode(True)  # только для macOS, притягивает кнопки переключения вкладок
        # непосредственно к вкладкам, иначе кнопки отображаются в виде отдельной ленты
        for color in ['red', 'green', 'blue', 'yellow']:
            self.tabs.addTab(Color(color), color)
        self.setCentralWidget(self.tabs)


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
