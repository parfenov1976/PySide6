"""
Пример создания пользовательского виджета.
9-ой шаг - добавление возможности изменять значение регулятора кликом по шкале.
Для этого нужно добавить обработчик событий с мыши.
"""
import sys

from PySide6.QtWidgets import QApplication, QVBoxLayout, QDial, QWidget, QSizePolicy
from PySide6.QtGui import QPaintEvent, QPainter, QBrush, QColor
from PySide6.QtCore import Qt, QRect, QSize, Signal

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета вращающегося регулятора QDial,
класса базового виджета QWidget, класса политики изменения размера QSizePolicy.
Импорт из модуля PySide6.QtCore класса Qt,содержащего различные идентификаторы, используемые
в библиотеке Qt, класса примитива прямоугольника QRect, класс сигнала Signal.
Импорт из модуля PySide6.QtGui класса обработчика событий рисования QPaintEvent, класса виджета
для рисования QPainter, класса кисти QBrush, класса объекта цветов QColor, класса размеров QSize.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class _Bar(QWidget):
    """
    Подкласс силовой шкалы от супер-класса базового виджета
    """
    clickedValue = Signal(int)  # создает экземпляр класс сигнала

    def __init__(self, steps: int or list) -> None:
        """
        Конструктор шкалы измерителя
        """
        QWidget.__init__(self)  # Явный вызов конструктора родительского класса
        self.setSizePolicy(QSizePolicy.MinimumExpanding,
                           QSizePolicy.MinimumExpanding
                           )
        if isinstance(steps, list):  # если в качестве аргумента передан список цветов
            self.n_steps = len(steps)  # количество делений равно количеству цветов в списке
            self.steps = steps  # сохранение списка цветов в аттрибуте экземпляра
        elif isinstance(steps, int):  # если в качестве аргумента передано количество делений
            self.n_steps = steps  # сохранение количества делений в атрибуте экземпляра
            self.steps = ['red'] * steps  # создание списка цветов
        else:  # в остальных случаях
            raise TypeError('steps must be a list or int')  # выброс исключения по типу
        self._bar_solid_percent = 0.8  # установка доли высоты шага для отрисовки прямоугольника деления
        self._background_color = QColor('black')  # установка цвета фона шкалы
        self._padding = 4  # установка отступа по краям прямоугольника деления в пикселях

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
        brush.setColor(self._background_color)  # установка цвета кисти
        brush.setStyle(Qt.SolidPattern)  # установка стиля заполнения сплошное
        rect = QRect(0, 0, painter.device().width(), painter.device().height())
        # Рисование прямоугольника. Использование метода .device() позволяют рисовать
        # прямоугольник согласно размеру окна виджета. Методы .width() и height() извлекают
        # размеры окна рисовальщика
        painter.fillRect(rect, brush)  # заливка прямоугольника цветом кисти

        # Отображение текущего состояния
        parent = self.parent()  # передача ссылки на регулятор в переменную через специальный
        # метод родительского класса
        vmin, vmax = parent.minimum(), parent.maximum()  # установка минимального и максимального значения регулятора
        value = parent.value()  # извлечение текущего значения регулятора

        # определение размеров поля для рисования делений шкалы
        d_height = painter.device().height() - (self._padding * 2)
        d_width = painter.device().width() - (self._padding * 2)

        step_size = d_height / self.n_steps  # вычисление размера шага для рисования деления шкалы
        bar_height = step_size * self._bar_solid_percent  # вычисление высоты прямоугольника деления шаклы

        pc = (value - vmin) / (vmax - vmin)  # вычисление доли шкалы, соответствующей значению регулятора
        n_steps_to_draw = int(pc * self.n_steps)  # вычисление количества сегментов, которые должны быть
        # отрисованы

        for n in range(n_steps_to_draw):  # цикл отрисовки делений шаклы
            brush.setColor(QColor(self.steps[n]))  # присвоение кисти цвета деления из списка цветов
            ypos = (1 + n) * step_size  # вычисление положения ЛВУ прямоугольника деления относительно самого деления
            rect = QRect(
                self._padding,  # отрисовка прямоугольника с вычисленными параметрами
                self._padding + d_height - int(ypos),  # вычисление высоты ЛВУ прямоугольника деления на шкале
                d_width,
                int(bar_height)
            )
            painter.fillRect(rect, brush)  # заливка прямоугольника деления шкалы цветом
        painter.end()  # метод завершения работы рисовальщика

    def _trigger_refresh(self):
        """
        Метод ресивер (слот) сигнала обновления виджета
        :return:
        """
        self.update()  # вызов метода обновления виджета родительского класса QWidget

    def _calculate_clicked_value(self, e) -> None:
        """
        Обработчик действий с мышью
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: None
        """
        parent = self.parent()
        vmin, vmax = parent.minimum(), parent.maximum()
        d_height = self.size().height() + (self._padding * 2)
        step_size = d_height / self.n_steps
        click_y = e.y() - self._padding - step_size / 2
        pc = (d_height - click_y) / d_height
        value = int(vmin + pc * (vmax - vmin))
        self.clickedValue.emit(value)

    def mouseMoveEvent(self, e) -> None:
        """
        Обработчик сигнала на перемещение мышью
        """
        self._calculate_clicked_value(e)

    def mousePressEvent(self, e) -> None:
        """
        Обработчик сигнала на нажатие кнопок мыши
        """
        self._calculate_clicked_value(e)


