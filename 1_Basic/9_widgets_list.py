import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout  # <2>
from PySide6.QtWidgets import QWidget  # <1>
from PySide6.QtWidgets import (
    QApplication,       # класс управления приложением
    QCheckBox,          # виджет чекбокса
    QComboBox,          # виджет выпадающий список
    QDateEdit,          # редактируемое поле для даты
    QDateTimeEdit,      # редактируемое поля для даты и времени
    QDial,              # ручка вращающаяся
    QDoubleSpinBox,     # спиннер для числа с плавающей точкой
    QFontComboBox,      # виджет списка шрифтов
    QLabel,             # ярлык для размещения текста
    QLCDNumber,         # виджет по типу сегментного ЖКД
    QLineEdit,          # виджет однострочного поля для ввода текса
    QMainWindow,        # виджет главного окна
    QProgressBar,       # виджет шкалы прогресса
    QPushButton,        # виджет нажимаемой кнопки
    QRadioButton,       # виджет радиокнопки (круглая дырка с точкой)
    QSlider,            # ручка слайдер
    QSpinBox,           # спиннер для целого числа
    QTimeEdit,          # редактируемое поле времени
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    """
    Подкласс QMainWindow для создания и настройки главного окна приложения
    """
    def __init__(self):
        QMainWindow.__init__(self)  # явный вызов родительского класса

        self.setWindowTitle("Widgets App")  # установка названия главного окна приложения

        layout = QVBoxLayout()  # создание слоя для размещения виджетов
        widgets = [     # список виджетов для создания экземпляров в цикле
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:  # цикл для создания коллекции виджетов
            layout.addWidget(w())  # размещение виджета на слое

        widget = QWidget()  # создание контейнера для хранения слоя
        widget.setLayout(layout)  # размещение слоя в контейнере

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)  # размещение контейнера на главном окне приложения


def main() -> None:
    """
    Функция запуска кода верхнего уровня.
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла приложения
    """
    На одно приложение нужен только один экземпляр QApplication.
    Передача sys.argv нужна, чтобы обеспечить возможность использования аргументов командной строки для приложения.
    Если использование аргументов командной строки не предполагается, то QApplication([]) тоже будет работать. 
    [] - пустой список.
    """
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.
    app.exec()  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен.


if __name__ == '__main__':  # данное условие предотвращает запуск кода верхнего уровня модуля при его импортировании
    main()  # вызов функции запуска кода верхнего уровня
