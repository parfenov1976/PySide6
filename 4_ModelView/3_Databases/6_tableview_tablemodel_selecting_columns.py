"""
Пример использования модели таблиц и представления QTableView. В данном примере в качестве
структуры данных для таблицы будет файл базы данных sqlite.
Пример отбора колонок для отображения путем удаления ненужного из модели
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
        self.model.setTable('Track')

        # tag::remove columns from model[]
        # self.model.removeColumns(3, 5)  # удаление колонок, первое число номер начиная с которой выполнять удаление,
        # второе число сколько колонок удалить
        # self.model.removeColumn(0)  # удаление одной колони по номеру

        columns_to_remove = ['name', 'something']  # список наименование колонок для удаления
        for cn in columns_to_remove:
            idx = self.model.fieldIndex(cn)  # извлечение индекса столбца по его имени в базе
            # данный метод не чувствителен к регистру
            self.model.removeColumn(idx)  # удаление одной колонки по номеру
        """
        Удаление колонок должно быть размещено до присвоения им названий, потому что несмотря на то, что имена
        колонкам присваиваются по названию из базы, закрепляются они в итоге за их номерами. Т.е. сохраняемые
        колонки сдвигаются под названия, которые будут соответствовать их новому номеру после удаления колонок
        из модели
        """
        # end::remove columns from model[]

        # tag::replace column titles[]
        column_titles = {
            'Name': 'Name',
            'AlbumId': 'Album (ID)',
            'MediaTypeId': 'Media Type (ID)',
            'GenreId': 'Genre (ID)',
            'Compose': 'Composer'
        }
        for n, t in column_titles.items():  # извлечение имени столбца в базе и имени для представления
            idx = self.model.fieldIndex(n)  # извлечение индекса столбца по его имени в БАЗЕ!!!
            # данный метод не чувствителен к регистру
            self.model.setHeaderData(idx, Qt.Horizontal, t)  # присвоение имени столбцу по его индексу в базе
        # для отображения в представлении
        # Qt.Horizontal или Qt.Vertical задают или проверяют? ориентацию чего-то? Если задать Vertical,
        # то имя не присвоится
        self.model.select()  # выборка всех данных из модели (из подключенной таблицы)
        # end::replace column titles[]

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
