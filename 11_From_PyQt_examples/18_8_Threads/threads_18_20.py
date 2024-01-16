"""
Пример вывод на экран загрузочной заставки
"""
import sys
import os
import time
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QSplashScreen,
                               QPushButton,
                               )
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Модуль os для извлечения путей операционной системы и работы с путями.

Модуль time для работы с объектами времени

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главного окна QMainWindow,
класса заставок QSplashScreen, класс виджета кнопок QPushButton,

Импорт из модуля PySide6.QtCore класса аттрибутов для настройки и управления виджетами Qt.

Импорт из модуля PySide6.QtGui класса для работы с изображениями
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
        self.setWindowTitle('Вывод заставки на загрузке')  # установка заголовка главного окна
        self.exit_btn = QPushButton('Закрыть окно')  # создание кнопки для закрытия приложения
        self.exit_btn.clicked.connect(QApplication.instance().quit)  # назначение встроенного обработчика сигнала
        # нажатия кнопки закрытия приложения
        self.setCentralWidget(self.exit_btn)  # размещение кнопки в главном окне приложения

    @staticmethod
    def load_data(sp: QSplashScreen) -> None:
        """
        Метод с имитацией длительной загрузки данных
        :param sp: QSplashScreen - ссылка на объект заставки
        """
        for i in range(1, 11):  # цикл имитации процесса загрузки данных
            time.sleep(2)
            sp.showMessage(f'Загрузка данных ... {i * 10}%',  # изменение надписи с отображением прогресса
                           Qt.AlignmentFlag.AlignHCenter |
                           Qt.AlignmentFlag.AlignBottom,
                           Qt.GlobalColor.red)
            QApplication.instance().processEvents()  # принудительно обрабатываем события


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивой темы (стиля) для графического интерфейса
    splash = QSplashScreen(QPixmap(os.path.join('data', 'icon.svg')))
    splash.showMessage(f'Загрузка данных ... 0%',  # вывод надписи с отображением прогресса
                       Qt.AlignmentFlag.AlignHCenter |
                       Qt.AlignmentFlag.AlignBottom,
                       Qt.GlobalColor.red)
    splash.show()  # отображение заставки
    QApplication.instance().processEvents()  # принудительно обрабатываем события
    window = MainWindow()  # создание главного окна приложения
    window.resize(300, 30)  # установка размера окна оп умолчанию
    window.load_data(splash)  # запуск имитации загрузки данных с передачей ссылки на загрузочный экран
    window.show()  # вывод главного окна приложения
    splash.finish(window)  # скрываем заставку
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
