"""
Основные компоненты интерфейса. Область редактирования, текстовый браузер.

Класс QTextBrowser расширяет возможности класса QTextEdi t и реализует текстовый браузер
с возможностью перехода по гиперссылкам. Иерархия наследования выглядит так:
(QObject, QPaintDevice) - QWidget - QFrame - QAbstractScrollArea - QTextEdit - QTextBrowser
Формат конструктора класса QTextBrowser:
QTextBrowser([parent=None])
Класс QTextBrowser поддерживает следующие основные методы (полный их список смотрите
на странице https://doc.qt.io/qt-6/qtextbrowser.html):
♦ setSource() - загружает ресурс. Формат метода:
  setSource(<Интернет-адрес>[, type=ResourceType.UnknownResource])
  Интернет-адрес указывается в виде объекта класса QUrl из класса QtCore. Параметр type
  задает тип открываемого ресурса в виде одного из следующих элементов перечисления_
  ResourceType из класса QTextDocument:
  • UnknownResource - неизвестный ресурс или ресурс вообще не загружен;
  • HtmlResource - НТМL-документ;
  • ImageResource - графическое изображение;
  • StyleSheetResource - таблица стилей CSS;
  • MarkdownResource - документ в формате Markdown.
  Пример:
  # Загружаем и выводим содержимое текстового файла
  url = QtCore.QUrl("text.txt")
  browser.setSource(url)
  Метод является слотом;
♦ source() - возвращает объект класса QUrl с адресом текущего ресурса;
♦ reload() - перезагружает текущий ресурс; Метод является слотом;
♦ home() - загружает первый ресурс из списка истории. Метод является слотом;
♦ backward() - загружает предыдущий ресурс из списка истории. Метод является слотом;
♦ forward() - загружает следующий ресурс из списка истории. Метод является слотом;
♦ backwardHistoryCount() - возвращает количество предыдущих ресурсов из списка истории;
♦ forwardHistoryCount() - возвращает количество следующих ресурсов из списка истории;
♦ isBackwardAvailable() - возвращает значение True, если существует предыдущий
  ресурс в списке истории, и False - в противном случае;
♦ isForwardAvailable() - возвращает значение True, если существует следующий ресурс
  в списке истории, и False - в противном случае;
♦ clearHistory() - очищает список истории;
♦ historyTitle(<Количество позиций>) - если в качестве параметра указано отрицательное
  число, возвращает заголовок предыдущего ресурса, отстоящего от текущего на заданное
  число позиций, если 0 - заголовок текущего ресурса, а если положительное
  число - заголовок следующего ресурса, также отстоящего от текущего на заданное
  число позиций;
♦ historyUrl(<Количество позиций>) - то же самое, что historyTitle(), но возвращает
  адрес ресурса в виде объекта класса QUrl;
♦ setOpenLinks(<Флаг>) - если в качестве параметра указано значение True, то переход
  по гиперссылкам будет разрешен (поведение по умолчанию). Значение False запрещает
  переход;
♦ setOpenExternalLinks(<Флаг>) - если в . качестве параметра указано значение True, то
  переход по гиперссылкам, ведущим на внешние ресурсы, будет разрешен (при этом сигнал
  anchorClicked() не генерируется). Значение False запрещает переход (поведение по
  умолчанию).
Класс QTextBrowser поддерживает сигналы:
♦ anchorClicked(<Интернет-адрес>) - генерируется при переходе по гиперссылке. Внутри
  обработчика через параметр доступен интернет-адрес гиперссылки в виде объекта
  класса QUrl;
♦ backwardAvailable (<Признак>) - генерируется при изменении списка предыдущих
  ресурсов. Внутри обработчика через параметр доступно значение True, если в списке
  истории имеются предыдущие ресурсы, и False - в противном случае;
♦ forwardAvailable (<Признак>) - генерируется при изменении списка следующих ресурсов.
  В обработчике через параметр доступно значение True, если в списке истории имеются
  следующие ресурсы, и False - в противном случае;
♦ highlighted(<Интернет-адрес>) - генерируется при наведении указателя мыши на гиперссылку.
  Внутри обработчика через параметр доступен интернет-адрес гиперссьmки
  в виде объекта класса QUrl или пустой объект;
♦ historyChanged() - генерируется при изменении списка истории;
♦ sourceChanged(<Интернет-адрес>). - генерируется при переходе на новый ресурс. Внутри
  обработчика через параметр доступен интернет-адрес загруженного ресурса в виде
  объекта класса QUrl.
"""
#TODO переделать в браузер
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
                           QTextCursor,
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
        # todo задокументировать код по курсору
        self.find_results = []  # создание аттрибута для хранения результатов поиска
        self.cursor_position = 0  # хранение текущего элемента в результатах поиска
        self.text_cursor = QTextCursor(self.document)  # создание объекта текстового курсора в документе
        self.search_btn.clicked.connect(self.text_search)  # привязка обработчика с реализацией поиска
        self.forward_btn.clicked.connect(self.cursor_forward)  # привязка обработчика с перебором результатов поиска

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

    def text_search(self) -> None:
        """
        Обработчик сигнала нажатия на кнопку поиска с реализаций поиска
        :return: None
        """
        self.find_results.clear()  # очистка результатов поиска
        if self.document.find(self.search_field.text()).isNull():  # проверка наличия результатов поиска
            pass  # если результатов нет, то поиск завершается
        else:
            self.find_results.append(self.document.find(self.search_field.text()))  # добавление первого
            # результата поиска
            while True:  # цикл поиска с добавлением последующих результатов поиска
                self.find_results.append(self.document.find(self.search_field.text(),
                                                            self.find_results[-1].selectionEnd()))
                if self.find_results[-1].isNull():  # проверка результативности последнего писка
                    self.find_results.pop()  # если результаты последнего поиска пустые, то удаляем их из списка
                    self.cursor_position = 0  # сбрасываем текущую позицию в списке результатов поиска
                    break  # если результат поиска нулевой, то выходим из цикла
            self.forward_btn.setEnabled(True)  # если поиска успешен активируем кнопку перебора результатов

    def cursor_forward(self) -> None:
        """
        Обработчик сигнала нажатия кнопки для перебора результатов поиска
        :return: None
        """
        if self.cursor_position == len(self.find_results):  # проверка текущей позиции в переборе
            self.cursor_position = 0  # сброс текущей позиции по достижении конца списка результатов поиска
        self.text_edit.setTextCursor(self.find_results[self.cursor_position])  # передачи указателя результатов поиска
        # в область редактирования
        self.cursor_position += 1  # увеличение счетчика текущей позиции
        self.text_edit.setFocus()  # установка фокуса ввода на область редактирования

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
