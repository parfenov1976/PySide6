"""
Получение служебных сведений о запросе

Класс QSqlQuery также позволяет получить всевозможные служебные сведения о запросе.
Для этого применяются следующие методы:
♦ nuRowsAffected() - возвращает количество записей, обработанных в процессе выполнения
  запроса, или -1, если это количество не удается определить. Для запросов выборки
  данных возвращает None - в этом случае следует вызывать метод size();
♦ lastInsertId() - возвращает идентификатор последней добавленной записи. Если запрос
  не добавлял записи или если формат базы данных не позволяет определить идентификатор
  последней добавленной записи, возвращает None;
♦ lastError() - возвращает объект класса QSqlError, описывающий последнюю возникшую
  в базе данных ошибку;
♦ executedQuery() - возвращает SQL-кoд последнего выполненного запроса или пустую
  строку, если никакой запрос еще не был выполнен. В возвращенном коде запроса вместо
  параметров будут подставлены указанные у них значения;
♦ lastQuery() - возвращает код последнего выполненного запроса или пустую строку,
  если никакой запрос еще не был выполнен. В возвращенном коде запроса вместо параметров
  не будут подставлены указанные у них значения;
♦ boundValue(<Номер параметра>) - возвращает значение параметра запроса с указанным
  номером;
♦ boundValue(<Имя параметра>) - возвращает значение параметра запроса с указанным
  именем;
♦ boundValues() - возвращает словарь, ключами элементов которого служат имена параметров,
  а значениями элементов - значения этих параметров. В случае позиционных
  параметров в качестве ключей будут использованы произвольные строки вида :а для
  первого параметра, :bb для второго и т. д.
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
        self.setWindowTitle('Получение служебных сведений о запросе')  # установка заголовка главного окна приложения
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
    Код примера выполнения запроса и его очистки
    :return: None
    """
    sqlite_con = QSqlDatabase.addDatabase('QSQLITE')  # создание объекта соединения с базой данных
    sqlite_con.setDatabaseName('data.sqlite')  # подключение базы данных
    sqlite_con.open()  # открытие базы данных

    # Первый запрос и обработка его результатов
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

    # вывод количества обработанных записей, вернет 0 для запроса на выборку
    window.append_txt(f'\nКоличество записей обработано: {query.numRowsAffected()}')

    # вывод SQL-кода последнего запроса с параметрами если есть
    window.append_txt(f'\nSQL-код последнего запроса (с параметрами, если есть): {query.executedQuery()}')

    # вывод кода последнего запроса без параметров
    window.append_txt(f'\nКод последнего запроса без параметров: {query.lastQuery()}')

    # очистка запроса
    query.clear()

    # новый запрос
    query.exec('SELECT COUNT(*) AS CNT FROM good')  # выполнение запроса на подсчет количества строк
    query.first()  # позиционирование указателя запроса на первую запись результата
    window.append_txt(f'\nДанные о результатах нового запроса запроса{query.record()}')
    window.append_txt(f'\nКоличество строк в таблице {query.value('CNT')}')  # вывод значения поля из результата запроса
    window.append_txt(f'\nСостояние активности нового запроса: {query.isActive()}')

    # вывод SQL-кода последнего запроса с параметрами если есть
    window.append_txt(f'\nSQL-код последнего запроса (с параметрами, если есть): {query.executedQuery()}')

    # запрос данных о последней ошибке в БД
    window.append_txt(f'\nДанные о последней ошибке в БД: {query.lastError()}')
    window.append_txt(f'Была ли ошибка: {query.lastError().isValid()}')
    window.append_txt(f'Сообщение БД: {query.lastError().databaseText()}')
    window.append_txt(f'Сообщение драйвера БД: {query.lastError().driverText()}')
    window.append_txt(f'Код ошибки от БД {query.lastError().nativeErrorCode()}')
    window.append_txt(f'Текст ошибки: {query.lastError().text()}')
    window.append_txt(f'Тип ошибки: {query.lastError().type()}')

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
