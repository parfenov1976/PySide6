"""
Пример использования библиотеки PyQtGraph для черчения графиков, диаграмм и других визуализаций данных
с примером изменения цвета, толщины и стиля линий.
В данном примере также добавлены:
- маркеры на линию
- название графика/диаграммы
- ярлыки на оси
- условные обозначения
- сетка
- пределы значений для осей графика
"""
import sys

from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QtWidgets.QApplication([]) в качестве аргумента передается пустой список.
Импорт из библиотеки PySide6 модуля виджетов QtWidgets.
Из библиотеки pyqtgraph.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QtWidgets.QMainWindow):
    """
    Класс главного окна приложения от супер-класса виджета главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QtWidgets.QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.graph_widget = pg.PlotWidget()  # создание виджета холста для черчения
        self.setCentralWidget(self.graph_widget)  # размещение холста в главном окне приложения

        # набор данных для построения графика
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graph_widget.setBackground('w')  # установка белого цвета на задний фон
        # можно использовать для цвета объект QColor, можно задавать цвет в hex или RGB и RGBA
        # также можно использовать цвет заднего фона согласно настройкам системы
        # color = self.palette().color(QtGui.QPalette.Window)
        # по умолчанию цвет заднего фона черный
        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)  # создание пера для рисования
        # с установкой цвета линий, толщины в пикселях и стиля линии (Qt.SolidLine, Qt.DashLine, Qt.DotLine,
        # Qt.DashDotLine, Qt.DashDotDotLine)

        self.graph_widget.addLegend(offset=(100, 100))  # добавление условных обозначений на холст
        # !!! Добавление легенды должно быть до вызова метода .plot()

        self.graph_widget.showGrid(x=True, y=True)  # добавление линий сетки на холст

        self.graph_widget.setTitle('Название графика', color='#ffcc00', size='15pt', bold=True, italic=True)
        # установка названия графика с примером установки стиля текста
        # можно использовать синтаксис заголовков html
        # self.graph_widget.setTitle("<span style=\"color:blue;font-size:30pt\">Your Title Here</span>")

        # Создание наименования осей
        styles = {'color': '#ff0000', 'font-size': '30pt'}  # сохранение настроек стиля текста в словаре
        self.graph_widget.setLabel('left', 'Temperature (°C)', **styles)  # создание ярлыка
        # с притяжкой к оси по левому краю холста
        self.graph_widget.setLabel('bottom', 'Hour (H)', **styles)  # создание ярлыка с притяжкой
        # к оси по нижнему краю холста
        # можно использовать синтаксис html
        # self.graph_widget.setLabel('left', "<span style=\"color:red;font-size:30px\">Temperature (°C)</span>")
        # self.graph_widget.setLabel('bottom', "<span style=\"color:red;font-size:30px\">Hour (H)</span>")

        self.graph_widget.setXRange(0, 10, padding=0)  # ограничение отображаемого диапазона по оси x
        self.graph_widget.setYRange(20, 55, padding=0)  # ограничение отображаемого диапазона по оси x
        # padding устанавливает величину отступа от пределов ограничения отображаемого диапазона

        self.graph_widget.plot(hour, temperature, name='Sensor 1', pen=pen, symbol='+', symbolSize=30, symbolBrush='b')
        # вызов метода рисования графика по величинам x, y и с подключением настроек пера, добавлением маркера
        # типы маркеров обозначаются + - крестик, o - кружочек, s - квадратик, t - треугольник, d - ромб


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QtWidgets.QApplication(sys.argv)  # создание основного цикла событий приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window.show()  # установка видимости главного окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # проверка имени запущенного модуля для предотвращения запуска
    # кода верхнего уровня данного модуля при его импортировании
    main()  # вызов функции запуска кода приложения верхнего уровня
