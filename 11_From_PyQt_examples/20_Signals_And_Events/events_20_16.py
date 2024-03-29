"""
События мыши. Наведение и увод курсора мыши

Обработать наведение курсора мыши на компонент и увод его с компонента позволяют
следующие специальные методы:
♦ enterEvent(self, <event>) - вызывается при наведении курсора мыши на компонент.
  Через параметр <event> доступен объект класса QEnterEvent, не несущий никакой
  дополнительной информации;
♦ leaveEvent(self, <event>) - вызывается при уводе курсора мыши с компонента. Через
  параметр <event> доступен объект класса QLeaveEvent, не несущий никакой дополнительной
  информации.
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QVBoxLayout,
                               QPushButton,
                               QLineEdit,
                               QWidget)

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класс виджета кнопки QPushButton, класс слоя с вертикальной организацией виджетов QVBoxLayout,
базовый класс пустого виджета QWidget, класс редактируемого однострочного текстового поля QLindeEdit
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Обработка наведения мыши на объект интерфейса')  # установка заголовка окна
        self.resize(300, 200)  # установка исходного размера окна
        self.txt_line = QLineEdit()  # создание однострочного текстового поля
        self.btn = MyButton(self.txt_line, 'Наведи на меня курсор')
        # создание виджета кнопки на основе пользовательского класса
        self.btn.clicked.connect(self.clear_txt)  # привязка обработчика на нажатие кнопки
        self.vbox = QVBoxLayout()  # создание слоя для виджетов
        self.vbox.addWidget(self.txt_line)  # добавление на слой текстового поля
        self.vbox.addWidget(self.btn)  # добавление на слой кнопки
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера со слоями в главном окне приложения

    def clear_txt(self) -> None:
        """
        Обработчик сигнала на нажатие кнопки
        :return: None
        """
        self.txt_line.setText('')  # очистка текстового поля


class MyButton(QPushButton):
    """
    Пользовательский класс виджета кнопки
    """

    def __init__(self, txt_line, *args, **kwargs):
        """
        Конструктор пользовательского виджета кнопки
        :param txt_line: ссылка на текстовое поле главного окна
        :param args: неопределенный набор позиционных аргументов
        :param kwargs: неопределенный набор ключевых аргументов
        """
        QPushButton.__init__(self, *args, **kwargs)  # явный вызов конструктора родительского класса
        self.txt_line = txt_line  # сохранение ссылки на текстовое поле главного окна в аттрибуте
        # пользовательского класса виджета кнопки

    def enterEvent(self, event) -> None:
        """
        Обработчик события наведения курсора на кнопку
        :param event: QEnterEvent - объект класса события наведения курсора мыши
        :return: None
        """
        self.txt_line.setText('Курсор наведен на кнопку')

    def leaveEvent(self, event) -> None:
        """
        Обработчик события увода курсора с кнопки
        :param event: QLeaveEvent - объект класса события увода курсора мыши
        :return: None
        """
        self.txt_line.setText('Курсор убран с кнопки')


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
