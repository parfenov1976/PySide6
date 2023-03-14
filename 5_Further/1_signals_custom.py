"""
Пример создания пользовательского сигнала с использованием класса Signal
из модуля PySide6.QtCore.
"""
import sys

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow.
Импорт из модуля PySide6.QtCore класса сигнала Signal.
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """
    message = Signal(str)  # создание экземпляра класса сигнала с указанием, что сигнал передает строку
    value = Signal(int, str, int)  # создание экземпляра класса сигнала с указанием,
    # что сигнал передает три разных значения разных типов
    another = Signal(list)  # создание экземпляра класса сигнала с указанием, что сигнал передает список
    onemore = Signal(dict)  # создание экземпляра класса сигнала с указанием, что сигнал передает словарь
    anything = Signal(object)  # создание экземпляра класса сигнала с указанием, что сигнал может передать любой объект

    def __init__(self):
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.message.connect(self.custom_slot)  # создание сигнала с привязкой метода ресивера
        # с помощью метода .connect()
        self.value.connect(self.custom_slot)
        self.another.connect(self.custom_slot)
        self.onemore.connect(self.custom_slot)
        self.anything.connect(self.custom_slot)
        self.message.emit('my message')  # передача сигнала c данными c помощью метода .emit()
        self.value.emit(23, 'abc', 1)
        self.another.emit([1, 2, 3, 4, 5])
        self.onemore.emit({'a': 2, 'b': 7})
        self.anything.emit(1223)

    def custom_slot(self, *args: object) -> None:
        """
        Метод ресивер (слот) для приема данных сигнала
        :param args: object - любой объект
        :return: None
        """
        print(args)


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла главного окна приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # вызов метода главного окна, разрешающего его показ (по умолчанию окно скрыто)
    app.exec()  # запуска основного цикла главного окна приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()
