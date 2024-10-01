"""
Работа с графикой. Преобразование системы координат

Существуют две системы координат: физическая (viewport, система координат устройства)
и логическая (window). При рисовании координаты из логической системы координат
преобразуются в систему координат устройства. По умолчанию эти две системы координат
совпадают.
В некоторых случаях возникает необходимость изменить координаты. Выполнить изменение
физической системы координат позволяет метод setViewport(<Х>, <Y>, <Ширина>, <Высота>)
или setViewport(<Объект класса QRect>), а получить текущие значения - метод
viewport(). Выполнить изменение логической системы координат позволяет метод
setWindow(<Х>, <Y>, <111ирина>, <Высота>) или setWindow(<Объект класса QRect>),
а получить текущие значения - метод window() класса QPainter.
Произвести дополнительную трансформацию системы координат позволяют следующие
методы того же класса QPainter:
♦ translate() - перемещает начало координат в указанную точку. По умолчанию начало
координат находится в левом верхнем углу. Положительная ось X направлена вправо, а
положительная ось Y - вниз. Форматы метода:
translate(<X>, <Y>)
translate(<Точка QPoint или QPointF>)
♦ rotate(<Угол>) - поворачивает систему координат на заданный угол (указывается
в виде вещественного числа в градусах). Положительное значение вызывает поворот по
часовой стрелке, а отрицательное значение - против часовой стрелки;
♦ scale(<По оси Х>, <По оси Y>) - масштабирует систему координат. В качестве значений
указываются вещественные числа. Если значение меньше единицы, то выполняется
уменьшение, а если больше единицы - то увеличение;
♦ shear(<По горизонтали>, <По вертикали>) - сдвигает систему координат. В качестве
значений указываются вещественные числа.
Все указанные трансформации влияют на последующие операции рисования и не изменяют
ранее нарисованные фигуры. Чтобы после трансформации восстановить систему координат,
следует предварительно сохранить состояние в стеке с помощью метода save(), а после
окончания рисования вызвать метод restore():
    painter.save() # Сохраняем состояние
    # Трансформируем и рисуем
    painter.restore() # Восстанавливаем состояние
Несколько трансформаций можно произвести последовательно друг за другом. При этом
надо учитывать, что порядок следования трансформаций имеет значение.
Если одна и та же последовательность трансформаций выполняется несколько раз, то ее
можно сохранить в объекте класса QTransform, а затем установить с помощью метода
setTransform(<Трансформация>):
transform = QtGui.QTransform()
transform.translate(105, 105)
transform.rotate(45.0)
painter.setTransform(transform)
painter.fillRect(-25, -25, 50, 50, QtCore.Qt.green)
"""

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QTransform,
                           )
from PySide6.QtCore import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, класс объекта трансформаций QTransform

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt
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
        self.setWindowTitle('Преобразование системы координат')  # установка заголовка главного окна
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
        painter.setPen(QPen(black, 5))  # настройка пера рисовальщика
        painter.setBrush(QBrush(white))  # настройка кисти рисовальщика
        painter.drawRect(3, 3, 594, 594)  # рисование прямоугольника

        painter.fillRect(10, 10, 50, 50, Qt.GlobalColor.red)  # рисование прямоугольника
        painter.save()  # сохранение текущей системы координат
        painter.translate(105, 105)  # перемещение начала координат
        painter.rotate(45.0)  # поворот системы координат
        painter.fillRect(-25, -25, 50, 50, Qt.GlobalColor.green)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.save()  # сохранение текущей системы координат
        painter.translate(105, 105)  # перемещение начала координат
        painter.rotate(20.0)  # поворот системы координат
        painter.fillRect(-25, -25, 50, 50, Qt.GlobalColor.black)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.fillRect(150, 150, 50, 50, Qt.GlobalColor.blue)  # рисование прямоугольника

        painter.translate(300, 0)  # смещение начала координат для удобства примера
        painter.fillRect(10, 10, 50, 50, Qt.GlobalColor.red)  # рисование прямоугольника
        painter.save()  # сохранение текущей системы координат
        painter.translate(300, 0)  # перемещение начала координат
        painter.scale(0.5, 0.5)  # масштабирование системы координат по осям
        painter.fillRect(80, 80, 50, 50, Qt.GlobalColor.green)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.save()  # сохранение текущей системы координат
        painter.translate(300, 0)  # перемещение начала координат
        painter.scale(1.5, 1.5)  # масштабирование системы координат по осям
        painter.fillRect(80, 80, 50, 50, Qt.GlobalColor.black)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.fillRect(50, 150, 50, 50, Qt.GlobalColor.blue)  # рисование прямоугольника
        painter.translate(-300, 0)  # смещение начала координат в исходную точку

        painter.translate(0, 300)  # смещение начала координат для удобства примера
        painter.fillRect(10, 10, 50, 50, Qt.GlobalColor.red)  # рисование прямоугольника
        painter.save()  # сохранение текущей системы координат
        painter.fillRect(80, 80, 50, 50, Qt.GlobalColor.magenta)  # рисование прямоугольника
        painter.shear(0.2, 0.2)  # настройки взаимного смещения координат
        painter.fillRect(80, 80, 50, 50, Qt.GlobalColor.green)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.fillRect(150, 150, 50, 50, Qt.GlobalColor.blue)  # рисование прямоугольника
        painter.translate(0, -300)  # смещение начала координат в исходную точку

        painter.fillRect(310, 310, 50, 50, Qt.GlobalColor.red)  # рисование прямоугольника
        trans_1 = QTransform()  # создание объекта трансформаций
        trans_1.translate(405, 405)  # сохранение в объекте трансформаций перемещения начала координат
        trans_1.rotate(45.0)  # сохранение в объекте трансформаций поворота системы координат
        trans_2 = QTransform()  # создание объекта трансформаций
        trans_2.translate(505, 505)  # сохранение в объекте трансформаций перемещения начала координат
        trans_2.rotate(25.0)  # сохранение в объекте трансформаций поворота системы координат
        trans_2.scale(0.5, 0.5)  # сохранение масштабирования в объекте трансформаций
        painter.save()  # сохранение текущей системы координат
        painter.setTransform(trans_1)  # установка объекта трансформаций в рисовальщик
        painter.fillRect(10, 10, 50, 50, Qt.GlobalColor.green)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.save()  # сохранение текущей системы координат
        painter.setTransform(trans_2)  # установка объекта трансформаций в рисовальщик
        painter.fillRect(10, 10, 50, 50, Qt.GlobalColor.magenta)  # рисование прямоугольника
        painter.restore()  # восстановление исходной системы координат
        painter.fillRect(370, 370, 50, 50, Qt.GlobalColor.blue)  # рисование прямоугольника


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