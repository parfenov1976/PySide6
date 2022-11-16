import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
QSize - класс для управления размерами окон
Qt - ???
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса виджетов окон QMainWindow и класса виджетов кнопок QPushButton
Это стандартный набор для любого приложения
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс QMainWindow для создания и настройки главного окна приложения
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        # при наследовании всегда нужно вызывать конструктор родительского класса
        self.setWindowTitle('My App')  # установка названия главного окна приложения
        self.button = QPushButton('Press Me!')  # создание кнопки
        self.button.setFixedSize(QSize(200, 50))  # можно задать размер кнопки
        self.button.clicked.connect(self.the_button_was_clicked)  # привязка метода (слота) получателя сигнала к кнопке
        self.setFixedSize(QSize(400, 300))  # установка ФИКСИРОВАННОГО размера главного окна приложения
        # если установить минимальный и максимальный размер окна, то setFixedSize() будет указывать
        # на стартовые размеры окна
        self.setMinimumSize(QSize(200, 200))  # установка минимального размера окна
        self.setMaximumSize(QSize(1000, 1000))  # установка максимального размера окна
        self.setCentralWidget(self.button)  # метод QMainWindow для размещения кнопки в главно окне приложения

    def the_button_was_clicked(self) -> None:
        """
        Метод получателя сигнала - слот.
        :return: None
        """
        self.button.setText('You already clicked me')  # меняет надпись на кнопке
        self.button.setEnabled(False)  # отключает кнопку - делает ее не активной
        self.setWindowTitle("My Oneshot App")  # меняет название главного окна приложения
        print('Clicked')


def main() -> None:
    """
    Функция запуска кода верхнего уровня.
    :return: None
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':  # данное условие предотвращает запуск кода верхнего уровня модуля при его импортировании
    main()  # вызов функции запуска кода верхнего уровня
