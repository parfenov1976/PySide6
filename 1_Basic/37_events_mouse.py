"""
Пример использования событий для отслеживания действий мышью.
"""
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Qt из модуля PySide6.QtCore содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса ярлыка QLabel, класса базового пустого виджета QWidget (данный класс 
импортирован, чтобы работало документирование, сами ручки работает и без этого импорта).

Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса виджета главного окна.
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Mouse evnet app')  # присваивает имя главному окну приложения
        self.label = QLabel('Click on this window!')  # создает виджет ярлыка с надписью
        self.setMouseTracking(True)  # устанавливаем флаг для отслеживания движения мыши даже когда не зажата кнопка
        self.setCentralWidget(self.label)  # размещаем виджет ярлыка в главном окне приложения

    def mouseMoveEvent(self, event: QWidget.mouseMoveEvent) -> None:
        """
        Метод обработчик событий PySide6.QtGui.QMouseEvent, отрабатывающий перемещения мыши
        :param: event - событие специального обработчика событий мыши
        :return: None
        """
        self.label.setText('mouseMoveEvent')  # заменяем текст в ярлыке при вызове обработчика

    def mousePressEvent(self, event: QWidget.mouseMoveEvent) -> None:
        """
        Метод обработчик событий PySide6.QtGui.QMouseEvent, отрабатывающий нажатие кнопки мыши
        :param: event - событие специального обработчика событий мыши
        :return: None
        """
        print(event)
        if event.button() == Qt.LeftButton:
            self.label.setText('mousePressEvent LEFT')
        elif event.button() == Qt.MiddleButton:
            self.label.setText('mousePressEvent MIDDLE')
        elif event.button() == Qt.RightButton:
            self.label.setText('mousePressEvent RIGHT')
        elif event.button() == Qt.BackButton:
            self.label.setText('mousePressEvent BACK')
        elif event.button() == Qt.ForwardButton:
            self.label.setText('mousePressEvent FORWARD')

    def mouseReleaseEvent(self, event: QWidget.mouseMoveEvent) -> None:
        """
        Метод обработчик событий PySide6.QtGui.QMouseEvent, отрабатывающий отпускание кнопки мыши
        :param: event - событие специального обработчика событий мыши
        :return: None
        """
        if event.button() == Qt.LeftButton:
            self.label.setText('mouseReleaseEvent LEFT')
        elif event.button() == Qt.MiddleButton:
            self.label.setText('mouseReleaseEvent MIDDLE')
        elif event.button() == Qt.RightButton:
            self.label.setText('mouseReleaseEvent RIGHT')
        elif event.button() == Qt.BackButton:
            self.label.setText('mouseReleaseEvent BACK')
        elif event.button() == Qt.ForwardButton:
            self.label.setText('mouseReleaseEvent FORWARD')

    def mouseDoubleClickEvent(self, event: QWidget.mouseMoveEvent) -> None:
        """
        Метод обработчик событий PySide6.QtGui.QMouseEvent, отрабатывающий двойное нажатие кнопки мыши
        :param: event - событие специального обработчика событий мыши
        :return: None
        """
        if event.button() == Qt.LeftButton:
            self.label.setText('mouseDoubleClickEvent LEFT')
        elif event.button() == Qt.MiddleButton:
            self.label.setText('mouseDoubleClickEvent MIDDLE')
        elif event.button() == Qt.RightButton:
            self.label.setText('mouseDoubleClickEvent RIGHT')
        elif event.button() == Qt.BackButton:
            self.label.setText('mouseDoubleClickEvent BACK')
        elif event.button() == Qt.ForwardButton:
            self.label.setText('mouseDoubleClickEvent FORWARD')


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # методы вывода главного окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла событий главного окна приложения


if __name__ == '__main__':  # эта конструкция предотвращает запуск кода верхнего уроня приложения
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
