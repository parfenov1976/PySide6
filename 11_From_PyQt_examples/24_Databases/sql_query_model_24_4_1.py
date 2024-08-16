"""
Модель, связанная с SQL-запросом.

Если данные, извлеченные в результате выполнения SQL-запроса, не требуется редактировать,
имеет смысл использовать класс QSqlQueryModel. Он представляет модель, связанную
с SQL-запросом. Иерархия наследования этого класса:
QObject - QAbstractItemModel - QAbstractTableModel - QSqlQueryModel
Формат конструктора класса:
QSqlQueryModel([parent=None])
Класс QSqlQueryModel поддерживает следующие методы (здесь приведен их сокращенный
список, а полный список методов этого класса доступен на страницах
https://doc.qt.io/qt-6/qsqlquerymodel.html и
https://doc.qt.io/qt-6/qabstracttablemodel.html):
♦ setQuery(<Код запроса> [, db=QSqlDatabase ()]) - задает SQL-кoд запроса у модели.
  Необязательный параметр db задает соединение с базой данных, запрос к которой следует
  выполнить, если он не указан, будет использоваться соединение по умолчанию;
♦ setQuery(<Запрос QSqlQuery>) - задает запрос у модели;
♦ query() - возвращает запрос (объект класса QSqlQuery), заданный у модели;
♦ record() - возвращает объект класса QSqlRecord, хранящий сведения о структуре результата
  запроса;
♦ record(<Индекс записи>) - возвращает объект класса QSqlRecord, хранящий сведения
  о записи с указанным индексом;
♦ lastError() - возвращает объект объекта QSqlError, описывающий последнюю возникшую
  в базе данных ошибку;
♦ index(<Строка>, <Столбец> [, parent=QModelIndex ()]) - возвращает индекс (объект
  класса QModelIndex) элемента модели, находящегося на пересечении строки и столбца
  с указанными индексами. Необязательный параметр parent задает элемент верхнего
  уровня (объект класса QModelIndex) для искомого элемента - если таковой не задан, будет
  выполнен поиск элемента на самом верхнем уровне иерархии;
♦ data(<Индекс QModelIndex> [, role=ItemDataRole.DisplayRole]) - возвращает данные,
  хранимые в указанной в параметре role роли элемента, на который ссылается заданный
  индекс;
♦ rowCount([parent=QModelIndex()]) - возвращает количество элементов в модели. Необязательный
  параметр parent указывает элемент верхнего уровня (объект класса
  QModelIndex), при этом будет возвращено количество вложенных в него элементов. Если
  параметр не задан, возвращается количество элементов верхнего уровня иерархии;
♦ setHeaderData() - задает значение для указанной роли заголовка. Формат метода:
  SetHeaderData(<Индекс>, <Ориентация>, <Значение>[, role=ItemDataRole.EditRole])
  В первом параметре указывается индекс строки или столбца, а во втором - ориентация
  (элемент Horizontal или Vertical перечисления Orientation из модуля QtCore.Qt). Метод
  возвращает значение True, если операция успешно выполнена;
♦ headerData (<Индекс>, <Ориентация> [, role=ItemDataRole.DisplayRole]) - возвращает
  значение, соответствующее указанной роли заголовка. В первом параметре указывается
  индекс строки или столбца, а во втором - ориентация.
"""

from PySide6.QtWidgets import (QMainWindow,
                               QTableView,
                               )
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel

from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса представления таблицы QTableView

Импорт из модуля PySide6.QtSql класса соединений с базами данных QSqlDatabase,
класса модели запросов QSqlQueryModel

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Модель, связанная с SQL-запросом')  # установка заголовка главного окна приложения
        self.resize(600, 600)  # установка исходного размера окна
        self.table = QTableView()  # создание представления таблицы
        self.setCentralWidget(self.table)  # размещение текстового поля в главном окне приложения


def main() -> None:
    """
    Код примера выполнения запроса и его очистки
    :return: None
    """
    sqlite_con = QSqlDatabase.addDatabase('QSQLITE')  # создание объекта соединения с базой данных
    sqlite_con.setDatabaseName('data.sqlite')  # подключение базы данных
    sqlite_con.open()  # открытие базы данных

    sql_query_model = QSqlQueryModel(parent=window.table)  # создаем модель запроса
    sql_query_model.setQuery('SELECT * FROM good ORDER BY goodname')  # задаем запрос в модели

    # задаем заголовки для столбцов
    sql_query_model.setHeaderData(1, Qt.Orientation.Horizontal, 'Название')
    sql_query_model.setHeaderData(2, Qt.Orientation.Horizontal, 'Кол-во')

    window.table.setModel(sql_query_model)  # задаем представлению таблицы модель запроса
    window.table.hideColumn(0)  # скрываем первый столбец с идентификатором
    window.table.setColumnWidth(1, 150)
    window.table.setColumnWidth(2, 60)

    sqlite_con.close()  # закрытие базы данных


if __name__ == '__main__':  # проверка условия запуска для предотвращения исполнения
    # кода верхнего уровня при импортировании данного файла как модуля
    from PySide6.QtWidgets import QApplication
    import sys

    """
    Импорт из модуля PySide6.QtWidgets класса управления приложением QApplication
    Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
    к аргументам командной строки. Если использование аргументов командной строки не предполагается,
    то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
    в качестве аргумента передается пустой.
    """
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # включение видимости окна, по умолчанию окно спрятано
    main()  # запуск функции с кодом верхнего уровня
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
