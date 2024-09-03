"""
Работа с графикой. Вспомогательные классы. Класс QPolygon: многоугольник

Класс QPolygon описывает координаты вершин многоугольника. Форматы конструктора
класса:
QPolygon()
QPolygon(<Список с координатами вершин QPoint>)
QPolygon(<Прямоугольник QRect>[, closed=False])
QPolygon(<Количество вершин>)
QPolygon(<Исходный многоугольник QPolygon>)
Первый формат создает многоугольник, не имеющий вершин. Заполнить его координатами
вершин можно с помощью оператора <<. Пример:
polygon = QtGui.QPolygon()
polygon << QtCore.QPoint(20, 50) << QtCore.QPoint(280, 50)
polygon << QtCore.QPoint(150, 280)
Во втором формате указывается список с координатами отдельных вершин:
polygon = QtGui.QPolygon([QtCore.QPoint(20, 50), QtCore.QPoint(280, 50), QtCore.QPoint(150, 280)])
Третий формат создает многоугольник, имеющий вид заданного прямоугольника. Если параметр
closed имеет значение False, то созданный многоугольник не будет замкнут, а если значение True
- то будет замкнут.
В четвертом формате можно указать количество вершин, а затем задать координаты путем
присваивания значения по индексу:
polygon = QtGui.QPolygon(З) НЕ РАБОТАЕТ в PySide6!!!
polygon[0] = QtCore.QPoint(20, 50)  РАБОТАЕТ, НО ВЫДАЕТ ПРЕДУПРЕЖДЕНИЕ!!!
polygon[1] = QtCore.QPoint(280, 50)
polygon[2] = QtCore.QPoint(150, 280)
Пятый конструктор создает копию заданного исходного объекта.
Класс QPolygon поддерживает следующие методы (здесь приведены только основные -
полный их список можно найти на странице https://doc.qt.io/qt-6/qpolygon.html):
♦ setPoints() - устанавливает координаты вершин. Ранее установленные значения удаляются.
  Форматы метода: НЕТ В PySide6
  setPoints(<Список с координатами вершин QPoint>)
  setPoints(<X1>, <Y1>[, . . ., <Xn>, <Yn>])
  Пример указания значений:
  polygon = QtGui.QPolygon()
  polygon.setPoints([20,50, 280,50, 150,280])
♦ prepend(<Вершина QPoint>) - добавляет новую вершину в начало объекта;
♦ append(<Вершина QPoint>) - добавляет новую вершину в конец объекта. Добавить вершину
  можно также с помощью операторов << и +=;
♦ insert(<Индекс>, <Вершина QPoint>) - добавляет новую вершину в позицию с указанным
  индексом;
♦ setPoint() -задает координаты вершины с указанным индексом. Форматы метода:
  setPoint(<Индекс>, <Вершина QPoint>)
  setPoint(<Индекс>, <Х>, <У>)
  Также можно задать координаты путем присваивания значения по индексу:
  polygon = QtGui.QPolygon(З)
  polygon.setPoint(O, QtCore.QPoint(20, 50))
  polygon.setPoint(1, 280, 50)
  polygon[2] = QtCore.QPoint(150, 280)
♦ point(<Индекс>) - возвращает объект класса QPoint с координатами вершины, индекс
  которой указан в параметре. Получить значение можно также с помощью операции доступа
  по индексу, например:
  polygon = QtGui.QPolygon([20,50, 280,50, 150,280])
  print(polygon.point(O))   # PyQt6.QtCore.QPoint(20, 50)
  print(polygon[1])         # PyQt6.QtCore.QPoint(280, 50)
♦ remove(<Индекс>[, <Количество>]) - удаляет указанное количество вершин, начиная
  с индекса <Индекс>. Если второй параметр не указан, удаляется одна вершина.
  Удалить вершину можно также с помощью оператора del по индексу или срезу;
♦ clear() - удаляет все вершины;
♦ size() - возвращает количество вершин;
♦ count([<Координаты QPoint>]) - возвращает количество вершин. Если указан параметр
  <Координаты>, возвращается только количество вершин с этими координатами.
  Получить количество вершин можно также с помощью функции len();
♦ isEmpty() - возвращает значение True, если многоугольник не содержит ни одной вершины,
  и False - в противном случае;
♦ boundingRect() - возвращает объект класса QRect с координатами и размерами прямоугольной
  области, в которую вписан многоугольник.
    ПРИМЕЧАНИЕ
    Класс QPolygon предназначен для работы с целыми числами. Чтобы работать с вещественными
    числами, необходимо использовать класс QPolygonF.
"""

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QBrush,
                           QPen,
                           QPolygon,
                           )
from PySide6.QtCore import (Qt,
                            QRect,
                            QPoint,
                            )

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса пера QPen, класса инструментов для рисования QPainter,
класса кисти QBrush, класса многоугольника QPolygon

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt, класса прямоугольника QRect,
класса точки c координатами QPoint
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
        self.setWindowTitle('Класс объекта кисти QBrush')  # установка заголовка главного окна
        self.resize(300, 300)  # установка исходного размера главного окна

    def paintEvent(self, event) -> None:
        """
        Обработчик события рисования
        :param event: событие рисования
        :return: None
        """
        painter = QPainter(self)  # создание объекта рисовальщика с подключением поверхности рисования
        black = Qt.GlobalColor.black  # создание объекта цвета из глобального перечислителя цветов
        white = Qt.GlobalColor.white  # создание объекта цвета из глобального перечислителя цветов
        red = Qt.GlobalColor.red  # создание объекта цвета из глобального перечислителя цветов
        painter.setPen(QPen(black))  # создание пера с настройками и установка пера в рисовальщик
        painter.setBrush(QBrush(white))  # создание и применение кисти для заливки фигур к рисовальщику
        painter.drawRect(3, 3, 294, 294)  # рисование прямоугольника
        painter.setPen(QPen(red, 5))  # установка настроек пера в рисовальщик

        polygon_1 = QPolygon((QPoint(20, 20), QPoint(20, 70), QPoint(70, 70)))  # создание многоугольника по
        # списку / кортежу с объектами точек
        polygon_1.prepend(QPoint(50, 20))  # добавление вершины в начало списка
        painter.drawPolygon(polygon_1)  # рисование многоугольника

        polygon_2 = QPolygon(QRect(100, 20, 50, 50), closed=False)  # создание многоугольника из объекта прямоугольника
        polygon_2.insert(2, QPoint(125, 45))  # добавление вершины по индексу
        painter.drawPolygon(polygon_2)

        polygon_3 = QPolygon([QPoint()] * 3)  # не совсем работает создание по количеству вершин
        polygon_3[0] = QPoint(200, 20)  # установка координаты вершины
        polygon_3[1] = QPoint(225, 70)
        polygon_3[2] = QPoint(175, 70)
        polygon_3.append(QPoint(200, 45))  # добавление вершины в конец списка
        painter.drawPolygon(polygon_3)


if __name__ == '__main__':  # проверка условия запуска для предотвращения исполнения
    # кода верхнего уровня при импортировании данного файла как модуля
    from PySide6.QtWidgets import QApplication
    import sys

    """
    Импорт из модуля PySide6.QtWidgets класса управления приложением QApplication
    Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
    к аргументам командной строки. Если использование аргументов командной строки не предполагается,
    то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
    в качестве аргумента передается пустой.
    """
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # включение видимости окна, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла
