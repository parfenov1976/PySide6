"""
Обработка результатов выполнения SQL запросов

Если был выполнен запрос на выборку данных (SQL-команда SELECT), следует получить
результат его выполнения. Для этого мы используем методы класса QSqlQuery, описанные
ниже.
Запрос на выборку данных поддерживает особый внутренний указатель, указывающий на
запись результата, содержимое которой в настоящее время доступно для получения. Однако
сразу после выполнения запроса этот указатель хранит неопределенное значение, не
идентифицирующее никакую реальную запись. Поэтому перед собственно выборкой данных
необходимо позиционировать этот указатель на нужную запись:
♦ first() - позиционирует указатель запроса на первую запись результата. Возвращает
  True, если позиционирование прошло успешно, и False - если результат пуст (не содержит
  записей);
♦ next() - позиционирует указатель запроса на следующую запись результата или на
  первую запись, если этот метод был вызван сразу после выполнения запроса. Возвращает
  True, если позиционирование прошло успешно, и False - если записей в результате
  больше нет, результат пуст или указатель ранее не был установлен ни на какую запись;
♦ previous() - позиционирует указатель запроса на предыдущую запись результата или
  на последнюю запись, если указатель в текущий момент находится за последней записью.
  Возвращает True, если позиционирование прошло успешно, и False - если записей
  в результате больше нет, результат пуст или указатель ранее не был установлен ни на
  какую запись;
♦ last() - позиционирует указатель запроса на последнюю запись результата. Возвращает
  True, если позиционирование прошло успешно, и False - если результат пуст;
♦ seek(<Номер записи>[, relative=False]) - позиционирует указатель на запись с указанным
  номером (нумерация записей начинается с нуля). Если необязательным параметром
  relative передано значение True, то позиционирование выполняется относительно
  текущей записи: положительные значения вызывают смещение указателя «вперед»
  (к концу), а отрицательные - «назад» (к началу). Возвращает True, если позиционирование
  прошло успешно, и False - в противном случае;
♦ isValid() - возвращает True, если указатель указывает на какую-либо запись, и False,
  если он имеет неопределенное значение;
♦ at() - возвращает номер записи, на которую указывает указатель результата, или отрицательное
  число, если указатель имеет неопределенное значение;
♦ size() - возвращает количество записей, возвращенных в результате выполнения запроса,
  или -1, если этот запрос не выполнял выборку данных.
Для собственно выборки данных следует применять описанные далее методы:
♦ value(<Индекс поля>) - возвращает значение поля текущей записи с заданным индексом.
  Поля нумеруются в том порядке, в котором они присутствуют в таблице базы или
  в SQL-коде запроса;
♦ value(<Имя поля>) - возвращает значение поля текущей записи с заданным именем;
♦ isNull(<Индекс поля>) - возвращает True, если в поле с указанным индексом нет значения,
  и False - в противном случае;
♦ isNull(<Имя поля>) - возвращает True, если в поле с указанным именем нет значения,
  и False - в противном случае;
♦ record() - если внутренний указатель установлен на какую-либо запись, возвращает
  сведения об этой записи, в противном случае возвращаются сведения о самой таблице.
  Возвращаемым результатом является объект класса QSqlRecord;
♦ record(<Индекс записи>) - возвращает сведения о записи с указанным индексом. Возвращаемым
  результатом является объект класса QSqlRecord;
♦ isSelect() - возвращает True, если был выполнен запрос на выборку данных, и False,
  если исполнялся запрос иного рода.
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
        self.setWindowTitle('Обработка результатов выполнения SQL запросов')
        # установка заголовка главного окна приложения
        self.resize(600, 600)  # установка исходного размера окна
        self.txt_field = QPlainTextEdit()  # создание многострочного текстового поля
        self.setCentralWidget(self.txt_field)  # размещение текстового поля в главном окне приложения

    def append_txt(self, txt: str) -> None:
        """
        Метод добавления текста в текстовое поле
        :param txt: str - текст для добавления в поле
        """
        self.txt_field.appendPlainText(txt)  # добавление текста


def main() -> None:
    """
    Код примера выполнения запроса на выборку данных и вывода его результатов
    :return: None
    """
    sqlite_con = QSqlDatabase.addDatabase('QSQLITE')  # создание объекта соединения с базой данных
    sqlite_con.setDatabaseName('data.sqlite')  # подключение базы данных
    sqlite_con.open()  # открытие базы данных

    query = QSqlQuery()  # создание объекта запроса
    query.exec('SELECT * FROM good ORDER BY goodname')  # выполнение запроса на выборку данных
    lst = []  # создание списка для сохранения результатов запроса
    if query.isActive():  # проверка активности запроса
        query.first()  # позиционирование указателя запроса на первую запись результата
        while query.isValid():  # выполнять пока указатель указывает на какую-либо запись
            lst.append(f'{query.value('goodname')}: {str(query.value('goodcount'))} шт.')  # формирование строки
            # по данным записи и сохранение в список для результатов
            query.next()  # позиционирование указателя на следующую запись
        for item in lst:  # вывод списка с результатами в текстовое поле
            window.append_txt(item)

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