class PowerBar(QWidget):
    """
    Подкласс пользовательского виджета от супер-класса базового виджета
    """

    def __init__(self, parent=None, steps: int or list = 5) -> None:
        """
        Конструктор пользовательского виджета
        """
        QWidget.__init__(self, parent)  # явный вызов конструктора родительского класса
        layout = QVBoxLayout()  # создание экземпляра класса слоев для виджетов
        self._bar = _Bar(steps)  # создание экземпляра класса силовой шкалы
        layout.addWidget(self._bar)  # размещение силовой объекта силовой шкалы в слое
        self._dial = QDial()  # создание экземпляра класса виджета вращающегося регулятора
        self._dial.valueChanged.connect(self._bar._trigger_refresh)  # создание сигнала на изменение
        # положения регулятора
        layout.addWidget(self._dial)  # размещение виджета регулятора на слое
        self.setLayout(layout)  # размещение слоя с виджетами в окне пользовательского виджета
        self._bar.clickedValue.connect(self._dial.setValue)  # создание сигнала и подключение к методу обработчика

    def __getattr__(self, item) -> None:
        """
        Магический метод для перехвата имени атрибутов экземпляра
        :param item: имя аттрибута экземпляра
        :return: None
        """
        if item in self.__dict__:  # если аттрибут существует в словаре аттрибутов экземпляра
            return self[item]  # вызов метода согласно имени аттрибута
        try:
            return getattr(self._dial, item)  # в противном случае пытается извлечь и вернуть значение
            # аттрибута из экземпляра вращающегося регулятора
        except AttributeError:  # если аттрибут не обнаружен, выбрасывается исключение с ошибкой аттрибута
            raise AttributeError(f"'{self.__class__.__name__}' объект не имеет аттрибута '{item}'")

    def setColor(self, color: str) -> None:
        """
        Метода для приема настройки одного цвета для всех делений
        :param color: str - название цвета или его шестнадцатеричный код
        :return: None
        """
        self._bar.steps = [color] * self._bar.n_steps  # создание списка цветов делений
        self._bar.update()  # вызов метода обновления виджета из родительского класса

    def setColors(self, colors: list) -> None:
        """
        Метода для приема настройки цветов для делений шкалы
        :param colors: list - список названий цветов или их шестнадцатеричных кодов
        :return: None
        """
        self._bar.n_steps = len(colors)  # определение количества делений шкалы
        self._bar.steps = colors  # сохранение списка цветов делений шкалы в аттрибут экземпляра
        self._bar.update()  # вызов метода обновления виджета из родительского класса

    def setBarPadding(self, i: int) -> None:
        """
        Метод для приема настройки величины отступа по краям делений
        :param i: int - величина отступа в пикселях
        :return: None
        """
        self._bar._padding = int(i)  # сохранение количества делений шкалы в аттрибут экземпляра
        self._bar.update()  # вызов метода обновления виджета из родительского класса

    def setBarSolidPercent(self, f: float) -> None:
        """
        Метод для приема настройки доли высоты прямоугольника деления
        :param f: float - доля высоты прямоугольника деления от высоты шага делений
        :return: None
        """
        self._bar._bar_solid_percent = float(f)  # сохранение доли высоты в аттрибуте экземпляра
        self._bar.update()  # вызов метода обновления виджета из родительского класса

    def setBackgraundColor(self, color: str) -> None:
        """
        Метод для приема настройки цвета заднего фона шкалы
        :param color: str - название цвета или его шестнадцатеричный код
        :return: None
        """
        self._bar._background_color = QColor(color)  # создание и сохранение объекта цвета в аттрибуте экземпляра
        self._bar.update()  # вызов метода обновления виджета из родительского класса

    def setNSteps(self, n_steps: int) -> None:
        """
        Метода для приема настройки количества делений шкалы
        :param n_steps: int - количество делений шкалы
        :return: None
        """
        self._bar.n_steps = n_steps  # сохранение количества делений в аттрибуте экземпляра
        self._bar.steps = [self._bar.steps[0]] * self._bar.n_steps  # создание списка цветов делений
        self._bar.update()  # вызов метода обновления виджета из родительского класса


def main() -> None:
    """
    Функция запуска кода верхнего уроня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла главного окна приложения
    volume = PowerBar()
    volume.setColor('green')
    volume.setNSteps(10)
    # volume = PowerBar(steps=["#5e4fa2", "#3288bd", "#66c2a5", "#abdda4", "#e6f598",
    #                          "#ffffbf", "#fee08b", "#fdae61", "#f46d43", "#d53e4f",
    #                          "#9e0142"])  # создание экземпляра пользовательского виджета
    # volume = PowerBar(steps=["#a63603", "#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2",
    #                          "#feedde"])
    # volume = PowerBar(steps=10)
    volume.show()  # вызов метода вывода виджета (по умолчанию виджет спрятан)
    app.exec()  # запуска основного цикла пользовательского виджета


if __name__ == '__main__':  # данное условие нужно для предотвращения запуска кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего
