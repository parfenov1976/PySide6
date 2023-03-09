"""
Пример использования модели таблиц и представления QTableView. В данном примере в качестве
структуры данных для таблицы будет файл базы данных sqlite.
Пример организации поиска по таблице.
"""

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QTableView,
                               QHBoxLayout,
                               QVBoxLayout,
                               QLineEdit,
                               QWidget)

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса ярлыка представления таблиц QTableView, классов слоев
с вертикальной и горизонтальной организацией виджетов QVBoxLayout и QHBoxLayout, класса 
однострочного редактируемого текстового поля QLideEdit, класса базового пустого виджета QWidget.
Импорт из модула PySide6.QtCore класса размеров двухмерных объектов QSize и класса Qt,
содержащего различные идентификаторы, используемые в библиотеке Qt.
Импорт из модуля PySide6.QtSql класса для установления связи с базой данных QSqlDatabase, 
класса модели запросов QSqlQueryModel, класса для создания запроса QSqlQuery.
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
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        container = QWidget()  # создание контейнера для слоев с виджетами
        layout_search = QHBoxLayout()  # создание экземпляра класса слоя с горизонтальной организацией виджетов
        self.track = QLineEdit()  # создание экземпляра класса виджета однострочного редактируемого
        # поля для поиска по названию трека
        self.track.setPlaceholderText('Track name...')  # установка затемненного текста, отображаемого в пустом поле
        self.track.textChanged.connect(self.update_query)  # создание сигнала на изменение содержимого поля для строки
        # поиска с привязкой метода ресивера
        self.composer = QLineEdit()
        self.composer.setPlaceholderText('Composer name...')
        self.composer.textChanged.connect(self.update_query)
        self.album = QLineEdit()
        self.album.setPlaceholderText('Album name...')
        self.album.textChanged.connect(self.update_query)
        layout_search.addWidget(self.track)  # размещение на слое виджета
        layout_search.addWidget(self.composer)
        layout_search.addWidget(self.album)
        layout_view = QVBoxLayout()  # создание экземпляра класса слоя с вертикальным расположением виджетов
        layout_view.addLayout(layout_search)  # размещение в слое другого слоя с виджетами
        self.table = QTableView()  # создание экземпляра класса представления таблиц
        layout_view.addWidget(self.table)
        container.setLayout(layout_view)
        self.model = QSqlQueryModel()  # создание экземпляра модели запросов
        self.table.setModel(self.model)  # подключение модели запросов к представлению таблиц
        self.query = QSqlQuery(db=db)  # создание подключения к базе данных
        self.query.prepare("SELECT Name, Composer, Album.Title FROM Track "
                           "INNER JOIN Album ON Track.AlbumId = Album.AlbumId WHERE "  # связывание таблиц через AlbumId
                           "Track.Name LIKE '%' || :track_name || '%' AND "
                           "Track.Composer LIKE '%' || :track_composer || '%' AND "
                           "Album.Title LIKE '%' || :album_title || '%' "
                           )  # подготовка запроса с параметрами
        self.update_query()  # вызов метода обновления, сборки и выполнения запроса в базу данных
        self.setMinimumSize(QSize(1024, 600))  # установка минимального размера главного окна приложения
        self.setCentralWidget(container)  # размещение представления таблицы в главном окне приложения

    def update_query(self, s: str = None) -> None:
        """
        Методы ресивер (слот) сигнала на обновление (сборку) и выполнения запроса в базу данных
        """
        track_name = self.track.text()  # извлечение текста из текстового поля в параметр
        track_composer = self.composer.text()  # извлечение текста из текстового поля в параметр
        album_title = self.album.text()  # извлечение текста из текстового поля в параметр
        self.query.bindValue(":track_name", track_name)  # присвоение значение параметру
        self.query.bindValue(":track_composer", track_composer)  # присвоение значение параметру
        self.query.bindValue(":album_title", album_title)  # присвоение значение параметру
        self.query.exec()  # выполнение запроса в базу данных
        self.model.setQuery(self.query)  # передача запроса в модель запросов


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
