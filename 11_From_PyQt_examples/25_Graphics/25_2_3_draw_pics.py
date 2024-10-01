"""
Работа с графикой. Вывод изображений.

Для вывода растровых изображений предназначены методы drawPixmap() и drawImage()
класса QPainter.

Метод drawPixmap() обеспечивает вывод изображений, хранимых в объекте
класса QPixmap. Форматы метода:
drawPixmap(<X>, <У>, <Изображение QPixmap>)
drawPixmap(<Координаты QPoint или QPointF>, <Изображение QPixmap>)
drawPixmap(<X>, <У>, <Ширина>, <Высота>, <Изображение QPixmap>)
drawPixmap(<Прямоугольник QRect>, <Изображение QPixmap>)
drawPixmap(<X1>, <Y1>, <Изображение QPixmap>, <Х2>, <У2>, <Ширина 2>, <Высота 2>).
drawPixmap(<Координаты QPoint>, <Изображение QPixmap>, <Прямоугольник QRect>)
drawPixmap(<Координаты QPointF>, <Изображение QPixmap>, <Прямоугольник QRectF>)
drawPixmap(<X1>, <Y1>, <Ширина 1>, <Высота 1>, <Изображение QPixmap>, <Х2>, <У2>, <Ширина 2>, <Высота 2>)
drawPixmap(<Прямоугольник QRect>, <Изображение QPixmap>, <Прямоугольник QRect>)
drawPixmap(<Прямоугольник QRectF>, <Изображение QPixmap>, <Прямоугольник QRectF>)
Первые два формата задают координаты, в которые будет установлен левый верхний угол
выводимого изображения:
pixmap = QtGui.QPixmap("foto.jpg")
painter.drawPixmap(З, З, pixmap)
Третий и четвертый форматы позволяют ограничить вывод изображения указанной прямоугольной
областью. Если размеры области не совпадают с размерами изображения, то производится
масштабирование изображения. При несоответствии пропорций изображение
может быть искажено.
Пятый, шестой и седьмой форматы задают координаты, в которые будет установлен левый
верхний угол фрагмента изображения. Координаты и размеры вставляемого фрагмента изображения
указываются после объекта класса QPixmap в виде отдельных составляющих или
объектов классов QRect или QRectF.
Последние три формата ограничивают вывод фрагмента изображения указанной прямоугольной
областью. Координаты и размеры вставляемого фрагмента изображения указываются
после изображения в виде отдельных составляющих или объектов классов QRect или
QRectF. Если размеры области не совпадают с размерами фрагмента изображения, производится
масштабирование изображения. При несоответствии пропорций изображение может
быть искажено.

Метод drawImage() предназначен для вывода изображений, хранимых в объектах класса
QImage. Форматы метода:
drawImage(<Координаты QPoint или QPointF>, <Изображение QImage>)
drawImage(<Прямоугольник QRect или QRectF>, <Изображение QImage>)
drawImage(<X1>, <Y1>, <Изображение QImage>[, sx=O] [, sy=O] [,
          sw=-1) [, sh=-1] [, flags=ImageConversionFlag.AutoColor])
drawImage(<Координаты QPoint>, <Изображение QImage>,
          <Прямоугольник QRect>[, flags=ImageConversionFlag.AutoColor])
drawImage(<Координаты QPointF>, <Изображение QImage>,
          <Прямоугольник QRectF>[, flags=ImageConversionFlag.AutoColor])
drawImage(<Прямоугольник QRect>, <Изображение QImage>,
          <Прямоугольник QRect>[, flags=ImageConversionFlag.AutoColor])
drawImage(<Прямоугольник QRectF>, <Изображение QImage>,
          <Прямоугольник QRectF>[, flags=ImageConversionFlag.AutoColor])
Первый, а также третий формат со значениями по умолчанию задают координаты, по которым
будет находиться левый верхний угол выводимого изображения:
img = QtGui.QImage("foto.jpg")
painter.drawimage(З, 3, img)
Второй формат ограничивает вывод изображения указанной прямоугольной областью. Если
размеры области не совпадают с размерами изображения, то производится масштабирование
изображения. При несоответствии пропорций изображение может быть искажено.
Третий, четвертый и пятый форматы задают координаты, в которые будет установлен левый
верхний угол фрагмента изображения. Координаты и размеры вставляемого фрагмента
изображения указываются после изображения в виде отдельных составляющих или объектов
классов QRect или QRectF.
Последние два формата ограничивают вывод фрагмента изображения указанной прямоугольной
областью. Координаты и размеры вставляемого фрагмента изображения указываются
после изображения в виде объектов классов QRect или QRectF. Если размеры области
не совпадают с размерами фрагмента изображения, производится масштабирование изображения.
При несоответствии пропорций изображение может быть искажено.
Необязательный параметр flags задает цветовые преобразования, которые будут выполнены
при выводе изображения (фактически - при неявном преобразовании объекта класса
QImage в объект класса QPixmap, которое обязательно выполняется перед выводом). Они указываются
в виде элементов перечисления ImageConversionFlag из модуля QtCore. Qt, приведенных
на странице https://doc.qt.io/qt-6/qt.html#lmageConversionFlag-enum . В большинстве
случаев имеет смысл использовать заданный по умолчанию элемент Aut?Color этого
перечисления.
"""
import os
from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QImage,
                           QPixmap,
                           )
from PySide6.QtCore import (Qt,
                            QPoint,
                            QPointF,
                            QRect,
                            QRectF,
                            )

"""
Импорт модуля для работы с переменными среды os

Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, классы изображений QImage и QPixmap

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
        self.setWindowTitle('Вывод изображений')  # установка заголовка главного окна
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
        painter.setPen(QPen(black))  # настройка пера рисовальщика
        painter.setBrush(QBrush(white))  # настройка кисти рисовальщика
        painter.drawRect(3, 3, 594, 594)  # рисование прямоугольника

        img = QImage(os.path.join('data', 'photo.jpg'))  # создание объекта изображения из файла
        painter.drawImage(3, 3, img)
        painter.drawImage(QRect(3, 200, 150, 150), img)
        painter.drawImage(QPoint(3, 400), img, QRect(0, 0, 150, 150))
        painter.drawImage(QRect(175, 400, 100, 100), img, QRect(0, 0, 150, 150))

        pix = QPixmap(os.path.join('data', 'photo.jpg'))  # создание объекта изображения из файла
        painter.drawPixmap(300, 3, pix)
        painter.drawPixmap(QRect(300, 200, 150, 150), pix)
        painter.drawPixmap(QPoint(300, 400), pix, QRect(0, 0, 150, 150))
        painter.drawPixmap(QRect(475, 400, 100, 100), pix, QRect(0, 0, 150, 150))


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