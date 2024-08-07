"""
Выполнение SQL-запросов

Чтобы выполнить запрос к базе, сначала следует создать объект класса QSqlQuery. Для этого
используется один из следующих форматов вызова его конструктора:
QSqlQuery([<SQL-кoд>] [, db=QSqlDatabase()])
QSqlQuery(<Соединение с базой данных QSqlDatabase>)
QSqlQuery(<Объект класса QSqlQuery>)
Первый формат позволяет сразу задать SQL-кoд, который следует выполнить, и немедленно
запустить его на исполнение. Необязательный параметр db задает соединение с базой данных,
запрос к которой следует выполнить, если он не указан, будет использоваться соединение
по умолчанию.
Второй формат создает пустой запрос, не содержащий ни SQL-кода, ни каких-либо прочих
параметров, и сразу задает соединение с указанной базой данных. Третий запрос создает
копию запроса, переданного в параметре.
Для выполнения запросов используются следующие методы класса QSqlQuery:
♦ exec(<SQL-кoд>) - немедленно выполняет переданный в параметре SQL-кoд. Если последний
  был успешно выполнен, возвращает True и переводит запрос в активное состояние,
  в противном случае возвращает False.
  ПРИМЕЧАНИЕ:
  Метод exec() с немедленным выполнением запроса следует использовать в тех случаях,
  если SQL-запрос не принимает параметров. В противном случае следует предварительно
  подготовить запрос.
♦ prepare(<SQL-кoд>) - подготавливает запрос с заданным SQL-кодом к выполнению.
  Применяется, если SQL-запрос содержит параметры. Параметры в коде запроса могут
  быть либо позиционными (в стиле ODBC - заданные вопросительными знаками), либо
  именованными (в стиле Oracle - задаются произвольными именами, предваренными
  знаком двоеточия). Метод возвращает True, если SQL-запрос был успешно подготовлен,
  и False - в противном случае;
♦ exec() - выполняет подготовленный ранее запрос. Возвращает True, если запрос был
  успешно выполнен, и False - в противном случае;
♦ addBindValue(<Значение параметра> [, paramType=ParamType.In]) - задает значение
  очередного по счету позиционного параметра: первый вызов этого метода задает значение
  первого параметра, второй вызов - второго и т. д. Необязательный параметр
  paramType указывает тип параметра - здесь практически всегда используется элемент In
  перечисления ParamType из класса QSql, означающий, что этот параметр служит для занесения
  значения в запрос.
♦ bindValue() - задает значение позиционного параметра с указанным порядковым номером
  (нумерация параметров начинается с нуля) либо именованного параметра с указанным именем.
  Формат метода:
  bindValue(<Номер параметра>, <Значение параметра>[, paramType=ParamType.In])
  bindValue(<Имя параметра>, <Значение параметра>[, paramType=ParamType.In])
♦ execBatch([mode=BatchExecutionMode.ValuesAsRows]) если в вызове метода
  addBindValue() или bindValue() вторым параметром бьш указан список, выполнит подготовленный
  запрос.
  Необязательный параметр mode указывает, как будут интерпретироваться отдельные
  элементы заданного списка. В настоящее время в качестве его значения для всех форматов
  баз данных поддерживается лишь элемент ValuesAsRows перечисления
  BatchExecutionMode из класса QSqlQuery, указывающий, что подготовленный запрос
  должен быть выполнен столько раз, сколько элементов присутствует в списке, при этом
  на каждом выполнении запроса в его код подставляется очередной элемент списка.
  Метод возвращает True, если запрос бьш успешно выполнен, и False - в противном
  случае.
♦ setForwardOnly(<Флаг>) - если передано значение True, по результату запроса можно
  будет перемещаться только «вперед», т. е. от начала к концу. Такой режим выполнения
  запроса существенно сокращает потребление системных ресурсов. Этот метод должен
  быть вызван перед выполнением запроса, который возвращает результат, например:
  query.prepare("select * from good order by goodname")
  query.setForwardOnly(True)
  query.exec()
"""

from PySide6.QtWidgets import (QMainWindow,
                               QPlainTextEdit,
                               )
from PySide6.QtSql import QSqlDatabase, QSqlQuery

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса многострочного редактируемого текстового поля для простого текста QPlainTextEdit

Импорт из модуля PySide6.QtSql класса соединений с базами данных QSqlDatabase,
класса запросов QSqlQuery
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
        self.setWindowTitle('Получение данных о таблицах базы данных')  # установка заголовка главного окна приложения
        self.resize(600, 600)  # установка исходного размера окна
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


def main():
    """
    Код примеров
    :return:
    """
    sqlite_con = SQLiteDatabaseConnection('data.sqlite')  # создание объекта соединения с базой данных
    sqlite_con.open()  # открытие базы данных
    QSqlQuery().exec('DROP TABLE [IF EXISTS] good')  # удаление тестовой таблицы из базы данных если она существует

    # --== Использование метода exec() ==--
    # FIXME что-то не работает
    query = QSqlQuery()  # создание объекта запроса
    window.append_txt(f'Список таблиц до создания таблицы good: {str(sqlite_con.tables())}')
    query.exec('CREATE TABLE good(id integer primary key autoincrement, goodname text, goodcount integer)')
    window.append_txt(f'Список таблиц после создания таблицы good: {str(sqlite_con.tables())}')

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
