"""
Пример создания пользовательского виджета.
3-ий шаг - решение проблемы масштабирования виджетов измерителя и регулятора
"""
import sys

from PySide6.QtWidgets import QApplication, QVBoxLayout, QDial, QWidget, QSizePolicy
from PySide6.QtGui import QPaintEvent, QPainter, QBrush, QColor
from PySide6.QtCore import Qt, QRect, QSize

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета вращающегося регулятора QDial,
класса базового виджета QWidget, класса политики изменения размера QSizePolicy.
Импорт из модуля PySide6.QtCore класса Qt,содержащего различные идентификаторы, используемые
в библиотеке Qt, класса примитива прямоугольника QRect. 
Импорт из модуля PySide6.QtGui класса обработчика событий рисования QPaintEvent, класса виджета
для рисования QPainter, класса кисти QBrush, класса объекта цветов QColor, класса размеров QSize.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class _Bar(QWidget):
    """
    Подкласс силовой шкалы от супер-класса базового виджета
    """
    def __init__(self):
        """
        Конструктор шкалы измерителя
        """
        QWidget.__init__(self)  # Явный вызов конструктора родительского класса
        self.setSizePolicy(QSizePolicy.MinimumExpanding,
                           QSizePolicy.MinimumExpanding
                           )

    def sizeHint(self) -> QSize:
        """
        Метод, возвращающий минимальные размеры виджета
        :return: QSize - минимальный размер виджетов
        """
        return QSize(40, 120)

    def paintEvent(self, e: QPaintEvent) -> None:
        """
        Метод пользовательский обработчик события рисования
        :param e: QPaintEvent - событие базового обработчика рисования
        :return: None
        """
        painter = QPainter(self)  # создание экземпляра класса рисовальщика
        brush = QBrush()  # создание экземпляра класса кисти
        brush.setColor(QColor('black'))  # установка цвета кисти
        brush.setStyle(Qt.SolidPattern)  # установка стиля заполнения сплошное
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        # Рисование прямоугольника. Использование метода .device() позволяют рисовать
        # прямоугольник согласно размеру окна виджета
        painter.fillRect(rect, brush)  # заливка прямоугольника цветом кисти


class PowerBar(QWidget):
    """
    Подкласс пользовательского виджета от супер-класса базового виджета
    """
    def __init__(self, parent=None, steps: int = 5) -> None:
        """
        Конструктор пользовательского виджета
        """
        QWidget.__init__(self, parent)  # явный вызов конструктора родительского класса
        layout = QVBoxLayout()  # создание экземпляра класса слоев для виджетов
        self._bar = _Bar()  # создание экземпляра класса силовой шкалы
        layout.addWidget(self._bar)  # размещение силовой объекта силовой шкалы в слое
        self._dial = QDial()  # создание экземпляра класса виджета вращающегося регулятора
        layout.addWidget(self._dial)  # размещение виджета регулятора на слое
        self.setLayout(layout)  # размещение слоя с виджетами в окне пользовательского виджета


def main() -> None:
    """
    Функция запуска кода верхнего уроня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла главного окна приложения
    volume = PowerBar()  # создание экземпляра пользовательского виджета
    volume.show()  # вызов метода вывода виджета (по умолчанию виджет спрятан)
    app.exec()  # запуска основного цикла пользовательского виджета


if __name__ == '__main__':  # данное условие нужно для предотвращения запуска кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего
