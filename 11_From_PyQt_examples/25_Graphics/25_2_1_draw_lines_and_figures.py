"""
Работа с графикой. Рисование линий и фигур

После захвата контекста рисования следует установить перо и кисть. С помощью пера производится
рисование точек, линий и контуров фигур, а с помощью кисти - заполнение
фона фигур. Установить перо позволяет метод setPen() класса QPainter. Форматы метода:
setPen(<Перо QPen>)
setPen(<Цвет QColor>)
setPen(<Стиль пера PenStyle>)
Для установки кисти предназначен метод setBrush(). Форматы метода:
setBrush(<Кисть QBrush>)
setBrush(<Стиль кисти BrushStyle>)
Устанавливать перо или кисть необходимо перед каждой операцией рисования, требующей
изменения цвета или стиля. Если перо или кисть не установлены, будут использоваться
объекты с настройками по умолчанию. После установки пера и кисти можно приступать
к рисованию точек, линий, фигур, текста и др.
Для рисования точек, линий и фигур класс QPainter предоставляет следующие наиболее
часто употребляемые методы (полный их список приведен на странице
https://doc.qt.io/qt-6/qpainter.html):
♦ drawPoint() - рисует точку. Форматы метода:
  drawPoint(<X>, <У>)
  drawPoint(<Координаты QPoint или QPointF>)
♦ drawPoints() - рисует несколько точек. Форматы метода:
  drawPoints(<Координаты QPoint 1>[, . . . , <Координаты QPoint N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawPoints(<Координаты QPointF 1>[, . . . , <Координаты QPointF N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawPoints(<Многоугольник QPolygon или QPolygonF>)
♦ drawLine() - рисует линию. Форматы метода:
  drawLine(<Линия QLine или QLineF>)
  drawLine(<Начальная точка QPoint>, <Конечная точка QPoint>)
  drawLine(<Начальная точка QPointF>, <Конечная точка QPointF>)
  drawLine(<X1>, <Y1>, <Х2>, <У2>)
♦ drawLines() - рисует несколько отдельных линий. Форматы метода:
  drawLines(<Пиния QLine 1>[, . . . , <Пиния QLine N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawLines(<Линия QLineF 1>[, . . . , <Пиния QLineF N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawLines(<Список с линиями QLineF>)
  drawLines(<Точка QPoint 1>[, . . . , <Точка QPoint N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawLines(<Точка QPointF 1>[, . . . , <Точка QPointF N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
♦ drawPolyline() - рисует несколько линий, которые соединяют указанные точки. Первая
  и последняя точки не соединяются. Форматы метода:
  drawPolyline(<Точка QPoint 1>[, . . . , <Точка QPoint N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawPolyline(<Точка QPointF 1>[, . . . , <Точка QPointF N>]) НЕ РАБОТАЕТ, ДОЛЖЕН БЫТЬ СПИСОК ИЛИ КОРТЕЖ
  drawPolyline(<Многоугольник QPolygon или QPolygonF>)
♦ drawRect() - рисует прямоугольник с границей и заливкой. Чтобы убрать границу, следует
  использовать перо со стилем NoPen, а чтобы убрать заливку - кисть со стилем
  NoBrush. Форматы метода:
  drawRect(<X>, <У>, <Ширина>, <Высота>)
  drawRect(<Прямоугольник QRect или QRectF>)
♦ fillRect () - рисует прямоугольник с заливкой без границы. Форматы метода:
  fillRect(<X>, <У>, <Ширина>, <Высота>, <Заливка>)
  fillRect(<Прямоугольник QRect или QRectF>, <Заливка>)
  <Заливка> может быть задана объектами классов <QColor>, <QBrush>, в виде стиля кисти
  или элемента перечисления GlobalColor;
♦ drawRoundedRect() - рисует прямоугольник с границей, заливкой и скругленными
  краями. Форматы метода:
  drawRoundedRect(<X>, <У>, <Ширина>, <Высота>,
                  <Скругление по горизонтали>, <Скругление по вертикали> [,
                  mode=SizeMode.AbsoluteSize])
  drawRoundedRect(<Прямоугольник QRect или QRectF>,
                  <Скругление по горизонтали>, <Скругление по вертикали>[,
                  mode=SizeMode.AbsoluteSize])
  Параметры <Скругление по горизонтали> и <Скругление по вертикали> задают радиусы
  скругления углов по горизонтали и вертикали. Необязательный параметр mode указывает,
  в каких единицах измеряются радиусы скругления углов, и задается одним из следующих
  элементов перечисления SizeMode из модуля QtCore.Qt:
  • AbsoluteSize - радиусы указываются в пикселах;
  • RelativeSize - радиусы указываются в процентах от соответствующего размера рисуемого
    прямоугольника;
♦ drawPolygon() - рисует многоугольник с границей и заливкой. Форматы метода:
  drawPolygon(<Вершина QPoint 1>[, ..., <Вершина QPoint N>])
  drawPolygon(<Вершина QPointF 1>[, ..., <Вершина QPointF N>])
  drawPolygon(<Многоугольник QPolygon или QPolygonF>[,
              fillRule=FillRule.OddEvenFill])
  Необязательный параметр fillRule задает алгоритм определения, находится ли какая-либо
  точка внутри нарисованного многоугольника или вне его. В качестве его значения
  указывается атрибут OddEvenFill или WindingFill перечисления FillRule из модуля
  QtCore.Qt;
♦ drawEllipse() - рисует эллипс с границей и заливкой. Форматы метода:
  drawEllipse(<X>, <У>, <Ширина>, <Высота>)
  drawEllipse(<Прямоугольник QRect или QRectF>)
  drawEllipse(<Точка QPoint или QPointF>, <int rX>, <int rY>)
  В первых двух форматах указываются координаты и размеры прямоугольника, в который
  необходимо вписать эллипс. В последнем формате первый параметр задает координаты
  центра, параметр rx - радиус по оси х, а параметр rY - радиус по оси У;
♦ drawArc() - рисует дугу. Форматы метода:
  drawArc(<X>, <У>, <ШИрина>, <Высота>, <Начальный угол>, <Угол>)
  drawArc(<Прямоугольник QRect или QRectF>, <Начальный угол>, <Угол>)
  Значения углов задаются в значениях 1/16°. Полный круг эквивалентен значению
  5760 = 16 х 360. Нулевой угол находится в позиции «трех часов». Положительные значения
  углов отсчитываются против часовой стрелки, а отрицательные - по часовой
  стрелке;
♦ drawChord() - рисует замкнутую дугу. Аналогичен методу drawArc(), но соединяет
  крайние точки дуги прямой линией. Форматы метода:
  drawChord(<X>, <У>, <ШИрина>, <Высота>, <Начальный угол>, <Угол>)
  drawChord(<Прямоугольник QRect или QRectF>, <Начальный угол>, <Угол>)
♦ drawPie() - рисует замкнутый сектор. Аналогичен методу drawArc(), но соединяет
  крайние точки дуги с центром окружности. Форматы метода:
  drawPie(<X>, <У>, <ШИрина>, <Высота>, <Начальный угол>, <Угол>)
  drawPie(<Прямоугольник QRect или QRectF>, <Начальный угол>, <Угол>)
При выводе некоторых фигур (например, эллипса) контур может отображаться в виде
«лесенки». Чтобы сгладить контуры фигур, следует вызвать метод setRenderHint(<Режим
сглаживания>) и передать ему в качестве единственного параметра элемент Antialiasing
перечисления RenderHint из класса QPainter:
painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
Если требуется отключить сглаживание, следует вызвать тот же метод, но передать ему
вторым параметром значение False:
painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, False)
"""

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QPolygon,
                           QPolygonF,
                           )
