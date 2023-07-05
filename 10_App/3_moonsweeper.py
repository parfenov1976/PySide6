"""
Пример игры аналога минера из windows
"""
import random
import sys
import time

from paths import Paths  # импорт класса настроек путей к ресурсам приложения

from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QMainWindow,
                               QGridLayout,
                               QVBoxLayout,
                               QHBoxLayout,
                               QLayout,
                               )

from PySide6.QtGui import (QImage,
                           QColor,
                           )

from PySide6.QtCore import QTimer

"""
Импорт модуля для работы со случайностями (величины, выбор и т.д.) random.
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой 
Импорт модуля time для работы величинами времени.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса базового виджета QWidget,
класса главных окон QMainWindow,  
класса слоя с организацией по сетке QGridLayout, класса слоя с вертикальной организацией QVBoxLayout,
класса слоя с горизонтальной организацией QHBoxLayout, класса базового менеджера геометрии слоев QLayout,

Импорт из модуля PySide6.QtGui класса графических изображений QImage, класса представления цветов QColor,

Импорт из модуля PySide6.QtCore класса таймера QTimer,

"""

# глобальные переменные для хранения объектов изображений
IMG_BOMB = QImage(Paths.icon('bug.png'))
IMG_FLAG = QImage(Paths.icon('flag.png'))
IMG_START = QImage(Paths.icon('rocket.png'))
IMG_CLOCK = QImage(Paths.icon('clock-select.png'))

# словарь с цветами цифр
NUM_COLORS = {1: QColor('#f44336'),
              2: QColor('#9C27B0'),
              3: QColor('#3F51B5'),
              4: QColor('#03A9F4'),
              5: QColor('#00BCD4'),
              6: QColor('#4CAF50'),
              7: QColor('#E91E63'),
              8: QColor('#FF9800')}

# глобальные переменные для хранения кодов состояния
STATUS_READY = 0
STATUS_PAYING = 1
STATUS_FAILED = 2
STATUS_SUCCESS = 3

# словарь с иконками состояний
STATUS_ICONS = {STATUS_READY: Paths.icon('plus.png'),
                STATUS_PAYING: Paths.icon('smile.png'),
                STATUS_FAILED: Paths.icon('cross.png'),
                STATUS_SUCCESS: Paths.icon('smile_lol.png')}

# список кортежей с уровнями сложности и размерами поля с количеством пришельцев
# (сложность, размер поля, количество пришельцев)
LEVELS = [('Easy', 8, 10), ('Medium', 16, 40), ('Hard', 24, 99)]


class Pos(QWidget):
    pass


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от класса главных окон
    """

    def __init__(self):
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        w = QWidget()  # создание игрового поля
        hb = QHBoxLayout()  # создание горизонтальной панели
        hb.setSizeConstraint(QLayout.SetFixedSize)  # установка фиксированного размера горизонтальной панели
        self._timer = QTimer()  # создание таймера игры
        self._timer.timeout.connect(self.update_timer)  # создание сигнала на истечение таймера с привязкой
        # метода обновления таймера
        self._timer.start(1000)  # запуск таймера на 1000 мсек = 1 сек


        self.grid = QGridLayout()  # создание сетки игрового поля
        self.grid.setSpacing(5)  # установка расстояния между ячейками сетки
        self.grid.setSizeConstraint(QLayout.SetFixedSize)  # установка фиксированного размера сетки

    def set_level(self, level):
        self.level_name, self.b_size, self.n_mines = LEVELS[level]
        self.setWindowTitle(f'Moonsweeper - {self.level_name}')
        self.mines.setText(f'{self.n_mines:03d}')
        self.clear_map()  # вызов метода для очистки карты
        self.init_map()  # вызов метода для инициализации карты
        self.reset_map()  # вызов метода для перезагрузки параметров игры

    def clear_map(self):
        # todo
        pass

    def init_map(self):
        # todo
        pass

    def reset_map(self):
        # todo
        pass

    def update_timer(self):
        # TODO
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание основного цикла событий главного окна
    window = MainWindow()  # создание главного окна приложения
    app.setStyle('Fusion')  # установка более красивого стиля интерфейса
    window.show()  # вызов метода главного окна, делающего его видимым (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий главного окна
