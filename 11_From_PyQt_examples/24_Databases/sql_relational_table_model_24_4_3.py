"""
Модель, поддерживающая межтабличные связи (отношения)

Создать связи между таблицами поможет класс QSqlRelationalTableModel, реализующий модель вторичной
таблицы, которая связывается с первичной таблицей. Иерархия наследования этого класса:
QObject - QAbstractItemModel - QAbstractTableModel - QSqlQueryModel -
QSqlTableModel - QSqlRelationalTableModel
Формат конструктора класса:
QSqlRelationalQueryModel([parent=None] [, db=QSqlDatabase()])
Необязательный параметр db задает соединение с базой данных, запрос к которой следует
выполнить, - если он не указан, будет использоваться соединение по умолчанию.
Класс QSqlRelationalTableModel наследует все методы класса QSqlTableModel
и в дополнение к ним определяет следующие методы (полный их список
приведен на странице https://doc.qt.io/qt-6/qsqlrelationaltablemodel.html):
♦ setRelation(<Индекс поля>, <Связь>) - задает связь для поля внешнего ключа с указанным
  индексом. Сама связь представляется объектом класса QSqlRelation, рассматриваемым
  чуть позже;
♦ setJoinMode(<Режим связывания>) - задает режим связывания для всей модели. В качестве
  параметра указывается один из элементов перечисления JoinModel, из класса
  QSqlRelationalTableModel:
  • InnerJoin - каждой записи вторичной таблицы должна соответствовать связанная
    с ней запись первичной таблицы. Используется по умолчанию;
  • LeftJoin - записи вторичной таблицы не обязательно должна соответствовать связанная
    запись первичной таблицы.
Класс QSqlRelation представляет саму межтабличную связь. Его конструктор имеет такой
формат:
QSqlRelation(<Имя первичной таблицы>, <Имя поля первичного ключа>, <Имя поля, выводящегося на экран>)
Поля, чьи имена указываются во втором и третьем параметрах, относятся к первичной таблице.
"""

import PySide6.QtCore
from PySide6.QtWidgets import (QMainWindow,
                               QTableView,
                               QVBoxLayout,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtSql import (QSqlDatabase,
                           QSqlRelationalTableModel,
                           QSqlRelation,
                           )

from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса представления таблицы QTableView, класса вертикальной стопки для виджетов QVBoxLayout,
класса виджета кнопки QPushButton, класса базового пустого виджета QWidget

Импорт из модуля PySide6.QtSql класса соединений с базами данных QSqlDatabase,
класса модели таблицы базы данных с поддержкой отношений QSqlRelationalTableModel,
класса отношения таблиц базы данных QSqlRelation

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
        self.setWindowTitle('Модель, с поддержкой отношений с другими таблицами')
        # установка заголовка главного окна приложения
        self.resize(420, 350)  # установка исходного размера окна
        self.table_view = QTableView()  # создание представления таблицы
        self.btn_add = QPushButton('&Добавить запись')  # создание кнопки добавление записи в таблицу
        self.btn_add.clicked.connect(add_record)  # привязываем обработчик на нажатие кнопки
        self.btn_del = QPushButton('&Удалить запись')  # создание кнопки удаления записи из таблицы
        self.btn_del.clicked.connect(del_record)  # привязываем обработчик на нажатие кнопки
        self.vbox = QVBoxLayout()  # создание вертикальной стопки для виджетов
        self.vbox.addWidget(self.table_view)  # добавление виджета в стопку
        self.vbox.addWidget(self.btn_add)  # добавление кнопки добавление записи в стопку
        self.vbox.addWidget(self.btn_del)  # добавление кнопки удаления записи в стопку
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # добавление в контейнер слоя с виджетами
        self.setCentralWidget(self.container)  # размещение контейнера с виджетами в главном окне приложения

    def closeEvent(self, event: PySide6.QtCore.QEvent):
        """
        Обработчик сигнала события закрытия окна приложения
        :param event: объект события PySide6.QtCore.QEvent
        :return: None
        """
        sqlite_con.close()
        print(f'База закрыта {event.type()}')


def add_record() -> None:
    """
    Обработчик сигнала кнопки добавления записи
    :return: None
    """
    sql_table_model.insertRow(sql_table_model.rowCount())  # вставляем пустую запись для ввода данных


def del_record() -> None:
    """
    Обработчика сигнала кнопки удаления записи
    :return: None
    """
    sql_table_model.removeRow(window.table_view.currentIndex().row())  # удаляем текущую строку
    sql_table_model.select()  # обновляем данные в представлении для удаления мусорной записи


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

    sqlite_con = QSqlDatabase.addDatabase('QSQLITE')  # создание объекта соединения с базой данных
    sqlite_con.setDatabaseName('data2.sqlite')  # подключение базы данных
    sqlite_con.open()  # открытие базы данных
    sql_table_model = QSqlRelationalTableModel()  # создаем модель таблицы
    sql_table_model.setTable('good')  # устанавливаем связь с таблицей БД
    sql_table_model.setSort(1, Qt.SortOrder.AscendingOrder)  # устанавливаем порядок сортировки по столбцу 1

    # Задаем для поля категории связь с таблицей списка категорий
    sql_table_model.setRelation(3, QSqlRelation('category', 'id', 'catname'))

    sql_table_model.select()  # производим чтение данных из таблицы
    # устанавливаем названия столбцов
    sql_table_model.setHeaderData(1, Qt.Orientation.Horizontal, 'Название')
    sql_table_model.setHeaderData(2, Qt.Orientation.Horizontal, 'Кол-во')
    sql_table_model.setHeaderData(3, Qt.Orientation.Horizontal, 'Категория')
    window.table_view.setModel(sql_table_model)  # привязываем к представлению созданную модель
    window.table_view.hideColumn(0)  # скрываем первый столбец с идентификаторами
    window.table_view.setColumnWidth(1, 150)  # устанавливаем ширину столбца
    window.table_view.setColumnWidth(2, 60)
    window.table_view.setColumnWidth(3, 150)

    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
