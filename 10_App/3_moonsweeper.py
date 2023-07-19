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
                               QLabel,
                               QPushButton,
                               )

from PySide6.QtGui import (QImage,
                           QColor,
                           QPainter,
                           QPixmap,
                           QPen,
                           QBrush,
                           QFont,
                           QIcon,
                           QAction,
                           )

from PySide6.QtCore import QTimer, Signal, QSize, Qt

"""
Импорт модуля для работы со случайностями (величины, выбор и т.д.) random.
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой 
Импорт модуля time для работы величинами времени.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса базового виджета QWidget,
класса главных окон QMainWindow, класса ярлыка QLabel, класса кнопок QPushButton
класса слоя с организацией по сетке QGridLayout, класса слоя с вертикальной организацией QVBoxLayout,
класса слоя с горизонтальной организацией QHBoxLayout, класса базового менеджера геометрии слоев QLayout,

Импорт из модуля PySide6.QtGui класса графических изображений QImage, класса представления цветов QColor,
класса пространства имен различных идентификаторов Qt, класса низкоуровневого рисования на виджетах
и других устройствах рисования QPainter, класса представления изображения QPixmap, класса настроек пера
рисовальщика QPen, класса настроек кисти QBrush, класс шрифтов QFont, класса иконок QIcon, абстрактного
класса пользовательских команд QAction

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
STATUS_PLAYING = 1
STATUS_FAILED = 2
STATUS_SUCCESS = 3

# словарь с иконками состояний
STATUS_ICONS = {STATUS_READY: Paths.icon('plus.png'),
                STATUS_PLAYING: Paths.icon('smiley.png'),
                STATUS_FAILED: Paths.icon('cross.png'),
                STATUS_SUCCESS: Paths.icon('smiley-lol.png')}

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
        self.adjacent_n = 0  # сброс подсчета мин в окружении
        self.is_revealed = False  # сброс состояния вскрытия ячейки
        self.is_flagged = False  # сброс флага
        self.update()  # вызов встроенного метода обновления виджета

    def paintEvent(self, event) -> None:
        """
        Метод обработчик событий отрисовки виджетов, вызываемый при перерисовке или обновлении виджетов
        :param event: PySide6.QtGui.QPaintEvent
        :return: None
        """
        p = QPainter(self)  # создание экземпляра класса рисовальщика
        p.setRenderHint(QPainter.Antialiasing)  # установка настройки рендеринга для рисовальщика
        r = event.rect()  # извлечение ссылки на прямоугольник для рисования
        if self.is_revealed:  # проверка вскрыта ли ячейка
            if self.is_start:  # проверка статуса стартового маркера
                p.drawPixmap(r, QPixmap(IMG_START))  # рисование на ячейке стартового маркера
            elif self.is_mine:  # проверка статуса минирования
                p.drawPixmap(r, QPixmap(IMG_BOMB))  # рисования на ячейке изображения мины
            elif self.adjacent_n > 0:  # проверка наличия мин в окружении ячейки
                pen = QPen(NUM_COLORS[self.adjacent_n])  # создание пера для рисовальщика и настройка его цвета
                p.setPen(pen)  # применение настроек пера к рисовальщику
                f = p.font()  # извлечение ссылки на настройки шрифта рисовальщика
                f.setBold(True)  # настройка шрифта рисовальщика
                p.setFont(f)  # применение настроек шрифта рисовальщика
                p.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, str(self.adjacent_n))  # рисование в ячейке надписи
                # с количеством мин в окружении ячейки
        else:
            p.fillRect(r, QBrush(Qt.lightGray))  # заливка ячейки светлосерым цветом
            pen = QPen(Qt.gray)  # создание пера рисовальщика с установкой цвета
            pen.setWidth(1)  # установка толщины линии для пера
            p.setPen(pen)  # применение настроек пера к рисовальщику
            p.drawRect(r)  # рисование прямоугольника в ячейке по ее контуру
            if self.is_flagged:  # проверка статуса флага в ячейке
                p.drawPixmap(r, QPixmap(IMG_FLAG))  # рисование флага в ячейке

    def mouseReleaseEvent(self, event) -> None:
        """
        Метод обработки отпускания кнопки мыши
        :param event: PySide6.QtGui.QMouseEvent
        :return: None
        """
        if event.button() == Qt.RightButton and not self.is_revealed:  # проверка правой кнопки мыши и статуса ячейки
            self.toggle_flag()  # вызов метода, переключающего состояние флага ячейки, который предотвращает
            # случайное вскрытие ячейки при установке на True
        elif event.button() == Qt.LeftButton:  # проверка левой кнопки мыши
            if not self.is_flagged and not self.is_revealed:  # проверка статуса ячейки, если ячейка не помечена флагом
                # и не открыта
                self.click()  # вызов метода клика по ячейке

    def toggle_flag(self) -> None:
        """
        Метод переключающий состояния флага ячейки
        :return: None
        """
        self.is_flagged = not self.is_flagged  # смена статуса флага на противоположный
        self.update()  # вызов метода перерисовки виджета
        self.clicked.emit()  # передача сигнала о том, что ячейка была нажата

    def click(self) -> None:
        """
        Метод, отрабатывающий нажатие на ячейку
        :return: None
        """
        self.reveal()  # вызов метода вскрытия ячейки
        if self.adjacent_n == 0:  # проверка наличия мин в окружении нажатой ячейки
            self.expandable.emit(self.x, self.y)  # передача сигнала на открытие прилегающей области, свободной от мин
        self.clicked.emit()  # передача сигнала о том, что ячейка была нажата

    def reveal(self, emit=True) -> None:
        """
        Метод, ставящий статус ячейки как открытой
        :param emit: bool флаг разрешения на передачу сигнала о вскрытии ячейки
        :return: None
        """
        if not self.is_revealed:  # проверка статуса открытости ячейки
            self.is_revealed = True  # установка статуса открытости ячейки
            self.update()  # вызов метода перерисовки виджета ячейки
            if emit:  # проверка разрешения на передачу сигнала
                self.revealed.emit(self)  # передача сигнала о вскрытии ячейки


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
        self.mines = QLabel()  # создание ярлыка для отображения количества мин на поле
        self.mines.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # настройка выравнивание по центру
        # по вертикали и горизонтали
        self.clock = QLabel()  # создание ярлыка для отображения часов
        self.clock.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # настройка выравнивание по центру
        # по вертикали и горизонтали
        f = self.mines.font()  # создание настроек для шрифта
        f.setPointSize(24)  # установка размера шрифта
        f.setWeight(QFont.Bold)  # установка толщины шрифта
        self.mines.setFont(f)  # применение настроек шрифта к ярлыку для отображения количества мин на поле
        self.clock.setFont(f)  # применение настроек шрифта к ярлыку для отображения часов
        self.clock.setText('000')  # установка начального значения часов
        self.button = QPushButton()  # создание кнопки для завершения текущей игры
        self.button.setFixedSize(QSize(32, 32))  # установка фиксированного размера кнопки
        self.button.setIconSize(QSize(32, 32))  # установка размера иконки, отображающейся на кнопке
        self.button.setIcon(QIcon(Paths.icon('smiley.png')))  # размещение на кнопке иконки
        self.button.setFlat(True)  # сделать кнопку плоской
        self.button.pressed.connect(self.button_pressed)  # создание сигнала нажатия на кнопку завершения игры
        # с привязкой слота
        self.statusBar()  # создание панели статусов в окне приложения
        l = QLabel()  # создание ярлыка для размещения изображения бомбы
        l.setPixmap(QPixmap.fromImage(IMG_BOMB))  # установка изображения бомбы
        l.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # настройка выравнивания изображения по правому краю
        # и посередине по вертикали
        hb.addWidget(l)  # добавление изображения мины на горизонтальную панель
        hb.addWidget(self.mines)  # добавление на горизонтальную панель счетчика мин
        hb.addWidget(self.button)  # добавление на горизонтальную панель кнопки завершения текущий игры
        hb.addWidget(self.clock)  # добавление на горизонтальную панель часов
        l = QLabel()  # создание ярлыка для размещения изображения символа часов
        l.setPixmap(QPixmap.fromImage(IMG_CLOCK))  # установка изображения часов
        l.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # настройка выравнивания для изображения часов
        hb.addWidget(l)  # добавление изображения часов на горизонтальную панель
        vb = QVBoxLayout()  # создание экземпляра слоя с вертикальной организацией виджетов
        vb.setSizeConstraint(QLayout.SetFixedSize)  # установка фиксированных размеров вертикальной панели
        vb.addLayout(hb)  # добавление горизонтальной панели на вертикальную панель
        self.grid = QGridLayout()  # создание сетки игрового поля
        self.grid.setSpacing(5)  # установка расстояния между ячейками сетки
        self.grid.setSizeConstraint(QLayout.SetFixedSize)  # установка фиксированного размера сетки
        vb.addLayout(self.grid)  # добавление на слой слоя сетки игрового поля
        w.setLayout(vb)  # добавление слоя с виджетами на виджет игрового поля
        self.setCentralWidget(w)  # размещение игрового поля в главном окне приложения

        self.menuBar().setNativeMenuBar(False)  # отказ от настроек панели меню, зависящих от платформы
        game_menu = self.menuBar().addMenu('&Game')  # выпадающего меню
        new_game_action = QAction('New game', self)  # создание команды на начало новой игры
        new_game_action.setStatusTip('Start a new game (your current game will be lost)')  # создание подсказки
        # для отображения в панели статуса
        new_game_action.triggered.connect(self.reset_map)  # создание сигнала для команды и привязка слота
        game_menu.addAction(new_game_action)  # размещение команды в выпадающем меню
        levels = game_menu.addMenu('Levels')  # создание выпадающего меню настроек уровня сложности (размеров)
        for n, level in enumerate(LEVELS):  # цикл для создания пунктов меню настроек размеров поля
            level_action = QAction(level[0], self)  # создание команды
            level_action.setStatusTip(f'{level[1]}x{level[1]} grid, with {level[2]} mines')  # создание подсказки
            level_action.triggered.connect(lambda checked=None, n=n: self.set_level(n))  # создание сигнала
            # с привязкой слота
            levels.addAction(level_action)  # размещение команды в выпадающем меню

        self.set_level(0)  # установка по умолчанию легкого уровня

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
                w.clicked.connect(self.trigger_start)  # создание сигнала на нажатие на ячейку игрового поля
                w.revealed.connect(self.on_reveal)  # сигнал на открытие нажатой ячейки
                w.expandable.connect(self.expand_reveal)  # сигнал на расширение раскрытия свободных от мин ячеек
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
                    random.randint(0, self.b_size - 1)  # генерация случайной координаты по вертикали
                    )
            w = self.grid.itemAtPosition(y, x).widget()  # извлечение ссылки на виджет ячейки игрового поля
            # из сетки слоя
            if not w.is_mine:  # проверка наличия мины
                w.is_start = True  # установка стартовой позиции
                w.is_revealed = True  # вскрытие ячейки старковой позиции
                w.update()  # вызов встроенного метода обновления виджета
                for w in self.get_surrounding(x, y):  # получение координат окружения и проход по ним
                    if not w.is_mine:  # проверка наличия мины в ячейках окружения
                        w.click()  # вызов метода, как бы нажимающего на виджет ячейки игрового поля
                break  # выход из цикла
        self.update_status(STATUS_READY)  # установка статуса готовности к клику по полую

    def get_surrounding(self, x: int, y: int) -> list:
        """
        Метод, возвращающий список координат окружающих ячеек
        :param x: координата по горизонтали
        :param y: координата по вертикали
        :return: список координат позиций окружения
        """
        positions = []  # создание списка для хранения координат окружения
        for xi in range(max(0, x - 1), min(x + 2, self.b_size)):  # обход по горизонтали
            for yi in range(max(0, y - 1), min(y + 2, self.b_size)):  # обход по вертикали
                if not (xi == x and yi == y):  # исключение координат входной ячейки
                    positions.append(self.grid.itemAtPosition(yi, xi).widget())  # добавление координат
                    # ячеек окружения в список
        return positions  # возврат списка

    def button_pressed(self) -> None:
        """
        Метод слот завершения игры по нажатию кнопки завершения
        :return: None
        """
        if self.status == STATUS_PLAYING:  # проверка статуса игры
            self.game_over()  # вызов метода завершения игры с поражением
        elif self.status == STATUS_FAILED or self.status == STATUS_SUCCESS:  # проверка статуса игры
            self.reset_map()  # вызов метода перезапуска игровой карты

    def reveal_map(self) -> None:
        """
        Метод для вскрытия всех ячеек игрового поля
        :return: None
        """
        for x in range(0, self.b_size):  # проход по горизонтали
            for y in range(0, self.b_size):  # проход по вертикали
                w = self.grid.itemAtPosition(y, x).widget()  # извлечение ссылки на игровую ячейку по координатам
                w.reveal(False)  # вызов метода открытия ячейки с запретом на подачу сигнала открытия ячейки

    def expand_reveal(self, x: int, y: int) -> None:
        """
        Метод расширения вскрытия ячеек, в окружении которых нет мин. Данный метод вызывается методом ".click()"
        Итерация выполняется в обратном порядке от начальной точки, добавляя новые ячейки в очередь. Это позволяет
        расширить область вскрытых ячеек за один раз, вместо большого количества обратных вызовов.
        :param x: Координата по горизонтали.
        :param y: Координата по вертикали.
        :return: None
        """
        to_expand = [(x, y)]  # создание списка координат ячеек, которые должны быть проверены на наличие мин
        # в окружении с добавлением в него координат исходной ячейки
        to_reveal = []  # создание списка ячеек, которые должны быть вскрыты по результатам проверки на наличие
        # мин в окружении
        any_added = True  # создание переменной для хранения статуса добавления ячеек в список на проверку
        while any_added:  # цикл проверки ячеек выполняется пока в список на проверку добавляются новые ячейки
            any_added = False  # сброс состояния добавления
            to_expand, l = [], to_expand  # перенос данных из списка ячеек на проверку во временную ячейку
            for x, y in l:  # цикл обхода списка ячеек на проверку
                positions = self.get_surrounding(x, y)  # получение списка окружающих ячеек
                for w in positions:  # обход списка окружающих ячеек
                    if not w.is_mine and w not in to_reveal:  # проверка статуса минирования ячейки и проверка наличия
                        # ячейки в списке вскрываемых
                        to_reveal.append(w)  # добавление ячейки в список вскрываемых
                        if w.adjacent_n == 0:  # проверка количества мин в окружении ячейки
                            to_expand.append((w.x, w.y))  # если мин в окружении нет, ячейка добавляется в список на
                            # расширение области вскрытия
                            any_added = True  # установка статуса пополнения списка на расширение
        for w in to_reveal:  # обход списка ячеек на вскрытие
            w.reveal()  # вызов метода вскрытия ячейки

    def trigger_start(self) -> None:
        """
        Метод для запуска новой игры
        :return: None
        """
        if self.status == STATUS_READY:  # проверка статуса готовности к новой игре
            self.update_status(STATUS_PLAYING)  # смена статуса на "в игре"
            self._timer_start_nsecs = int(time.time())  # запуск таймера игры

    def update_status(self, status) -> None:
        """
        Метод для обновления статуса игры
        :param status: статус
        :return: None
        """
        self.status = status  # установка статуса игры
        self.button.setIcon(QIcon(STATUS_ICONS[self.status]))  # обновление иконки на кнопке завершения игры
        if status == STATUS_READY:  # проверка статуса готовности к новой игре
            self.statusBar().showMessage('Ready')  # вывод сообщения о готовности

    def update_timer(self) -> None:
        if self.status == STATUS_PLAYING:
            n_secs = int(time.time()) - self._timer_start_nsecs
            self.clock.setText(f'{n_secs:03d}')
        elif self.status == STATUS_READY:
            self.clock.setText(f'{0:03d}')

    def on_reveal(self, w: Pos) -> None:
        """
        Метод проверки результатам нажатия на ячейку
        :param w: экземпляр ячейки игрового поля
        :return: None
        """
        if w.is_mine:  # проверка минирования нажатой ячейки
            self.game_over()  # вызов метода, завершающего игру с поражением
        else:
            self.end_game_n -= 1  # уменьшение количества не заминированных ячеек
            if self.end_game_n == 0:  # проверка количества не заминированных ячеек, которые еще не открыты
                self.game_won()  # завершение игры с победой

    def game_over(self) -> None:
        """
        Метод для завершения игры с поражением
        :return: None
        """
        self.reveal_map()  # метод для вскрытия всей карты
        self.update_status(STATUS_FAILED)  # установка статуса игры на поражение

    def game_won(self) -> None:
        """
        Метода для завершения игры с победой
        :return: None
        """
        self.reveal_map()  # метод для вскрытия всей карты
        self.update_status(STATUS_SUCCESS)  # установка статуса игры на победу


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создание основного цикла событий главного окна
    window = MainWindow()  # создание главного окна приложения
    app.setStyle('Fusion')  # установка более красивого стиля интерфейса
    window.show()  # вызов метода главного окна, делающего его видимым (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий главного окна
