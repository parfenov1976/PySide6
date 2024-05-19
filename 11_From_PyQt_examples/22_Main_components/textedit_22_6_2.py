"""
Основные компоненты интерфейса. Область редактирования, дополнительные параметры.

Задать другие параметры области редактирования можно вызовами следующих методов класса
QTextEdit (полный их список смотрите на странице https://doc.qtio/qt-6/qtextedit.html):
♦ setTextInteractionFlags(<Режим>) - задает режим взаимодействия пользователя с текстом.
  Можно указать следующие элементы (или их комбинацию через оператор 1) перечисления
  TextInteractionFlag из модуля QtCore.Qt:
  • NoTextInteraction- пользователь не может взаимодействовать с текстом;
  • TextSelectableByMouse- текст можно выделить мышью;
  • TextSelectableByKeyboard-текст можно выделить с помощью клавиатуры. Внутри
    поля будет отображен текстовый курсор;
  • LinkAccessibleByMouse - на гиперссылках, присутствующих в тексте, можно щелкать мышью;
  • LinksAccessibleByKeyboard - с гиперссьmками, присутствующими в тексте, можно
    взаимодействовать с клавиатуры: перемещаться между гиперссылками - с помощью клавиши <Tab>,
    а переходить по гиперссылке - нажав клавишу <Enter>;
  • TextEditable - текст можно редактировать;
  • TextEditorInteraction - комбинация TextSelectableByMouse |
    TextSelectableByKeyboard | TextEditable;
  • TextBrowserInteraction - комбинация TextSelectableByMouse |
    LinksAccessibleByMouse | LinksAccessibleByKeyboard;
♦ setReadOnly(<Флаг>) - если в качестве параметра указано значение True, область
  редактирования будет доступна только для чтения;
♦ isReadOnly() - возвращает значение True, если область доступна только для чтения,
  и False - в противном случае;
♦ setLineWrapMode(<Режим>) - задает режим переноса строк. В качестве значения могут
  быть указаны следующие элементы перечисления LineWrapMode из класса QTextEdit:
  • NoWrap - перенос строк не производится;
  • WidgetWidth - перенос строк при достижении ими правого края области редактирования;
  • FixedPixelWidth - перенос строк при достижении ими фиксированной ширины в пикселах,
    которую можно задать с помощью метода setLineWrapColumnOrWidth();
  • FixedColumnWidth - перенос строк при достижении ими фиксированной ширины в символах,
    которую можно задать с помощью метода setLineWrapColumnOrWidth();
♦ setLineWrapColumnOrWidth(<Ширина>) - задает фиксированную ширину строк, при достижении
  которой будет выполняться перенос, в пикселах или символах (в зависимости от заданного
  режима переноса);
♦ setWordWrapMode(<Режим>) - задает режим переноса по словам. В качестве значения могут
  быть указаны следующие элементы перечисления WrapMode класса QTextOption из модуля QtGui:
  • NoWrap или ManualWrap - перенос по словам не производится;
  • WordWrap - перенос строк только по словам;
  • WrapAnywhere - перенос строки может быть внутри слова;
  • WrapAtWordВoundaryOrAnywhere - перенос по возможности по словам, но может быть выполнен
    и внутри слова;
♦ setOverwriteMode(<Флаг>) - если в качестве параметра указано значение True, вводимый
  текст будет замещать ранее введенный. Значение False отключает замещение;
♦ overwriteMode() - возвращает значение True, если вводимый текст замещает ранее введенный,
  и False - в противном случае;
♦ setAutoFormatting(<Режим>) - задает режим автоматического форматирования. В качестве
  значения могут быть указаны следующие элементы перечисления AutoFormattingFlag из
  класса QTextEdit:
  • AutoNone - автоматическое форматирование ни используется;
  • AutoBulletList - автоматическое создание маркированного списка при вводе пользователем
    в начале строки символа *;
  • AutoAll - включить все режимы;
♦ setCursorWidth(<Толщина>) - задает толщину текстового курсора;
♦ setTabChangesFocus(<Флаг>) - если параметром передать значение False, то с помощью нажатия
  клавиши <Tab> можно вставить в область редактирования символ табуляции. Если указано значение
  True, клавиша <Tab> используется для передачи фокуса следующему компоненту;
♦ setTabStopDistance(<Ширина>) - задает ширину табуляции в пикселах;
♦ tabStopDistance() - возвращает ширину табуляции в пикселах
"""
from PySide6.QtWidgets import (QMainWindow,
                               QTextEdit,
                               QGridLayout,
                               QWidget,
                               QLabel,
                               QFrame,
                               QPushButton,
                               )
