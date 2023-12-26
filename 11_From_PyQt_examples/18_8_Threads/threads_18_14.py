"""
Пример многопоточного приложения с управлением потоком - запуск и остановка (пауза)
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
    Класс потока от супер класса потоков
    """
    mysignal = Signal(str)  # создание экземпляра сигнала, которое принимает строку

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор класса потока
        """
        QThread.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.running = False  # атрибут для хранения флага выполнения потока
        self.count = 0  # счетчик секунд работы потока

    def run(self) -> None:
        """
        Метод, содержащий код для выполнения в отдельном потоке
        """
        self.running = True  # изменение флага выполнения потока
        while self.running:  # цикл с проверкой флага выполнения
            self.count += 1  # увеличиваем счетчик
            self.mysignal.emit(f'count = {self.count}')
            self.sleep(1)  # имитируем нагрузку засыпанием на 1 секунду


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent: object = None) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Многопоточное приложение с управлением потоком')  # установка заголовка главного окна
        self.label = QLabel('Нажмите кнопку для запуска потока')  # создание ярлыка с надписью
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # установка флага выравнивания для ярлыка
        self.btn_start = QPushButton('Запустить поток')  # создание кнопки для запуска потока
        self.btn_start.clicked.connect(self.on_start)  # назначение слота обработчика сигналу на нажатие кнопки
        self.btn_stop = QPushButton('Остановить поток')  # создание кнопки для остановки потока
        self.btn_stop.clicked.connect(self.on_stop)  # назначение слота обработчика сигналу на нажатие кнопки
        self.vbox = QVBoxLayout()  # создание слоя для виджетов с вертикальной организацией
        self.vbox.addWidget(self.label)  # размещение в слое виджета ярлыка
        self.vbox.addWidget(self.btn_start)  # размещение в слое виджета кнопки старт
        self.vbox.addWidget(self.btn_stop)  # размещение в слое виджета кнопки стоп
        self.widget = QWidget()  # создание контейнера для слоев с виджетами
        self.widget.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере для слоев
        self.setCentralWidget(self.widget)  # размещение контейнера с виджетами на главном окне приложения
        self.mythread = MyThread()  # создаем поток
        self.mythread.mysignal.connect(self.on_change, Qt.ConnectionType.QueuedConnection)  # назначение слота
        # обработчика сигналу об изменении потоков с указанием, что сигнал помещается в очередь обработки
        # событий и обработчик должен выполняться в основном потоке приложения

    def on_start(self) -> None:
        """
        Слот обработчик сигнала кнопки на запуск потока
        """
        if not self.mythread.isRunning():  # проверка выполнения потока с помощью встроенного метода
            self.mythread.start()  # запуск потока на выполнение

    def on_stop(self):
        """
        Слот обработчика сигнала кнопки на остановку потока
        """
        self.mythread.running = False  # установка флага выполнения на ложь

    def on_change(self, s: str) -> None:
        """
        Обработчик сигнала из выполняемого потока
        :param s: str - данные, передаваемы сигналом из потока
        :return: None
        """
        self.label.setText(s)  # вывод данных сигнала на ярлык

    def closeEvent(self, event: QMainWindow.closeEvent) -> None:
        """
        Обработчик события, вызываемый при закрытии окна
        """
        self.hide()  # скрываем главное окно приложения
        self.mythread.running = False  # меняем флаг выполнения
        self.mythread.wait(5000)  # выделяем время на завершение потока
        event.accept()  # закрываем окно приложения


if __name__ == '__main__':  # проверка условия запуска модуля предотвращает запуск кода после условия при
    # импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий (основного потока) главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.resize(300, 100)  # установка размеров окна по умолчанию
    window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.
    sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
