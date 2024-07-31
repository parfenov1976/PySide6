"""
Получение данных о базе данных. Получений сведений об ошибках

Сведения об ошибке, возникшей при работе с базой данных, представляются объектом
класса QSqlError. Выяснить, что за ошибка произошла и каковы ее причины, позволят следующие
методы этого класса:
♦ type() - возвращает код ошибки в виде одного из следующих элементов перечисления
  ErrorType из класса QSqlError:
  • NoError - никакой ошибки не возникло;
  • ConnectionError - ошибка соединения с базой данных;
  • StatementError - ошибка в коде SQL-зaпpoca;
  • TransactionError - ошибка в обработке транзакции;
  • UnknownError - ошибка неустановленной природы.
Если код ошибки не удается определить, возвращается -1;
♦ text() - возвращает полное текстовое описание ошибки (фактически - значения, возвращаемые
  методами databaseText() и driverText(), объединенные в одну строку);
♦ databaseText () - возвращает текстовое описание ошибки, сгенерированное базой данных;
♦ driverText() - возвращает текстовое описание ошибки, сгенерированное драйвером
  базы данных, который входит в состав PySide6;

♦ nativeErrorCode() - возвращает строковый код ошибки, специфический для выбранного
  формата баз данных;
♦ isValid() - возвращает True, если текущий объект корректен (описывает реально возникшую
  ошибку), и False - в противном случае.
Пример:
con = QtSql.QSqlDatabase.addDatabase('QSQLITE')
con.setDatabaseName ('data.sqlite')
if con.open():
    # Работаем с базой данных
else:
    # Выводим текст описания ошибки
    print(con.lastError().text())
Полное описание класса QSqlError можно найти на странице https://doc.qt.io/qt-6/qsqlerror.html.
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
    sqlite_con.open()  # открытие базы данных
    window.append_txt(str(sqlite_con.tables()) + '\n')  # вывод списка таблиц базы данных
    db_error = sqlite_con.lastError()  # запрос данных по последней ошибке в БД
    window.append_txt(f'Объект данных об ошибке: {str(db_error)}')
    window.append_txt(f'Тип ошибки: {str(db_error.type())}')
    window.append_txt(f'Текстовое описание ошибки: {str(db_error.text())}')
    window.append_txt(f'Код ошибки используемого формата базы данных: {str(db_error.nativeErrorCode())}')
    window.append_txt(f'Возникла ли ошибка: {str(db_error.isValid())}')
    sqlite_con.close()  # закрытие базы данных
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
