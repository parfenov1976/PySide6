"""
Пример использования создания диалогового окна с использованием класса виджета диалоговых окон QDialog.
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QDialog,
                               QDialogButtonBox,
                               QVBoxLayout,
                               QLabel)

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета кнопки QPushButton и класса 
виджета диалогового окна QDialog, виджета кнопок диалоговых окон QDialogButtonBox, 
виджета слоев диалогового окна QVBoxLayout, виджета надписей QLabel.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
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
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.button = QPushButton('Press me for a dialog')  # создание кнопки для вызова диалогового окна
        self.button.clicked.connect(self.button_clicked)  # создание сигнала на нажатие кнопки вызова
        # диалогового окна с привязкой метода
        self.setCentralWidget(self.button)  # размещение виджета кнопки в главном окне приложения

    def button_clicked(self, s: bool) -> None:
        """
        Метод ресивер (слот) для создания диалогового окна при нажатии на кнопку его вызова
        :param s:  bool - состояние кнопки, передаваемое сигналом
        :return: None
        """
        print('click', s)  # вывод состояния кнопки
        dlg = CustomDialog(self)  # создание диалогового окна в главном окне приложения
        # dlg = CustomDialog() # в случае, если не передать родителя, то диалоговое окно появится в стороне от главного
        if dlg.exec():
            print('Success')
        else:
            print('Cancel')


class CustomDialog(QDialog):
    """
    Подкласс диалогового окна от супер класса диалоговых окон.
    """
    def __init__(self, parent: QMainWindow = None) -> None:
        """
        Конструктор диалогового окна
        """
        QDialog.__init__(self, parent)  # явный вызов родительского класса
        self.setWindowTitle('Hello!')  # присвоение имени диалоговому окну
        self.buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel  # создание списка кнопок диалогового окна
        # из стандартного пространства имен класса QDialogButtonBox
        self.button_box = QDialogButtonBox(self.buttons)  # создание кнопок диалогового окна из списка
        self.button_box.accepted.connect(self.accept)  # создание сигнала для кнопки OK
        self.button_box.rejected.connect(self.reject)  # создание сигнала для кнопки Cancel
        self.layout = QVBoxLayout()  # создание слоя диалогового окна
        self.message = QLabel('Something happens, is that OK?')  # создание сообщения для диалогового окна
        self.layout.addWidget(self.message)  # добавление сообщения на слой диалогового окна
        self.layout.addWidget(self.button_box)  # добавление кнопок на слой диалогового окна
        self.setLayout(self.layout)  # размещение слоя диалогового окна в экземпляре класса
        # диалогового окна


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QApplication(sys.argv)  # Создание экземпляра класса основного цикла событий главного окна приложения.
    window = MainWindow()  # создание главного окна приложения
    window.show()  # метод вывода главного окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # данная конструкция необходима для предотвращения запуска кода
    # верхнего уровня при импортировании данного файла как модуля
    main()  # вызов функции запуска кода приложения верхнего уровня