from PySide6.QtCore import (Qt,
                            QLine,
                            QLineF,
                            QPoint,
                            QPointF,
                            QRect,
                            QRectF,
                            )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, классы многоугольников QPolygon и QPolygonF

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt, классов линий QLine и QLineF,
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
        self.setWindowTitle('Рисование линий и фигур')  # установка заголовка главного окна
        self.resize(600, 700)  # установка исходного размера главного окна

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
        blue = Qt.GlobalColor.blue
        cyan = Qt.GlobalColor.darkCyan
        magenta = Qt.GlobalColor.magenta
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # установка режима сглаживания лесенок
        painter.setPen(QPen(black))  # создание пера с настройками и установка пера в рисовальщик
        painter.setBrush(QBrush(white))  # создание и применение кисти для заливки фигур к рисовальщику
        painter.drawRect(3, 3, 594, 694)  # рисование прямоугольника

        # --== Рисование точки drawPoint() ==--
        painter.setPen(QPen(cyan, 10))  # установка настроек пера в рисовальщик
        painter.drawPoint(QPoint(50, 75))
        painter.drawPoint(QPointF(75.0, 75.0))
        painter.drawPoint(100, 75)
        for n in range(1, 5):
            painter.drawPoint(QPoint(25 + n * 25, 125))

        # --== Рисование нескольких точек drawPoints() ==--
        painter.setPen(QPen(cyan, 10))  # установка настроек пера в рисовальщик
        painter.drawPoints([QPoint(50, 165), QPoint(75, 185), QPoint(100, 175)])
        painter.drawPoints([QPointF(175.0, 165.0), QPointF(200.0, 185.0), QPointF(225.0, 175.0)])
        polygon = QPolygon([QPoint(50, 240), QPoint(100, 240), QPoint(75, 290)])
        painter.drawPoints(polygon)
        polygon_f = QPolygonF([QPointF(150.0, 240.0), QPointF(200.0, 240.0), QPointF(175.0, 290.0)])
        painter.drawPoints(polygon_f)

        # --== Рисование линии drawLine() ==--
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.SolidLine))  # установка настроек пера в рисовальщик
        painter.drawLine(QLine(20, 50, 280, 50))  # рисование линии
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DashLine))  # установка настроек пера в рисовальщик
        painter.drawLine(QLineF(20.0, 100.0, 280.0, 100.0))  # рисование линии
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DotLine))  # установка настроек пера в рисовальщик
        painter.drawLine(QPoint(20, 150), QPoint(280, 150))  # рисование линии
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DashDotLine))  # установка настроек пера в рисовальщик
        painter.drawLine(QPointF(20.0, 200.0), QPointF(280.0, 200.0))  # рисование линии
        painter.setPen(QPen(red, 4, s=Qt.PenStyle.DashDotDotLine))  # установка настроек пера в рисовальщик
        painter.drawLine(20, 250, 280, 250)  # рисование линии

        # --== Рисование нескольких линий drawLines() ==--
        painter.setPen(QPen(blue, 2, s=Qt.PenStyle.SolidLine))  # установка настроек пера в рисовальщик
        painter.drawLines((QLine(20, 350, 280, 350), QLine(20, 360, 280, 360)))
        painter.drawLines([QLineF(20.0, 370.0, 280.0, 370.0), QLineF(20.0, 380.0, 280, 380.0)])
        painter.drawLines([QPoint(20, 430), QPoint(280, 430), QPoint(20, 440), QPoint(280, 440)])
        painter.drawLines([QPointF(20.0, 450.0), QPointF(280.0, 450.0), QPointF(20.0, 460.0), QPointF(280.0, 460.0)])

        # --== Рисование полилинии drawPolyline() ==--
        painter.setPen(QPen(red, 2, s=Qt.PenStyle.SolidLine))
        painter.drawPolyline([QPoint(20, 500), QPoint(70, 525), QPoint(20, 550), QPoint(35, 525)])
        painter.drawPolyline(QPolygon([QPoint(120, 500), QPoint(170, 525), QPoint(120, 550), QPoint(135, 525)]))
        painter.drawPolyline(
            [QPointF(220.0, 500.0), QPointF(270.0, 525.0), QPointF(220.0, 550.0), QPointF(235.0, 525.0)])

        # --== Рисование прямоугольника drawRect() ==--
        painter.setPen(QPen(magenta, 2, s=Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.black, bs=Qt.BrushStyle.Dense5Pattern))
        painter.drawRect(350, 50, 80, 80)

        painter.setBrush(QBrush(Qt.GlobalColor.black, bs=Qt.BrushStyle.CrossPattern))
        painter.drawRect(QRect(450, 50, 80, 80))

        painter.setBrush(QBrush(Qt.GlobalColor.black, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawRect(QRectF(350.0, 150.0, 80.0, 80.0))

        painter.setPen(QPen(magenta, 2, s=Qt.PenStyle.NoPen))
        painter.setBrush(QBrush(Qt.GlobalColor.green, bs=Qt.BrushStyle.SolidPattern))
        painter.drawRect(QRect(450, 150, 80, 80))

        # --== Рисование прямоугольника с заливкой без границ fillRect() ==--
        painter.setPen(QPen(magenta, 2, s=Qt.PenStyle.SolidLine))
        painter.fillRect(350, 250, 80, 80, QBrush(Qt.GlobalColor.green, bs=Qt.BrushStyle.Dense5Pattern))
        painter.fillRect(QRect(450, 250, 80, 80), Qt.GlobalColor.green)

        # --== Рисование прямоугольника с закруглением на углах drawRoundedRect() ==--
        painter.setBrush(QBrush(Qt.GlobalColor.black, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawRoundedRect(350, 350, 80, 80, 20, 20, mode=Qt.SizeMode.AbsoluteSize)
        painter.drawRoundedRect(QRect(450, 350, 80, 80), 20, 20, mode=Qt.SizeMode.RelativeSize)

        # --== Рисование многоугольников drawPolygon() ==--
        painter.setPen(QPen(blue, 2, s=Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.magenta, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawPolygon(QPolygon([QPoint(20, 600), QPoint(120, 600), QPoint(120, 675), QPoint(120, 675),
                                      QPoint(20, 675), QPoint(100, 615), QPoint(100, 660)]),
                            fillRule=Qt.FillRule.OddEvenFill)
        painter.drawPolygon(QPolygon([QPoint(170, 600), QPoint(270, 600), QPoint(270, 675), QPoint(270, 675),
                                      QPoint(170, 675), QPoint(250, 615), QPoint(250, 660)]),
                            fillRule=Qt.FillRule.WindingFill)

        # --== Рисование эллипса drawEllipse() ==--
        painter.setPen(QPen(blue, 2, s=Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.magenta, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawEllipse(350, 450, 80, 40)
        painter.drawEllipse(QRect(450, 450, 80, 40))
        painter.drawEllipse(QPoint(390, 525), 40, 20)

        # --== Рисование дуги drawArc() ==--
        painter.setPen(QPen(red, 2, s=Qt.PenStyle.SolidLine))
        painter.drawArc(350, 555, 80, 40, 2880, -2880)
        painter.drawArc(QRect(450, 555, 80, 40, ), 2880, -2880)

        # --== Рисование сегмента drawChord() ==--
        painter.setPen(QPen(red, 2, s=Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.blue, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawChord(350, 600, 80, 80, 2880, -1440)
        painter.drawChord(QRect(400, 600, 80, 80, ), 2880, -1440)

        # --== Рисование сектора drawPie() ==--
        painter.setPen(QPen(red, 2, s=Qt.PenStyle.SolidLine))
        painter.setBrush(QBrush(Qt.GlobalColor.blue, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawPie(440, 600, 80, 80, 2160, -1440)
        painter.drawPie(QRect(510, 600, 80, 80, ), 2160, -1440)


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
