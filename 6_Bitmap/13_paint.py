"""
Пример создания простого приложения для рисования.
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPainter, QColor

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtCore и класса Qt - содержит различные идентификаторы, используемые
в библиотеке Qt, класса размеров QSize.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета ярлыка QLabel, класса нажимаемой кнопки QPushButton,
класса базового виджета QWidget, слоев виджетов QVBoxLayout, QHBoxLayout.
Импорт из модуля PySide6.QtGui класса поверхности для графических изображений QPixmap,
класса виджета для рисования QPainter, класс объекта цветов QColor.  
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

COLORS = [  # коды цветов для цветовой палитры
    "#000000",
    "#141923",
    "#414168",
    "#3a7fa7",
    "#35e3e3",
    "#8fd970",
    "#5ebb49",
    "#458352",
    "#dcd37b",
    "#fffee5",
    "#ffd035",
    "#cc9245",
    "#a15c3e",
    "#a42f3b",
    "#f45b7a",
    "#c24998",
    "#81588d",
    "#bcb0c2",
    "#ffffff"
]


class MainWindow(QMainWindow):
    """
    Подкласса главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.canvas = Canvas()  # создание экземпляра класса холста
        w = QWidget()  # создание контейнера для слоев виджетов
        l = QVBoxLayout()  # создание экземпляра слоя с вертикальной организацией виджетов
        w.setLayout(l)  # размещение в контейнере слоя для виджетов
        l.addWidget(self.canvas)  # добавление на слой холста для рисования
        palette = QHBoxLayout()  # создание слоя для размещения элементов палитры
        self.add_palette_buttons(palette)  # вызов метода для создания элементов палитры
        # с передачей ему ссылки на слой для их размещения
        l.addLayout(palette)
        self.setCentralWidget(w)

    def add_palette_buttons(self, layout: QHBoxLayout) -> None:
        """
        Метода для создания элементов палитры и размещения их на слое
        :param layout: слой для размещения элементов палитры
        :return: None
        """
        for c in COLORS:
            b = QPaletteButton(c)  # создание экземпляра класса элемента палитры
            b.pressed.connect(lambda color=c: self.canvas.set_pen_color(color))
            layout.addWidget(b)


class QPaletteButton(QPushButton):
    """
    Подкласс палитры для выбора цветов от супер класса нажимаемой кнопки
    """

    def __init__(self, color) -> None:
        """
        Конструктор палитры
        """
        QPushButton.__init__(self)  # явный вызов конструктора родительского класса
        self.setFixedSize(QSize(24, 24))  # установка размера элемента палитры
        self.color = color  # сохранение цвета в атрибут объекта элемента палитры
        self.setStyleSheet(f'background-color: {color}')  # установка цвета фона для элемента палитры


class Canvas(QLabel):
    """
    Подкласс холста для рисования от супер класса ярлыка
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QLabel.__init__(self)  # явный вызов конструктора родительского класса
        self._pixmap = QPixmap(800, 600)  # создание поверхности для графической информации - холста для рисования
        self._pixmap.fill(Qt.white)  # заполнение холста белым цветом
        self.setPixmap(self._pixmap)  # привязка холста для отображения содержимого
        self.last_x, self.last_y = None, None  # вводим атрибуты за хранения координат предыдущей точки
        self.pen_color = QColor('#000000')  # создание атрибута для хранения цвета пера

    def set_pen_color(self, c: str) -> None:
        """
        Метод изменения цвета в атрибуте для хранения цвета пера
        """
        self.pen_color = QColor(c)

    def mouseMoveEvent(self, e) -> None:
        """
        Обработчик событий движения курсора мышки
        (срабатывает только с одновременным нажатием на кнопку мыши если не установлено постоянное отслеживание
        self.setMouseTracking(True) - не работает???)
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: None
        """
        if self.last_x is None:  # первое событие или нет
            self.last_x = e.x()  # извлечение координаты и помещение ее в атрибут для последней координаты
            self.last_y = e.y()
            return
        painter = QPainter(self._pixmap)  # создание экземпляра класса виджета для рисования
        p = painter.pen()  # создание пера для рисования
        p.setWidth(4)  # установка толщины линии
        p.setColor(self.pen_color)  # установка цвети пера
        painter.setPen(p)  # применение настроек пера к рисовальщику
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())  # рисование линии по координатам,
        # извлекаемым из события мыши
        painter.end()  # подача команды на завершение рисования, закрытие рисовальщика и сохранения изменений
        self.setPixmap(self._pixmap)  # после завершения рисования холст должен быть передан на отображение
        self.last_x = e.x()  # извлечение координаты и помещение ее в атрибут для последней координаты
        self.last_y = e.y()

    def mouseReleaseEvent(self, e) -> None:
        """
        Обработчик событий отпускания кнопок мышки
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: None
        """
        self.last_x = None
        self.last_y = None


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
