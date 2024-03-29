"""
Пример создания поверхности для отображения растровой графической информации (холста для рисования).
Пример использования текста на поверхности для рисования.
"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QPainter, QPen, QColor, QFont

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtCore и класса Qt - содержит различные идентификаторы, используемые
в библиотеке Qt. 
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета ярлыка QLabel.
Импорт из модуля PySide6.QtGui класса поверхности для графических изображений QPixmap,
класса виджета для рисования QPainter, класс для установки размера пера (толщины линии)
и цвета для рисования QPen, класс объекта цветов QColor, класс для создания текста QFont.  
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласса главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.label = QLabel()  # создание экземпляра класса виджета ярлыка
        self.canvas = QPixmap(400, 300)  # создание поверхности для графической информации - холста для рисования
        self.canvas.fill(Qt.GlobalColor.white)  # заполнение холста белым цветом
        self.label.setPixmap(self.canvas)  # привязка холста к ярлыку для отображения содержимого холста
        self.setCentralWidget(self.label)  # размещение ярлыка в главном окне приложения
        self.draw_something()  # вызов метода рисования

    def draw_something(self) -> None:
        """
        Метод рисования
        :return: None
        """
        painter = QPainter(self.canvas)  # создание экземпляра класса виджета для рисования
        pen = QPen()  # создание экземпляра класса пера для рисования
        pen.setWidth(1)  # установка толщины пера, для текста ширина пера не имеет эффекта
        pen.setColor(QColor('green'))  # установка цвета пера
        painter.setPen(pen)  # применение настроек пера к рисовальщику
        font = QFont()  # создаем экземпляр класса для рисования текста
        font.setFamily('Times')  # установка шрифта
        font.setBold(True)  # установка жирности шрифта
        font.setPointSize(40)  # установка размера шрифта
        painter.setFont(font)  # применение настроек шрифта к рисовальщику
        painter.drawText(100, 100, 'Hello world!!!')  # рисование текста, первые два числа координаты ЛНУ строки
        painter.drawText(200, 200, 100, 100, Qt.AlignHCenter, 'Hello world!!!')  # рисование текста, первые два числа
        # координаты ЛНУ строки, вторые - ширина и высота текстового поля, далее флаг выравнивания
        painter.end()  # подача команды на завершение рисования, закрытие рисовальщика и сохранения изменений
        self.label.setPixmap(self.canvas)  # после завершения рисования холст должен быть передан на отображение


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # вызов метода, устанавливающего видимость окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла главного окна приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуски кода верхнего уровня при
    # импортировании данного файла как модуля
    main()
