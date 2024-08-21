"""
Использование связанных делегатов

Модель QSqlRelationalTableModel в предыдущем примере sql_relational_table_model_24_4_3.py
«не знает», как перевести введенное название категории в ее идентификатор,
который и хранится в поле category таблицы good.
Поэтому, при попытке добавить запись в таблицу она лишь выполнит попытку занести строковое
название категории в поле целочисленного типа, что вполне ожидаемо вызовет ошибку,
и запись в таблице не сохранится.
Исправить такое положение дел нам позволит особый делегат, называемый связанным
Он способен выполнить поиск в первичной таблице
нужной записи, извлечь ее идентификатор и сохранить его в поле вторичной таблицы.
А, кроме того, он представляет все доступные для занесения в поле значения, взятые из
первичной таблицы, в виде раскрывающегося списка - очень удобно!
Функциональность связанного делегата реализует класс QSqlRelationalDelegate. Иерархия
наследования:
QObject - QAbstractItemDelegate - QStyledItemDelegate - QSqlRelationalDelegate
Использовать связанный делегат очень просто - нужно лишь создать его объект, передав
конструктору класса ссылку на компонент-представление (в нашем случае - таблицу),
и вызвать у представления метод setItemDelegate(), setItemDelegateForColumn() или
setItemDelegateForRow(), указав в нем только что созданный делегат.
Доработаем программу, дав возможность выбирать категории товаров
из списка. Для чего вставим в код одно новое выражение.
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
                           QSqlRelationalDelegate,
                           )

from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса представления таблицы QTableView, класса вертикальной стопки для виджетов QVBoxLayout,
класса виджета кнопки QPushButton, класса базового пустого виджета QWidget

Импорт из модуля PySide6.QtSql класса соединений с базами данных QSqlDatabase,
класса модели таблицы базы данных с поддержкой отношений QSqlRelationalTableModel,
класса отношения таблиц базы данных QSqlRelation, класс связанного делегата QSqlRelationalDelegate

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

    # создаем объект связанного делегата с передачей в него ссылки на представление
    # и устанавливаем данный делегат в представление таблицы с указанием индекса поля
    # с которым установлена связь с другой таблицей
    window.table_view.setItemDelegateForColumn(3, QSqlRelationalDelegate(window.table_view))

    window.table_view.hideColumn(0)  # скрываем первый столбец с идентификаторами
    window.table_view.setColumnWidth(1, 150)  # устанавливаем ширину столбца
    window.table_view.setColumnWidth(2, 60)
    window.table_view.setColumnWidth(3, 150)
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
