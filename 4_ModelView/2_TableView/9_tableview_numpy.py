"""
Пример использования модели таблиц и представления QTableView. В данном примере в качестве структуры данных для таблицы
будет применяться таблица (двухмерный массив) из NumPy

"""

import sys
import numpy as np
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QPersistentModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QColor, QIcon

"""
Импорт пакета NumPy для научных расчетов.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса ярлыка представления таблиц QTableView.
Импорт из модула PySide6.QtCore абстрактного класса QAbstractTableModel, предоставляющего стандартный 
интерфейс для моделей, которые представляют свои данные в табличной форме, а также классов индексов QModelIndex
и QPersistentModelIndex
Импорт из модула PySide6.QtGui класса QColor для создания объектов цвета, класса QIcon для создания иконки.
Он не используется напрямую, но должен быть супер-классом для модели.
Qt из модуля PySide6.QtCore содержит различные идентификаторы, используемые в библиотеке Qt.
"""


class TableModel(QAbstractTableModel):
    """
    Подкласс создаваемой модели таблицы от супер-класса абстрактной модели таблиц
    """

    def __init__(self, data: np.array) -> None:
        """
        Конструктор модели таблицы
        """
        QAbstractTableModel.__init__(self)  # явный вызов конструктора родительского класса
        self._data = data  # помещаем таблицу с данным в аттрибут экземпляра класса модели таблицы

    def data(self, index: QModelIndex | QPersistentModelIndex, role: int) -> int or float or str:
        """
        Метод для обработки запросов из представления на выборку данных из списка списков с проверкой типов данных
        :param index: координаты запрашиваемых данных предоставляемых методами .row() и .column().
        index является экземпляром классов QModelIndex и QPersistentModelIndex из библиотеки PySide6.QtCore.
        :param role: int - код типа данных. Подробнее https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum
        :return: str - наименование запрошенного дела
        """
        value = self._data[index.row(), index.column()]
        # извлечение содержимого ячейки таблицы по координатам, предоставляемым методами .row() и .column()
        # при этом, извлеченные данные представляют собой собственный класс NumPy
        # двойная индексация по-прежнему работает self._data[index.row()][index.column()]
        if role == Qt.DisplayRole:  # проверка соответствия данных роли текстовой строки (role=0)
            return str(value)  # для отображения нужно обязательно переводить экземпляры классов NumPy в тип строка

    def rowCount(self, index: QModelIndex | QPersistentModelIndex) -> int:
        """
        Метод подсчета количества строк в таблице
        :param index: экземпляр классов QModelIndex и QPersistentModelIndex из библиотеки PySide6.QtCore
        :return: int - количество строк (длина внешнего списка)
        """
        return self._data.shape[0]

    def columnCount(self, index: QModelIndex | QPersistentModelIndex) -> int:
        """
        Метод подсчета количества столбцов. Данный метод считает количество элементов 0-ой строке и работает только
        в том случае, если во всех строках одинаковое количество элементов.
        :param index: экземпляр классов QModelIndex и QPersistentModelIndex из библиотеки PySide6.QtCore
        :return: int - количество строк (длина внешнего списка)
        """
        return self._data.shape[1]


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер-класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.table = QTableView()  # создание экземпляра класса представления таблицы
        data = np.array([  # создание из списка списков двухмерного массива NumPy
            [1, 9, 2],
            [1, 0, -1],
            [3, 5, 2],
            [3, 3, 2],
            [5, 8, 9]
        ])
        self.model = TableModel(data)  # создание экземпляра модели таблицы с данными примера
        self.table.setModel(self.model)  # помещаем модель таблицы в представление (связывание модели и представления)
        self.setCentralWidget(self.table)  # размещение представления таблицы в главном окне приложения
        self.setGeometry(600, 100, 400, 200)  # установка размеров и координат окна (NW угла - NWx, NWy, W, H)


def main() -> None:
    """
    Функция запуска кода верхнего уроня приложения
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий главного окна приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # установка видимости окна, по умолчанию окно скрыто
    app.exec()  # запуск основного цикла событий главного окна приложения


if __name__ == '__main__':  # конструкция для предотвращения запуска кода верхнего уровня при импортировании
    # данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
