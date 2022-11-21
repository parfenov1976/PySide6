#!/usr/bin/env python3
import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap

"""
Модуль os нужен для создания путей к файлам, которые не зависят от платформы
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtCore PySide6 класса аттрибутов для настройки и управления виджетами Qt.
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса виджетов окон QMainWindow, класса основного окна QMainWindow, класса ярлыка QLabel, 
класса слоя для виджетов QVBoxLayout, класса базового пустого виджета QWidget.
Импорт из модуля QtGui PySide6 класса QPixmap для работы с графическими файлами.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

basedir = os.path.dirname(__file__)  # извлечение пути до данного файла


class MainWindow(QMainWindow):
    """
    Подкласс QMainWindow для создания и настройки главного окна приложения
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов родительского класса главного окна приложения
        self.setWindowTitle('My App')  # установка названия главного окна приложения
        widget = QLabel('Hello')  # создание экземпляра виджета ярлыка с надписью
        # также текст можно задавать через метод widget.setText('text')
        font = widget.font()  # извлечение текущего шрифта из виджета и его сохранение в переменной
        font.setPointSize(30)  # установка размера шрифта
        widget.setFont(font)  # применение измененного шрифта к виджету
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # размещение виджета по центру
        # для других вариантов см. флаги выравнивания (flags for alignment)
        widget2 = QLabel()  # создание экземпляра виджета ярлыка с надписью
        widget2.setPixmap(QPixmap(os.path.join(basedir, 'data', 'otje.jpg')))
        # на ярлыке также можно размещать картинки
        widget2.setScaledContents(True)  # данный флаг разрешает масштабирование картинки в ярлыке
        # при этом, она может только увеличиваться относительно исходного размера
        layout = QVBoxLayout()  # создание слоя для размещения виджетов на нем
        layout.addWidget(widget)  # размещение на слое поля строки ввода текста
        layout.addWidget(widget2)  # размещение на слое ярлыка для отображения текста
        conteiner = QWidget()  # создание контейнера для хранения слоя
        conteiner.setLayout(layout)  # помещение слоя в контейнер
        self.setCentralWidget(conteiner)  # размещение виджета ярлыка в главном окне приложения


def main() -> None:
    """
    Функция запуска кода верхнего уровня.
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла приложения
    """
    На одно приложение нужен только один экземпляр QApplication.
    Передача sys.argv нужна, чтобы обеспечить возможность использования аргументов командной строки для приложения.
    Если использование аргументов командной строки не предполагается, то QApplication([]) тоже будет работать. 
    [] - пустой список.
    """
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.
    app.exec()  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен.


if __name__ == '__main__':  # данное условие предотвращает запуск кода верхнего уровня модуля при его импортировании
    main()  # вызов функции запуска кода верхнего уровня
