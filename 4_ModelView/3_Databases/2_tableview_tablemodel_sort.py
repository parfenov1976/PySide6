"""
Пример использования модели таблиц и представления QTableView. В данном примере в качестве
структуры данных для таблицы будет файл базы данных sqlite.
Пример применения сортировки к таблице
"""

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса ярлыка представления таблиц QTableView.
Импорт из модула PySide6.QtCore класса размеров двухмерных объектов QSize и класса Qt,
содержащего различные идентификаторы, используемые в библиотеке Qt.
Импорт из модуля PySide6.QtSql класса для установления связи с базой данных QSqlDatabase, 
класса модели таблиц, не имеющих связей с другими таблица базы данных, QSqlTableModel.
"""

db = QSqlDatabase('QSQLITE')  # создание экземпляра объекта базы данных с присвоением имени
db.setDatabaseName('chinook.sqlite')  # указание имени файл базы данных
db.open()  # команда на открытие базы данных


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный запуск конструктора родительского класса
        self.table = QTableView()  # создание экземпляра класса представления таблиц
        self.model = QSqlTableModel(db=db)  # создание экземпляра класса модели таблицы базы данных
        # с подключением файла базы данных
        self.table.setModel(self.model)  # привязка модели к представлению

        # tag::sortTable[]
        self.model.setTable('Track')  # установка подключения модели к таблице Track в базе данных
        self.model.setSort(2, Qt.DescendingOrder)  # сортировка таблицы по 2-му столбцу по убыванию
        # (нумерация столбцов от 0)
        self.model.select()  # выборка всех данных из модели (из подключенной таблицы)
        # end::sortTable[]

        self.setMinimumSize(QSize(1024, 600))  # установка минимального размера главного окна
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
