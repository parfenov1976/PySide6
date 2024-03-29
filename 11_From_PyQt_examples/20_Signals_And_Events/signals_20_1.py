"""
Назначение сигналу нескольких обработчиков

Чтобы назначить сигналу обработчик, следует использовать метод connect() компонента.
Форматы вызова этого метода таковы:
<Сигнал>.connect(<Обработчик>[,
                <Тип соединения>=ConnectionType.AutoConnection][, no receiver_check=False])
<Сигнал>[<Тип>] .connect(<Обработчик>[,
                <Тип соединения>=ConnectionType.AutoConnection][, no_receiver_check=False])

В качестве обработчика можно указать:
♦ ссылку на пользовательскую функцию;
♦ ссылку на метод класса;
♦ ссылку на объект класса, в котором определен метод_call_();
♦ анонимную функцию;
♦ ссылку на слот класса.
Остальные два параметра будут описаны позже.
Вот пример назначения функции on_clicked_button() в качестве обработчика сигнала clicked кнопки button:
button.clicked.connect(on_clicked_button)
Сигналы могут принимать произвольное число параметров, каждый из которых может относиться
к любому типу данных. При этом бывает и так, что в классе существуют два сигнала с одинаковыми
наименованиями, но разными наборами параметров. Тогда следует дополнительно в квадратных скобках
указать <Тип> данных, принимаемых сигналом, в виде - либо ссылки на его класс, либо в виде
строкового имени. Например, оба следующих выражения назначают обработчик сигнала, принимающего
один параметр логического типа:
button.clicked[bool] .connect(on_clicked_button)
button.clicked["bool"] .connect(on_clicked_button)
Одному и тому же сигналу можно назначить произвольное количество обработчиков.
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QPushButton,
                               )

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса виджета кнопки QPushButton
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
        self.setWindowTitle('Обработчики сигнала')  # установка заголовка главного окна приложения
        self.setFixedSize(300, 300)  # установка фиксированного размера окна
        self.btn = QPushButton('Нажми меня', self)  # создание экземпляра виджета кнопки
        self.btn.setFixedSize(150, 30)  # установка фиксированных размеров кнопки
        self.btn.move(75, 135)  # смещение кнопки относительно левого верхнего угла окна
        self.btn.clicked.connect(on_clicked)  # назначение сигналу на нажатие кнопки обработчика

        obj = Handler()  # создание экземпляра обработчика сигнала
        self.btn.clicked.connect(obj.on_clicked)  # назначение сигналу на нажатие кнопки обработчика
        # в виде метода класса

        self.btn.clicked.connect(Handler(10))  # назначение обработчика в виде ссылки на объект класса

        self.btn.clicked.connect(lambda: Handler(5)())  # назначение обработчика в виде анонимной функции


class Handler:
    """
    Класс обработчика сигнала
    """

    def __init__(self, x=0) -> None:
        """
        Конструктор обработчика
        """
        self.x = x

    def __call__(self):
        print('Кнопка нажата. Метод Handler.__call__()')
        print(f'x = {self.x}')

    @staticmethod
    def on_clicked():
        print('Кнопка нажата. Метод Handler.on_clicked()')


def on_clicked():
    print('Кнопка нажата. Функция on_clicked()')


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
