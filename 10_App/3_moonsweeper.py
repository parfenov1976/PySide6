"""
Пример игры аналога минера из windows
"""
import random
import sys
import time

from paths import Paths  # импорт класса настроек путей к ресурсам приложения

from PySide6.QtWidgets import (QApplication,
                               )

from PySide6.QtGui import (QImage,
                           QColor,
                           )

"""
Импорт модуля для работы со случайностями (величины, выбор и т.д.) random.
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой 
Импорт модуля time для работы величинами времени.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication,

Импорт из модуля PySide6.QtGui класса графических изображений QImage, класса представления цветов QColor,

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

# TODO: продолжить здесь


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание основного цикла событий главного окна
    window = MainWindow()  # создание главного окна приложения
    app.setStyle('Fusion')  # установка более красивого стиля интерфейса
    window.show()  # вызов метода главного окна, делающего его видимым (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий главного окна
