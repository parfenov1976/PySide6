"""
Блокировка и удаление обработчика сигнала


Для блокировки и удаления обработчиков предназначены следующие методы компонентов:
♦ bloockSignals(<Состояние>) - временно блокирует прием сигналов, если параметр имеет значение тrue,
  и снимает блокировку, если параметр имеет значение False. Метод возвращает предыдущее состояние;
♦ signalsBlocked() - возвращает значение True, если блокировка сигналов установлена, и False -
  в противном случае;
♦ disconnect() - удаляет заданный обработчик. Форматы метода:
<Сигнал>.disconnect([<Обработчик>]) <Сигнал>[<Тип>] .disconnect([<Обработчик>])
Если обработчик не указан, удаляются все обработчики. Параметр <Тип> указывается лишь в том случае,
если существуют сигналы с одинаковыми именами, но принимающие разные параметры. Примеры:
button.clicked.disconnect()
button.clicked[bool].disconnect(on_clicked_button) button.clicked ["bool"]..disconnect(on_clicked_button)
"""

import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import Slot

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса виджета кнопки QPushButton, класс базового пустого виджета QWidget

Импорт из модуля PySide6.QtCore класса декоратора слота Slot
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
        self.setWindowTitle('Блокировка и удаление обработчика')  # присвоение заголовка главному окну приложения
        self.resize(300, 150)  # установка исходного размера окна
        self.btn1 = QPushButton('Нажми меня')  # создание экземпляра виджета кнопки
        self.btn2 = QPushButton('Блокировать')
        self.btn3 = QPushButton('Разблокировать')
        self.btn4 = QPushButton('Удалить обработчик')
        self.btn3.setEnabled(False)  # блокирование кнопки
        self.vbox = QVBoxLayout()  # создание слоя для виджетов
        self.vbox.addWidget(self.btn1)  # размещение виджета кнопки на слое
        self.vbox.addWidget(self.btn2)
        self.vbox.addWidget(self.btn3)
        self.vbox.addWidget(self.btn4)
        self.container = QWidget()  # создание контейнера для слоя с виджетами
        self.container.setLayout(self.vbox)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(self.container)  # размещение в окне контейнера со слоями
        self.btn1.clicked.connect(self.on_clicked_btn1)  # создание сигнала на нажатие кнопки с привязкой обработчика
        self.btn2.clicked.connect(self.on_clicked_btn2)
        self.btn3.clicked.connect(self.on_clicked_btn3)
        self.btn4.clicked.connect(self.on_clicked_btn4)

    @staticmethod
    @Slot()
    def on_clicked_btn1():
        """
        Обработчик сигнала на нажатие кнопки
        """
        print('Нажата кнопка 1')

    @Slot()
    def on_clicked_btn2(self):
        """
        Обработчик сигнала на нажатие кнопки
        """
        self.btn1.blockSignals(True)  # Блокирование сигнала
        self.btn2.setEnabled(False)  # Блокирование кнопки
        self.btn3.setEnabled(True)  # Разблокирование кнопки

    @Slot()
    def on_clicked_btn3(self):
        """
        Обработчик сигнала на нажатие кнопки
        """
        self.btn1.blockSignals(False)  # Блокирование сигнала
        self.btn2.setEnabled(True)  # Разблокирование кнопки
        self.btn3.setEnabled(False)  # Блокирование кнопки

    def on_clicked_btn4(self):
        """
        Обработчик сигнала на нажатие кнопки
        """
        self.btn1.clicked.disconnect(self.on_clicked_btn1)  # отвязка обработчика от сигнала (удаление)
        self.btn2.setEnabled(False)  # Блокирование кнопки
        self.btn3.setEnabled(False)
        self.btn4.setEnabled(False)


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
