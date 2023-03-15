"""
Пример подмешивания дополнительных пользовательских данных к встроенным в виджеты сигналам.
"""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса нажимаемой кнопки QPushButton.
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """
    def __init__(self):
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        btn = QPushButton('Press me')  # создание экземпляра класса нажимаемой кнопки
        btn.setCheckable(True)  # настройка кнопки на фиксацию положения (режим переключателя)
        btn.clicked.connect(lambda checked: self.button_clicked(checked, btn))  # создание сигнала на нажатие кнопки
        # с привязкой ресивера через анонимную функцию с передачей в него состояния кнопки и самого объекта кнопки
        self.setCentralWidget(btn)  # размещение в главном окне виджета кнопки

    def button_clicked(self, checked: bool, btn: QPushButton) -> None:
        """
        Метод ресивер (слот) сигнала на нажатие кнопки
        :param checked: bool - состояние кнопки, передаваемое сигналом
        :param btn: QPushButton - объект, передаваемый вместе с сигналом
                                  (подмешанные пользовательские данные)
        :return: None
        """
        print(btn, checked)
        btn.hide()  # метода, вызов которого прячет кнопку


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла главного окна приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # вызов метода главного окна, разрешающего его показ (по умолчанию окно скрыто)
    app.exec()  # запуска основного цикла главного окна приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()
