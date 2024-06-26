"""
Списки и таблицы. Список для выбора шрифта.

Класс QFontComboBox реализует раскрывающийся список с названиями шрифтов. Шрифт
можно выбрать из списка или ввести его название в поле при этом станут
отображаться названия, начинающиеся с введенных букв. Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QComboBox - QFontComboBox
Формат конструктора класса QFontComboBox:
QFontComboBox([parent=None])
Класс QFontComboBox наследует все методы и сигналы класса QComboBox:
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

Класс QFontComboBox еще определяет несколько дополнительных методов:
♦ setCurrentFont(<Шрифт QFont>) - делает текущим элемент, соответствующий указанному
  шрифту:
  comboBox.setCurrentFont(QtGui.QFont("Verdana"))
  Метод является слотом;
♦ currentFont() - возвращает объект класса QFont с выбранным шрифтом. Вот пример
  вывода названия шрифта:
  print(comboBox.currentFont().family())
♦ setFontFilters(<Фильтр>) - выводит в списке только шрифты типов, соответствующих
  указанному фильтру. В качестве параметра указывается комбинация следующих элементов
  перечисления FontFilter из класса QFontComboBox:
  • AllFonts - все типы шрифтов;
  • ScalableFonts - масштабируемые шрифты;
  • NonScalableFonts - немасштабируемые шрифты;
  • MonospacedFonts - моноширинные шрифты;
  • ProportionalFonts - пропорциональные шрифты.
Класс QFontComboBox поддерживает сигнал currentFontChanged(<Шрифт QFont>), который
генерируется при изменении выбранного шрифта. Внутри обработчика доступен выбранный шрифт.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QFontComboBox,
                               QTextEdit,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtGui import QFont

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, класса списка выбора
шрифта QFontComboBox, класса текстового редактируемого опля QTextEdit, класса вертикальной
стопки для виджетов QVBoxLayout, класса базового пустого виджета QWidget

Импорт из модуля PySide6.QtGui класса шрифта QFont
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
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        # super().__init__(parent)  # вызов конструктора родительского класса функцией super()
        self.setWindowTitle('Список выбора шрифта')  # установка заголовка главного окна
        self.resize(300, 300)  # установка размера окна по умолчанию
        self.font_combobox = QFontComboBox()  # создание списка для выбора шрифта
        self.text_edit = QTextEdit()  # создание много строчного текстового поля
        self.font_combobox.setCurrentFont(self.text_edit.font())  # извлечение текущего шрифта из редактируемого
        # текстового поля и установка списка на него
        self.font_combobox.currentFontChanged.connect(self.on_font_change)  # привязка обработчика на изменение
        # текущего шрифта

        self.vbox = QVBoxLayout()  # создание слоя для виджетов с вертикальной организацией
        self.vbox.addWidget(self.font_combobox)  # размещение виджета в стопке
        self.vbox.addWidget(self.text_edit)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера внутри главного окна приложения

    def on_font_change(self, font: QFont) -> None:
        """
        Обработчик изменения текущего шрифта
        :param font: QFont - объект шрифта
        :return: None
        """
        self.text_edit.setCurrentFont(font)  # изменение текущего шрифта в текстовом редактируемом поле
        self.text_edit.setFocus()  # возврат фокуса на редактируемое текстовое поле


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
