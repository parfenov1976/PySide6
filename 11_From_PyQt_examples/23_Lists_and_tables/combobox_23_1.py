"""
Списки и таблицы. Раскрывающийся список.

Класс QComboBox реализует раскрывающийся список с возможностью выбора единственного
пункта. Иерархия наследования выглядит так:
(QObject, QPaintDevice) - QWidget - QComboBox
Формат конструктора класса QComboBox:
QComboBox([parent=None])

Добавление, изменение и удаление элементов
=======================================
Для добавления, изменения, удаления и получения значений элементов предназначены следующие
методы класса QComboBox:
♦ addItem() - добавляет один элемент в конец списка. Форматы метода:
  addItem(<Текст элемента>[, <Данные>])
  addItem(<Значок QIcon>, <Текст элемента>[, <Данные>])
  В параметре <Значок> задается значок, который будет отображен перед текстом. Необязательный
  параметр <Данные> указывает произвольные данные, сохраняемые в элементе
  (например, индекс в таблице базы данных);
♦ addItems(<Список строк>) - добавляет несколько элементов в конец списка;
♦ insertItem() - вставляет один элемент в указанную позицию списка. Форматы метода:
  insertItem(<Индекс позиции>, <Текст элемента>[, <Данные>])
  insertItem(<Индекс позиции>, <Значок QIcon>, <Текст элемента>[; <Данные>])
♦ insertItems(<Индекс позиции>, <Список строк>) - вставляет несколько элементов в
  указанную позицию списка;
♦ insertSeparator(<Индекс позиции>) - вставляет разделительную линию в указанную
  позицию;
♦ setItemText (<Индекс>, <Строка>) - изменяет текст элемента с указанным индексом;
♦ setItemIcon (<Индекс>, <Значок QIcon>) - изменяет значок элемента с указанным индексом;
♦ setItemData (<Индекс>, <Данные> [, role=ItemDataRole.UserRole]) - изменяет данные
  у элемента с указанным индексом. Необязательный параметр role указывает роль, для
  которой задаются данные. Например, если указать элемент ToolTipRole перечисления
  ItemDataRole из модуля QtCore.Qt, данные зададут текст всплывающей подсказки, которая
  будет отображена при наведении курсора мыши на элемент. По умолчанию изменяются
  пользовательские данные;
♦ removeItem (<Индекс>) - удаляет элемент с указанным индексом;
♦ setCurrentIndex (<Индекс>) - делает элемент с указанным индексом текущим. Метод
  является слотом;
♦ currentIndex() - возвращает индекс текущего элемента;
♦ setCurrentText(<Текст>) - делает элемент с указанным текстом текущим. Метод является
  слотом;
♦ currentText() - возвращает текст текущего элемента;
♦ currentData([role=ItemDataRole.userRole]) - возвращает данные текущего элемента,
  относящиеся к заданной роли;
♦ itemText(<Индекс>) - возвращает текст элемента с указанным индексом;
♦ itemData(<Индекс> [, role=ItemDataRole. UserRole]) - возвращает данные, сохраненные
  в роли role элемента с индексом <Индекс>;
♦ count() - возвращает общее количество элементов списка. Получить количество элементов
  можно также с помощью функции len() ;
♦ clear() - удаляет все элементы списка. Метод является слотом.

Изменение параметров списка
===============================
Управлять параметрами раскрывающегося списка позволяют следующие методы класса
QComboBox:
♦ setEditable(<Флаг>) - если в качестве параметра указано значение True, пользователь
  сможет вводить текст в раскрывающийся список и, возможно, добавлять таким образом
  в него новые элементы;
♦ setInsertPolicy(<Режим>) - задает режим добавления в список элементов, введенных
  пользователем. В качестве параметра указываются следующие элементы перечисления
  InsertPolicy из класса QComboBox:
  • NoInsert - элемент не будет добавлен;
  • InsertAtTop - элемент вставляется в начало списка;
  • InsertAtCurrent - будет изменен текст текущего элемента;
  • InsertAtBottom - элемент добавляется в конец списка;
  • InsertAfterCurrent - элемент вставляется после текущего элемента;
  • InsertBeforeCurrent - элемент вставляется перед текущим элементом;
  • InsertAlphabetically - при вставке учитывается алфавитный порядок следования
    элементов;
♦ setEditText(<Текст>) - вставляет текст в поле редактирования. Метод является слотом;
♦ clearEditText() - удаляет текст из поля редактирования. Метод является слотом;
♦ setCompleter(<Список QCompleter>) - задает список вариантов значений для автозавершения;
♦ setValidator(<Валидатор>) - устанавливает валидатор в виде объекта класса, производного
  от QValidator;
♦ setDuplicatesEnabled(<Флаг>) - если в качестве параметра указано значение True,
  пользователь может добавить элемент с повторяющимся текстом. По умолчанию повторы
  запрещены;
♦ setMaxCount(<Количество>) - задает максимальное количество элементов в списке. Если
  до вызова метода количество элементов превышало это количество, лишние элементы
  будут удалены;
♦ setMaxVisibleItems(<Количество>) - задает максимальное количество видимых элементов
  в раскрывающемся списке;
♦ setMinimumContentsLength(<Количество>) - задает минимальное количество символов,
  которое должно помещаться в раскрывающемся списке;
♦ setSizeAdjustPolicy(<Режим>) - задает режим установки ширины списка при изменении
  содержимого. В качестве параметра указываются следующие элементы перечисления
  SizeAdjustPolicy из класса QComboBox:
  • AdjustToContents - ширина списка подстраивается под ширину текущего содержимого;
  • AdjustToContentsOnFirstShow - ширина списка подстраивается под ширину содержимого,
    имевшегося в списке при первом его отображении;
  • AdjustToMinimumContentsLengthWithIcon - используется значение минимальной
    ширины, которое установлено с помощью метода setMinimumContentsLength(), плюс
    ширина значка;
♦ setFrame(<Флаг>) - если в качестве параметра указано значение False, список будет
  отображаться без рамки;
♦ setIconSize(<Размеры QSize>) - задает максимальные размеры значков;
♦ showPopup() - разворачивает список;
♦ hidePopup() - сворачивает список.

Поиск элементов
======================
Произвести поиск элемента в списке позволяют методы findText() (по тексту элемента)
и findData() (по данным с указанной ролью). Методы возвращают индекс найденного элемента
или значение -1, если таковой не был найден. Форматы методов:
findText(<Текст>[, flags=MatchFlag.MatchExactly |
                        MatchFlag.MatchCaseSensitive])
findData(<Данные> [, role=ItemDataRole.UserRole] [,
                    flags=MatchFlag.MatchExactly | MatchFlag.MatchCaseSensitive])
Параметр flags задает режим поиска. В качестве значения через оператор | можно указать
комбинацию следующих элементов перечисления MatchFlag из модуля QtCore.Qt:
♦ MatchExactly - полное совпадение с текстом элемента;
♦ MatchContains - совпадение с любой частью текста элемента;
♦ MatchStartsWith - совпадение с началом;
♦ MatchEndsWith- совпадение с концом;
♦ MatchRegularExpression -поиск с помощью регулярного выражения;
♦ MatchWildcard - используются подстановочные знаки;
♦ MatchFixedString - поиск полного совпадения внутри строки, выполняемый по умолчанию
  без учета регистра символов;
♦ MatchCaseSensitive - поиск с учетом регистра символов;
♦ MatchWrap - если просмотрены все элементы и подходящий элемент не найден, поиск
  начнется с начала списка;
♦ MatchRecursive - просмотр всей иерархии.

Сигналы
===================
Класс QComboBox поддерживает следующие сигналы:
♦ activated(<Индекс>) - генерируется при выборе пользователем пункта в списке (даже
  если индекс не изменился). Внутри обработчика доступен целочисленный индекс элемента;
♦ currentIndexChanged(<Индекс>) - генерируется при изменении текущего индекса.
  Внутри обработчика доступен целочисленный индекс элемента (или значение -1, если
  ни один элемент не выбран);
♦ currentTextChanged(<Текст>) - то же самое, что и currentIndexChanged(), только в обработчик
  передается текст элемента (или пустая строка, если ни один элемент не выбран);
♦ editTextChanged (<Текст>) - генерируется при изменении текста в поле. Внутри обработчика
  через параметр доступен новый текст;
♦ highlighted(<Индекс>) - генерируется при наведении курсора мыши на пункт в списке.
  Внутри обработчика доступен целочисленный индекс элемента;
♦ textActivated(<Индекс>) - то же самое, что и activated(), только в обработчик передается
  текст элемента;
♦ textHighlighted(<Текст>) - то же самое, что и highlighted(), только в обработчик передается
  текст элемента.
"""

