"""
Пример использования изображения в качестве фона окна

В качестве фона окна (или компонента) можно использовать изображение. Для этого необходимо
получить текущую палитру компонента с помощью метода palette (), а затем вызвать
метод setBrush() объекта палитры. Формат метода:
setBrush([<Cocтoяниe>, ]<Составная часть окна>, <Кисть QBrush>)

Состояние окна указывается в виде одного из следующих элементов перечисления
ColorGroup из класса QPalette:
♦ Active и Normal -окно активно;
♦ Disabled -окно недоступно;
♦ Inactive -окно неактивно.
Составная часть окна задается в виде одного из элементов перечисления ColorRole из класса
QPalette. Так, элемент Window (или Background) обозначает фон окна, а элемент
WindowТext (или Foreground)- текста. Полный список элементов перечисления ColorRole
имеется по интернет-адресу https://doc.qt.io/qt-6/qpalette.html#ColorRole-enum.

В третьем параметре указывается кисть - объект класса QBrush из модуля QtGui.
Форматы конструктора класса:
QBrush(<Cтиль кисти>)
QBrush(<Цвeт>[, <Стиль киcти>=BrushStyle.SolidPattern])
QBrush(<Цвeт>, <Изображение QPixmap>)
QВrush(<Изображение QPixmap>)
QВrush(<Изображение Qimage>)
QВrush(<Градиент QGradient>)
QBrush(<Oбъeкт класса QBrush>)

В качестве _стиля кисти указывается один из элементов перечисления BrushStyle из модуля
QtCore. Qt: NoBrush, SolidPattern, Dense1Pattern, Dense2Pattern, / Dense3Pattern,
Dense4Pattern, Dense5Pattern, Dense6Pattern, Dense7Pattern, CrossPattern И др. С помощью
этого параметра можно сделать цвет сплошным (solidPattern) или имеющим текстуру
(например, элемент CrossPattern задает текстуру в виде сетки).
Цвет можно задать в виде элемента перечисления GlobalColor из модуля QtCore.Qt (например,
Blасk, white и т. д.) или объекта класса QColor (Например, QColor("red"),
QColor("#ff0000"), QColor(255, 0, 0) и др.). При этом установка сплошного цвета фона
окна может выглядеть так:
pal = window. palette()
pal.setBrush(QtGui.QPalette.ColorGroup.Normal, QtGui.QPalette.ColorRole.Window,
QtGui.QBrush(QtGui.QColor("#008800"), QtCore.Qt.BrushStyle.SolidPattern))
window.setPalette(pal)

Третий, четвертый и пятый форматы позволяют указать изображение в ·виде объекта класса
QPixmap или QImage. Конструкторы этих классов принимают путь к файлу с нужным изображением.
Шестой формат создает новую кисть на основе градиента, представленного объектом класса
QGradient (см. главу 25), а седьмой-на основе указанной кисти.
После настройки палитры у окна также следует вызвать метод setPalette(),
передав ему измененный объект палитры. Следует помнить, что компоненты-потомки по
умолчанию имеют прозрачный фон и не перерисовываются автоматически. Чтобы включить
перерисовку, необходимо передать значение True в метод setAutoFillBackground().
Указать фоновое изображение также можно с помощью СSS-атрибутов background и
background-image. Воспользовавшись СSS-атрибутом background-repeat, можно задать режим
повтора фонового рисунка: repeat (повтор по горизонтали и вертикали), repeat-x
(только по горизонтали), repeat-y (только по вертикали) и no-repeat (не повторяется)
"""
import sys
import os
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel,
                               )
from PySide6.QtGui import QPalette, QBrush, QPixmap
from PySide6.QtCore import Qt, QSize

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Модуль os для извлечения путей операционной системы и работы с путями.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класса ярлыка QLabel

Импорт из модуля PySide6.QtCore класса аттрибутов для настройки и управления виджетами Qt.

Импорт из модуля PySide6.QtGui класса палитр QPalette,класса кистей QBrush,
класса работы с изображениями QPixmap
"""

base = os.path.dirname(__file__)  # извлечение абсолютного пути к данному модулю


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
        self.resize(300, 300)  # установка исходного размера окна
        self.setWindowTitle('Изменение цвета фона окна')  # установка заголовка окна
        pal = self.palette()  # извлечение текущей палитры окна
        pal.setBrush(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window,
                     QBrush(QPixmap(os.path.join(base, 'data', 'background1.jpg'))))
        # установка фона активного окна
        self.setPalette(pal)  # передача измененной палитры методу установки палитры
        self.lbl = QLabel('Текст надписи', self)  # создание ярлыка с надписью
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        # установка настроек выравнивание надписи
        self.lbl.setStyleSheet('background-color: #afffff; color: "red"')
        # установка цвета фона ярлыка и цвета надписи
        self.lbl.resize(QSize(100, 100))  # установка размера ярлыка
        self.lbl.setStyleSheet(r'background-image: url(data/background2.jpg);')  # установка фонового изображения ярлыка
        self.setAutoFillBackground(True)  # включение автоматической перерисовки компонентов в окне

    def resizeEvent(self, e) -> None:
        """
        Метод обработчик (слот) сигнала на изменение размера окна
        :param e: объект события изменения размера окна QResizeEvent
        :return: None
        """
        self.lbl.move((e.size().width() - 100) / 2, (e.size().height() - 100) / 2)
        # центрирование ярлыка в окне


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
