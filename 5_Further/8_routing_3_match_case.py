"""
Пример с методом маршрутизатором, перенаправляющем события в соответствующий конкретному событию обработчик.
Вариант с использованием конструкции match/case
"""
import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета ярлыка QLabel.
Импорт из модуля PySide6.QtCore класса для создания объектов размеров QSize и класса Qt,
содержащего различные идентификаторы, используемые в библиотеке Qt
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self):
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.label = QLabel('Click in this window')  # создание экземпляра класса ярлыка с надписью
        self.status = self.statusBar()  # записываем в аттрибут для объекта ссылку на метод класс основного окна
        # для вывода сообщений в строку статусов главного окна
        self.setFixedSize(QSize(200, 200))  # Установка фиксированного размера окна, т.е. без возможности изменения
        self.setCentralWidget(self.label)  # размещение ярлыка с надписью в главном окне

    def mouseMoveEvent(self, e) -> None:
        """
        Обработчик событий движения курсора мышки
        (срабатывает только с одновременным нажатием на кнопку мыши)
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: None
        """
        self.label.setText('mouseMoveEvent')

    def mousePressEvent(self, e):
        """
        Метод маршрутизатор для перенаправления события в соответствующий ему обработчик
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: возвращает вызов метода обработчика для конкретного события
        """
        button = e.button()  # извлечение идентификатора нажатой кнопки мыши
        match button:  # проверка случаев нажатия клавиш мыши
            case Qt.LeftButton:  # случай для левой кнопки мыши
                return self.left_mouse_press_event(e)  # возврат вызова обработчика
            case Qt.MiddleButton: # случай для средней кнопки мыши
                self.middle_mouse_press_event(e)  # без return тоже работает
            # case Qt.RightButton:  # случай для правой кнопки мыши
            #     self.right_mouse_press_event(e)  # без return тоже работает
            case _:
                print('Unknown key pressed')
                return 'unknown key pressed'

    def left_mouse_press_event(self, e) -> None:
        """
        Метод обработчик нажатия левой кнопки мыши
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: None
        """
        self.label.setText('mousePressedEvent LEFT')  # смена надписи на ярлыке
        if e.x() < 100:  # извлечение из события координаты Х курсора в момент клика и сравнение с условием
            # <100 клик по левой половине окна, >100 клик по правой половине
            self.status.showMessage('Left click on left')  # вывод сообщения в строку статуса главного окна
            self.move(self.x() - 10, self.y())  # извлечение координат x и y ЛВУ окна и перемещение окна по заданным
            # координатам с приращением
        else:
            self.status.showMessage('Left click on right')
            self.move(self.x() + 10, self.y())  # извлечение координат x и y ЛВУ окна и перемещение окна по заданным
            # координатам с приращением

    def middle_mouse_press_event(self, e):
        """
        Метод обработчик нажатия средней кнопки мыши
        :param e: event из PySide6.QtGui.QMouseEvent содержит события с мыши
        :return: None
        """
        self.label.setText('mousePressedEvent MIDDLE')  # смена надписи на ярлыке

    def right_mouse_press_event(self, e):
        self.label.setText('mousePressedEvent RIGHT')  # смена надписи на ярлыке
        if e.x() < 100:  # извлечение из события координаты Х курсора в момент клика и сравнение с условием
            # <100 клик по левой половине окна, >100 клик по правой половине
            self.status.showMessage('Right click in left')  # вывод сообщения в строку статуса главного окна
            print('Something else here')  # вывод сообщения в терминал
            self.move(10, 10)  # перемещение окна по заданным координатам ЛВУ
        else:
            self.status.showMessage('Right click on right')  # вывод сообщения в строку статуса главного окна
            self.move(400, 400)  # перемещение окна по заданным координатам ЛВУ


def main() -> None:
    """
    Функция запуска кода верхнего уроня приложения
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла главного окна приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # вызов метода вывода окна приложения (по умолчанию окно спрятано)
    app.exec()  # запуска основного цикла главного окна приложения


if __name__ == '__main__':  # данное условие нужно для предотвращения запуска кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
