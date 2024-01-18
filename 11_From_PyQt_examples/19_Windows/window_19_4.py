"""
Пример использования методов для сворачивания и разворачивания окна
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса виджета кнопок QPushButton, класса слоя с вертикальной организацией виджетов QVBoxLayout,
класса базового пустого виджета QWidget
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: object - ссылка на родительский объект
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Разворачивание и сворачивание окна')  # установка заголовка главного окна
        self.btn_min = QPushButton('Свернуть')  # создание кнопки управления окном
        self.btn_max = QPushButton('Развернуть')
        self.btn_full = QPushButton('Полный экран')
        self.btn_normal = QPushButton('Нормальный размер')
        self.vbox = QVBoxLayout()  # создание слоя для виджетов кнопок с вертикальной организацией
        self.vbox.addWidget(self.btn_min)  # размещение кнопки на слое для виджетов
        self.vbox.addWidget(self.btn_max)
        self.vbox.addWidget(self.btn_full)
        self.vbox.addWidget(self.btn_normal)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне приложения
        self.btn_min.clicked.connect(self.on_min)  # назначение обработчика сигнала на нажатие кнопки
        self.btn_max.clicked.connect(self.on_max)
        self.btn_full.clicked.connect(self.on_full)
        self.btn_normal.clicked.connect(self.on_normal)

    def on_min(self) -> None:
        """
        Метод обработчика сигнала (слот) на сворачивание окна
        """
        self.showMinimized()

    def on_max(self) -> None:
        """
        Метод обработчика сигнала (слот) на разворачивание окна
        """
        self.showMaximized()

    def on_full(self) -> None:
        """
        Метод обработчика сигнала (слот) на вывод окна на полный экран
        """
        self.showFullScreen()

    def on_normal(self) -> None:
        """
        Метод обработчика сигнала (слот) на установку нормального размера окна
        """
        self.showNormal()


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.resize(300, 100)  # установка исходного размера окна
    window.show()  # вывод окна на экран, по умолчанию окно скрыто
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
