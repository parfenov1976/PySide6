"""
Пример программного закрытия окна

Чтобы закрыть окно, у него следует вызвать метод close(), Он возвращает значение True,
если окно успешно закрыто, и False - в противном случае. Закрыть сразу все окна программы
позволяет слот closeAllWindows() объекта программы.
Если у окна элемент WA_DeleteOnClose перечисления WidgetAttribute из модуля QtCore.Qt
установлен в значение True, после закрытия окна его объект будет автоматически удален,
в противном случае окно просто скроется. Установить или сбросить элемент можно с помощью
метода setAttribute() окна, например:

window.setAttribute(QtCore.Qt.WidgetAttribute.WA_DeleteOnClose, True)

После вызова метода close() или нажатия кнопки закрытия в заголовке окна возникает
событие QEvent.Close. Если внутри класса определить метод closeEvent(), это событие можно
перехватить и обработать. В качестве параметра метод принимает объект класса QCloseEvent,
который поддерживает методы accept() (позволяет закрыть окно) и ignore() (запрещает закрытие окна).
Вызывая эти методы, можно контролировать процесс закрытия окна.
"""

import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               )
from PySide6.QtCore import Qt

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса виджета кнопки QPushButton

Импорт из модуля PySide6.QtCore класса аттрибутов для настройки и управления виджетами Qt.
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Всплывающие и расширенные подсказки')  # установка заголовка окна
        self.setWindowFlag(Qt.WindowType.Dialog)  # установка флагов окна
        self.resize(300, 300)  # установка исходного размера окна
        self.btn = QPushButton('Закрыть окно', self)  # создание виджета кнопки с указанием родительского объекта
        self.btn.setFixedSize(150, 30)  # установка размеров кнопки
        self.btn.move(75, 135)  # смещение кнопки относительно левого верхнего угла окна
        self.btn.clicked.connect(self.close)  # привязка метода закрытия окна


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()