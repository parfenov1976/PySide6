"""
Пример использования виджета диалогового окна с уведомлением QMessageBox
и одного из встроенных в него диалогов
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)
parent - данный параметр содержит родительское окно для диалога
(как правило указывается self, т.е. MainWindow)
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QMessageBox)

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета кнопки QPushButton и класса 
виджета диалогового окна диалогового окна уведомлений QMessageBox.
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

    def button_clicked(self) -> None:
        """
        Метод ресивер (слот) для создания диалогового окна при нажатии на кнопку его вызова
        :return: None
        """
        button = QMessageBox.critical(self,
                                      'Oh dear!',
                                      'Something went very wrong.',
                                      buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
                                      defaultButton=QMessageBox.Discard
                                      )  # создание диалогового окна с уведомлением о критической ситуации
        # из набора встроенных методов класса диалоговых окон с уведомлениями

        if button == QMessageBox.Discard:
            print('Discard!')
        elif button == QMessageBox.NoToAll:
            print('No to all')
        else:
            print('Ignore!')


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
