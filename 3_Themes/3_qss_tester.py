"""
Пример использования QSS (Qt Style Sheets) правил для изменения стилей виджетов

В окно текстового редактора нужно вставить одно или несколько из правил.
1:
QLabel { background-color: yellow }

2:
QLineEdit { background-color: rgb(255, 0, 0) }

3:
QLineEdit {
border-width: 7px;
border-style: dashed;
border-color: red;
}

Перечень виджетов с настраиваемыми стилями и правила стилей (параметры и примеры) см по ссылке:
https://doc.qt.io/qt-5/stylesheet-reference.html
"""

import sys
from PySide6.QtWidgets import (QApplication,
                               QCheckBox,
                               QComboBox,
                               QLabel,
                               QLineEdit,
                               QMainWindow,
                               QPlainTextEdit,
                               QPushButton,
                               QSpinBox,
                               QVBoxLayout,
                               QWidget
                               )

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, a также набора простых виджетов для демонстрации.
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложений от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # Явный вызов конструктора родительского класса
        self.setWindowTitle('QSS Tester')  # присвоение названия главному окну приложения
        self.editor = QPlainTextEdit()  # создание экземпляра виджета поля многострочного редактируемого текста
        self.editor.textChanged.connect(self.update_style)  # создание сигнала на редактирование
        # текста с привязкой ресивера
        self.layout = QVBoxLayout()  # создание экземпляра слоев для виджетов с вертикальным расположением виджетов
        self.layout.addWidget(self.editor)  # размещение виджета на слое
        self.cb = QCheckBox('Checkbox')  # создание экземпляра виджета чекбокса
        self.layout.addWidget(self.cb)
        self.combo = QComboBox()  # создание экземпляра виджета выпадающего списка
        self.combo.addItems(['First', 'Second', 'Third', 'Fourth'])  # добавление элементов в список
        self.layout.addWidget(self.combo)
        self.sp = QSpinBox()  # создание экземпляра виджета спинбокса
        self.sp.setRange(0, 100)  # установка диапазона значений спинбокса
        self.layout.addWidget(self.sp)
        self.label = QLabel('This is label')  # создание ярлыка с надписью
        self.layout.addWidget(self.label)
        self.le = QLineEdit()  # создание экземпляра однострочного редактируемого текстового поля
        self.le.setObjectName('mylineedit')  # присвоение имени объекту
        self.layout.addWidget(self.le)
        self.pb = QPushButton('Push me!')  # создание экземпляра виджета кнопки с надписью
        self.layout.addWidget(self.pb)
        self.container = QWidget()  # создание контейнера для слоя из класса базового виджета
        self.container.setLayout(self.layout)  # помещение слоя с виджетами в контейнер
        self.setCentralWidget(self.container)  # размещение контейнера слоя в главном окне приложения

    def update_style(self) -> None:
        qss = self.editor.toPlainText()  # чтение текста из текстового поля и присвоение его переменной
        self.setStyleSheet(qss)  # применение правила к таблице стилей


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # Создание экземпляра класса основного цикла событий приложения.
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    # можно применять к главному окну в конструкторе
    window = MainWindow()  # Создание главного окна приложения.
    window.show()  # Метод вывода главного окна приложения (по умолчанию окно спрятано).
    app.exec()  # Запуск основного цикла событий главного окна приложения.


if __name__ == '__main__':  # Данное условие предотвращает запуск кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня
