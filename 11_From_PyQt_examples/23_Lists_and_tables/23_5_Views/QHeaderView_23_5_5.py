"""
Представления. Управление заголовками строк и столбцов

Класс QHeaderView представляет заголовки строк и столбцов в компонентах QTableView и
QTreeView. Получить ссылки на заголовки в классе QTableView позволяют методы
horizontalHeader() и verticalHeader(), а для установки заголовков предназначены методы
setHorizontalHeader() и setVerticalHeader(). Получить ссылку на заголовок в классе
QTreeView позволяет метод header(), а для установки заголовка предназначен метод
setHeader(). Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QFrame - QAbstractScrollArea -
QAbstractItemView - QHeaderView
Формат конструктора класса QHeaderView:
QHeaderView(<Ориентация>[, parent=None])
В качестве ориентации указываются элементы Horizontal(горизонтальная) или Vertical
(вертикальная) перечисления Orientation из модуля QtCore.Qt.
Класс QHeaderView наследует все методы и сигналы класса QAbstractItemView
(см. QAbstractItemView_23_5_1.py) и дополнительно определяет следующие основные методы
(полный их список можно найти на странице https://doc.qt.io/qt-6/qheaderview.html):
♦ count() - возвращает количество секций в заголовке. Получить количество секций
  можно также с помощью функции len();
♦ setDefaultSectionSize(<Размер>) - задает размер секций по умолчанию;
♦ defaultSectionSize() - возвращает размер секций по умолчанию;
♦ setMinimumSectionSize(<Размер>) - задает минимальный размер секций;
♦ minimumSectionSize() - возвращает минимальный размер секций;
♦ setMaximumSectionSize(<Размер>) - задает максимальный размер секций;
♦ maximumSectionSize() -возвращает максимальный размер секций;
♦ resizeSection(<Индекс>, <Размер>) - задает новый размер у секции с указанным индексом;
♦ sectionSize(<Индекс>) - возвращает размер секции с указанным индексом;
♦ setSectionResizeMode(<Режим>) - задает режим изменения размеров у всех секций.
  В качестве параметра могут быть указаны следующие элементы перечисления
  ResizeMode из класса QHeaderView:
  • Interactive - размер может быть изменен пользователем или программно;
  • stretch -секции равномерно распределяют свободное пространство между собой.
    Размер не может быть изменен ни пользователем, ни программно;
  • Fixed - размер может быть изменен только программно;
  • ResizeToContents - размер определяется автоматически по содержимому секции.
    Размер не может быть изменен ни пользователем, ни программно;
♦ setSectionResizeMode(<Индекс>, <Режим>) - задает режим изменения размеров у секции
  с указанным индексом;
♦ setStretchLastSection(<Флаг>) - если в качестве параметра указано значение True,
  последняя секция будет занимать все оставшееся свободное пространство;
♦ setCascadingSectionResizes(<Флаг>) - если в качестве параметра указано значение
  True, изменение размеров одной секции может привести к изменению размеров других
  секций;
♦ setSectionHidden(<Индекс>, <Флаг>) - если во втором параметре указано значение
  True, секция с индексом, указанным в первом параметре, будет скрыта. Значение False
  отображает секцию;
♦ hideSection(<Индекс>) - скрывает секцию с указанным индексом;
♦ showSection(<Индекс>) - отображает секцию с указанным индексом;
♦ isSectionHidden(<Индекс>) - возвращает значение True, если секция с указанным индексом
  скрыта, и False - в противном случае;
♦ sectionsHidden() - возвращает значение True, если существует хотя бы одна скрытая
  секция, и False - в противном случае;
♦ hiddenSectionCount() - возвращает количество скрытых секций;
♦ setDefaultAlignment(<Выравнивание>) - задает выравнивание текста внутри заголовков
  в виде элемента перечисления AlignmentFlag из модуля QtCore.Qt;
♦ setHighlightSections(<Флаг>) - если в качестве параметра указано значение True, то
  текст заголовка текущей секции будет выделен;
♦ setSectionsClickable(<Флаг>) - если в качестве параметра указано значение True, заголовок
  будет реагировать на щелчок мышью, при этом выделяя все элементы секции;
♦ setSectionsMovable(<Флаг>) - если в качестве параметра указано значение True, пользователь
  может перемещать секции с помощью мыши;
♦ sectionsMovable() - возвращает значение True, если пользователь может перемещать
  секции с помощью мыши, и False - в противном случае;
♦ moveSection(<Откуда>, <Куда>) - позволяет переместить секцию. В параметрах указываются
  визуальные индексы;
♦ swapSections(<Секция 1>, <Секция 2>) - меняет две секции местами. В параметрах
  указываются визуальные индексы;
♦ visualIndex(<Логический индекс>) - преобразует логический индекс (первоначальный
  порядок следования) в визуальный (отображаемый в настоящее время порядок следования).
  Если преобразование прошло неудачно, возвращается значение -1;
♦ logicalIndex(<Визуальный индекс>) - преобразует визуальный индекс (отображаемый
  в настоящее время порядок следования) в логический (первоначальный порядок следования).
  Если преобразование прошло неудачно, возвращается значение -1;
♦ saveState() - возвращает объект класса QByteArray с текущими размерами и положением
  секций;
♦ restoreState(<Объект QByteArray>) - восстанавливает размеры и положение секций на
  основе заданного объекта класса QByteArray, возвращаемого методом saveState().
Класс QHeaderView поддерживает следующие сигналы (здесь приведены только основные -
полный их список можно найти на странице https://doc.qt.io/qt-6/qheaderview.html):
♦ sectionPressed(<Логический индекс>) - генерируется при нажатии левой кнопки мыши
  над заголовком секции. Внутри обработчика через параметр доступен целочисленный
  логический индекс секции;
♦ sectionClicked(<Логический индекс>) - генерируется при нажатии и отпускании левой
  кнопки мыши над заголовком секции. Внутри обработчика через параметр доступен
  целочисленный логический индекс секции;
♦ sectionDoubleClicked(<Логический индекс>) - генерируется при двойном щелчке
  мышью на заголовке секции. Внутри обработчика через параметр доступен целочисленный
  логический индекс секции;
♦ sectionMoved(<Логический индекс>, <Старый визуальный индекс>, <Новый визуальный
  индекс>) - генерируется при изменении положения секции. Все параметры целочисленные;
♦ sectionResized(<Логический индекс>, <Старый размер>, <Новый размер>) - генерируется
  непрерывно при изменении размера секции. Все параметры целочисленные.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QTableView,
                               QVBoxLayout,
                               QWidget,
                               QPushButton,
                               )
from PySide6.QtGui import (QStandardItemModel,
                           QIcon,
                           QStandardItem,
                           )
from PySide6.QtCore import Qt
import os

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow,
класса представления таблицы QTableView, класс вертикальной стопки для виджетов QVBoxLayout,
класса базового пустого виджета QWidget, класса виджета кнопку QPushButton

Импорт из модуля PySide6.QtCore класса модели двухмерной модели QStandardItemModel,
класса иконок QIcon, класса стандартного элемента модели QStandardItem

Импорт из модуля PySide6.QtCore класса перечислителя свойств виджетов Qt

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
        self.setWindowTitle('Двухмерная модель')  # установка заголовка главного окна
        self.resize(500, 300)  # установка исходного размера главного окна
        self.table_view = QTableView(parent=self)  # создание экземпляра табличного представления
        self.table_model = QStandardItemModel()  # создание модели таблицы
        # создаем списки элементов строк таблицы
        lst_1 = ['Perl', 'РНР', 'Python', 'Ruby', 'C++']
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
        self.table_view.setModel(self.table_model)  # присоединяем модель к представлению
        self.table_view.setColumnWidth(0, 50)  # задаем исходную ширину столбца
        self.table_view.setColumnWidth(2, 200)
        self.h_header = self.table_view.horizontalHeader()  # извлекаем и сохраняем ссылку на горизонтальные заголовки
        self.v_header = self.table_view.verticalHeader()  # извлекаем и сохраняем ссылку на вертикальные заголовки
        self.btn_1 = QPushButton('Спрятать/показать 1-ый столбец')  # создаем кнопку
        self.btn_1.clicked.connect(lambda: self.h_header.setSectionHidden(0,
                                                                          not self.h_header.isSectionHidden(0)))
        # обработка сигнала нажатия на кнопку
        self.btn_2 = QPushButton('Поменять местами строки 1 и 4')
        self.btn_2.clicked.connect(lambda: self.v_header.swapSections(0, 3))
        self.h_header.setSectionsMovable(True)  # включает возможность перемещать столбцы с помощью мыши

        self.h_header.sectionMoved.connect(lambda logical_index, old_visual_index, new_visual_index:
                                           print(logical_index, old_visual_index, new_visual_index))
        # обработка сигнала на перемещение столбцов

        self.vbox = QVBoxLayout()  # создание вертикальной стопки для виджетов
        self.vbox.addWidget(self.table_view)  # добавление представления в стопку
        self.vbox.addWidget(self.btn_1)  # добавление кнопки в стопку
        self.vbox.addWidget(self.btn_2)
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
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
