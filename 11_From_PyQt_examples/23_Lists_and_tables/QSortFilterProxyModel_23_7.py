"""
Списки и таблицы. Промежуточные модели

Одну модель можно установить в нескольких представлениях. При этом изменение порядка
следования элементов в одном представлении повлечет за собой изменение порядка
следования элементов в другом. Чтобы предотвратить изменение порядка следования
элементов в базовой модели, следует создать промежуточную модель с помощью класса
QSortFilterProxyModel из модуля QtCore и установить ее в представлении. Иерархия
наследования класса QSortFilterProxyModel выглядит так:
QObject - QAbstractItemModel - QAbstractProxyModel - QSortFilterProxyModel
Формат конструктора класса QSortFilterProxyModel:
QSortFilterProxyModel([parent=None])
Класс QSortFilterProxyModel наследует следующие методы из класса QAbstractProxyModel
(здесь приведены только основные - полный их список можно найти на странице
https://doc.qt.io/qt-6/qabstractproxymodel.html):
♦ setSourceModel(<Модель>) - устанавливает базовую модель;
♦ sourceModel() - возвращает ссылку на базовую модель.
Класс QSortFilterProxyModel поддерживает основные методы обычных моделей и дополнительно
определяет следующие основные методы (полный их список можно найти на странице
https://doc.qt.io/qt-6/qsortfilterproxymodel.html):
♦ sort(<Индекс столбца>[, order=SortOrder.AscendingOrder]) - производит сортировку.
Если во втором параметре указан элемент AscendingOrder перечисления SortOrder из модуля
QtCore.Qt, сортировка производится в прямом порядке, а если элемент DescendingOrder
того же перечисления - в обратном. Если в параметре <Индекс столбца> указать значение -1,
будет использован порядок следования элементов из базовой модели.
ПРИМЕЧАНИЕ:
Чтобы включить сортировку столбцов пользователем, следует передать значение True в метод
setSortingEnabled() объекта представления.
♦ setSortRole(<Роль>) - задает роль (itemdatarole_23_3.py), по которой производится сортировка.
  По умолчанию сортировка производится по роли itemDataRole.DisplayRole;
♦ setSortCaseSensitivity(<Режим>) - если в качестве параметра указать элемент CaseInsensitive
  перечисления CaseSensitivity из модуля QtCore.Qt, при сортировке регистр символов
  учитываться не будет, а если элемент CaseSensitive того же перечисления - то будет;
♦ setSortLocaleAware(<Флаг>) - если в качестве параметра указать значение True, при сортировке
  будут учитываться настройки локали;
♦ setFilterFixedString(<Фрагмент>) - выбор из модели элементов, которые содержат заданный
  фрагмент. Если указать пустую строку, в результат попадут все строки из базовой модели.
  Метод является слотом;
♦ setFilterRegularExpression() - выбор из модели элементов, соответствующих указанному
  регулярному выражению. Если указать пустую строку, в результат попадут все строки из
  базовой модели. Форматы метода:
  setFilterRegularExpression(<Регулярное выражение QRegularExpression>)
  setFilterRegularExpression(<Строка с регулярным выражением>)
  Второй формат метода является слотом;
♦ setFilterWildcard(<Шаблон>) - выбор из модели элементов, соответствующих указанной строке,
  которая может содержать подстановочные знаки:
  • ? - один любой символ;
  • * - нуль или более любых символов;
  • [...] - диапазон значений.
  Остальные символы трактуются как есть. Если в качестве параметра указать пустую строку,
  в результат попадут все элементы из базовой модели. Метод является слотом;
♦ setFilterKeyColumn(<Индекс>) - задает индекс столбца, по которому будет производиться
  фильтрация. Если в качестве параметра указать значение -1, будут просматриваться
  элементы во всех столбцах. По умолчанию фильтрация производится по первому столбцу;
♦ setFilterRole(<Роль>) - задает роль (itemdatarole_23_3.py), по которой производится
  фильтрация. По умолчанию фильтрация производится по роли ItemDataRole. DisplayRole;
♦ setFilterCaseSensitivity(<Режим>) - если в качестве параметра указать элемент
  CaseInsensitive перечисления CaseSensitivity из модуля QtCore.Qt, при фильтрации регистр
  символов учитываться не будет, а если элемент CaseSensitive того же перечисления - то будет;
♦ setRecursiveFilteringEnabled(<Флаг>) - если в качестве параметра указано True, также
  будет выполняться фильтрация вложенных элементов, и у всех вложенных элементов,
  соответствующих фильтру, будут видны родители. Если False, дочерние элементы фильтроваться
  не будут (поведение по умолчанию);
♦ setAutoAcceptChildRows(<Флаг>) - если в качестве параметра указано True, у родительских
  элементов будут показываться все дочерние элементы, даже не удовлетворяющие заданному
  фильтру. Если False, будут показываться лишь дочерние элементы, удовлетворяющие фильтру
  (поведение по умолчанию);
♦ setDynamicSortFilter(<Флаг>) - если в качестве параметра указано значение False, при
  изменении базовой модели не будет производиться повторная: сортировка или фильтрация.
"""

