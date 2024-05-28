"""
Основные компоненты интерфейса. Область редактирования, использование класса документа.

Класс QTextCursor из модуля QtGui предоставляет текстовый курсор - инструмент для работы
с документом, представленным объектом класса QTextDocument. Конструктор класса
QTextCursor поддерживает следующие форматы:
QTextCursor()
QTextCursor(<Объект класса QTextDocument>)
QTextCursor(<Объект класса QTextFrame>)
QTextCursor(<Объект класса QTextBlock>)
QTextCursor(<Объект класса QTextCursor>)
Создать текстовый курсор, установить его в документе и управлять им позволяют следующие
методы класса QTextEdit:
♦ textCursor() - возвращает видимый в текущий момент текстовый курсор в виде объекта
класса QTextCursor;
♦ setTextCursor(<Курсор QTextCursor>) - устанавливает новый текстовый курсор;
♦ cursorForPosition (<Позиция>) - возвращает текстовый курсор, который соответствует
  позиции, указанной в качестве параметра. Позиция задается в виде объекта класса
  QPoint в координатах области редактирования;
♦ moveCursor(<Позиция> [, mode=MoveMode. MoveAnchor]) - перемещает текстовый курсор
  внутри документа. В первом параметре можно указать следующие элементы перечисления
  MoveOperation из класса QTextCursor:
  • NoMove - не перемещать курсор;
  • Start - в начало документа;
  • up - на одну строку вверх;
  • StartOfLine - в начало текущей строки;
  • StartOfBlock - в начало текущего текстового блока;
  • StartOfWord - в начало текущего слова;
  • PreviousBlock - в начало предыдущего текстового блока;
  • PreviousCharacter - на предыдущий символ;
  • PreviousWord - в начало предыдущего слова;
  • Left - на один символ влево;
  • WordLeft - на одно слово влево;
  • End - в конец документа;
  • Down - на одну строку вниз;
  • EndOfLine - в конец текущей строки;
  • EndOfWord •- в конец текущего слова;
  • EndOfBlock - в конец текущего текстового блока;
  • NextBlock - в начало следующего текстового блока;
  • NextCharacter - на следующий символ;
  • NextWord - в начало следующего слова;
  • Right - сдвинуть на ОДИН СИМВОЛ вправо;
  • WordRight - в начало следующего слова.
Помимо указанных, в перечислении существуют также элементы NextCell,
PreviousCell, NextRow и PreviousRow, позволяющие перемещать текстовый курсор внутри
таблицы.
В параметре mode можно указать следующие элементы перечисления MoveMode из класса
QTextCursor:
  • MoveAnchor - если существует выделенный фрагмент, то выделение будет снято и
    текстовый курсор переместится в новое место (значение no умолчанию);
  • KeepAnchor - фрагмент текста от старой позиции курсора до новой будет выделен.
Класс QTextCursor поддерживает следующие методы (здесь приведены только основные -
полный их список смотрите на странице https://doc.qt.io/qt-6/qtextcursor.html):
♦ isNull() - возвращает значение True, если объект курсора является нулевым (создан
  вызовом конструктора без параметра), и False - в противном случае;
♦ setPosition(<Позиция> [, mode=MoveMode.MoveAnchor]) - перемещает текстовый курсор
  внутри документа. В первом параметре указывается позиция внутри документа. Необязательный
  параметр mode аналогичен одноименному параметру метода moveCursor()
  класса QTextEdit;
♦ movePosition(<Позиция>[, mode=MoveMode.MoveAnchor] [, n=1]) - перемещает текстовый
  курсор внутри документа. Параметры <Позиция> и mode аналогичны одноименным
  параметрам метода moveCursor() класса QTextEdit. Необязательный параметр n позволяет
  указать количество перемещений - например, переместить курсор на 10 символов
  вперед можно так:
  cur = textEdit.textCursor()
  cur.movePosition(QtGui.QTextCursor.MoveOperation.NextCharacter,
  mode=QtGui.QTextCursor.MoveMode.MoveAnchor, n=10)
  textEdit.setTextCursor(cur)
  Метод возвращает значение True, если операция успешно выполнена указанное количество
  раз. Если было выполнено меньшее количество перемещений (например, из-за достижения
  конца документа), метод возвращает значение False;
♦ position() - возвращает позицию текстового курсора внутри документа;
♦ positionInBlock() - возвращает позицию текстового курсора внутри блока;
♦ block() - возвращает объект класса QTextBlock, который описывает текстовый блок,
содержащий курсор;
♦ blockNumber() - возвращает номер текстового блока, содержащего курсор;
♦ atStart() - возвращает значение True, если текстовый курсор ,находится в начале документа,
  и False - в противном случае;
♦ atEnd() - возвращает значение True, если текстовый курсор находится в конце документа,
  и False - в противном случае;
♦ atBlockStart() - возвращает значение True, если текстовый курсор находится в начале
  блока, и False - в противном случае;
♦ atBlockEnd() - возвращает значение True, если текстовый курсор находится в конце
  блока, и False - в противном случае;
♦ select(<Режим>) - выделяет фрагмент в документе в соответствии с указанным режимом.
  В качестве параметра можно указать следующие элементы перечисления
  SelectionType из класса QTextCursor:
  • WordUnderCursor - выделяет слово, в котором расположен курсор;
  • LineUnderCursor - выделяет строку, в которой расположен курсор;
  • BlockUnderCursor - выделяет текстовый блок, в котором находится курсор;
  • Document - выделяет весь документ;
♦ hasSelection() - возвращает значение True, если существует выделенный фрагмент,
  и False - в противном случае;
♦ hasComplexSelection() - возвращает значение True, если выделенный фрагмент содержит
  сложное форматирование, а не просто текст, и False - в противном случае;
♦ clearSelection() - снимает выделение;
♦ selectionStart() - возвращает начальную позицию выделенного фрагмента;
♦ selectionEnd() - возвращает конечную позицию выделенного фрагмента;
♦ selectedText() - возвращает текст выделенного фрагмента;
    -=ВНИМАНИЕ=-!
    Если выделенный фрагмент занимает несколько строк, то вместо символа перевода строки
    вставляется символ с кодом \u2029. Попытка вывести этот символ в консоли приведет к
    исключению, поэтому следует произвести замену символа с помощью метода replace():
    print(cur.selectedText().replace("\u2029", "\n"))
♦ selection() - возвращает объект класса QTextDocumentFragment, который описывает
  выделенный фрагмент. Получить текст позволяют методы toPlainText() (возвращает
  простой текст) и toHtml() (возвращает текст в формате НТМL) этого класса;
♦ removeSelectedText() - удаляет выделенный фрагмент;
♦ deleteChar() - если нет выделенного фрагмента, удаляет символ справа от курсора,
  в противном случае удаляет выделенный фрагмент;
♦ deletePreviousChar() - если нет выделенного фрагмента, удаляет символ слева от курсора,
  в противном случае удаляет выделенный фрагмент;
♦ beginEditBlock() - задает начало блока операций ввода. Операции, входящие в такой
  блок, могут быть отменены или повторены как единое целое с помощью методов undo()
  и redo();
♦ endEditBlock() - задает конец блока операций ввода;
♦ joinPreviousEditBlock() - делает последующие операции ввода частью предыдущего
  блока операций;
♦ setKeepPositionOnInsert(<Флаг>) - если в качестве параметра указано значение True,
  то после операции вставки курсор сохранит свою предыдущую позицию. По умолчанию
  позиция курсора при вставке изменяется;
♦ insertText(<Текст> [, <Формат> ]) - вставляет простой текст с форматом, указанным
  в виде объекта класса QTextFormat;
♦ insertHtml(<Текст>) - вставляет текст в формате НТМL.
С помощью методов insertBlock(), insertFragment(), insertFrame(), insertImage(),
insertList() и insertTable() можно вставить различные элементы: изображения, списки
и др. Изменить формат выделенного фрагмента позволяют методы mergeBlockCharFormat(),
mergeBlockFormat() и mergeCharFormat() . За подробной информацией по этим методам
обращайтесь к странице документации https://doc.qt.io/qt-6/qtextcursor.html.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QTextEdit,
                               QGridLayout,
                               QWidget,
                               QLabel,
                               QFrame,
                               QPushButton,
                               QLineEdit,
                               )
from PySide6.QtCore import Qt
from PySide6.QtGui import (QFont,
                           QTextDocument,
                           )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса области редактирования QTextEdit, класса слоя сетки для виджетов QGridLayout,
класса пустого базового виджета QWidget, класса виджета ярлыка QLabel,
класса рамки для виджетов QFrame, класса виджета кнопки QPushButton,
класса однострочного редактируемого поля для текста QLineEdit

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt

Импорт из модуля PySide6.QtGui класса шрифтов QFont, класса текстового документа QTextDocument
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
        self.resize(300, 450)  # установка исходного размера главного окна
        self.text_edit = QTextEdit()  # создание экземпляра класса области ввода
        self.document = QTextDocument()  # создание экземпляра документа
        # если текст подать при создании экземпляра документа, то сигналы на доступность undo/redo
        # не будут работать корректно
        with open('textedit.txt', 'r', encoding="utf-8") as t:  # открытие файла на чтение
            self.document.setPlainText(t.read())  # добавление текста в документ
        self.document.setDefaultFont(QFont('Times New Roman', pointSize=15, weight=2, italic=True))  # изменение шрифта
        self.text_edit.setDocument(self.document)  # поместить документ в область редактирования

        self.save_btn = QPushButton('Сохранить')  # создать кнопку сохранения
        self.save_btn.setEnabled(False)  # по умолчанию кнопка не активна
        self.document.contentsChange.connect(lambda: self.save_btn.setEnabled(True))  # проверка изменений в тексте
        # и активация кнопки сохранения
        self.save_btn.clicked.connect(lambda: open('textedit.txt', 'w').write(self.document.toPlainText()))
        # обработчик сигнала сохранения

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
        self.document.contentsChange.connect(lambda: print('Content changed'))  # сигнал на изменения в тексте
        self.document.undoCommandAdded.connect(lambda: print('Undo added'))  # сигнал на добавление undo в очередь

        self.wrap_mode_btn = QPushButton('Режим переноса')  # создание кнопки переключения режима переноса
        self.wrap_mode_btn.clicked.connect(self.wrap_mode_change)  # привязка обработчика переключателя режима переноса

        self.auto_format_btn = QPushButton('Список (введите *)')  # создание кнопки автоформатирования
        self.auto_format_btn.clicked.connect(self.auto_format_mode_change)  # привязка обработчика переключателя
        # режима автоформата

        self.undo_btn = QPushButton('Undo')  # создание кнопки
        self.undo_btn.setEnabled(False)  # установка состояния кнопки по умолчанию
        self.document.undoAvailable.connect(lambda flag: self.undo_btn.setEnabled(flag))
        # создание сигнала о доступности операции
        self.undo_btn.clicked.connect(self.document.undo)  # привязка обработчика к кнопке
        self.redo_btn = QPushButton('Redo')  # создание кнопки
        # создание сигнала о доступности операции
        self.document.redoAvailable.connect(lambda flag: self.redo_btn.setEnabled(flag))
        self.redo_btn.setEnabled(False)  # установка состояния кнопки по умолчанию
        self.redo_btn.clicked.connect(self.document.redo)  # привязка обработчика к кнопке

        self.search_field = QLineEdit()  # создание редактируемого поля для поиска текста
        self.search_field.setPlaceholderText('Введите текст для поиска')  # установка подсказки
        self.search_btn = QPushButton('Поиск')  # создание кнопки для поиска
        self.search_btn.setEnabled(False)  # по умолчанию кнопка заблокирована
        self.forward_btn = QPushButton('Вперед')  # создание кнопки для перехода к следующей подстроке
        self.forward_btn.setEnabled(False)  # по умолчанию кнопка заблокирована
        # сигнал на изменение поля ввода и привязка обработчика для изменения активации кнопки поиска
        self.search_field.textChanged.connect(lambda: self.btn_status_change(self.search_btn, self.search_field))
        self.search_btn.clicked.connect()
        # TODO продолжить

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(self.text_edit, 0, 0, 1, 2)  # размещение виджета в сетке
        self.grid.addWidget(self.undo_indicator, 1, 0)
        self.grid.addWidget(self.redo_indicator, 1, 1)
        self.grid.addWidget(self.undo_btn, 2, 0)
        self.grid.addWidget(self.redo_btn, 2, 1)
        self.grid.addWidget(self.wrap_mode_btn, 3, 0)
        self.grid.addWidget(self.auto_format_btn, 3, 1)
        self.grid.addWidget(self.save_btn, 4, 0)
        self.grid.addWidget(self.search_field, 5, 0, 1, 2)
        self.grid.addWidget(self.search_btn, 6, 0)
        self.grid.addWidget(self.forward_btn, 6, 1)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в окне приложения

    @staticmethod
    def btn_status_change(btn: QPushButton, field: QLineEdit) -> None:
        """
        Обработчика сигнала на изменение поля ввода текста для поиска и изменения активности кнопки Поиск
        :param btn:  ссылка на кнопку
        :param field: ссылка на поле ввода
        :return: None
        """
        if field.text():
            btn.setEnabled(True)
        else:
            btn.setEnabled(False)

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
