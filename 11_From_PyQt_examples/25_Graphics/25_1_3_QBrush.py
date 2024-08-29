"""
Работа с графикой. Вспомогательные классы. Класс QBrush: кисть

Класс QBrush описывает виртуальную кисть, с помощью которой производится заливка
фигур. Форматы конструктора класса:
QBrush()
QBrush(<Цвет>[, style=BrushStyle.SolidPattern])
QBrush(<Стиль кисти>)
QBrush(<Градиент>)
QBrush(<Цвет>, <Изображение QPixmap>)
QBrush(<Изображение QPixmap или QImage>)
QBrush(<Объект класса QBrush>)
Первый формат создает кисть с черной сплошной. заливкой и стилем NoBrush (т. е. заливка
фактически не рисуется).
Во втором и пятом форматах цвет может быть задан в виде объекта класса QColor или элемента
перечисления GlobalColor из модуля QtCore.Qt (например: black).
Во втором и третьем форматах стиль кисти в параметрах <Стиль кисти> и style указывается в
виде элемента перечисления BrushStyle из модуля QtCore.Qt: NoBrush, SolidPattern,
Dense1Pattern, Dense2Pattern, DenseЗPattern, Dense4Pattern, Dense5Pattern, Dense6Pattern,
Dense7Pattern, CrossPattern и др. Так, можно сделать цвет сплошным (SolidPattern) или
имеющим текстуру (например, элемент CrossPattern задает текстуру в виде сетки).
Четвертый формат создает кисть с градиентной заливкой. В параметре <Градиент> указывается
объект одного из классов, производных от QGradient: QLinearGradient (линейный градиент),
QConicalGradient (конический градиент) или QRadialGradient (радиальный градиент).
За подробной информацией по этим классам обращайтесь к документации.
Пятый формат создает кисть с заданным сплошным цветом и текстурой, создаваемой указанным
изображением. Шестой формат создает кисть с черным цветом и текстурой, создаваемой указанным
изображением.
Последний формат создает копию указанной кисти.
Класс QBrush поддерживает следующие полезные для нас методы (полный их список приведен на
странице https://doc.qt.io/qt-6/qbrush.html):
♦ setColor(<Цвет>) - задает цвет кисти (объект класса QColor или элемент перечисления
  GlobalColor из модуля QtCore.Qt);
♦ setStyle(<Стиль BrushStyle>) - задает стиль кисти;
♦ setTexture(<Изображение QPixmap>) - устанавливает растровое изображение в качестве текстуры;
♦ setTextureImage (<Изображение QImage>) - устанавливает изображение в качестве текстуры.
"""
from PIL.ImageOps import grayscale
from PySide6.QtWidgets import (QMainWindow,
                               QStyle,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QLinearGradient,
                           QConicalGradient,
                           QRadialGradient,
                           )
from PySide6.QtCore import (Qt,
                            QSize,
                            )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, класс настроек стилей QStyle

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, класс линейного градиента QLinearGradient, класс конического градиента QConicalGradient,
класса радиального градиента QRadialGradient

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt,
класса объекта размеров QSize
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
        self.setWindowTitle('Класс объекта кисти QBrush')  # установка заголовка главного окна
        self.resize(300, 410)  # установка исходного размера главного окна

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
        painter.drawRect(3, 3, 294, 404)

        #--== Пример использования стилей кистей ==--
        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.SolidPattern))  # добавление к рисовальщику кисти
        # с настройками цвета и стиля
        painter.drawRect(10, 10, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense1Pattern))
        painter.drawRect(10, 50, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense2Pattern))
        painter.drawRect(10, 90, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense3Pattern))
        painter.drawRect(10, 130, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense4Pattern))
        painter.drawRect(10, 170, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense5Pattern))
        painter.drawRect(10, 210, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense6Pattern))
        painter.drawRect(10, 250, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.Dense7Pattern))
        painter.drawRect(10, 290, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.CrossPattern))
        painter.drawRect(10, 330, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.HorPattern))
        painter.drawRect(10, 370, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.VerPattern))
        painter.drawRect(190, 10, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.BDiagPattern))
        painter.drawRect(190, 50, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.FDiagPattern))
        painter.drawRect(190, 90, 100, 30)

        painter.setBrush(QBrush(red, bs=Qt.BrushStyle.DiagCrossPattern))
        painter.drawRect(190, 130, 100, 30)

        # --== Пример использования градиентов ==--
        gradient_1 = QLinearGradient(190, 185, 290, 185)
        gradient_1.setColorAt(0, Qt.GlobalColor.black)
        gradient_1.setColorAt(0.5, Qt.GlobalColor.white)
        gradient_1.setColorAt(1, Qt.GlobalColor.black)
        painter.setBrush(QBrush(gradient_1))
        painter.drawRect(190, 170, 100, 30)

        gradient_2 = QConicalGradient(240, 225, 0)
        gradient_2.setColorAt(0, Qt.GlobalColor.black)
        gradient_2.setColorAt(0.5, Qt.GlobalColor.white)
        gradient_2.setColorAt(1, Qt.GlobalColor.red)
        painter.setBrush(QBrush(gradient_2))
        painter.drawRect(190, 210, 100, 30)

        gradient_3 = QRadialGradient(240, 265, 70)
        gradient_3.setColorAt(0, Qt.GlobalColor.white)
        gradient_3.setColorAt(1, Qt.GlobalColor.red)
        painter.setBrush(QBrush(gradient_3))
        painter.drawRect(190, 250, 100, 30)

        # --== Пример использования текстур ==--
        ico = self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxCritical)
        painter.setBrush(QBrush(ico.pixmap(QSize(32, 32))))
        painter.drawRect(190, 290, 100, 30)
        brush = QBrush(black)
        brush.setTexture(ico.pixmap(QSize(16, 16)).mask())
        painter.setBrush(brush)
        painter.drawRect(190, 330, 100, 30)


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
