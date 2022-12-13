import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QDial

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета диска регулятора QDial 
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от родительского класса главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктов главного окна приложения.
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.widget = QDial()  # создание экземпляра класса виджета дискового регулятора
        self.widget.setRange(-10, 100)  # установка диапазона значений регулятора
        self.widget.setMinimum(-10)  # можно также задать нижний порог
        self.widget.setMaximum(100)  # и верхний порог отдельно
        self.widget.setSingleStep(1)  # установка шага регулятора
        self.widget.valueChanged.connect(self.value_changed)  # создание сигнала изменения значения,
        # передается число методу ресиверу
        self.widget.sliderMoved.connect(self.slider_position)  # создание сигнала изменения положения регулятора,
        # методу ресиверу передается положение регулятора. Данный сигнал передается только если управление
        # дисковым регулятором производится курсором мышки
        self.widget.sliderPressed.connect(self.slider_pressed)  # создается сигнал о нажатии на слайдер
        self.widget.sliderReleased.connect(self.slider_released)  # создается сигнал об отпуске слайдера
        self.setCentralWidget(self.widget)

    @staticmethod
    def value_changed(i: int) -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета.
        :param i: int значение дискового регулятора.
        :return: None
        """
        print(i)

    @staticmethod
    def slider_position(p: int) -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета о положении дискового регулятора.
        :param p: int значение дискового регулятора.
        :return: None
        """
        print(f'position {p}')

    @staticmethod
    def slider_pressed() -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета о нажатии на дисковый регулятор
        """
        print('Pressed!')

    @staticmethod
    def slider_released() -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета об отпускании дискового регулятора
        """
        print('Released!')


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # метод вывода главного окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла событий главного окна приложения


if __name__ == '__main__':  # конструкция для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода приложения верхнего уровня
