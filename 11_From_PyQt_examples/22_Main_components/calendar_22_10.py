"""
Основные компоненты интерфейса. Виджет календаря для выбора даты

Класс QCalendarWidget реализует календарь с возможностью выбора даты и перемещения
по месяцам с помощью мыши и клавиатуры. Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QCalendarWidget
Формат конструктора класса QCalendarWidget:
QCalendarWidget([parent=None])
Класс QCalendarWidget поддерживает следующие методы (здесь представлены только основные
- полный их список смотрите на странице https://doc.qt.io/qt-6/qcalendarwidget.html):
♦ setSelectedDate(<Дата QDate или date>) - устанавливает дату. Метод является слотом;
♦ selectedDate() - возвращает объект класса QDate с выбранной датой;
♦ setDateRange(<Минимум>, <Максимум>) - задает минимальное и максимальное допустимые
  значения для даты. Метод является слотом;
♦ setMinimumDate (<Минимум>) - задает минимальное допустимое значение даты;
♦ setMaximumDate (<Максимум>) -задает максимальное допустимое значение даты.
  В параметрах трех последних методов указывается объект класса QDate или date;
♦ setcurrentPage(<Год>, <Месяц>) - делает текущей страницу календаря с указанными
  годом и месяцем, которые задаются целыми числами. Выбранная дата при этом не изменяется.
  Метод является слотом;
♦ monthShown() - возвращает месяц (число от 1 до 12), отображаемый на текущей странице;
♦ yearShown() - возвращает год, отображаемый на текущей странице;
♦ showSelectedDate() - отображает страницу с выбранной датой. Выбранная дата при
  этом не изменяется. Метод является слотом;
♦ showToday() - отображает страницу с сегодняшней датой. Выбранная дата при этом не
  изменяется. Метод является слотом;
♦ showPreviousMonth() - отображает страницу с предыдущим месяцем. Выбранная дата
  при этом не изменяется. Метод является слотом;
♦ showNextMonth() - отображает страницу со следующим месяцем. Выбранная дата при
  этом не изменяется. Метод является слотом;
♦ showPreviousYear() - отображает страницу с текущим месяцем в предыдущем году.
  Выбранная дата не изменяется. Метод является слотом;
♦ showNextYear() - отображает страницу с текущим месяцем в следующем году. Выбранная
  дата при этом не изменяется. Метод является слотом;
♦ setFirstDayOfWeek(<День>) - задает первый день недели. По умолчанию используется
  воскресенье. Чтобы первым днем недели сделать понедельник, следует в качестве параметра
  указать элемент Monday перечисления DayOfWeek из класса QtCore.Qt;
♦ setNavigationBarVisible(<Флаг>) - если в качестве параметра указано значение False,
  то панель навигации выводиться не будет. Метод является слотом;
♦ setHorizontalHeaderFormat(<Формат>) - задает формат горизонтального заголовка.
  В качестве параметра можно указать следующие элементы перечисления
  HorizontalHeaderFormat класса QCalendarWidget:
  • NoHorizontalHeader - заголовок не отображается;
  • SingleLetterDayNames - отображается только первая буква из названия дня недели;
  • ShortDayNames - отображается сокращенное название дня недели;
  • LongDayNames - отображается полное название дня недели;
♦ setVerticalHeaderFormat(<Формат>) - задает формат вертикального заголовка. В качестве
  параметра можно указать следующие элементы перечисления VerticalHeaderFormat
  из класса QCalendarWidget:
  • NoVerticalHeader - заголовок не отображается;
  • ISOWeekNumbers - отображается номер недели в году;
♦ setGridVisible(<Флаг>) - если в качестве параметра указано значение True, линии сетки
  будут отображены. Метод является слотом;
♦ setSelectionMode(<Режим>) - задает режим выделения даты. В качестве параметра
  можно указать следующие элементы перечисления SelectionMode из класса
  QCalendarWidget:
  • NoSelection - дата не может быть выбрана пользователем;
  • SingleSelection - может быть выбрана одна дата;
♦ setHeaderTextFormat(<Формат>) - задает формат ячеек заголовка. В параметре указывается
  объект класса QTextCharFormat из модуля QtGui;
♦ setWeekdayTextFormat(<День недели>, <Формат>) - определяет формат ячеек для· указанного
  дня недели. В первом параметре задаются следующие элементы перечисления
  DayOfWeek из модуля QCore.Qt: Monday (понедельник), Tuesday (вторник), Wednesday (среда),
  Thursday (четверг), Friday (пятница), Saturday (суббота) или sunday (воскресенье), а
  во втором параметре - объект класса QTextCharFormat;
♦ setDateTextFormat (<Дата QDate или date>, <Формат QTextCharFormat>) - задает формат
  ячейки с указанной датой.
Класс QCalendarWidget поддерживает такие сигналы:
♦ activated(<Дата QDate>) - генерируется при двойном щелчке мышью или нажатии клавиши
  <Enter>. Внутри обработчика через параметр доступна текущая дата;
♦ clicked(<Дата QDate>) - генерируется при щелчке мышью на какой-либо дате. Внутри
  обработчика через параметр доступна выбранная дата;
♦ currentPageChanged (<Год>, <Месяц>) - генерируется при изменении страницы. Внутри
  обработчика через первый параметр доступен год, а через второй - месяц. Обе величины
  задаются целыми числами;
♦ selectionChanged() - генерируется при изменении выбранной даты пользователем или
  из программного кода.
"""
import PySide6.QtCore
from PySide6.QtWidgets import (QMainWindow,
                               QCalendarWidget,
                               QGridLayout,
                               QWidget,
                               QLabel,
                               QFrame,
                               )
