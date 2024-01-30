"""
Пример смены значка в заголовке окна
"""
import sys
import os
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               )
from PySide6.QtGui import QIcon

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Модуль os для извлечения путей операционной системы и работы с путями.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,

Импорт из модуля PySide6.QtGui класса иконок QIcon
"""

base = os.path.dirname(__file__)  # извлечение абсолютного пути к данному модулю


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Смена значка в заголовке окна')  # установка заголовка окна
        self.ico = QIcon(os.path.join(base, 'data', 'lightning.png'))  # создание объекта иконки
        self.setWindowIcon(self.ico)  # установка иконки для окна


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления графического интерфейса
    app.setWindowIcon(QIcon(os.path.join(base, 'data', 'lightning.png')))  # установка иконки для программы
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно скрыто
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()