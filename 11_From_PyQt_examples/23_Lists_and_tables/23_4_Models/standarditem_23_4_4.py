"""
Модели. Класс элемента модели

Каждый элемент модели QStandardItemModel представлен классом QStandardItem из модуля
QtGui. Этот класс не только описывает элемент, но и позволяет создавать вложенные структуры,
в которых любой элемент может иметь произвольное количество вложенных в него
дочерних элементов или элементов-потомков (что пригодится при выводе иерархического
списка). Форматы конструктора класса:
QStandardItem()
QStandardItem(<Текст>)
QStandardItem(<Значок QIcon>, <Текст>)
QStandardItem(<Количество строк>[, <Количество столбцов>=l])
Последний формат задает количество дочерних элементов и столбцов в них.
Наиболее часто используемые методы класса QStandardItem приведены далее (полный их
список можно найти на странице https://doc.qt.io/qt-6/qstandarditem.html):
♦ setRowCount(<Количество строк>) - задает количество дочерних строк;
♦ setColumnCount(<Количество столбцов>) - задает количество столбцов в дочерних
  строках;
♦ rowCount() - возвращает количество дочерних строк;
♦ columnCount() - возвращает количество столбцов в дочерних строках;
♦ row() - возвращает индекс строки в дочерней таблице родительского элемента или значение
  -1, если элемент яе содержит родителя (находится на самом верхнем уровне иерархии);
♦ column() - возвращает индекс столбца в дочерней таблице родительского элемента или
  значение -1, если элемент не содержит родителя;
♦ setChild(<Строка>, <Столбец>, <Элемент QStandard:I:tem>) - устанавливает заданный
  третьим параметром элемент в указанную ячейку дочерней таблицы текущего элемента.
♦ appendRow(<Список элементов QStandardItem>) - добавляет одну строку в конец дочерней
  таблицы текущего элемента. В качестве параметра указывается список отдельных
  столбцов;
♦ appendRow(<Элемент QStandardItem>) - добавляет заданный элемент в конец дочерней
  таблицы текущего элемента, формируя строку с одним столбцом;
♦ appendRows(<Список элементов QStandardItem>) - добавляет несколько строк, содержащих
  по одному столбцу, в конец дочерней таблицы текущего элемента, В качестве параметра
  указывается список добавляемых строк;
♦ appendColumn(<Список элементов QStandardItem>) - добавляет один столбец в конец
  дочерней таблицы текущего элемента. В качестве параметра указывается список отдельных
  строки;
♦ insertRow(<Индекс строки>, <Список элементов QStandardItem>) - вставляет одну
  строку в указанную позицию дочерней таблицы у текущего элемента. В качестве параметра
  <Список> указывается список объектов отдельных столбцов;
♦ insertRow(<Индекс строки>, <Элемент QStandardItem>) - вставляет заданный элемент
  в указанную позицию дочерней таблицы у текущего элемента, формируя строку с одним
  столбцом;
♦ insertRows(<Индекс строки>, <Список элементов QStandardItem>) - вставляет несколько
  строк, содержащих по одному столбцу, в указанную позицию дочерней таблицы у текущего
  элемента. В качестве параметра <Список> указывается список отдельных строк;
♦ insertRows(<Индекс строки>, <Количество>) - вставляет заданное количество пустых
  строк в указанную позицию дочерней таблицы для текущего элемента;
♦ insertColumn(<Индекс столбца>, <Список элементов QStandardItem>) - вставляет один
  столбец в указанную позицию дочерней таблицы у текущего элемента. В качестве параметра
  <Список> указывается список отдельных строк;
♦ insertColumns (<Индекс>, <Количество>) - вставляет заданное количество пустых
  столбцов в указанную позицию дочерней таблицы у текущего элемента;
♦ removeRow(<Индекс>) - удаляет строку с указанным индексом;
♦ removeRows(<Индекс>, <Количество>) - удаляет указанное количество строк, начиная со
  строки, имеющей заданный индекс;
♦ removeColumn(<Индекс>) - удаляет столбец с указанным индексом;
♦ removeColumns(<Индекс>, <Количество>) - удаляет указанное количество столбцов, начиная
  со столбца, имеющего заданный индекс;
♦ takeChild(<Строка>[, <Столбец>=0]) - удаляет указанный дочерний элемент и возвращает
  его в виде объекта класса QStandardItem;
♦ takeRоw(<Индекс>) - удаляет указанную строку из дочерней таблицы и возвращает ее
  в виде списка объектов класса QStandardItem;
♦ takeColumn(<Индекс>) - удаляет указанный столбец из дочерней таблицы и возвращает
  его в виде списка объектов класса QStandardItem;
♦ parent() - возвращает ссылку на родительский элемент (объект класса QStandardItem)
  или значение None, если текущий элемент не имеет родителя;
♦ child(<Строка>[, <Столбец>=0]) - возвращает ссылку на дочерний элемент (объект
  класса QStandardItem) или значение None, если такового нет;
♦ hasChildren() - возвращает значение True, если существует хотя бы один дочерний
  элемент, и False - в противном случае;
♦ setData(<Значение>[, role=ItemDataRole.UserRole+1]) - устанавливает значение для
  указанной роли;
♦ data([<Роль>=ItemDataRole.UserRole+1]) - возвращает значение, которое соответствует
  указанной роли;
♦ setText (<Текст>) - задает текст элемента;
♦ text() - возвращает текст элемента;
♦ setTextAlignment(<Выравнивание>) - задает выравнивание текста внутри элемента в
  виде элемента перечисления AlignmentFlag из модуля QtCore.Qt;
♦ setIcon( <Значок QIcon>) - задает значок, который будет отображен перед текстом;
♦ setToolTip(<Текст>) - задает текст всплывающей подсказки;
♦ setWhatsThis(<Текст>) - задает текст расширенной подсказки;
♦ setFont(<Шрифт QFont>) - задает шрифт элемента;
♦ setBackground(<Цвет QBrush>) - задает цвет фона;
♦ setForeground(<Цвет QBrush>) - задает цвет текста;
♦ setCheckable(<Флаг>) - если в качестве параметра указано значение True, после текста
  элемента будет выведен флажок, который можно устанавливать и сбрасывать;
♦ isCheckable() - возвращает значение True, если после текста элемента выводится флажок,
  и False - в противном случае;
♦ setCheckState(<Статус>) - задает состояние флажка. Могут быть указаны следующие
  элементы перечисления CheckState из модуля QtCore.Qt: Unchecked (флажок сброшен),
  PartiallyChecked (находится в неопределенном состоянии) и Checked (установлен);
♦ checkState() - возвращает текущее состояние флажка в виде элемента перечисления
  CheckState из модуля QtCore.Qt;
♦ setUserTristate(<Флаг>) - если в качестве параметра указано значение True, флажок
  может иметь три состояния: установленное, сброшенное и неопределенное (промежуточное);
♦ isUserTristate() - возвращает значение True, если флажок может иметь три состоя-
  ния, и False - в противном случае;
♦ setFlags(<Флаги>) - задает свойства элемента (см. modelindex_23_4_1.py);
♦ flags () - возвращает значение установленных свойств элемента;
♦ setSelectable(<Флаг>) - если в качестве параметра указано значение True, пользователь
  может выделить элемент;
♦ setEditable(<Флаг>) - если в качестве параметра указано значение True, пользователь
  может редактировать текст элемента;
♦ setDragEnabled(<Флаг>) - если в качестве параметра указано значение True, перетаскивание
  элемента разрешено;
♦ setDropEnabled(<Флаг>) - если в качестве параметра указано значение True, сброс
  перетаскиваемых данных в элемент разрешен;
♦ setEnabled(<Флаг>) - если в качестве параметра указано значение True, пользователь
  может взаимодействовать с элементом. Значение False делает элемент недоступным;
♦ clone() - возвращает копию элемента в виде объекта класса QStandardItem;
♦ index() - возвращает индекс элемента (объект класса QModelIndex);
♦ model() - возвращает ссылку на модель (объект класса QStandardItemModel);
♦ sortChildren(<Индекс столбца>[, order=SortOrder.AscendingOrder]) - производит
  сортировку дочерней таблицы. Если во втором параметре указан элемент AscendingOrder
  перечисления sortOrder из модуля QtCore.Qt, сортировка производится в прямом порядке,
  а если элемент DescendingOrder того же перечисления - в обратном.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QTreeView,
                               )
from PySide6.QtGui import QStandardItem, QStandardItemModel
"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow,
класса представления иерархического списка QTreeView

Импорт из модуля PySide6.QtGui класса элемента модели QStandardItem,
класса стандартной двухмерная модели QStandardItemModel
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект верхнего уровня
        """
        # super(parent).__init__()  # вызов конструктора родительского класса через функцию super()
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Класс элемента модели')  # установка заголовка главного окна приложения
        self.resize(300, 300)  # установка исходного размера главного окна приложения
        self.tree_view = QTreeView()  # создание представления иерархического списка
        self.standard_item_model = QStandardItemModel()  # создание модели иерархического списка
        # сборка иерархического списка
        rootitem_1 = QStandardItem('QAbstractItemView')
        rootitem_2 = QStandardItem('Базовый класс')
        item_1 = QStandardItem('QListView')
        item_1.setToolTip('Список')  # добавление подсказки к элементу
        item_2 = QStandardItem('Список')
        item_2.setCheckable(True)
        rootitem_1.appendRow([item_1, item_2])
        item_3 = QStandardItem('QTableView')
        item_4 = QStandardItem('Таблица')
        rootitem_1.appendRow([item_3, item_4])
        item_5 = QStandardItem('QTreeView')
        item_6 = QStandardItem('Иерархический список')
        rootitem_1.appendRow([item_5, item_6])
        self.standard_item_model.appendRow([rootitem_1, rootitem_2])
        self.standard_item_model.setHorizontalHeaderLabels(['Класс', 'Описание'])
        self.standard_item_model.itemChanged.connect(lambda item: print(f'{item.text()} - {item.checkState()}'))
        # обработчик сигнала на изменение элемента списка

        self.tree_view.setModel(self.standard_item_model)  # подключение модели к представлению
        self.tree_view.setColumnWidth(0, 170)
        self.setCentralWidget(self.tree_view)  # размещение представления в главном окне приложения


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
