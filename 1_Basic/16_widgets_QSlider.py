import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtWidgets import QVBoxLayout, QWidget

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета слайдера QSlider 
Дополнительно импортируем класс слоев для размещения виджетов QVBoxLayout и базовый класс виджета QWidget.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от родительского класса главного окна.
    """

    def __init__(self):
        """
        Конструктов главного окна приложения.
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.widget1 = QSlider(Qt.Vertical)  # создание экземпляра вертикального слайдера
        # (если не указать ориентировку слайдера по умолчанию создается вертикальный)
        self.widget2 = QSlider(Qt.Horizontal)  # создание экземпляра горизонтального слайдера
        self.widget1.setMinimum(-10)  # установка минимального значения для слайдера
        self.widget1.setMaximum(3)  # установка максимального значения для слайдера
        self.widget2.setRange(-10, 3)  # также можно задать диапазон значений
        # стартовое значение по умолчанию равно 0
        self.widget1.setValue(-10)  # стартовое значение можно задать так
        self.widget1.setSingleStep(3)  # установка размера шага изменения значения
        # значение этого шага умножается на шаг колесика мышки если им управлять слайдером
        # в остальных случаях шаг всегда равен 1
        self.widget2.setSingleStep(1)  # установка размера шага изменения значения
        # если поставить дробный шаг, то слайдером можно будет управлять только курсором мыши
        self.widget1.valueChanged.connect(self.value_changed)  # создание сигнала изменения значения,
        # передается число методу ресиверу
        self.widget1.sliderMoved.connect(self.slider_position)  # создание сигнала изменения положения слайдера,
        # методу ресиверу передается положение слайдера. Данный сигнал передается только если управление
        # слайдером производится курсором мышки
        self.widget1.sliderPressed.connect(self.slider_pressed)  # создается сигнал о нажатии на слайдер
        self.widget1.sliderReleased.connect(self.slider_released)  # создается сигнал об отпуске слайдера
        self.widget2.valueChanged.connect(self.value_changed)
        self.widget2.sliderMoved.connect(self.slider_position)
        self.widget2.sliderPressed.connect(self.slider_pressed)
        self.widget2.sliderReleased.connect(self.slider_released)
        self.layout = QVBoxLayout()  # создание слоя для размещения виджетов
        self.layout.addWidget(self.widget1)  # добавление виджета на слой для их размещения
        self.layout.addWidget(self.widget2)  # добавление виджета на слой для их размещения
        self.widget3 = QWidget()  # создание контейнера для хранения слоя из класса базового виджета
        self.widget3.setLayout(self.layout)  # размещение слоя в контейнере
        self.setCentralWidget(self.widget3)  # размещение контейнера в главном окне приложения

    @staticmethod
    def value_changed(i: int) -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета
        :param i: int значение слайдера
        :return: None
        """
        print(i)

    @staticmethod
    def slider_position(p: int) -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета о положении слайдера
        :param p: int значение слайдера
        :return: None
        """
        print(f'position {p}')

    @staticmethod
    def slider_pressed() -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета о нажатии на слайдер
        """
        print('Pressed!')

    @staticmethod
    def slider_released() -> None:
        """
        Метод ресивер (слот) для получения сигнала от виджета об отпускании слайдера
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
