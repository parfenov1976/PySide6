"""
Основные компоненты интерфейса. Поле для ввода даты.

Для ввода даты и времени предназначены классы QDateTimeEdit (ввод временной отметки,
т. е. значения даты и времени), QDateEdit (ввод даты) и QTimeEdit (ввод времени).
Поля могут содержать кнопки, которые позволяют щелчками мыши увеличивать и уменьшать
значение внутри поля.
Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QAbstractSpinBox - QDateTimeEdit
(QObject, QPaintDevice) - QWidget - QAbstractSpinВox - QDateTimeEdit - QDateEdit
(QObject, QPaintDevice) - QWidget - QAbstractSpinВox - QDateTimeEdit - QTimeEdit
Форматы конструкторов классов:
QDateTimeEdit([parent=None])
QDateTimeEdit(<Временная отметка>[, parent=None])
QDateTimeEdit(<Дата>[, parent=None])
QDateTimeEdit(<Время>[, parent=None])
QDateEdit([parent=None])
QDateEdit(<Дата>[, parent=None])
QTimeEdit([parent=None])
QTimeEdit(<Время>[, parent=None])
В параметре <Временная отметка> можно указать объект класса QDateTime или datetime
(из Python). Преобразовать объект класса QDateTime в объект класса datetime позволяет
метод toPyDateTime() класса QDateTime:
>> from PyQtб import QtCore
>> d = QtCore.QDateTime(2022, 2, 18, 14, 23)
>> dPyQt6.QtCore.QDateTime(2022, 2, 18, 14, 23) >>> d.toPyDateTime()
datetime.datetime(2022, 2, 18, 14, 23)
В качестве параметра <Дата> можно указать объект класса QDate или date (из Python).
Преобразовать объект класса QDate в объект класса date позволяет метод toPyDate()
класса QDate.
В параметре <Время> можно указать объект класса QTime или time (из Python).
Преобразовать объект класса QTime в объект класса time позволяет метод toPyTime()
класса QTime.
Классы QDateTime, QDate и QTime определены в модуле QtCore.
Класс QDateTimeEdit наследует все методы из класса QAbstractSpinBox и дополнительно
реализует следующие методы (здесь приведены только самые полезные - полный их список
смотрите на странице https://doc.qt.io/qt-6/qdatetimeedit.html):
♦ setDateTime(<Временная отметка QDateTime или <datetime>) - устанавливает временную
  отметку. Метод является слотом;
♦ setDate(<Дата QDate или date>) - устанавливает дату. Метод является слотом;
♦ setTime(<Время QTime или time>) - устанавливает время. Метод является слотом;
♦ dateTime() - возвращает объект класса QDateTime с временной отметкой;
♦ date() - возвращает объект класса QDate с датой;
♦ time() - возвращает объект класса QTime со временем;
♦ setDateTimeRange(<Минимум>, <Максимум>) - задает минимальное и максимальное допустимые
  значения для временной отметки;
♦ setMinimumDateTime(<Минимум>) - задает минимальное допустимое значение временной
  отметки;
♦ setMaximumDateTime(<Максимум>) - задает максимальное допустимое значение временной
  отметки.
В параметрах трех последних методов указываются объекты класса QDate или date;
♦ setDateRange(<Минимум>, <Максимум>) - задают минимальное и максимальное допустимые
  значения для даты;
♦ setMinimumDate(<Минимум>) -задает минимальное допустимое значение даты;
♦ setMaximumDate(<Максимум>) - задает максимальное допустимое значение даты.
  В параметрах трех последних методов указываются объекты класса QDateTime или dateTime;
♦ setTimeRange (<Минимум>, <Максимум>) - задает минимальное и максимальное допустимые
  значения для времени;
♦ setMinimumTime(<Минимум>) - задает минимальное допустимое значение времени;
♦ setMaximumTime(<Максимум>) - задает максимальное допустимое значение времени.
  В параметрах трех последних методов указываются объекты класса QTime или time;
♦ setDisplayFormat(<Формат>) -задает формат отображения даты и времени. В качестве
  параметра указывается строка, содержащая специальные символы. Пример задания строки
  формата:
  dateTimeEdit.setDisplayFormat("dd.ММ.yyyy HH:mm:ss")
♦ setTimeSpec(<Зона>) - задает временную зону. В качестве параметра можно указать
  следующие элементы перечисления TimeSpec из модуля QtCore.Qt: LocalTime (местное
  время), uтс (всемирное координированное время) или OffsetFromUTC (смещение относительно
  всемирного координированного времени, исчисляемое в секундах);
♦ setCalendarPopup(<Флаг>) - если в качестве параметра указано значение True, то дату
  можно будет выбрать с помощью календаря, который появится на экране при щелчке на
  кнопке с направленной вниз стрелкой, выведенной вместо стандартных кнопок-стрелок
♦ setSelectedSection(<Секция>) - выделяет указанную секцию. В качестве параметра можно
  задать один из следующих элементов перечисления section из класса QDateTimeEdit:
  • NoSection - ни одна секция не будет выделена;
  • DaySection - будет выделена секция числа;
  • MonthSection - секция месяца;
  • YearSection - секция года;
  • HourSection - секция часов;
  • MinuteSection - секция минут;
  • SecondSection - секция секунд;
  • MSecSection - секция миллисекунд;
  • AmPmSection - секция времени суток (АМ или РМ);
♦ setCurrentSection(<Секция Section>) - делает указанную секцию текущей;
♦ setCurrentSectionIndex(<Индекс>) - делает секцию с указанным индексом текущей;
♦ currentSection() - возвращает тип текущей секции в виде одного из элементов
  перечисления Section из класса QDateTimeEdit;
♦ currentSectionIndex() - возвращает индекс текущей секции;
♦ sectionCount () - возвращает количество секций внутри поля;
♦ sectionAt (<Индекс>) - возвращает обозначение типа секции по указанному индексу
  в виде одного из элементов перечисления Section из класса QDateTimeEdit;
♦ sectionText (<Секция Section>) - возвращает текст указанной секции.
При изменении значений даты или времени генерируются сигналы timeChanged(<Время>),
dateChanged(<Дата>) и dateTimeChanged(<Временная отметка>). Внутри обработчиков через
параметр доступно новое значение в виде объекта класса QTime, QDate или QDateTime
соответственно.
Классы QDateEdit и QTimeEdit отличаются от класса QDateTimeEdit только форматом
отображаемых данных. Эти классы наследуют методы базовых классов и не добавляют
никаких своих методов.
"""

