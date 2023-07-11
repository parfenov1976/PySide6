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

from PySide6.QtCore import QTimer, Signal, QSize

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

Импорт из модуля PySide6.QtCore класса таймера QTimer, класс сигналов Signal, класс размеров QSize

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
    expandable = Signal(int, int)  # создание объекта сигнала расширения вскрытой области
    revealed = Signal(object)  # создание объекта сигнала вскрытия ячейки
    clicked = Signal()  # создание объекта сигнала клика по ячейки

    def __init__(self, x, y) -> None:
        """
        Конструктор ячейки игрового поля
        :param x: int - координата ячейки по горизонтали
        :param y: int - координата ячейки по вертикали
        """
        QWidget.__init__(self)  # явный вызов конструктора родительского класса
        self.setFixedSize(QSize(20, 20))  # установка фиксированного размера виджета ячейки игрового поля
        self.x = x  # сохранение координаты по горизонтали в атрибут ячейки
        self.y = y  # сохранение координаты по вертикал в атрибут ячейки
        self.reset()  # вызов метода сброса состояний ячейки игрового поля к исходным значениям

    def reset(self) -> None:
        """
        Метод сброса состояний ячейки игрового поля к исходным значениям
        :return: None
        """
        self.is_start = False  # сброс состояния стартовой точки
        self.is_mine = False  # сброс состояния мины
        self.adjacent = 0  # сброс подсчета мин в окружении
        self.is_revealed = False  # сброс состояния вскрытия ячейки
        self.is_flagged = False  # сброс флага
        self.update()  # вызов встроенного метода обновления виджета


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

        # todo
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

    def clear_map(self) -> None:
        """
        Метод удаления ячеек игрового поля с карты. Размер карты для всех случаев принимаем максимальный
        :return: None
        """
        # цикл очистки игрового поля
        for x in range(0, LEVELS[-1][1]):  # проход по горизонтали
            for y in range(0, LEVELS[-1][1]):  # проход по вертикали
                c = self.grid.itemAtPosition(y, x)  # выбор объекта в сетке по координатам
                if c:  # проверка наличия объекта в сетке
                    c.widget().close()  # подача сигнала на закрытие выбранного виджета ячейки
                    self.grid.removeItem(c)  # удаление выбранного виджета из сетки

    def init_map(self) -> None:
        """
        Метод инициализации игровой карты
        :return: None
        """
        # цикл создания ячеек игрового поля
        for x in range(0, self.b_size):  # проход по горизонтали
            for y in range(0, self.b_size):  # проход по вертикали
                w = Pos(x, y)  # создание экземпляра класса виджета ячейки игрового поля
                self.grid.addWidget(w, x, y)  # добавление виджета ячейки игрового поля в сетку слоя для виджетов
                w.clicked.connect(self.tirgger_start)  # создание сигнала на нажатие на ячейку игрового поля
                w.revealed.connect(self.on_reveal)  # сигнал на открытие нажатой ячейки
                w.expandable.connect(self.expand_reveal)  # сигнал на расширение раскрытия свободных ячеек
                # вокруг нажатой
        QTimer.singleShot(0, lambda: self.resize(1, 1))  # помещает изменение размера в очередь, возвращая управление
        # Qt до выполнения изменения размера

    def reset_map(self) -> None:
        """
        Методы вызова внутриклассовых методов для инициализации и ренинициализации игровой карты
        :return: None
        """
        self._reset_position_data()  # вызов метода для удаления мин и их очистки данных
        self._reset_add_mines()  # вызов метода для добавления мин на карту
        self._reset_calculate_adjacency()  # вызов метода для подсчета количества мин рядом с каждой позицией
        self._reset_add_starting_marker()  # вызов метода добавления маркера старта и запускающего начало исследования
        self.update_timer()  # вызов метода перезагрузки таймера

    def _reset_position_data(self) -> None:
        """
        Внутренний метод для удаления мин и очистки их данных
        :return: None
        """
        for x in range(0, self.b_size):  # проход по горизонтали
            for y in range(0, self.b_size):  # проход по вертикали
                w = self.grid.itemAtPosition(y, x).widget()  # выбирает ячейку сетки слоя и возвращает
                # находящийся в ней виджет
                w.reset()  # вызов метода ячейки игрового поля для перезагрузки виджета к исходному состоянию

    def _reset_add_mines(self) -> list:
        """
        Внутренний метод для расстановки мин на игровом поле
        :return: list - список заминированных ячеек
        """
        positions = []  # создание списка для хранения позиций мин
        while len(positions) < self.n_mines:  # цикл по условию заполнения списка мин
            x, y = (random.randint(0, self.b_size - 1),  # случайный выбор ячейки игрового поля
                    random.randint(0, self.b_size - 1)
                    )
            if (x, y) not in positions:  # проверка условия нахождения позиции в списке мин
                w = self.grid.itemAtPosition(y, x).widget()  # выбор ячейки и возврат виджета, размещенного в ней
                w.is_mine = True  # размещение мины в ячейке
                positions.append((x, y))  # добавление заминированной ячейки в список мин
                self.end_game_n = (self.b_size * self.b_size) - (self.n_mines + 1)  # расчет условия завершения игры
        return positions

    def _reset_calculate_adjacency(self):
        """
        Метод подсчета количества мни в окружении позиции
        :return: None
        """
        def get_adjacency(x: int, y: int) -> int:
            """
            Внутренний метод подсчета количества мин в окружении позиции
            :param x: int - координата позиции по горизонтали
            :param y: int - координата позиции по вертикали
            :return: int - количество мин в окружении позиции
            """
            positions = self.get_surrounding(x, y)  # вызов метода, возвращающего координаты окружающих позиций
            return sum(1 for w in positions if w.is_mine)  # подсчет количества мин в окружении
        for x in range(0, self.b_size):  # проход по ячейкам игрового поля по горизонтали
            for y in range(0, self.b_size):  # проход по ячейкам игрового поля по вертикали
                w = self.grid.itemAtPosition(y, x).widget()  # извлечение ссылки на виджет ячейки игрового поля из
                # сетки слоя по координатам
                w.adjacent_n = get_adjacency(x, y)  # запись в игровую ячейку количество мин в ее окружении

    def _reset_add_starting_marker(self) -> None:
        """
        Метод для установки стартовой позиции исследования игрового поля
        :return: None
        """
        self.update_status(STATUS_READY)  # установка начального статуса
        while True:  # цикл случайного выбора стартовой позиции
            x, y = (random.randint(0, self.b_size - 1),  # генерация случайной координаты по горизонтали
                    random.randint(0, self.b_size - 1)   # генерация случайной координаты по вертикали
                    )
            w = self.grid.itemAtPosition(y, x).widget()  # извлечение ссылки на виджет ячейки игрового поля
            # из сетки слоя
            if not w.is_mine:  # проверка наличия мины
                w.is_start = True  # установка стартовой позиции
                w.is_revealed = True  # вскрытие ячейки старковой позиции
                w.update()  # вызов встроенного метода обновления виджета
                for w in self.get_surroundig(x, y):  # получение координат окружения и проход по ним
                    if not w.is_mine:  # проверка наличия мины в ячейках окружения
                        w.click()  # вызов метода, как бы кликающего по виджету
                break  # выход из цикла
        self.update_status(STATUS_READY)  # установка статуса готовности к клику по полую

    # TODO

    def update_timer(self):
        # TODO
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание основного цикла событий главного окна
    window = MainWindow()  # создание главного окна приложения
    app.setStyle('Fusion')  # установка более красивого стиля интерфейса
    window.show()  # вызов метода главного окна, делающего его видимым (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий главного окна
