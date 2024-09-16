"""
Работа с графикой. Вывод текста

Вывести текст позволяет метод drawТext() класса QPainter. Форматы метода:
drawТext(<X>, <У>, <Текст>)
drawТехt(<Координаты QPoint или QPointF>, <Текст>)
drawТext(<X>, <У>, <Ширина>, <Высота>, <Флаги>, <Текст>)
drawТехt(<Прямоугольник QRect или QRectF>, <Флаги>, <Текст>)
drawТехt(<Прямоугольник QRectF>, <Текст>[, option=QTextOption()])
Первые два формата метода выводят текст, начиная с указанных координат.
Следующие два формата выводят текст.в указанную прямоугольную область: При этом текст,
который не помещается в эту область, будет обрезан, если не указан флаг тextDontClip.
Методы возвращают объект класса QRect (QRectF для четвертого формата) с координатами и
размерами прямоугольника, в который вписан текст. В параметре <Флаги> через оператор |
указываются элементы AlignLeft, AlignRight, AlignНCenter, AlignTop, AlignBottom,
AlignVCenter или AlignCenter перечисления AlignmentFlag из модуля QtCore.Qt, задающие
выравнивание текста внутри прямоугольной области, а также следующие элементы
перечисления TextFlag из того же модуля:
♦ TextSingleLine - все пробельные символы (табуляция, возвраты каретки и переводы строки)
  трактуются как пробелы, и текст выводится в одну строку;
♦ TextDontClip - часть текста, вышедшая за пределы указанной прямоугольной области,
  не будет обрезаться;
♦ TextExpandTabs- символы табуляции будут обрабатываться;
♦ TextShowМnemonic - символ, перед которым указан знак &, будет подчеркнут. Чтобы
  вывести символ &, его необходимо удвоить;
♦ TextWordWrap - если текст не помещается на одной строке, будет произведен перенос
  слова без его разрыва;
♦ тextWrapAnywhere - перенос строки может быть выполнен внутри слова;
♦ TextHideМnemonic - то же самое, что и TextShowМnemonic, но символ не подчеркивается;
♦ TextDontPrint - текст не будет напечатан;
♦ TextIncludeTrailingSpaces - размеры текста будут возвращаться с учетом начальных и
  конечных пробелов, если таковые есть в тексте;
♦ TextJustificationForced- задает выравнивание по ширине у последней строки текста.
Пятый формат метода drawТext() также выводит текст в указанную прямоугольную область,
но выравнивание текста и другие опции задаются с помощью объекта класса QТextOption.
Например, с помощью этого класса можно отобразить непечатаемые символы (символ пробела,
табуляцию и др.).
Получить координаты и размеры прямоугольника, в который вписывается текст, позволяет
метод boundingRect() класса QPainter. Форматы метода:
boundingRect(<X>, <У>, <Ширина>, <Высота>, <Флаги>, <Текст>)
boundingRect(<Прямоугольник QRect>, <Флаги>, <Текст>)
boundingRect(<Прямоугольник QRectF>, <Флаги>, <Текст>)
boundingRect(<Прямоугольник QRectF>, <Текст>[, option=QТextOption()])
Первые два формата возвращают объект класса QRect, а последние два - объект класса QRectF.
При выводе текста линии букв могут отображаться в виде «лесенки». Чтобы сгладить контуры,
следует вызвать метод setRenderHint(<Режим сглаживания>) и передать ему элемент TextAntialiasing
перечисления RenderHint из класса QPainter:
painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing)
Если требуется отключить сглаживание, следует вызвать тот же метод, но передать ему вторым
параметром значение False:
painter.setRenderHint(QtGui.QPainter.RenderHint.TextAntialiasing, False)
"""

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QFont,
                           )
from PySide6.QtCore import (Qt,
                            QPoint,
                            QPointF,
                            QRect,
                            QRectF,
                            )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, класс шрифтов QFont

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt,
классов точек QPoint и QPointF, классов прямоугольников QRect и QRectF
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
        self.setWindowTitle('Вывод текста')  # установка заголовка главного окна
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
        painter.setPen(QPen(black))  # установка настроек пера в рисовальщик
        painter.setBrush(QBrush(white))  # установка настроек кисти в рисовальщик
        painter.drawRect(3, 3, 294, 294)  # рисование прямоугольника в области рисования
        painter.setRenderHint(QPainter.RenderHint.TextAntialiasing)  # установка настроек сглаживания
        painter.setPen(QPen(red, 1))
        painter.setFont(QFont("Tahoma", 12))  # установка настроек шрифта в рисовальщик
        painter.drawText(20, 30, "Строка 1")  # вывод текста в область рисования
        painter.drawText(QPoint(150, 30), "Строка 2")

        painter.drawRect(QRect(20, 40, 210, 50))
        print(painter.drawText(20, 40, 210, 50,
                               Qt.TextFlag.TextDontClip,
                               "Строка 3 текст будет выходить за границы"))

        painter.drawRect(QRect(20, 100, 260, 30))
        print(painter.drawText(20, 100, 260, 30,
                               Qt.AlignmentFlag.AlignCenter |
                               Qt.TextFlag.TextShowMnemonic,
                               "Строка &4"))

        painter.drawRect(QRect(20, 140, 260, 50))
        print(painter.drawText(QRect(20, 140, 260, 50),
                               Qt.AlignmentFlag.AlignRight |
                               Qt.TextFlag.TextSingleLine,
                               "Строка 5\nвсе специальные символы трактуются как пробелы и текст выводится в одну строку"))

        painter.drawRect(QRect(20, 190, 260, 50))
        print(painter.drawText(QRect(20, 190, 260, 50),
                               Qt.AlignmentFlag.AlignRight |
                               Qt.TextFlag.TextWordWrap,
                               "Строка 6 очень длинный текст на двух строках"))

        painter.drawRect(QRect(20, 240, 260, 50))
        print(painter.drawText(QRect(20, 240, 260, 50),
                               Qt.AlignmentFlag.AlignRight |
                               Qt.TextFlag.TextWrapAnywhere,
                               "Строка7оченьдлинныйтекстнадвухстрокахоченьдлинныйтекстнадвухстроках"))

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
