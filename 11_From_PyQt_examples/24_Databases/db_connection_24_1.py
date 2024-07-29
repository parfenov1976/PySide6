"""
Работа с базами данных. Соединение с базой данных.

За соединение с базой данных и обработку транзакций отвечает класс QSqlDatabase.
Чтобы установить соединение с базой, следует вызвать статический метод addDatabase()
этого класса. Формат вызова:
addDatabase (<Формат базы данных> [, connectionName=""])
Формат базы данных указывается в виде одного из следующих строковых обозначений:
11QSQLITE" (SQLite) "QМYSQL" или "МARIADB" (MySQL или MariaDB), "QOCI" (Oracle), "QPSQL"
(PostgreSQL), "QDB2" (DB2) или "QODBC" (ODBC).
Вторым параметром можно задать имя соединения, что может оказаться полезным, если
программа одновременно работает с несколькими базами. Если имя соединения не указано,
устанавливаемое соединение будет помечено как используемое по умолчанию.
Метод addDatabase () возвращает объект класса QSqlDatabase, представляющий «пустое»
соединение с базой данных. В этот объект следует занести параметры базы, с которой требуется
соединиться, с помощью следующих методов класса QSqlDatabase:
♦ setHostName(<Хост>) - задает хост, на котором расположена база данных. Используется
  только для серверных баз данных наподобие MySQL;
♦ setPort(<Номер порта>) - задает номер ТСР-порта, через который будет выполнено
  подключение к хосту. Используется только для серверных баз данных и лишь в том случае,
  если для соединения с базой задействуется порт, отличный от порта по умолчанию;
♦ setDatabaseName(<Имя или путь к базе данных>) - задает имя базы данных (для серверных
  баз), путь к ней (для локальных баз данных, таких как SQLite) или полный набор
  параметров подключения (если используется ODBC);
♦ setUserName(<Имя>) - задает имя пользователя для подключения к базе. Используется
  только для серверных баз данных;
♦ setPassword(<Пароль>) - задает пароль для подключения к базе. Используется только
  для серверных баз данных;
♦ setConnectOptions(<Параметры>) - задает набор дополнительных параметров для подключения
  к базе в виде строки. Набор поддерживаемых дополнительных параметров различен в
  зависимости от выбранного формата и приведен в документации по классу QSqlDatabase.
Для работы с базой предназначены следующие методы класса QSqlDatabase:
♦ open() - открывает базу данных. Возвращает True, если база была успешно открыта,
  и False - в противном случае;
    ---===ВНИМАНИЕ!===---
    Перед созданием соединения с базой данных обязательно следует создать объект программы
    (объект класса QApplication). Если этого не сделать, PySide не сможет загрузить
    драйвер указанного формата баз данных, и соединение не будет создано.
    Открываемая база данных уже должна существовать на локальном диске или сервере.
    Единственное исключение - база формата SQLite, которая в случае ее отсутствия будет
    создана автоматически.
    ---===---
♦ open(<Имя>, <Пароль>) - открывает базу данных под указанными именем пользователя
  и паролем. Возвращает True, если база была успешно открыта, и False - в противном
  случае;
♦ isOpen() - возвращает True, если база данных в настоящее время открыта, и False -
  в противном случае;
♦ isOpenError() - возвращает True, если при попытке открытия базы данных возникли
  ошибки, и False - в противном случае;
♦ transaction() - запускает транзакцию, если формат базы поддерживает таковые. Если
  же формат базы не поддерживает транзакции, то не делает ничего. Возвращает True,
  если транзакция была успешно запущена, и False - в противном случае;
♦ commit() - подтверждает транзакцию, если формат базы поддерживает таковые. Если
  же формат базы не поддерживает транзакции, то не делает ничего. Возвращает True,
  если транзакция была успешно подтверждена, и False - в противном случае;
♦ rollback() - отклоняет транзакцию, если формат базы поддерживает таковые. Если же
  формат базы не поддерживает транзакции, то не делает ничего. Возвращает True, если
  транзакция была успешно отклонена, и False - в противном случае;
♦ lastError() - возвращает сведения о последней возникшей при работе с базой ошибке
  в виде объекта класса QSqlError;
♦ connectionName() - возвращает строку с именем соединения с базой или пустую строку
  для соединения по умолчанию;
♦ tables ([type=TableType.Tables]) - возвращает список таблиц, хранящихся в базе.
  В параметре type можно указать тип таблиц в виде одного из элементов перечисления
  TableType из класса QSql или их комбинации через оператор |:
  • Tables - обычные таблицы;
  • SystemTables - служебные таблицы;
  • Views - представления;
  • AllTables - все упомянутое ранее;
♦ record(<Имя таблицы>) - возвращает сведения о структуре таблицы с переданным именем,
  представленные объектом класса QSqlRecord, или пустой объект этого класса, если
  таблицы с таким именем нет;
♦ primaryIndex(<Имя таблицы>) - возвращает сведения о ключевом индексе таблицы
  с переданным именем, представленные объектом класса QSqlindex, или пустой объект
  этого класса, если таблицы с таким именем нет;
♦ close() - закрывает базу данных;
♦ isValid() - возвращает True, если текущий объект корректен, и False - в противном
  случае.
Также могут пригодиться следующие статические методы класса QSqlDatabase:
♦ contains([connectionName=""]) - возвращает True, если имеется соединение с базой
  данных с именем, указанным в параметре connectionName, и False - в противном случае;
♦ connectionNames() - возвращает список имен всех созданных соединений с базами
  данных. Соединение по умолчанию обозначается пустой строкой;
♦ database([connectionName=""] [, ] [open=True]) - возвращает сведения о соединении
  с базой данных, имя которого указано в параметре connectionName, в виде объекта класса
  QSqlDatabase. Если в параметре open указано значение True, база данных будет открыта.
  Если такового соединения нет, возвращается некорректно сформированный объект класса
  QSqlDatabase;
♦ cloneDatabase(<Соединение QSqlDatabase>, <Имя соединения>) - создает копию указанного
  в первом параметре соединения с базой и дает ему имя, заданное во втором
  параметре. Возвращаемый результат - объект класса QSqlDatabase, представляющий
  созданную копию соединения;
♦ removeDatabase(<Имя соединения>) - удаляет соединение с указанным именем. Соединение
  по умолчанию обозначается пустой строкой;
♦ isDriverAvailable(<Формат>) - возвращает True, если указанное в виде строки обозначение
  формата баз данных поддерживается PySide6, и False - в противном случае:
>> from PySide6 import QtSql
>> QtSql.QSqlDatabase.isDriverAvailable("QSQLITE")
   True
>> QtSql.QSqlDatabase.isDriverAvailable("QМSSQL")
   False
♦ drivers() - возвращает список обозначений всех форматов баз данных, с которыми
  в текущий момент может работать PySide6. Список может быть неполным, если на компьютере
  не установлены клиенты каких-либо из баз данных, поддерживаемых библиотекой.
Пример:
>> QtSql.QSqlDatabase.drivers()
   ['QSQLITE', 'QODBC', 'QPSQL']
Полное описание класса QSqlDatabase приведено на странице https://doc.qt.io/qt-6/qsqldatabase.html.
"""

