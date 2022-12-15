"""
Модуль собственного пользовательского виджета цвета для установки цветов фона виджетов
"""

from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

"""
Импорт из библиотеки PySide6.QtGui класса виджета цвета QColor и класса виджета палитры QPalette
"""


class Color(QWidget):
    """
    Создание подкласса собственного пользовательского виджета цвета от супер-класса виджетов
    """

    def __init__(self, color: str) -> None:
        """
        Конструктор подкласса пользовательского виджета цвета.
        :param color: строка с названием цвета (на английском)
        """
        QWidget.__init__(self)  # явный запуск конструктора родительского класса
        self.setAutoFillBackground(True)  # указание на автоматическое заполнение фона цветом
        palette = self.palette()  # создание палитры для хранения цвета при помощи метода palette,
        # унаследованного от QWidget.
        palette.setColor(QPalette.Window, QColor(color))  # Изменение цвета фона виджета QPalette. Window на новый цвет
        # QColor который указан в переменной color
        self.setPalette(palette)  # установка цвета для виджета