"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow,
класса виджета ярлыка QLabel, класса слоя сетки для виджетов QGridLayout,
базового класса пустого виджета QWidget, класса рамки для виджетов QFrame
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
        # QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        super().__init__(parent)  # вызов конструктора родительского класса через функцию super()
        self.setWindowTitle('Календарь')  # установка заголовка главного окна приложения
        self.resize(300, 300)  # установка исходного размера главного окна приложения
        self.calendar = QCalendarWidget()  # создание экземпляра виджета календаря
        self.calendar.showToday()  # установка по умолчанию страницы с текущей датой
        self.calendar.setGridVisible(True)  # установка флага отображения сетки календаря
        self.calendar.activated.connect(self.on_activated)  # привязка обработчика на выбор даты двойным
        # кликом или клавишей Ввод
        self.lbl_1 = QLabel()  # создание ярлыка
        self.lbl_1.setFrameStyle(QFrame.Shape.Box)  # создание рамки вокруг ярлыка
        self.calendar.clicked.connect(self.on_clicked)  # привязка обработчика выделения даты
        self.lbl_2 = QLabel()  # создание ярлыка
        self.lbl_2.setFrameStyle(QFrame.Shape.Box)  # создание рамки вокруг ярлыка
        self.calendar.currentPageChanged.connect(self.on_changed)  # привязка обработчика смены страницы календаря
        self.lbl_year = QLabel(str(self.calendar.yearShown()))  # создание ярлыка для отображения года
        self.lbl_year.setFrameStyle(QFrame.Shape.Box)  # создание рамки вокруг ярлыка
        self.lbl_month = QLabel(str(self.calendar.monthShown()))  # создание ярлыка для отображения номера месяца
        self.lbl_month.setFrameStyle(QFrame.Shape.Box)  # создание рамки вокруг ярлыка

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(self.calendar, 0, 0, 1, 2)  # размещение виджета на слое сетке
        self.grid.addWidget(QLabel('Выбранная дата'), 1, 0)
        self.grid.addWidget(self.lbl_1, 1, 1)
        self.grid.addWidget(QLabel('Выделенная дата'), 2, 0)
        self.grid.addWidget(self.lbl_2, 2, 1)
        self.grid.addWidget(self.lbl_year, 3, 0)
        self.grid.addWidget(self.lbl_month, 3, 1)

        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(self.container)  # размещение контейнера со слоями с виджетами в главном окне

    def on_activated(self, date: PySide6.QtCore.QDate) -> None:
        """
        Обработчик сигнала выбора даты
        :param date: PySide6.QtCore.QDate - объект даты
        :return: None
        """
        self.lbl_1.setText(date.toString())

    def on_clicked(self, date: PySide6.QtCore.QDate) -> None:
        """
        Обработчик сигнала на выделение даты
        :param date: PySide6.QtCore.QDate - объект даты
        :return: None
        """
        self.lbl_2.setText(date.toString())

    def on_changed(self, year: int, month: int) -> None:
        """
        Обработчик сигнала смены страницы календаря
        :param year: int - год
        :param month: int - номер месяцы
        :return: None
        """
        self.lbl_year.setText(f'{year}')
        self.lbl_month.setText(f'{month}')


if __name__ == '__main__':  # проверка условия запуска данного модуля для предотвращения
    # запуска кода верхнего уровня при импортировании
    from PySide6.QtWidgets import QApplication
    import sys

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
    window.show()  # включение видимости окна, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
