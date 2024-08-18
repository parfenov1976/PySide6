"""
Модель, обеспечивающая связь с таблицей базы данных.

Если необходимо дать пользователю возможность редактировать данные, хранящиеся
в базе, следует использовать класс QSqlTableModel. Он представляет модель, связанную
непосредственно с указанной таблицей базы данных. Иерархия наследования:
QObject - QAbstractItemModel - QAbstractTableModel - QSqlQueryModel - QSqlTableModel
Формат конструктора класса:
QSqlTableModel([parent=None] [, db=QSqlDatabase()])
Необязательный параметр db задает соединение с базой данных, запрос к которой следует
выполнить, если он не указан, будет использоваться соединение по умолчанию.
Класс QSqlTableModel наследует все методы из класса QSqlQueryModel и в
дополнение к ним определяет следующие наиболее полезные для нас методы (полный их
список приведен на странице https://doc.qt.io/qt-6/qsqltablemodel.html):
♦ setTable(<Имя таблицы>) - задает таблицу, данные из которой будут представлены
  в модели. Отметим, что этот метод лишь выполняет получение из базы данных структуры
  указанной таблицы, но не загружает сами эти данные;
♦ tableName() - возвращает имя таблицы, заданной для модели;
♦ setSort(<Индекс столбца>, <Порядок сортировки>) - задает сортировку данных по
  столбцу с указанным индексом. Если вторым параметром передан элемент AscendingOrder
  перечисления sortOrder из модуля QtCore. Qt, сортировка будет производиться в прямом
  порядке, а если элемент DescendingOrder того же перечисления - в обратном;
♦ setFilter(<Условие фильтрации>) - задает условие для фильтрации данных в виде
  строки в формате, который применяется в SQL-команде WHERE;
♦ filter() - возвращает строку с фильтром, заданным для модели;
♦ select() - считывает в модель данные из заданной ранее таблицы с учетом указанных
  параметров сортировки и фильтрации. Возвращает True, если считывание данных прошло
  успешно, и False - в противном случае:
  stm = QtSql.QSqlTableModel(parent=window)
  stm.setTable('good')
  stm.setSort(1, QtCore.Qt.SortOrder.DescendingOrder)
  stm.setFilter('goodcount > 2')
  stm.select()
  Метод является слотом;
♦ setEditStrategy(<Режим>) -указывает режим редактирования данных в модели. В качестве
  параметра задается один из элементов перечисления EditStrategy из класса
  QSqlTableModel:
  • OnFieldChange - все изменения переносятся в базу данных немедленно;
  • OnRowChange - изменения переносятся в базу лишь после того, как пользователь перейдет
    на другую строку;
  • OnManualSubmit - изменения переносятся в базу только после вызова метода
    submit() или submitAll();
♦ insertRow(<Индекс>) - добавляет пустую запись по индексу, заданному первым параметром.
  Возвращает значение True, если запись была успешно добавлена, и False -
  в противном случае;
♦ insertRows (<Индекс>, <Количество>) - добавляет указанное количество пустых записей
  по индексу, заданному первым параметром. Если указан индекс -1, записи добавляются
  в конец модели. Возвращает значение True, если записи были успешно добавлены,
  и False - в противном случае;
♦ removeRow(<Индекс>) - удаляет запись с указанным индексом. Возвращает значение
  True, если запись была успешно удалена, и False - в противном случае;
♦ removeRows (<Индекс>, <Количество>) - удаляет указанное количество записей, начиная
  с записи с указанным индексом. Возвращает значение True, если записи были успешно
  удалены, и False - в противном случае;

    ПРИМЕЧАНИЕ
    Нужно отметить, что после удаления записи вызовом метода removeRow() или removeRows()
    в модели останется пустая запись, реально не представляющая никакой записи из таблицы.
    Чтобы убрать ее, достаточно выполнить повторное считывание данных в модель вызовом
    метода select().

♦ insertRecord(<Индекс>, <Запись>) - добавляет в модель новую запись по индексу, указанному
  первым параметром. Если задан отрицательный индекс, запись добавляется
  в конец модели. Добавляемая запись представляется объектом класса QSqlRecord, уже
  заполненным необходимыми данными. Возвращает True, если запись была успешно
  добавлена, и False - в противном случае;
♦ setRecord(<Индекс>, <Запись>) - заменяет запись по индексу, указанному первым параметром,
  другой записью, которая передается вторым параметром в виде объекта класса
  QSqlRecord, уже заполненного необходимыми данными. Возвращает True, если запись
  была успешно изменена, и False - в противном случае;
♦ submit() - переносит в базу данных изменения, сделанные в текущей записи, если был
  задан режим редактирования OnManualSubmit. Возвращает True, если изменения были
  успешно перенесены, и False - в противном случае. Метод является слотом;
♦ submitAll() - переносит в базу данных изменения, сделанные во всех записях, если
  был задан режим редактирования OnManualSubmit. Возвращает True, если изменения
  были успешно перенесены, и False - в противном случае. Метод является слотом;
♦ revert() - отменяет изменения, сделанные в текущей записи, если был задан режим
  редактирования OnManualSubmit. Возвращает True, если изменения были успешно отменены,
  и False - в противном случае. Метод является слотом;
♦ revertRow(<Индекс записи>) - отменяет изменения, сделанные в записи с заданным
  индексом, если был задан режим редактирования OnManualSubmit;
♦ revertAll() - отменяет изменения, сделанные во всех записях, если был задан режим
  редактирования OnManualSubmit. Возвращает True, если изменения были успешно отменены,
  и False - в противном случае. Метод является слотом;
♦ selectRow(<Индекс записи>) - обновляет содержимое записи с указанным индексом.
  Возвращает True, если запись была успешно обновлена, и False - в противном случае.
  Метод является слотом;
♦ isDirty(<Индекс QModelindex>) - возвращает True, если запись с указанным индексом
  была изменена, но эти изменения еще не были перенесены в базу данных, и False -
  в противном случае;
♦ isDirty() - возвращает True, если хотя бы одна запись в модели была изменена, но эти
  изменения еще не были перенесены в базу данных, и False - в противном случае;
♦ fieldIndex(<Имя поля>) - возвращает индекс поля с указанным именем или -1, если
  такого поля нет;
♦ primaryKey() - возвращает сведения о ключевом индексе таблицы, представленные
  объектом класса QSqlIndex, или пустой объект этого класса, если таблица не содержит
  ключевого индекса.
Методы insertRecord() и setRecord(), предназначенные соответственно для добавления и
изменения записи, принимают в качестве второго параметра объект класса QSqlRecord.
Формат вызова конструктора этого класса:
QSqlRecord([<Объект класса QSqlRecord>])
Если в параметре указать объект класса QSqlRecord, будет создана его копия. Обычно при
создании новой записи здесь указывают значение, возвращенное методом record() класса
QSqlDatabase (оно хранит сведения о структуре таблицы и, следовательно, представляет
пустую запись), а при правке существующей записи - значение, возвращенное методом
record(), который унаследован классом QSqlTableModel от класса QSqlQueryModel (оно
представляет запись, которую нужно отредактировать).
Класс QSqlRecord, поддерживает следующие методы (полное описание класса QSqlRecord
приведено на странице https://doc.qt.io/qt-6/qsqlrecord.html.):
♦ count() - возвращает количество полей в таблице;
♦ fieldName(<Индекс поля>) - возвращает имя поля, имеющее заданный индекс, или пустую
  строку, если индекс некорректен;
♦ field(<Индекс поля>) - возвращает сведения о поле (объект класса QSqlField), чей индекс
  задан в качестве параметра;
♦ field(<Имя поля>) - возвращает сведения о поле (объект класса QSqlField), чье имя
  задано в качестве параметра;
♦ indexOf(<Имя поля>) - возвращает-индекс поля с указанным именем или -1, если такого
  поля нет. При поиске поля не учитывается регистр символов;
♦ contains(<Имя поля>) - возвращает True, если поле с указанным именем существует,
  и False - в противном случае;
♦ isEmpty() - возвращает True, если в таблице нет полей, и False - в противном случае.
♦ value(<Индекс поля>) - возвращает значение поля текущей записи с заданным индексом;
♦ value(<Имя поля>) - возвращает значение поля текущей записи с заданным именем;
♦ setValue (<Индекс поля>, <Значение>) - заносит в поле с указанным индексом новое
  значение;
♦ setValue (<Имя поля>, <Значение>) - заносит в поле с указанным именем новое значение;
♦ isNull(<Индекс поля>) - возвращает True, если в поле с указанным индексом нет значения,
  и False - в противном случае;
♦ isNull(<Имя поля>) - возвращает True, если в поле с указанным именем нет значения,
  и False - в противном случае;
♦ setNull(<Индекс поля>) - удаляет значение из поля с указанным индексом;
♦ setNull(<Имя поля>) - удаляет значение из поля с указанным именем;
♦ clearValues() - удаляет значения из всех полей записи;
♦ setGenerated(<Индекс поля>, <Флаг>) - если вторым параметром передано False, поле
  с указанным индексом помечается как неактуальное, и хранящееся в нем значение не
  будет перенесено в таблицу;
♦ setGenerated(<Имя поля>, <Флаг>) - если вторым параметром передано False, поле
  с указанным именем помечается как неактуальное, и хранящееся в нем значение не
  будет перенесено в таблицу;
♦ isGenerated(<Индекс поля>) - возвращает False, если поле с указанным индексом помечено
  как неактуальное, и True - в противном случае;
♦ isGenerated(<Имя поля>) - возвращает False, если поле с указанным именем помечено
  как неактуальное, и True - в противном случае.

--== Пример кода, добавляющего новую запись в модель:
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName('data.sqlite')
con.open()
stm = QtSql.QSqlTableModel()
stm.setTable('good')
stm.select()
rec = con.record('good')
rec.setValue('goodname', 'Коврик для мыши' )
rec.setValue('goodcount', 2)
stm.insertRecord(-1, rec)

--== Пример кода, редактирующего существующую запись с индексом 3:
rec = stm.record(З)
rec.setValue('goodcount', 5)
stm.setRecord(З, rec)

Класс QSqlTableModel поддерживает такие сигналь􀁂:
♦ primeInsert(<Индекс>, <Запись QSqlRecord>) - генерируется при вызове метода
  insertRows() перед добавлением каждой из записей в модель. В первом параметре доступен
  целочисленный индекс добавляемой записи, а во втором - сама добавляемая
  запись, пустая, в которую можно занести какие-либо значения по умолчанию;
♦ beforeInsert(<Запись QSqlRecord>) - генерируется перед добавлением новой записи
  в таблицу. В параметре доступна добавляемая запись;
♦ beforeUpdate(<Индекс>, <Запись QSqlRecord>) - генерируется перед изменением записи
  в таблице. В параметрах доступны целочисленный индекс изменяемой записи и сама
  изменяемая запись;
♦ beforeDelete (<Индекс>) - генерируется перед удалением записи из таблицы. В параметре
  доступен целочисленный индекс удаляемой записи;
♦ dataChanged( <Индекс QSqlRecord 1>, <Индекс QSqlRecord 2>, roles=[] ) - генерируется
  при изменении данных в модели пользователем. Первым параметром передается
  индекс верхней левой из набора измененных записей, вторым - индекс правой нижней.
  Необязательный параметр roles хранит список ролей, данные которых изменились.
  Если указан пустой список, значит, изменились данные во всех ролях.
  Сигнал dataChanged - идеальное место для вызова методов submit() или submitAll()
  в случае, если у модели был задан режим редактирования OnManualSubmit. Как мы знаем,
  эти методы выполняют сохранение отредактированных данных в базе.
"""
import PySide6.QtCore
from PySide6.QtWidgets import (QMainWindow,
                               QTableView,
                               QVBoxLayout,
                               QPushButton,
                               QWidget,
                               )
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса представления таблицы QTableView, класса вертикальной стопки для виджетов QVBoxLayout,
класса виджета кнопки QPushButton, класса базового пустого виджета QWidget

