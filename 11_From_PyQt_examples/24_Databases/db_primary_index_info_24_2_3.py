"""
Получение данных о базе данных. Получений сведений о ключевом индексе

Сведения о ключевом индексе, возвращаемые методом primaryIndex() класса QSqlDatabase,
представляются объектом класса QSqlIndex. Он наследует все методы класса QSqlRecord,
тем самым позволяя узнать, в частности, список полей, на основе которых создан индекс.
Также он определяет следующие методы:
♦ name() - возвращает имя индекса или пустую строку для ключевого индекса;
♦ isDescending(<Номер поля>) - возвращает True, если поле с указанным номером в индексе
  отсортировано по убыванию, и False - в противном случае.
Полное описание класса QSqlIndex приведено на странице https://doc.qt.io/qt-6/qsqlindex.html.
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
    primary_index = sqlite_con.primaryIndex('albums')  # запрос данных ключевого индекса из таблички базы данных
    window.append_txt(f'Объект ключевого индекса: {str(primary_index)}')
    primary_index.setName('Тро-ло-ло')  # установка имени для индекса
    window.append_txt(f'Имя ключевого индекса: {str(primary_index.name())} (если пусто, то имя не задано)')
    window.append_txt(f'Сортировка по убыванию: {str(primary_index.isDescending(0))}')
    sqlite_con.close()  # закрытие базы данных
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
