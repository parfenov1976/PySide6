"""
Получение данных о базе данных. Получений сведений о таблицах

Сведения о структуре таблицы можно получить вызовом метода record() класса
QSqlDatabase. Эти сведения представляются объектом класса QSqlRecord.
Для получения сведений о полях таблицы используются следующие методы этого класса:
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
  и False -в противном случае;
♦ isEmpty() -возвращает True, если в таблице нет полей, и False - в противном случае.
  Полное описание класса QSqlRecord приведено на странице https://doc.qt.io/qt-6/qsqlrecord.html.
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
    sqlite_con.open()  # открытие базы
    window.append_txt(str(sqlite_con.tables()))  # вывод списка таблиц базы данных
    table = sqlite_con.record('albums')  # запрос структуры одной из таблиц базы данных
    window.append_txt(str(table))  # вывод данных объекта информации о таблице
    window.append_txt(f'Количество полей в таблице: {str(table.count())}')
    window.append_txt(f'Имя поля 1: {str(table.fieldName(1))}')
    window.append_txt(f'Индекс поля AlbumId: {str(table.indexOf('AlbumId'))}')
    window.append_txt(f'В таблице существует поле ArtistId: {str(table.contains('ArtistId'))}')
    sqlite_con.close()  # закрытие базы
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