from PySide6.QtWidgets import (QMainWindow,
                               QComboBox,
                               QGridLayout,
                               QLabel,
                               QWidget,
                               QFrame,
                               )
from PySide6.QtGui import QIcon

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow,
класса раскрывающегося списка QCombobox, класса слоя сетки для виджетов QGridLayout,
класса ярлыка QLabel, класса базового пустого виджета QWidget
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект
        """
        super().__init__(parent)  # вызов конструктора родительского класса через функцию super()
        # QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Раскрывающийся список')  # установка заголовка главного окна приложения
        self.setWindowIcon(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear))
        self.resize(450, 300)  # установка исходного размера главного окна приложения
        self.dd_lst_1 = QComboBox()  # создание списка
        self.dd_lst_1.addItems(['One', 'Two', 'Three'])  # добавление элементов в список
        self.dd_lst_1.addItem(QIcon.fromTheme(QIcon.ThemeIcon.WeatherClear), 'Icon', 123)  # добавление
        # отдельного элемента в конец списка
        self.lbl_1 = QLabel()  # создание ярлыка для отображения выбранного элемента
        self.lbl_1.setFrameStyle(QFrame.Shape.Box)  # настройка рамки ярлыка
        self.lbl_2 = QLabel()  # создание ярлыка для отображения подсвеченного элемента
        self.lbl_2.setFrameStyle(QFrame.Shape.Box)  # настройка рамки ярлыка
        self.dd_lst_1.textActivated.connect(lambda txt: self.lbl_1.setText(txt))  # привязка обработчика
        # на выбор элемента списка
        self.dd_lst_1.textHighlighted.connect(lambda txt: self.lbl_2.setText(txt))  # привязка обработчика
        # на подсветку элемента списка

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(QLabel('Раскрывающийся список'), 0, 0)  # размещение виджета в сетке
        self.grid.addWidget(self.dd_lst_1, 0, 1)
        self.grid.addWidget(self.lbl_1, 0, 2)
        self.grid.addWidget(self.lbl_2, 0, 3)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя с виджетами в контейнере
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
