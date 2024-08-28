"""
Работа с графикой. Вспомогательные классы. Класс QPen: перо

Класс QPen описывает виртуальное перо, с помощью которого производится рисование
точек, линий и контуров фигур. Форматы конструктора класса:
QPen()
QPen(<Цвет QColor>)
QPen(<Стиль линий>)
QPen(<Цвет QColor или кисть QBrush>, <Ширина>[, s=PenStyle.SolidLine][,
     c=PenCapStyle.SquareCap][, j=PenJoinStyle.BevelJoin])
QPen(<Исходное перо QPen>)
Первый формат создает перо черного цвета с настройками по умолчанию. Второй формат
задает только цвет пера. Третий формат позволяет указать стиль линий - в виде элемента
перечисления PenStyle из модуля QtCore.Qt:
♦ NoPen - линия не выводится;
♦ SolidLine - сплошная линия;
♦ DashLine - штриховая линия;
♦ DotLine - точечная линия;
♦ DashDotLine - штрих и точка, штрих и точка и т.д.;
♦ DashDotDotLine - штрих и две точки, штрих и две точки и т.д.;
♦ CustomDashLine - пользовательский стиль.
Четвертый формат позволяет задать все характеристики пера за один раз. В параметре style
указывается стиль линий. Необязательный параметр cap задает стиль концов линий в виде
элемента перечисления PenCapStyle из модуля QtCore.Qt:
♦ FlatCap - квадратные концы линии. Длина линии не превышает указанных граничных
  точек;
♦ SquareCap - квадратные концы. Длина линии увеличивается с обоих концов на половину
  ширины линии;
♦ RoundCap - скругленные концы. Длина линии увеличивается с обоих концов на половину
  ширины линии.
Необязательный параметр join задает стиль соединения линий - в качестве значения указываются
следующие элементы перечисления PenJoinStyle из модуля QtCore.Qt:
♦ BevelJoin - линии соединяются под острым углом;
♦ MiterJoin - острые утлы срезаются на определенную величину;
♦ RoundJoin - скругленные углы;
♦ SvgMiterJoin - линии соединяются под острым утлом, как определено в спецификации
  SVG 1.2 Tiny.
Последний формат создает новый объект на основе указанного в параметре.
Класс QPen поддерживает следующие методы (здесь приведены только основные - полный
их список можно найти на странице https://doc.qt.io/qt-6/qpen.html):
♦ setColor(<Цвет QColor>) - задает цвет линий;
♦ setBrush(<Кисть QBrush>) - задает кисть;
♦ setWidth(<Ширина типа int>) и setWidthF(<Ширина типа float>) - задают ширину линий
  целым числом или числом с плавающей точкой соответственно;
♦ setStyle(<Стиль PenStyle>) - задает стиль линий;
♦ setCapStyle(<Стиль PenCapStyle>) - задает стиль концов линий;
♦ setJoinStyle(<Стиль PenJoinStyle>) - задает стиль соединения линий;
♦ setMiterLimit(<Величина срезания>) - задает величину срезания острых углов, если
  указан режим соединения MiterJoin.
"""

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen)
from PySide6.QtCore import Qt, QPoint

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow,

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt,
класса точки на плоскости QPoint
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
        self.setWindowTitle('Класс объекта пера QPen')  # установка заголовка главного окна
        self.resize(600, 600)  # установка исходного размера главного окна

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
        painter.drawRect(3, 3, 594, 594)  # рисование прямоугольника
        painter.drawLine(20, 20, 20, 280)  # рисование линии
        painter.drawLine(280, 20, 280, 280)  # рисование линии

        # --== Пример стиля окончания линии ==--
        painter.setPen(QPen(red, 15, c=Qt.PenCapStyle.FlatCap))  # создание пера с настройками и
        # установка пера в рисовальщик
        painter.drawLine(20, 50, 280, 50)  # рисование линии
        painter.setPen(QPen(red, 15, c=Qt.PenCapStyle.SquareCap))  # создание пера с настройками и
        # установка пера в рисовальщик
        painter.drawLine(20, 100, 280, 100)  # рисование линии
        painter.setPen(QPen(red, 15, c=Qt.PenCapStyle.RoundCap))  # создание пера с настройками и
        # установка пера в рисовальщик
        painter.drawLine(20, 150, 280, 150)  # рисование линии

        # --== Пример стиля соединения линий ==--
        painter.setPen(QPen(red, 15, j=Qt.PenJoinStyle.MiterJoin))
        painter.drawPolygon((QPoint(320, 20), QPoint(420, 20), QPoint(320, 120)))
        painter.setPen(QPen(red, 15, j=Qt.PenJoinStyle.BevelJoin))
        painter.drawPolygon((QPoint(580, 20), QPoint(480, 20), QPoint(580, 120)))
        painter.setPen(QPen(red, 15, j=Qt.PenJoinStyle.RoundJoin))
        painter.drawPolygon((QPoint(580, 280), QPoint(480, 280), QPoint(580, 180)))
        painter.setPen(QPen(red, 15, j=Qt.PenJoinStyle.SvgMiterJoin))
        painter.drawPolygon((QPoint(320, 280), QPoint(320, 180), QPoint(420, 280)))

        # --== Пример стиля линий ==--
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.SolidLine))
        painter.drawLine(20, 350, 280, 350)
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DashLine))
        painter.drawLine(20, 400, 280, 400)
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DotLine))
        painter.drawLine(20, 450, 280, 450)
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DashDotLine))
        painter.drawLine(20, 500, 280, 500)
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DashDotDotLine))
        painter.drawLine(20, 550, 280, 550)


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
