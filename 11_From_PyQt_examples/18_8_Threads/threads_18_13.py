"""
Пример многопоточного приложения.
Окно приложения остается активным (не блокируется) при выполнении нагрузки в потоке.
"""

import sys

from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import (QThread,
                            Signal,
                            Qt,
                            )

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication,
класса ярлыка QLabel, класса главных окон QMainWindow, класса кнопок QPushButton,
класса контейнера с вертикальным расположение виджетов QVBoxLayout,
класса виджета кнопки QPushButton, класса слоев с вертикальной организацией виджетов QVBoxLayout,


Импорт из модуля PySide6.QtCore класса потоков QThread, класса набора аттрибутов и настроек Qt,
класс сигналов Signal
"""


class MyThread(QThread):
    """
    Класс потока от супер класс потоков
    """
    mysignal = Signal(str)  # создание экземпляра сигнала, которые принимает строку

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор класс потока.
        :param parent: Ссылка на родительский объект.
        """
        QThread.__init__(self, parent)  # явный вызов конструктора родительского класса

    def run(self) -> None:
        """
        Метод, содержащий код для выполнения в отдельном потоке
        :return: None
        """
        for i in range(1, 21):  # цикл для эмуляции нагрузки
            self.sleep(3)  # эмуляция продолжительной нагрузки засыпанием на 3 секунды
            self.mysignal.emit(f'i = {i}')  # генерация сигнала из потока с передачей текущего значения переменной


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор класса главного окна приложения.
        :param parent: Ссылка на родительский объект.
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Многопоточное приложение')  # установка заголовка главного окна
        self.label = QLabel('Нажмите кнопку для запуска потока')  # создание ярлыка с надписью
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # установка параметров выравнивания
        self.button = QPushButton('Запустить поток')  # создание кнопки с надписью
        self.vbox = QVBoxLayout()  # создание слоя для виджетов с вертикальной организацией
        self.vbox.addWidget(self.label)  # размещение ярлыка в слое для виджетов
        self.vbox.addWidget(self.button)  # размещение кнопки в слое для виджетов
        self.widget = QWidget()  # создание контейнера для слоев с виджетами
        self.widget.setLayout(self.vbox)  # размещение слоя для виджетов в контейнере для слоев
        self.setCentralWidget(self.widget)  # размещение контейнера в главном окне приложения
        self.mythread = MyThread()  # создаем поток
        self.button.clicked.connect(self.on_clicked)  # назначение слота обработчика сигналу на нажатие кнопки
        self.mythread.started.connect(self.on_started)  # назначение слота обработчика сигналу на запуск потока
        self.mythread.finished.connect(self.on_finished)  # назначение слота обработчика сигналу о завершении потока
        self.mythread.mysignal.connect(self.on_change, Qt.ConnectionType.QueuedConnection)  # назначение слота
        # обработчика сигналу об изменении потоков с указанием, что сигнал помещается в очередь обработки
        # событий и обработчик должен выполняться в основном потоке приложения

    def on_clicked(self) -> None:
        """
        Слот обработчик сигнала о нажатии кнопки на запуск потока
        :return: None
        """
        self.button.setDisabled(True)  # делаем кнопку не активной
        self.mythread.start()  # запускаем поток

    def on_started(self) -> None:
        """
        Обработчик сигнала на запуск потока
        :return: None
        """
        self.label.setText('Выполнение потока начато')  # изменение надписи ярлыка

    def on_finished(self) -> None:
        """
        Обработчик сигнала о завершении выполнения потока
        :return: None
        """
        self.label.setText('Выполнение потока завершено') # изменение надписи ярлыка
        self.button.setDisabled(False)  # активируем кнопку запуска потока

    def on_change(self, s: str) -> None:
        """
        Обработчик сигнала из выполняемого потока
        :param s: str - данные, передаваемы сигналом из потока
        :return: None
        """
        self.label.setText(s)  # вывод данных сигнала на ярлык


if __name__ == '__main__':  # условие для предотвращения запуска кода верхнего уровня при импортировании данного модуля
    app = QApplication(sys.argv)  # создание основного цикла событий главного окна
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.resize(300, 70)  # установка размеров окна по умолчанию
    window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
