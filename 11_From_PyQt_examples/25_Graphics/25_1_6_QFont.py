"""
Работа с графикой. Вспомогательные классы. Класс QFont: шрифт

Класс QFont описывает характеристики шрифта. Форматы конструктора класса:
QFont()
QFont(<Название шрифта>[, pointSize=-1] [, weight=-1] [, italic=False])
QFont(<Исходный объект QFont>)
Первый формат создает объект шрифта с настройками, используемыми приложением по
умолчанию. Установить шрифт приложения по умолчанию позволяет статический метод
setFont() класса QApplication.
Второй формат позволяет указать основные характеристики шрифта. В первом параметре
указывается название шрифта или семейства в виде строки. Необязательный параметр
pointSize задает размер шрифта. В параметре weight можно указать степень жирности
шрифта: число от О до 99 или значение элемента Thin, ExtraLight, Light, Normal, Medium,
DemiBold, Bold, ExtraBold или Black перечисления Weight из класса QFont. Если в параметре
italic указано значение True, шрифт будет курсивным.
Третий формат создает копию заданного исходного объекта.
Класс QFont поддерживает следующие методы (здесь приведены только основные - полный
их список можно найти по адресу https://doc.qt.io/qt-6/qfont.html):
♦ setFamily(<Название шрифта>) - задает название шрифта или семейства шрифтов;
♦ family() - возвращает название шрифта;
♦ setPointSize(<Размер типа int>) и setPointSizeF(<Размер типа float>) - задают
  размер шрифта в пунктах;
♦ setPixelSize(<Размер>) - задает размер шрифта в пикселах;
♦ pointSize() - возвращает размер шрифта в пунктах в виде целого числа или значение
  -1, если размер шрифта был установлен в пикселах;
♦ pointSizeF() - возвращает размер шрифта в пунктах в виде вещественного числа или
  значение -1, если размер шрифта был установлен в пикселах;
♦ pixelSize() - возвращает размер шрифта в пикселах или -1, если размер шрифта был
  установлен в пунктах;
♦ setWeight(<Жирность Weight>) - задает степень жирности шрифта;
♦ weight() - возвращает степень жирности шрифта;
♦ setBold(<Флаг>) - если в качестве параметра указано значение True, то жирность
  шрифта устанавливается равной значению элемента Bold, а если False - то равной значению
  элемента Normal перечисления Weight из класса QFont;
♦ bold() - возвращает значение True, если степень жирности шрифта больше значения
  элемента Normal перечисления Weight из класса QFont, и False - в противном случае;
♦ setItalic(<Флаг>) - если в качестве параметра указано значение True, шрифт будет
  курсивным, а если False - обычного начертания;
♦ italic() - возвращает значение True, если шрифт курсивный, и False - в противном
  случае;
♦ setUnderline(<Флаг>) - если в качестве параметра указано значение True, текст будет
  подчеркнутым, а если False - неподчеркнутым;
♦ underline() - возвращает значение True, если текст подчеркнут, и False - в противном
  случае;
♦ setOverline(<Флаг>) - если в качестве параметра указано значение True, то текст будет
  надчеркнутым;
♦ overline() - возвращает значение True, если текст надчеркнут, и False - в противном
  случае;
♦ setStrikeOut (<Флаг>) - если в качестве параметра указано значение True, текст будет
  зачеркнутым;
♦ strikeOut() - возвращает значение True, если текст зачеркнут, и False - в противном
  случае.
Получить список всех доступных шрифтов позволяет метод families() класса
QFontDatabase. Метод возвращает список строк. Отметим, что перед его вызовом следует
создать объект класса QApplication, в противном случае мы получим ошибку исполнения:
from PyQt6 import QtGui, QtWidgets
арр = QtWidgets.QApplication(list())
print(QtGui.QFontDatabase.families())
Чтобы получить список доступных стилей для указанного шрифта, следует воспользоваться
статическим методом styles(<Название шрифта>) класса QFontDatabase:
print(QtGui.QFontDatabase.styles("Arial"))
# [ 'Обычный' , 'Полужирный' , 'Полужирный Курсив' , 'Курсив' ]
Получить допустимые размеры для указанного стиля можно с помощью статического метода
smoothSizes(<Название шрифта>, <Стиль>) класса QFontDatabase:
print(QtGui.QFontDatabase.smoothSizes("Arial", "Обычный"))
# (6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
Очень часто необходимо произвести выравнивание выводимого текста внутри некоторой
области. Чтобы это сделать, нужно знать размеры области, в которую вписан текст. Получить
эти значения можно с помощью класса QFontMetrics, конструктор которого имеет следующий
формат вызова:
QFontMetrics(<Шрифт QFont>)
Класс QFontMetrics поддерживает следующие полезные методы:
♦ horizontalAdvance(<Текст> [, length=-1]) - возвращает расстояние от начала текста
  <Текст> до позиции, в которой должен начаться другой текст. Параметр length позволяет
  ограничить количество символов;
♦ height() - возвращает высоту шрифта;
♦ boundingRect(<Текст>) - возвращает объект класса QRect с координатами и размерами
  прямоугольной области, в которую вписан текст.
Вот пример получения размеров области:
font = QtGui. QFont ( "Tahoma", 16)
fm = QtGui.QFontMetrics(font)
print(fm.horizontalAdvance("Строка"))   # 67
print(fm.height())                      # 25
print(fm.boundingRect("Строка"))        # PyQt6.QtCore.QRect(O, -21, 66, 25)
Обратите внимание, что значения, возвращаемые методами horizontalAdvance() и
QRect.width(), различаются.
    ПРИМЕЧАНИЕ
    Класс QFontMetrics предназначен для работы с целыми числами. Чтобы работать с вещественными
    числами, необходимо использовать класс QFontMetricsF.
"""

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QFont,
                           QFontMetrics,
                           )
from PySide6.QtCore import (Qt,
                            )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, класса шрифтов QFont, класса метрик области для вписывания текста QFontMetrics

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt, 
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
        self.setWindowTitle('Класс объекта шрифта QFont')  # установка заголовка главного окна
        self.resize(300, 300)  # установка исходного размера главного окна

    def paintEvent(self, event) -> None:
        """
        Обработчик события рисования
        :param event: событие рисования
        :return: None
        """
        painter = QPainter(self)  # создание объекта рисовальщика с подключением поверхности рисования
        black = Qt.GlobalColor.black  # создание объекта цвета из глобального перечислителя цветов
        white = Qt.GlobalColor.white  # создание объекта цвета из глобального перечислителя цветов
        red = Qt.GlobalColor.red  # создание объекта цвета из глобального перечислителя цветов
        painter.setPen(QPen(black))  # создание пера с настройками и установка пера в рисовальщик
        painter.setBrush(QBrush(white))  # создание и применение кисти для заливки фигур к рисовальщику
        painter.drawRect(3, 3, 294, 294)  # рисование прямоугольника
        painter.setPen(QPen(red, 5))  # установка настроек пера в рисовальщик

        font = QFont('Tahoma', 16)  # создание объекта шрифта
        fm = QFontMetrics(font)  # создание области для вписывания текста
        print(fm.horizontalAdvance('Строка'))  # расстояние от начала текста до начала другого текста
        print(fm.height())  # вывод высоты шрифта
        print(fm.boundingRect('Строка'))  # вывод прямоугольника, в который вписан текст
        painter.setFont(font)  # передача в рисовальщик настроек шрифта
        painter.drawText(50, 50, 'Строка')  # рисование текста


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
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
