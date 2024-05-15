"""
Основные компоненты интерфейса. Область редактирования, основные методы и сигналы.

Область редактирования предназначена для ввода и редактирования обычного текста, текста
в формате НТМL или Markdown. Она изначально поддерживает технологию drag &
drop, стандартные комбинации клавиш, работу с буфером обмена и многое другое.
Область редактирования реализуется с помощью класса QTextEdi t. Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QFrame - QAbstractScrollArea - QTextEdit
Конструктор класса QTextEdit имеет два формата вызова:
QTextEdit([parent=None])
QTextEdit(<Тексе>[, parent=None])
В параметре parent указывается ссылка на родительский компонент. Если параметр не указан
или имеет значение None, компонент будет обладать своим собственным окном. Параметр
<Текст> позволяет задать текст в формате НТМL, который будет отображен в области
редактирования.
ПРИМЕЧАНИЕ
Если поддержка HTML не нужна, то следует воспользоваться классом QPlainTextEdit,
который оптимизирован для работы с простым текстом большого объема.

Класс QTextEdit поддерживает следующие основные методы (полный их список смотрите
на странице https://doc.qt.io/qt-6/qtextedit.html):
♦ setText(<Текст>) - помещает указанный текст в область редактирования. Текст может
  быть простым или в формате НТМL. Метод является слотом;
♦ setPlainText(<Текст>) - помещает в область редактирования простой текст. Метод
  является слотом;
♦ setHtml(<Текст>) - помещает в область редактирования текст в формате HTML. Метод
  является слотом;
♦ setMarkdown(<Текст>) - помещает в область редактирования текст в формате Markdown.
  Метод является слотом;
♦ insertPlainText(<Текст>) - вставляет простой текст в текущую позицию текстового
  курсора. Если в области редактирования был выделен фрагмент, он будет удален. Метод
  является слотом;
♦ insertHtml(<Текст>) - вставляет текст в формате НТМL в текущую позицию текстового
  курсора. Если в области был выделен фрагмент, он будет удален. Метод является слотом;
♦ append(<Текст>) - добавляет новый абзац с указанным текстом в формате НТМL в конец
  области редактирования. Метод является слотом;
♦ setDocumentTitle(<Текст>) - задает текст заголовка документа (в теге <title>);
♦ documentTitle() - возвращает текст заголовка (из тега <title>);
♦ toPlainText() - возвращает содержимое области редактирования в виде простого текста;
♦ toHtml() - возвращает текст в формате НТМL;
♦ toMarkdown() - возвращает текст в формате Markdown;
♦ clear() - удаляет весь текст из области. Метод является слотом;
♦ selectAll() - выделяет весь текст в области. Метод является слотом;
♦ zoomIn([range=1]) - увеличивает размер шрифта на заданное в параметре range количество
  пунктов. Метод является слотом;
♦ zoomOut([range=1]) - уменьшает размер шрифта на заданное в параметре range количество
  пунктов. Метод является слотом;
♦ cut() - вырезает выделенный текст в буфер обмена при условии, что есть выделенный
  фрагмент. Метод является слотом;
♦ сору() - копирует выделенный текст в буфер обмена при условии, что есть выделенный
  фрагмент. Метод является слотом;
♦ paste() - вставляет текст из буфера обмена в текущую позицию текстового курсора
  при условии, что область доступна для редактирования. Метод является слотом;
♦ canPaste() - возвращает True, если из буфера обмена можно вставить текст, и False -
  в противном случае;
♦ setAcceptRichText(<Флаг>) - если в качестве параметра указано значение True, в область
  редактирования можно будет ввести, вставить из буфера обмена или перетащить
  текст в формате НТМL. Значение False дает возможность заносить в область лишь обычный
  текст;
♦ acceptRichText() - возвращает значение True, если в область можно занести текст
  в формате НТМL, и False - если доступно занесение лишь обычного текста;
♦ undo() - отменяет последнюю операцию ввода пользователем при условии, что отмена
  возможна. Метод является слотом;
♦ redo() - повторяет последнюю отмененную операцию ввода пользователем, если это
  возможно. Метод является слотом;
♦ setUndoRedoEnabled(<Флаг>) - если в качестве значения указано значение True, операции
  отмены и повтора действий будут разрешены, а если False - то будут запрещены;
♦ isUndoRedoEnabled() - возвращает значение True, если операции отмены и повтора
  действий разрешены, и False - если запрещены;
♦ createStandardContextMenu([<Координаты QPoint>]) - создает стандартное контекстное
  меню, которое отображается при щелчке правой кнопкой мыши в области .редактирования.
  В параметре можно указать координаты точки внутри содержимого области редактирования.
  Чтобы изменить стандартное меню, следует создать класс, производный от
  QTextEdit, и переопределить в нем метод contextMenuEvent(self, <event>). Внутри этого
  метода можно создать свое собственное меню или добавить новый пункт в стандартное
  меню;
♦ ensureCursorVisible() - прокручивает область таким образом, чтобы текстовый курсор
  оказался в зоне видимости;
♦ find() - производит поиск фрагмента (по умолчанию в прямом направлении без учета
  регистра символов) в области редактирования. Если фрагмент найден, то он выделяется
  и метод возвращает значение True, в противном случае - значение False. Форматы
  метода:
  find(<Искомый текст> | <Регулярное выражение> [, <Режим>])
  Искомый текст можно указать либо строкой, либо регулярным выражением, представленным
  объектом класса QRegularExpression из модуля QtCore. В необязательном параметре
  <Режим> можно указать комбинацию через оператор | следующих элементов
  перечисления FindFlag класса QTextDocument из модуля QtGui:
  • FindBackward - поиск в обратном направлении;
  • FindCaseSensitively- поиск с учетом регистра символов;
  • FindWholeWords - поиск целых слов, а не фрагментов;
♦ print(<Принтер>) - отправляет содержимое текстового поля на заданный принтер.
  В качестве параметра указывается объект одного из классов, производных от
  QPagedPaintDevice (модуль QtGui): QPrinter (модуль QtPrintSupport) или QPdfWriter
  (модуль QtGui). Пример вывода документа в РDF-файл:
  pdf = QtGui.QPdfWriter("document.pdf")
  textEdit.print(pdf)

Класс QTextEdit поддерживает следующие сигналы:
♦ copyAvailable(<Флаг>) - генерируется при выделении текста или, наоборот, снятии
  выделения. Значение параметра True указывает, что фрагмент выделен и его можно скопировать,
  значение False - обратное;
♦ currentCharFormatChanged(<Формат>) - генерируется при изменении формата текста.
  Внутри обработчика через параметр доступен новый формат в виде объекта класса
  QTextCharFormat;
♦ cursorPositionChanged() - генерируется при изменении положения текстового курсора;
♦ redoAvailable(<Флаг>) - генерируется при изменении возможности повторить отмененную
  операцию ввода. Значение параметра True обозначает возможность повтора отмененной
  операции, а значение False - невозможность сделать это;
♦ selectionChanged() - генерируется при изменении выделения текста;
♦ textChanged() - генерируется при изменении текста в области редактирования;
♦ undoAvailable(<Флаг>) - генерируется при изменении возможности отменить операцию
  ввода. Значение параметра True указывает, что операция ввода может быть отменена,
  значение False говорит об обратном.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QTextEdit,
                               QGridLayout,
                               QWidget,
                               QLabel,
                               QFrame,
                               )
from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса области редактирования QTextEdit,
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
        self.undo_indicator = QLabel('Undo')
        self.undo_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.undo_indicator.setFrameShape(QFrame.Shape.Box)
        self.undo_indicator.setStyleSheet('color: grey')
        self.redo_indicator = QLabel('Redo')
        self.redo_indicator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.redo_indicator.setFrameShape(QFrame.Shape.Box)
        self.redo_indicator.setStyleSheet('color: grey')
        self.text_edit.undoAvailable.connect(lambda flag: self.indicator_change(flag, self.undo_indicator))
        self.text_edit.redoAvailable.connect(lambda flag: self.indicator_change(flag, self.redo_indicator))

        self.grid = QGridLayout()
        self.grid.addWidget(self.text_edit, 0, 0, 1, 2)
        self.grid.addWidget(self.undo_indicator, 1, 0)
        self.grid.addWidget(self.redo_indicator, 1, 1)
        self.container = QWidget()
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

    @staticmethod
    def indicator_change(flag, indicator):
        if flag:
            indicator.setStyleSheet('color: black')
        else:
            indicator.setStyleSheet('color: gray')


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