from PySide6.QtWidgets import (QMainWindow,
                               QPlainTextEdit,
                               )
from PySide6.QtSql import QSqlDatabase
"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса многострочного редактируемого текстового поля для простого текста QPlainTextEdit

Импорт из модуля PySide6.QtSql класса соединений с базами данных QSqlDatabase
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
        self.setWindowTitle('Подключение баз данных')  # установка заголовка главного окна приложения
        self.resize(300, 300)  # установка исходного размера окна
        self.txt_field = QPlainTextEdit()  # создание многострочного текстового поля
        self.setCentralWidget(self.txt_field)  # размещение текстового поля в главном окне приложения

    def append_txt(self, txt: str) -> None:
        """
        Метод добавления текста в текстовое поле
        :param txt: str - текст для добавления в поле
        """
        self.txt_field.appendPlainText(txt)  # добавление текста


class SQLiteDatabaseConnection(QSqlDatabase):
    """
    Класс соединения с базой данных
    """

    def __init__(self, db_name: str) -> None:
        """
        Конструктов соединения с базой данных
        :param db_name: str - имя файла базы данных
        """
        QSqlDatabase.__init__(self, 'QSQLITE')  # явный вызов конструктора родительского класса
        self.setDatabaseName(db_name)  # подключение базы данных


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
    sqlite_con = SQLiteDatabaseConnection('data.sqlite')  # создание объекта соединения с базой данных
    sqlite_con.open()  # открытие базы
    window.append_txt(f'DB is open: {str(sqlite_con.isOpen())}')  # проверка наличия открытых баз данных
    window.append_txt(str(sqlite_con.record('data.sqlite')))  # вывод структуры таблицы
    window.append_txt(str(sqlite_con.tables()))  # вывод списка таблиц базы данных
    sqlite_con.close()  # закрытие базы
    window.append_txt(f'DB is open: {str(sqlite_con.isOpen())}')  # проверка наличия открытых баз данных
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
