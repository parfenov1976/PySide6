"""
Пример использования класса QPalette для изменения цветов по умолчанию
"""

import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета ярлыка QLabel.
Импорт из модуля PySide6.QtGui класса для создания палитры QPalette и класса цветов QColor.
Qt из модуля PySide6.QtCore содержит различные идентификаторы, используемые в библиотеке Qt
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложений от супер класса главных окон
    """
    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # Явный вызов конструктора родительского класса
        self.palette = QPalette()  # создание экземпляра класса палитры
        self.palette.setColor(QPalette.Window, QColor(0, 128, 255))  # установка цвета фона главного окна
        self.palette.setColor(QPalette.WindowText, Qt.white)  # установка цвета текса в главно окне
        self.label = QLabel('Palette Test')  # создание ярлыка с надписью
        self.setCentralWidget(self.label)  # Размещение ярлыка в главном окне приложения
        self.setPalette(self.palette)  # применение настроенной палитры к главному окну приложения
        # палитры могут применяться и к отдельным виджетам


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # Создание экземпляра класса основного цикла событий приложения.
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    # можно применять к главному окну в конструкторе
    window = MainWindow()  # Создание главного окна приложения.
    window.show()  # Метод вывода главного окна приложения (по умолчанию окно спрятано).
    app.exec()  # Запуск основного цикла событий главного окна приложения.


if __name__ == '__main__':  # Данное условие предотвращает запуск кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня
