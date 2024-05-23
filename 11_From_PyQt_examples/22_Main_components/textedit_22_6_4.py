"""
Основные компоненты интерфейса. Область редактирования, использование класса документа.

Класс QTextDocument из модуля QtGui представляет документ, который отображается в области
редактирования. Получить ссылку на текущий документ позволяет метод document()
класса QTextEdit. Занести в область редактирования новый документ можно с помощью
метода setDocument(<Документ>). Иерархия наследования:
QObject - QTextDocument
Конструктор класса QTextDocument имеет два формата:
QTextDocument([parent=None])
QTextDocument(<Текст>[, parent=None])
В параметре parent указывается ссылка на родителя. Параметр <Текст> задает простой
текст (не в НТМL-формате), который будет отображен в области редактирования.
Класс QTextDocument поддерживает следующий набор методов (полный их список смотрите
на странице https://doc.qt.io/qt-6/qtextdocument.html):
♦ setPlainText(<Текст>) - помещает в документ простой текст;
♦ setHtml(<Текст>) - помещает в документ текст в формате HTML;
♦ setMarkdown(<Текст>) - помещает в документ текст в формате Markdown;
♦ toPlainText() - возвращает простой текст, содержащийся в документе;
♦ toHtml() - возвращает текст в формате НТМL;
♦ toMarkdown() - возвращает текст в формате Markdown;
♦ clear() - удаляет весь текст из документа;
♦ isEmpty() - возвращает значение True, если документ пустой, и False - в противном
  случае;
♦ setModified(<Флаг>) - если передано значение True, документ помечается как измененный,
  если False - как неизмененный. Метод является слотом;
♦ isModified() - возвращает значение True, если документ был изменен, и False -
  в противном случае;
♦ undo() - отменяет последнюю операцию ввода пользователем при условии, что отмена
  возможна. Метод является слотом;
♦ redo() - повторяет последнюю отмененную операцию ввода пользователем, если это
  возможно. Метод является слотом;
♦ isUndoAvailable() - возвращает значение True, если можно отменить последнюю операцию
  ввода, и False - в противном случае;
♦ isRedoAvailable() - возвращает значение True, если можно повторить последнюю отмененную
  операцию ввода, и False - в противном случае;
♦ setUndoRedoEnabled(<Флаг>) - если в качестве параметра указано значение True, то
  операции отмены и повтора действий разрешены, а если False - то запрещены;
♦ isUndoRedoEnabled() - возвращает значение True, если операции отмены и повтора
  действий разрешены, и False - если запрещены;
♦ availableUndoSteps() - возвращает количество возможных операций отмены;
♦ availableRedoSteps() - возвращает количество возможных повторов отмененных операций;
♦ clearUndoRedoStacks([stacks=Stacks.UndoAndRedoStacks]) - очищает список возможных
  отмен и/или повторов. В качестве параметра можно указать следующие элементы
  перечисления Stacks из класса QTextDocument:
  • UndoStack - только список возможных отмен;
  • RedoStack - только список возможных повторов;
  • UndoAndRedoStacks - оба списка;
♦ print(<Принтер>) - отправляет содержимое документа на указанный принтер. В качестве
  параметра указывается объект одного из классов, производных от QPagedPaintDevice
  (модуль QtGui): QPrinter (модуль QtPrintSupport) или QPdfWriter (модуль QtGui);
♦ find() - производит поиск фрагмента в документе. Метод возвращает объект класса
  QTextCursor из модуля QtGui. Если фрагмент не найден, то возвращенный объект будет
  нулевым. Проверить успешность операции можно с помощью метода isNull() класса
  QTextCursor. Форматы метода:
  find(<Текст> | <Регулярное выражение> [, position=O] [, options=O])
  find(<Текст> | <Регулярное выражение>, <Курсор>[, options=O])
  Параметр <Текст> задает искомый фрагмент, а параметр <Регулярное выражение> - регулярное
  выражение в виде объекта класса QRegularExpression из модуля QtCore. По
  умолчанию обычный поиск производится без учета регистра символов в прямом направлении,
  начиная с позиции position или от текстового курсора, указанного в параметре
  <Курсор> в виде объекта класса QTextCursor. Поиск по регулярному выражению по
  умолчанию производится с учетом регистра символов. Чтобы поиск производился без
  учета регистра, необходимо передать элемент CaseInsensitiveOption перечисления
  PatternOption из класса QRegularExpression в метод setPatternOptions() регулярного
  выражения. В необязательном параметре options можно указать комбинацию (через оператор
  |) следующих элементов перечисления FindFlag из класса QTextDocument:
  • FindBackward - поиск в обратном направлении;
  • FindCaseSensitively- поиск с учетом регистра символов. При использовании регулярного
    выражения значение игнорируется;
  • FindWholeWords - поиск целых слов, а не фрагментов;
♦ setDefaultFont(<Шрифт>) - задает шрифт по умолчанию для документа. В качестве
  параметра указывается объект класса QFont из модуля QtGui;
♦ setDefaultStyleSheet(<Таблица стилей>) - устанавливает для документа таблицу
  стилей CSS по умолчанию. Таблица стилей задается в виде строки;
♦ setDocumentMargin(<Отступ>) - задает отступ от краев поля до текста;
♦ documentMargin() - возвращает величину отступа от краев поля до текста;
♦ setMaximumBlockCount(<Количество>) - задает максимальное количество текстовых
  блоков в документе. Если количество блоков становится больше указанного значения,
  первые блоки будут удалены;
♦ maximumBlockCount() - возвращает максимальное количество текстовых блоков;
♦ characterCount() - возвращает количество символов в документе;
♦ lineCount() - возвращает количество строк в документе;
♦ blockCount() - возвращает количество текстовых блоков в документе;
♦ firstBlock() - возвращает объект класса QTextBlock, объявленного в модуле QtGui,
  который содержит первый текстовый блок документа;
♦ lastBlock() - возвращает объект класса QTextBlock, который содержит последний текстовый
  блок документа;
♦ findBlock(<Индекс символа>) : возвращает объект класса QTextBlock, который содержит
  текстовый блок документа, включающий символ с указанным индексом;
♦ findBlockВyLineNшnЬer( <Индекс абзаца>) - возвращает объект класса QTextBlock, который
  содержит текстовый блок документа, включающий абзац с указанным индексом;
♦ findBlockByNшnЬer (<Индекс блока>) - возвращает объект класса QTextBlock, который
  содержит текстовый блок документа с указанным индексом.

Класс QTextDocument поддерживает сигналы:
♦ blockCountChanged(<Новое количество блоков>) - генерируется при изменении количества
  текстовых блоков. Внутри обработчика через параметр доступно новое количество
  текстовых блоков, заданное целым числом;
♦ contentsChange(<Позиция курсора>, <Количество удаленных символов>, <Количество
  добавленных символов>) - генерируется при изменении текста. Все три параметра целочисленные;
♦ contentsChanged() -генерируется при любом изменении документа;
♦ cursorPositionChanged(<Курсор QTextCursor>) - генерируется при изменении позиции
  текстового курсора из-за операции редактирования. При простом перемещении текстового
  курсора сигнал не генерируется. Внутри обработчика через параметр доступен объект
  обновленного курсора;
♦ modificationChanged(<Флаг>) - генерируется при изменении состояния документа: из
  неизмененного в измененное или наоборот. Значение параметра True обозначает, что
  документ помечен как измененный, значение False - что он теперь неизмененный;
♦ redoAvailable(<Флаг>) - генерируется при изменении возможности повторить отмененную
  операцию ввода. Значение параметра True обозначает наличие возможности повторить
  отмененную операцию ввода, а False - отсутствие такой возможности;
♦ undoAvailable(<Флаг>) - генерируется при изменении возможности отменить операцию
  ввода. Значение параметра True обозначает наличие возможности отменить операцию
  ввода, а False - отсутствие такой возможности;
♦ undoCommandAdded() - генерируется при добавлении операции ввода в список возможных
  отмен.
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
from PySide6.QtGui import (QFont,
                           QColor,
                           QTextDocument,
                           )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса области редактирования QTextEdit, класса слоя сетки для виджетов QGridLayout,
класса пустого базового виджета QWidget, класса виджета ярлыка QLabel,
класса рамки для виджетов QFrame, класса виджета кнопки QPushButton

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt

Импорт из модуля PySide6.QtGui класса шрифтов QFont, класса цветов QColor,
класса текстового документа QTextDocument
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
        self.document = QTextDocument("Текст текст текст текст текст текст текст текст")
        self.document.setDefaultFont(QFont('Times New Roman', pointSize=20, weight=2, italic=True))
        self.text_edit.setDocument(self.document)

        # TODO продолжить

        self.undo_indicator = QLabel('Undo')  # создание индикатора
        self.undo_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания
        self.undo_indicator.setFrameShape(QFrame.Shape.Box)  # создание рамки
        self.undo_indicator.setStyleSheet('color: grey')  # установка цвета шрифта
        self.redo_indicator = QLabel('Redo')  # создание индикатора
        self.redo_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания
        self.redo_indicator.setFrameShape(QFrame.Shape.Box)  # создание рамки
        self.redo_indicator.setStyleSheet('color: grey')  # установка цвета шрифта
        self.document.undoAvailable.connect(lambda flag: self.indicator_change(flag, self.undo_indicator))
        self.document.redoAvailable.connect(lambda flag: self.indicator_change(flag, self.redo_indicator))

        self.wrap_mode_btn = QPushButton('Режим переноса')  # создание кнопки переключения режима переноса
        self.wrap_mode_btn.clicked.connect(self.wrap_mode_change)  # привязка обработчика переключателя режима переноса

        self.auto_format_btn = QPushButton('Список (введите *)')  # создание кнопки автоформатирования
        self.auto_format_btn.clicked.connect(self.auto_format_mode_change)  # привязка обработчика переключателя
        # режима автоформата

        self.undo_btn = QPushButton('Undo')  # создание кнопки
        self.undo_btn.setDisabled(True)  # установка состояния кнопки по умолчанию
        self.document.undoAvailable.connect(lambda flag: self.undo_btn.setEnabled(flag))
        # создание сигнала о доступности операции
        self.undo_btn.clicked.connect(lambda: self.document.undo())  # привязка обработчика к кнопке
        self.redo_btn = QPushButton('Redo')  # создание кнопки
        # создание сигнала о доступности операции
        self.document.redoAvailable.connect(lambda flag: self.redo_btn.setEnabled(flag))
        self.redo_btn.setDisabled(True)  # установка состояния кнопки по умолчанию
        self.redo_btn.clicked.connect(lambda: self.document.redo())  # привязка обработчика к кнопке

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
