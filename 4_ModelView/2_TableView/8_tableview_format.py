"""
Пример использования модели таблиц и представления QTableView. С примером добавления иконки в ячейку.
Иконка всегда размещается слева в ячейке. В данном варианте также перенесен градиент по значениям
с заднего фона в декоратор. Декораторе цвет отображается в виде маленького квадратика слева в ячейке, как иконка
"""

import sys
from datetime import datetime  # импорт модуля для работы с форматами дат и времени
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QPersistentModelIndex
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QColor, QIcon

"""
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

COLORS = ['#053061', '#2166ac', '#4393c3', '#92c5de', '#d1e5f0',
          '#f7f7f7', '#fddbc7', '#f4a582', '#d6604d', '#b2182b', '#67001f']


class TableModel(QAbstractTableModel):
    """
    Подкласс создаваемой модели таблицы от супер-класса абстрактной модели таблиц
    """

    def __init__(self, data: list) -> None:
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
        value = self._data[index.row()][index.column()]
        # извлечение содержимого ячейки таблицы по координатам, предоставляемым методами .row() и .column()
        if role == Qt.ForegroundRole:
            if (isinstance(value, int) or isinstance(value, float)) and value < 0:
                return QColor(Qt.red)
        if role == Qt.TextAlignmentRole:  # проверка соответствия типа данных роли выравнивания текста
            if isinstance(value, int) or isinstance(value, float):  # проверка типа данных
                return Qt.AlignVCenter | Qt.AlignRight  # возврат указателей выравнивания
        if role == Qt.DisplayRole:  # проверка соответствия данных роли текстовой строки (role=0)
            # и сохранение в переменную
            if isinstance(value, datetime):  # проверка типа форматов дат
                return value.strftime("%Y-%m-%d")  # возврат строки даты
            elif isinstance(value, float):  # проверка типа числа с плавающей запятой
                return f'{value:.2f}'  # возврат строки
            elif isinstance(value, str):  # проверка типа строки
                return f'"{value}"'  # возврат строки в кавычках
            else:
                return value
        # if role == Qt.BackgroundRole:  # проверка соответствия данных роли заднего фона
        #     if isinstance(value, int) or isinstance(value, float):
        #         value = int(value)  # отбрасывание дробной части для подбора дискретного цвета
        #         # подбор цвета производим в пределах -5...+5 все, что больше или меньше принимаем по границе диапазона
        #         value = max(-5, value)  # все, что ниже -5 принимается равным -5
        #         value = min(5, value)  # все, что выше 5 принимается равным 5
        #         value = value + 5  # смещаем 0 на -5 для индексирования списка цветов
        #         return QColor(COLORS[value])  # возвращаем объект цвета с цветом согласно значению ячейки

        if role == Qt.DecorationRole:  # проверка соответствия данных роли декоратора
            if isinstance(value, datetime):  # проверка типа данных
                return QIcon('calendar.png')  # добавление иконки в ячейку
            elif isinstance(value, bool):  # проверка типа данных
                if value:
                    return QIcon('tick.png')  # добавление иконки в ячейку
                return QIcon('cross.png')  # добавление иконки в ячейку
            elif isinstance(value, int) or isinstance(value, float):
                value = int(value)  # отбрасывание дробной части для подбора дискретного цвета
                # подбор цвета производим в пределах -5...+5 все, что больше или меньше принимаем по границе диапазона
                value = max(-5, value)  # все, что ниже -5 принимается равным -5
                value = min(5, value)  # все, что выше 5 принимается равным 5
                value = value + 5  # смещаем 0 на -5 для индексирования списка цветов
                return QColor(COLORS[value])  # возвращаем объект цвета с цветом согласно значению ячейки

    def rowCount(self, index: QModelIndex | QPersistentModelIndex) -> int:
        """
        Метод подсчета количества строк в таблице
        :param index: экземпляр классов QModelIndex и QPersistentModelIndex из библиотеки PySide6.QtCore
        :return: int - количество строк (длина внешнего списка)
        """
        return len(self._data)

    def columnCount(self, index: QModelIndex | QPersistentModelIndex) -> int:
        """
        Метод подсчета количества столбцов. Данный метод считает количество элементов 0-ой строке и работает только
        в том случае, если во всех строках одинаковое количество элементов.
        :param index: экземпляр классов QModelIndex и QPersistentModelIndex из библиотеки PySide6.QtCore
        :return: int - количество строк (длина внешнего списка)
        """
        return len(self._data[0])


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
        data = [
                [True, 9, 2],
                [1, 0, -1],
                [3, 5, False],
                [3, 3, 2],
                [datetime(2019, 5, 4), 8, 9],
                ]
        self.model = TableModel(data)  # создание экземпляра модели таблицы с данными примера
        self.table.setModel(self.model)  # помещаем модель таблицы в представление (связывание модели и представления)
        self.setCentralWidget(self.table)  # размещение представления таблицы в главном окне приложения


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