from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса области редактирования QTextEdit, класса слоя сетки для виджетов QGridLayout,
класса пустого базового виджета QWidget, класса виджета ярлыка QLabel,
класса рамки для виджетов QFrame, класса виджета кнопки QPushButton

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt
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
        self.setWindowTitle('Область редактирования')  # установка заголовка главного окна приложения
        self.resize(300, 300)  # установка исходного размера главного окна
        self.text_edit = QTextEdit()  # создание экземпляра класса области ввода
        self.undo_indicator = QLabel('Undo')  # создание индикатора
        self.undo_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания
        self.undo_indicator.setFrameShape(QFrame.Shape.Box)  # создание рамки
        self.undo_indicator.setStyleSheet('color: grey')  # установка цвета шрифта
        self.redo_indicator = QLabel('Redo')  # создание индикатора
        self.redo_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания
        self.redo_indicator.setFrameShape(QFrame.Shape.Box)  # создание рамки
        self.redo_indicator.setStyleSheet('color: grey')  # установка цвета шрифта
        self.text_edit.undoAvailable.connect(lambda flag: self.indicator_change(flag, self.undo_indicator))
        self.text_edit.redoAvailable.connect(lambda flag: self.indicator_change(flag, self.redo_indicator))

        self.wrap_mode_btn = QPushButton('Режим переноса')  # создание кнопки переключения режима переноса
        self.wrap_mode_btn.clicked.connect(self.wrap_mode_change)  # привязка обработчика переключателя режима переноса

        self.auto_format_btn = QPushButton('Список (введите *)')  # создание кнопки автоформатирования
        self.auto_format_btn.clicked.connect(self.auto_format_mode_change)  # привязка обработчика переключателя
        # режима автоформата

        self.text_edit.setCursorWidth(5)  # изменение ширины текстового курсора

        self.undo_btn = QPushButton('Undo')  # создание кнопки
        self.undo_btn.setDisabled(True)  # установка состояния кнопки по умолчанию
        self.text_edit.undoAvailable.connect(lambda flag: self.undo_btn.setEnabled(flag))
        # создание сигнала о доступности операции
        self.undo_btn.clicked.connect(lambda: self.text_edit.undo())  # привязка обработчика к кнопке
        self.redo_btn = QPushButton('Redo')  # создание кнопки
        # создание сигнала о доступности операции
        self.text_edit.redoAvailable.connect(lambda flag: self.redo_btn.setEnabled(flag))
        self.redo_btn.setDisabled(True)  # установка состояния кнопки по умолчанию
        self.redo_btn.clicked.connect(lambda: self.text_edit.redo())  # привязка обработчика к кнопке

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(self.text_edit, 0, 0, 1, 2)  # размещение виджета в сетке
        self.grid.addWidget(self.undo_indicator, 1, 0)
        self.grid.addWidget(self.redo_indicator, 1, 1)
        self.grid.addWidget(self.undo_btn, 2, 0)
        self.grid.addWidget(self.redo_btn, 2, 1)
        self.grid.addWidget(self.wrap_mode_btn, 3, 0)
        self.grid.addWidget(self.auto_format_btn, 3, 1)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в окне приложения

    @staticmethod
    def indicator_change(flag: bool, indicator: QLabel) -> None:
        """
        Обработчик сигнала о доступности операции
        :param flag: флаг доступности операции
        :param indicator: ссылка на индикатор
        :return: None
        """
        if flag:
            indicator.setStyleSheet('color: black')  # Изменение отображения индикатора
        else:
            indicator.setStyleSheet('color: gray')  # Изменение отображения индикатора

    def wrap_mode_change(self) -> None:
        """
        Обработчика сигнала переключения режима переноса
        """
        if self.text_edit.lineWrapMode() is QTextEdit.LineWrapMode.NoWrap:  # проверка текущего режима
            self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)  # установка переноса по ширине области
        else:
            self.text_edit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)  # отключение переноса
        self.text_edit.setFocus()  # возврат фокуса в область после нажатия кнопки

    def auto_format_mode_change(self):
        """
        Обработчик сигнала переключения режима автоформатирования
        """
        if self.text_edit.autoFormatting() is QTextEdit.AutoFormattingFlag.AutoAll:  # проверка текущего режима
            self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)  # отключение автоформата
        else:
            self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)  # включение всех режимов автоформата
        self.text_edit.setFocus()  # возврат фокуса в область после нажатия кнопки


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    import sys
    from PySide6.QtWidgets import QApplication

    """
    Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
    к аргументам командной строки. Если использование аргументов командной строки не предполагается,
    то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
    в качестве аргумента передается пустой.
    Импорт из модуля PySide6.QWidgets класса управления приложением QApplication.
    """
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
