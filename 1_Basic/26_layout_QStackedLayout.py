"""
Пример использования виджета стэка слоев QStackedLayout в комбинации с виджетом кнопки QPushButton
для переключения видимости виджетов в стэке
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedLayout,
    QLabel,
    QPushButton
)

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, классов стэка слоев QStackedLayout, виджетов слоев с горизонтальным расположением
виджетов QHBoxLayout, вертикальным расположением виджетов QVBoxLayout, базового виджета QWidget, виджета ярлыка QLabel
и виджета кнопка QPushButton.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""
from layout_colorwidget import Color  # импорт класса пользовательского виджета цвета из модуля


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный запуск конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.page_layout = QVBoxLayout()  # создание нижнего слоя для размещения других слоев
        self.button_layout = QHBoxLayout()  # создание слоя для размещения экземпляров виджета кнопок
        self.stack_layout = QStackedLayout()  # создание стэка слоев для размещения виджетов
        self.page_layout.addLayout(self.button_layout)  # размещение на нижнем слое слоя кнопок
        self.page_layout.addLayout(self.stack_layout)  # размещение на нижнем слое стэка слоев

        self.button_red = QPushButton('red')  # создание кнопки для переключения на слой red
        self.button_red.pressed.connect(self.activate_tab_red)  # создание события на нажатие кнопки с
        # привязкой ресивера
        self.button_layout.addWidget(self.button_red)  # размещение виджета кнопки на слое для кнопок
        self.stack_layout.addWidget(Color('red'))  # помещение в стэк слоев экземпляра пользовательского класса цвета

        self.button_blue = QPushButton('blue')  # создание кнопки для переключения на слой blue
        self.button_blue.pressed.connect(self.activate_tab_blue)  # создание события на нажатие кнопки с
        # привязкой ресивера
        self.button_layout.addWidget(self.button_blue)  # размещение виджета кнопки на слое для кнопок
        self.blue_widget = Color('blue')
        self.stack_layout.addWidget(self.blue_widget)  # помещение в стэк слоев экземпляра пользовательского
        # класса цвета

        self.button_green = QPushButton('green')  # создание кнопки для переключения на слой green
        self.button_green.pressed.connect(self.activate_tab_green)  # создание события на нажатие кнопки с
        # привязкой ресивера
        self.button_layout.addWidget(self.button_green)  # размещение виджета кнопки на слое для кнопок
        self.stack_layout.addWidget(Color('green'))


        # self.stack_layout.setCurrentIndex(2)  # установка индекса виджета, которые будет показан на верхнем видимом слое
        # индекс указывается в порядке добавления виджетов в стэк слоев

        self.widget = QWidget()  # создание контейнера для размещения слоя
        self.widget.setLayout(self.page_layout)  # размещение нижнего слоя в контейнере
        self.setCentralWidget(self.widget)  # размещение контейнера, содержащего слой, в главном окне приложения

    def activate_tab_red(self) -> None:
        """
        Метод ресивер (слот) для переключения видимости слоя.
        :return: None
        """
        self.stack_layout.setCurrentIndex(0)  # установка индекса виджета, которые будет показан на верхнем видимом слое
        # индекс указывается в порядке добавления виджетов в стэк слоев

    def activate_tab_blue(self) -> None:
        """
        Метод ресивер (слот) для переключения видимости слоя.
        :return: None
        """
        """
        Также можно указать текущий виджет с помощью self.layout.setCurrentWidget(self.widget)
        передав в метод непосредственно сам виджет
        """
        self.stack_layout.setCurrentWidget(self.blue_widget)

    def activate_tab_green(self) -> None:
        self.stack_layout.setCurrentIndex(2)  # установка индекса виджета, которые будет показан на верхнем видимом слое
        # индекс указывается в порядке добавления виджетов в стэк слоев


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # Создание экземпляра класса основного цикла событий приложения.
    window = MainWindow()  # Создание главного окна приложения.
    window.show()  # Метод вывода главного окна приложения (по умолчанию окно спрятано).
    app.exec()  # Запуск основного цикла событий главного окна приложения.


if __name__ == '__main__':  # Данное условие предотвращает запуск кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня
