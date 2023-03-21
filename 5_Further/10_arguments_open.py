"""
Пример открытия файла, название которого передается в качестве аргумента командной строки
Данный файл нужно запустить с аргументами командной строки
python3 9_arguments.py arg1 arg2 arg3
"""
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета многострочного редактируемого текста QTextEdit,
класса слоев с вертикальной организацией виджетов QVBoxLayout.
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
        self.editor = QTextEdit()  # создание экземпляра виджета многострочного текстового поля
        filename = sys.argv[-1]  # запись в переменную имени файла
        self.open_file(filename)  # вызов метода для открытия файла и передачи его содержимого в текстовое поле
        self.setCentralWidget(self.editor)  # размещение контейнера в главном окне приложения
        self.setWindowTitle('Text viewer')  # присвоение имени главному окну приложения

    def open_file(self, fn: str) -> None:
        """
        Метод открытия файлов
        """
        with open(fn, 'r') as f:  # открытие файла на чтение
            text = f.read()  # чтение строк из файла
        self.editor.setPlainText(text)  # размещение текста в текстовом поле


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