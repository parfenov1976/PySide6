"""
Основные компоненты интерфейса. Область редактирования, указание параметров текста и фона.

Для изменения параметров текста и фона предназначены следующие методы класса QTextEdit
(полный их список смотрите на странице https://doc.qt.io/qt-6/qtextedit.html):
♦ setCurrentFont(<Шрифт>) - задает текущий шрифт. Метод является слотом. В качестве
  параметра указывается объект класса QFont из модуля QtGui. Конструктор этого класса
  имеет следующий формат:
  <Шрифт> = QFont(<Название шрифта>[, pointSize=-1][, weight=-1][, italic=False])
  В первом параметре задается название шрифта в виде строки. Необязательный параметр
  pointSize устанавливает размер шрифта. В параметре weight можно указать степень
  жирности шрифта в виде числа от О до 99 или следующего элемента перечисления
  Weight из класса QFont: Thin, ExtraLight, Light, Normal, Medium, DemiBold, Bold,
  ExtraBold или Black. Если в параметре italic указано значение True, шрифт будет
  курсивным;
♦ currentFont() - возвращает объект класса QFont с текущими характеристиками шрифта;
♦ setFontFamily(<Название шрифта>) - задает название текущего шрифта. Метод являет
  ся слотом;
♦ fontFamily() - возвращает название текущего шрифта;
♦ setFontPointSize(<Размер>) - задает размер текущего шрифта В пунктах. Метод является
  слотом;
♦ fontPointSize() - возвращает размер текущего шрифта;
♦ setFontWeight(<Жирность>) - задает жирность текущего шрифта в виде числа от О до
  99 или одного из элементов перечисления weight из класса QFont. Метод является слотом;
♦ fontWeight() - возвращает жирность текущего шрифта;
♦ setFontItalic(<Флаг>) - если в качестве параметра указано значение True, шрифт будет
  курсивным. Метод является слотом;
♦ fontItalic() - возвращает True, если шрифт курсивный, и False - в противном случае;
♦ setFontUnderline(<Флаг>) - если в качестве параметра указано значение True, текст
  будет подчеркнутым. Метод является слотом;
♦ fontUnderline() - возвращает True, если текст подчеркнутый, и False - в противном
  случае;
♦ setTextColor(<Цвет>) - задает цвет текущего текста. В качестве значения можно указать
  один из элементов перечисления GlobalColor из модуля QtCore.Qt (например, black,
  white и т. д.) или объект класса QColor из модуля QtGui (например, QColor("red"),
  QColor("#ff0000"), QColor(255, о, О)идр.). Метод является слотом;
♦ textColor() - возвращает объект класса QColor с цветом текущего текста;
♦ setTextBackgroundColor(<Цвет>) - задает цвет фона. В качестве значения можно указать
  один из элементов перечисления GlobalColor из модуля QtCore.Qt (например, black,
  white и т. д.) или объект класса QColor (например, QColor("red"), QColor("#ff0000"),
  QColor(255, о, О)идр.). Метод является слотом;
♦ textBackgroundColor() - возвращает объект класса QColor с цветом фона;
♦ setAlignment(<Выравнивание>) - задает горизонтальное выравнивание текста внутри
  абзаца. Метод является слотом;
♦ alignment() - возвращает значение выравнивания текста внутри абзаца.
Задать формат символов также можно с помощью класса QTextCharFormat, который определен
в модуле QtGui и поддерживает дополнительные настройки. После создания объекта класса,
его следует передать в метод setCurrentCharFormat(<Формат>). Получить объект класса с
текущими настройками позволяет метод currentCharFormat(). За подробной информацией по
классу QTextCharFormat обращайтесь к странице https://doc.qt.io/qt-6/ qtextcharformat.html.
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
from PySide6.QtGui import QFont, QColor

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класса области редактирования QTextEdit, класса слоя сетки для виджетов QGridLayout,
класса пустого базового виджета QWidget, класса виджета ярлыка QLabel,
класса рамки для виджетов QFrame, класса виджета кнопки QPushButton

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt

Импорт из модуля PySide6.QtGui класса шрифтов QFont, класса цветов QColor
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

        # указание настроек шрифта
        self.text_edit.setCurrentFont(QFont('Times New Roman', pointSize=20, weight=2, italic=True))
        self.text_edit.append(f'{self.text_edit.fontFamily()}')
        self.text_edit.setFontUnderline(True)  # настройки подчеркивания
        self.text_edit.append(f'Underline {self.text_edit.fontUnderline()}')
        self.text_edit.setTextColor(QColor('red'))  # настройки цветка шрифта
        self.text_edit.append(f'Color {self.text_edit.textColor()}')
        self.text_edit.setTextBackgroundColor(QColor('blue'))  # настройки цвета фона текста
        self.text_edit.append(f'BG color {self.text_edit.textBackgroundColor()}')

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