from PySide6.QtWidgets import (QMainWindow,
                               QTableView,
                               QVBoxLayout,
                               QWidget,
                               QLabel,
                               QLineEdit,
                               )
from PySide6.QtGui import (QStandardItemModel,
                           QIcon,
                           QStandardItem,
                           )
from PySide6.QtCore import QSortFilterProxyModel, Qt
import os

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow,
класса представления таблицы QTableView, класс вертикальной стопки для виджетов QVBoxLayout,
класса базового пустого виджета QWidget, класса ярлыка QLabel, 
класс однострочного редактируемого текстового поля QLineEdit

Импорт из модуля PySide6.QtCore класса модели двухмерной модели QStandardItemModel,
класса иконок QIcon, класса стандартного элемента модели QStandardItem

Импорт из модуля PySide6.QtCore класса модели управления сортировкой и фильтрацией QSortFilterProxyModel,
класса перечислителя настроек виджетов Qt

Импорт модуля для работы с переменными среды os
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект, объект верхнего уровня
        """
        super().__init__(parent)  # вызов конструктора родительского класса через функцию super()
        # QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Промежуточные модели, сортировка и фильтрация')  # установка заголовка главного окна
        self.resize(500, 600)  # установка исходного размера главного окна
        self.table_view_1 = QTableView()  # создание экземпляра табличного представления
        self.table_view_2 = QTableView()  # создание экземпляра табличного представления
        self.table_model = QStandardItemModel()  # создание модели таблицы
        # создаем списки элементов строк таблицы
        lst_1 = ['Perl', 'PHP', 'Python', 'Ruby', 'C++']
        lst_2 = [' http://www.perl.org/', 'http://php.net/', 'https://www.python.org/',
                 'https://www.ruby-lang.org/', 'https://cplusplus.com/']
        lst_3 = [QIcon(os.path.join('data', 'perl.png')),
                 QIcon(os.path.join('data', 'php.png')),
                 QIcon(os.path.join('data', 'python.png')),
                 QIcon(os.path.join('data', 'ruby.png')),
                 QIcon(os.path.join('data', 'ruby.png'))]
        lst_4 = ['Перл', 'ПХП', 'Пайтон', 'Руби', 'Плюса']
        for name, link, ico, trans in zip(lst_1, lst_2, lst_3, lst_4):
            self.table_model.appendRow([QStandardItem(ico, ''),  # создаем экземпляры элементов модели
                                        QStandardItem(name),
                                        QStandardItem(link),
                                        QStandardItem(trans)])
        self.table_model.setHorizontalHeaderLabels(['Значок', 'Название', 'Сайт', 'Перевод'])  # задаем строку
        # заголовков столбцов
        self.table_proxy_model_1 = QSortFilterProxyModel()  # создание промежуточной модели для сортировки и фильтарции
        self.table_proxy_model_1.setSourceModel(self.table_model)  # подключение исходной модели данный к промежуточной
        # модели
        self.table_proxy_model_2 = QSortFilterProxyModel()
        self.table_proxy_model_2.setSourceModel(self.table_model)

        self.table_view_1.setModel(self.table_proxy_model_1)  # присоединяем модель к представлению
        self.table_view_1.setColumnWidth(0, 50)  # задаем исходную ширину столбца
        self.table_view_1.setColumnWidth(2, 200)
        self.table_view_1.setSortingEnabled(True)

        self.table_view_2.setModel(self.table_proxy_model_2)  # присоединяем модель к представлению
        self.table_view_2.setColumnWidth(0, 50)  # задаем исходную ширину столбца
        self.table_view_2.setColumnWidth(2, 200)
        self.table_view_2.setSortingEnabled(True)

        self.filter_field = QLineEdit()  # создание однострочного редактируемого поля для строки фильтрации
        self.filter_field.setPlaceholderText('Введите значение для фильтрации по названию')
        # размещение в редактируемом поле текста подсказки
        self.table_proxy_model_2.setFilterKeyColumn(1)  # включение фильтрации по 2-му столбцу
        self.table_proxy_model_2.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        # включение режима фильтрации без учета регистра
        self.filter_field.textChanged.connect(lambda txt: self.table_proxy_model_2.setFilterFixedString(txt))
        # сигнал на изменение текста и его обработчик с фильтрацией по образцу текста

        self.vbox = QVBoxLayout()  # создание вертикальной стопки для виджетов
        self.vbox.addWidget(QLabel('Первое представление'))  # добавление ярлыка с надписью
        self.vbox.addWidget(self.table_view_1)  # добавление представления в стопку
        self.vbox.addWidget(QLabel('Второе представление'))
        self.vbox.addWidget(self.table_view_2)
        self.vbox.addWidget(self.filter_field)

        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне приложения


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
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
