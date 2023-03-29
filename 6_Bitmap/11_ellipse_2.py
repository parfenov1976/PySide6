"""
Пример создания поверхности для отображения растровой графической информации (холста для рисования).
Пример рисования эллипсов.
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QBrush

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtCore и класса Qt - содержит различные идентификаторы, используемые
в библиотеке Qt, класса точки QPoint. 
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета ярлыка QLabel.
Импорт из модуля PySide6.QtGui класса поверхности для графических изображений QPixmap,
класса виджета для рисования QPainter, класс для установки размера пера (толщины линии)
и цвета для рисования QPen, класс объекта цветов QColor, класс кисти для закрашивания QBrush.  
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласса главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.label = QLabel()  # создание экземпляра класса виджета ярлыка
        self.canvas = QPixmap(400, 300)  # создание поверхности для графической информации - холста для рисования
        self.canvas.fill(Qt.GlobalColor.white)  # заполнение холста белым цветом
        self.label.setPixmap(self.canvas)  # привязка холста к ярлыку для отображения содержимого холста
        self.setCentralWidget(self.label)  # размещение ярлыка в главном окне приложения
        self.draw_something()  # вызов метода рисования

    def draw_something(self) -> None:
        """
        Метод рисования
        :return: None
        """
        painter = QPainter(self.canvas)  # создание экземпляра класса виджета для рисования
        pen = QPen()  # создание экземпляра класса пера для рисования
        pen.setWidth(3)  # установка толщины пера
        pen.setColor(QColor(204, 0, 0))  # установка цвета пера rgb
        painter.setPen(pen)  # применение настроек пера к рисовальщику
        brush = QBrush()  # создание экземпляра класса кисти для закрашивания
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)  # установка стиля (плотности) закрашивания
        brush.setColor(QColor(250, 220, 210))  # установка цвета кисти rgb
        painter.setBrush(brush)  # применение настроек кисти к рисовальщику
        painter.drawEllipse(QPoint(100, 100), 10, 10)  # рисование эллипса, точка - координаты центра
        # вторые числа - радиусы
        painter.drawEllipse(QPoint(100, 100), 15, 20)
        painter.drawEllipse(QPoint(100, 100), 20, 30)
        painter.drawEllipse(QPoint(100, 100), 25, 40)
        painter.drawEllipse(QPoint(100, 100), 30, 50)
        painter.drawEllipse(QPoint(100, 100), 35, 60)
        painter.end()  # подача команды на завершение рисования, закрытие рисовальщика и сохранения изменений
        self.label.setPixmap(self.canvas)  # после завершения рисования холст должен быть передан на отображение


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # вызов метода, устанавливающего видимость окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла главного окна приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуски кода верхнего уровня при
    # импортировании данного файла как модуля
    main()