Импорт из модуля PySide6.QtSql класса соединений с базами данных QSqlDatabase,
класса модели таблицы базы данных QSqlTableModel

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
        self.setWindowTitle('Модель, связанная с таблицей БД')  # установка заголовка главного окна приложения
        self.resize(270, 350)  # установка исходного размера окна
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
    sqlite_con.setDatabaseName('data.sqlite')  # подключение базы данных
    sqlite_con.open()  # открытие базы данных
    sql_table_model = QSqlTableModel()  # создаем модель таблицы
    sql_table_model.setTable('good')  # устанавливаем связь с таблицей БД
    sql_table_model.setSort(1, Qt.SortOrder.AscendingOrder)  # устанавливаем порядок сортировки по столбцу 1
    sql_table_model.select()  # производим чтение данных из таблицы
    # устанавливаем названия столбцов
    sql_table_model.setHeaderData(1, Qt.Orientation.Horizontal, 'Название')
    sql_table_model.setHeaderData(2, Qt.Orientation.Horizontal, 'Кол-во')
    window.table_view.setModel(sql_table_model)  # привязываем к представлению созданную модель
    window.table_view.hideColumn(0)  # скрываем первый столбец с идентификаторами
    window.table_view.setColumnWidth(1, 150)  # устанавливаем ширину столбца
    window.table_view.setColumnWidth(2, 60)

    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
