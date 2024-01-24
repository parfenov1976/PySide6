"""
Пример создания и использования модальных окон.
Модальным называется окно, которое перекрывает другие окна программы
и не дает пользователю взаимодействовать с ними. Модальными обычно делают
всевозможные диалоговые окна.
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import Qt

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса виджета кнопок QPushButton, класса слоя с вертикальной организацией виджетов QVBoxLayout,
класса базового пустого виджета QWidget

Импорт из модуля PySide6.QtCore класса аттрибутов для настройки и управления виджетами Qt.
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent: QWidget | QMainWindow = None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: object - ссылка на родительский объект
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Главное окно')  # установка заголовка главного окна
        self.resize(300, 300)  # установка исходного размера окна
        self.btn_modal_window = QPushButton('Создать модальное окно')  # создание кнопки для открытия модального окна
        self.vbox = QVBoxLayout()  # создание слоя для виджетов с вертикальной организацией
        self.vbox.addWidget(self.btn_modal_window)  # добавление на слой виджета кнопки вызова модального окна
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(self.container)  # размещение контейнера с соями на главном окне приложения
        self.btn_modal_window.clicked.connect(self.show_modal_window)  # назначение обработчика на нажатие кнопки

    def show_modal_window(self):
        """
        Метод обработчик (слот) сигнала нажатия кнопки показа модального окна
        """
        modal_window = ModalWindow(self)  # создание модального окна
        modal_window.show()  # показ модального окна


class Window(QWidget):
    """
    Класс окна приложения из супер класса базового пустого виджета
    """

    def __init__(self, parent: QWidget | QMainWindow = None) -> None:
        """
        Конструктор окон приложения
        :param parent: object - ссылка на родительский объект
        """
        QWidget.__init__(self, parent, Qt.WindowType.Window)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Обычное окно приложения')  # установка заголовка окна
        self.resize(300, 150)  # установка исходного размера окна


class ModalWindow(QWidget):
    """
    Класс модального окна приложения из супер класса базового пустого виджета
    """

    def __init__(self, parent: QWidget | QMainWindow) -> None:
        """
        Конструктор окон приложения
        :param parent: object - ссылка на родительский объект
        """
        QWidget.__init__(self, parent, Qt.WindowType.Window)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Модальное окно')  # установка заголовка окна
        self.resize(150, 150)  # установка исходного размера окна
        self.parent = parent  # сохранение ссылки на родительский объект
        self.setWindowModality(Qt.WindowModality.WindowModal)  # установка модальности окна, при этом,
        # под MacOS элементы управления окном и строка заголовка исчезнут
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, True)  # установить аттрибут удаления окна при закрытии
        self.btn_close = QPushButton('Закрыть')  # создание кнопки на закрытие модельного окна
        self.vbox = QVBoxLayout()  # создание слоя для виджетов
        self.vbox.addWidget(self.btn_close)  # размещение кнопки в слое для виджетов
        self.setLayout(self.vbox)  # размещение слоя в модальном окне
        self.btn_close.clicked.connect(self.close)  # назначение обработка встроенного метода на закрытие окна


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно скрыто
    window1 = Window()  # создание обычного окна приложения
    window1.move(200, 200)
    window1.show()  # вывод окна на экран, по умолчанию окно скрыто
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
