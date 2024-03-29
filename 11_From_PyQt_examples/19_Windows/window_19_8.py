"""
Пример работы с палитрой цветов окна на примере изменения цвета фона

Изменить цвет фона окна (или компонента) можно через его палитру. Палитра - это набор
цветов для различных составных частей и состояний окна.
Получить текущую палитру окна позволяет его метод palette(). Палитра возвращается
в виде объекта класса QPalette из модуля QtGui.
Чтобы изменить цвет для какой-либо роли и состояния, следует воспользоваться методом
setColor() палитры. Формат метода: sеtСоlоr([<Состояние>,]<Составная часть окна>, <Цвет>)
Состояние окна указывается в виде одного из следующих элементов перечисления
ColorGroup из класса QPalette:
♦ Active и Normal -окно активно;
♦ Disabled -окно недоступно;
♦ Inactive -окно неактивно.
Составная часть окна задается в виде одного из элементов перечисления ColorRole из класса
QPalette. Так, элемент Window (или Background) обозначает фон окна, а элемент
WindowТext (или Foreground)- текста. Полный список элементов перечисления ColorRole
имеется по интернет-адресу https://doc.qt.io/qt-6/qpalette.html#ColorRole-enum.
Цвет указывается в виде элемента перечисления GlobalColor из модуля QtCore.Qt (скажем,
black) или объекта класса QColor (например, QColor("red"), QColor("#ff0000"), QColor(255,
О, О) и др.).
После настройки палитры необходимо вызвать метод setPalette (<Палитра>) окна и передать
этому методу измененный объект палитры. Следует помнить, что компоненты потомки
по умолчанию имеют прозрачный фон и не перерисовываются автоматически.
Чтобы включить перерисовку, необходимо передать значение True методу
setAutoFillBackground (<Флаг>) окна.
Изменить цвет фона также можно с помощью СSS-атрибута background-color. Для этого
следует передать таблицу стилей в метод setStyleSheet (<Таблица стилей>) компонента.
Таблицы стилей могут быть внешними (подключение через командную строку), установленными
на уровне программы (с помощью метода setStyleSheet () класса QApplication)
или установленными на уровне компонента (с помощью метода setStyleSheet() класса
QWidget). Атрибуты, установленные последними, обычно перекрывают значения аналогичных
атрибутов, указанных ранее.
Создадим окно с надписью. У активного окна установим зеленый цвет, а у неактивного -
красный. Цвет фона надписи сделаем белым. Для изменения фона окна используем палитру,
а для изменения цвета фона надписи -СSS-атрибут background-color
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel,
                               QVBoxLayout,
                               QWidget)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса ярлыка QLabel, класса слоев для виджетов с вертикальной организацией QVBoxLayout,
класс базового пустого виджета QWidget

Импорт из модуля PySide6.QtCore класса аттрибутов для настройки и управления виджетами Qt.

Импорт из модуля PySide6.QtGui класса палитр QPalette, класса объекта цвета QColor
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.resize(300, 100)  # установка исходного размера окна
        self.setWindowTitle('Изменение цвета фона окна')  # установка заголовка окна
        pal = self.palette()  # извлечение текущей палитры окна
        pal.setColor(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, QColor('#008800'))
        # изменение цвета фона активного окна
        pal.setColor(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, QColor('#ff0000'))
        # изменение цвета фона неактивного окна
        self.setPalette(pal)  # передача измененной палитры методу установки палитры
        self.lbl = QLabel('Текст надписи')  # создание ярлыка с надписью
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # установка настроек выравнивание надписи
        self.lbl.setStyleSheet('background-color: #afffff; color: "red"')
        # установка цвета фона ярлыка и цвета надписи
        self.lbl.setAutoFillBackground(True)  # включение автоматической перерисовки компонентов в окне
        self.vbox = QVBoxLayout()  # создание слоя для виджетов
        self.vbox.addWidget(self.lbl)  # размещение ярлыка на слое
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера для виджетов в главном окне приложения


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()