from PySide6.QtWidgets import (QMainWindow,
                               QDateTimeEdit,
                               QDateEdit,
                               QTimeEdit,
                               QGridLayout,
                               QLabel,
                               QWidget,
                               )
from PySide6.QtCore import (QDateTime,
                            QDate,
                            QTime,
                            )

import datetime

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, класса поля ввода
даты и времени QDateTimeEdit, класса ввода даты QDateEdit, класса ввода времени QTimeEdit,
класса слоя сетки для виджетов QGridLayout, класса ярлыка QLabel, класса базового пустого
виджета QWidget

Импорт из модуля PySide6.QtCore класса даты и времени QDateTime, класса даты QDate,
класса времени QTime

Импорт из стандартной библиотеки модуля datetime, содержащего классы даты и времени datetime, 
date и time
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
        self.setWindowTitle('Поле ввода даты и времени')  # установка заголовка главного окна приложения
        self.resize(600, 200)  # установка исходного размера главного окна приложения
        self.date_time_1 = QDateTimeEdit(QDateTime(2024, 6, 9, 11, 12, 0))  # создание поля для ввода даты и времени
        # с установка значения
        self.date_time_1.setWrapping(True)  # настройка прокрутки значений по кругу
        self.date_time_1.dateTimeChanged.connect(self.date_time_changed)  # привязка обработчика на изменение значения
        self.date_time_2 = QDateTimeEdit(datetime.datetime(2024, 6, 9, 11, 12))
        # создание поля для ввода времени и даты с установкой значения
        self.date_time_2.setWrapping(True)  # настройка прокрутки значений по кругу
        self.date_time_2.dateTimeChanged.connect(self.date_time_changed)  # привязка обработчика на изменение значения
        self.date_1 = QDateEdit()  # создание поля ввода даты
        self.date_1.setDate(QDate(2024, 6, 9))  # установка значения даты
        self.date_1.setCalendarPopup(True)  # подключение всплывающего календаря для установки даны
        self.date_1.dateChanged.connect(self.date_time_changed)  # привязка обработчика на изменение значения
        self.date_2 = QDateEdit(datetime.date(2024, 6, 9))  # создание поля для ввода даты
        # с установкой значения
        self.date_2.setDisplayFormat('yy.M.d')  # настройка формата отображения даты
        self.date_2.setWrapping(True)  # настройка прокрутки значений по кругу
        self.date_2.dateChanged.connect(self.date_time_changed)  # привязка обработчика на изменение значения поля
        self.time_1 = QTimeEdit(QTime(12, 30))  # создание поля ввода времени с установкой значения
        self.time_1.setWrapping(True)  # настройка прокрутки значений по кругу
        self.time_1.timeChanged.connect(self.date_time_changed)  # привязка обработчика на изменение значения поля
        self.time_2 = QTimeEdit(datetime.time(12, 30))  # создание поля для ввода времени
        # с установкой значения
        self.time_2.setWrapping(True)  # настройка прокрутки значений по кругу
        self.time_2.setButtonSymbols(QTimeEdit.ButtonSymbols.PlusMinus)  # изменение символов на кнопках прокрутки
        self.time_2.timeChanged.connect(self.date_time_changed)  # привязка обработчика на изменение значения поля
        self.lbl = QLabel()  # создание ярлыка для отображения измененных значений

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(QLabel('Объекты даты и времени'), 0, 0)  # размещение виджета в сетке
        self.grid.addWidget(QLabel('PySide6'), 0, 1)
        self.grid.addWidget(QLabel('Python'), 0, 2)
        self.grid.addWidget(self.date_time_1, 1, 1)
        self.grid.addWidget(self.date_time_2, 1, 2)
        self.grid.addWidget(QLabel('Дата и Время: ДД.ММ.ГГГГ ЧЧ:ММ'), 1, 0)
        self.grid.addWidget(QLabel('Дата ДД.ММ.ГГГГ / ГГ.М.Д'), 2, 0)
        self.grid.addWidget(self.date_1, 2, 1)
        self.grid.addWidget(self.date_2, 2, 2)
        self.grid.addWidget(QLabel('Время'), 3, 0)
        self.grid.addWidget(self.time_1, 3, 1)
        self.grid.addWidget(self.time_2, 3, 2)
        self.grid.addWidget(QLabel('Новое значение'), 4, 0)
        self.grid.addWidget(self.lbl, 4,1)

        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя сетки в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне приложения

    def date_time_changed(self, dt: QDateTime | QDate | QTime) -> None:
        """
        Обработчика сигнала на изменение значения поля
        :param dt: QDateTime, QDate, QTime - объект времени и/или даты
        :return: None
        """
        self.lbl.setText(dt.toString())  # преобразование объекта времени и/или даты в строку и вывод в ярлык


if __name__ == "__main__":  # условие проверки запуска данного файла для предотвращения запуска
    # кода верхнего уровня при импортировании данного файла как модуля
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
