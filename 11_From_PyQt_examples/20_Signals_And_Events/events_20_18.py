"""
События мыши. Изменение курсора мыши при наведении на объект интерфейса

Для изменения внешнего вида курсора мыши при вхождении его в область компонента
предназначены следующие методы класса QWidget:
♦ setCursor(<Курсор>) - задает внешний вид курсора мыши для компонента. В качестве
  параметра указывается объект класса QCursor или следующие элементы перечисления
  CursorShape из модуля QtCore.Qt:
    ArrowCursor (стандартная стрелка),
    UpArrowCursor (стрелка, направленная вверх),
    CrossCursor (крестообразный курсор),
    WaitCursor (песочные часы),
    IBeamCursor (I-образный курсор),
    SizeVerCursor (стрелки, направленные вверх и вниз),
    SizeHorCursor (стрелки, направленные влево и вправо),
    SizeBDiagCursor (стрелки, направленные в правый верхний угол и левый нижний угол),
    SizeFDiagCursor (стрелки, направленные в левый верхний угол и правый нижний угол),
    SizeAllCursor (стрелки, направленные вверх, вниз, влево и вправо),
    ВlankCursor (невидимый курсор),
    SplitVCursor (указатель изменения высоты),
    SplitHCursor (указатель изменения ширины),
    PointingHandCursor (курсор в виде руки),
    ForBiddenCursor (перечеркнутый круг),
    OpenHandCursor (разжатая рука),
    ClosedHandCursor (сжатая рука),
    WhatsThisCursor (стрелка с вопросительным знаком),
    BusyCursor (стрелка с песочными часами),
    DragMoveCursor (обозначение перемещения путем перетаскивания),
    DragCopyCursor (обозначение копирования путем перетаскивания) и
    DragLinkCursor (обозначение создания ссылку путем перетаскивания).
    Пример:
    self.setCursor(QtCore.Qt.CursorShape.WaitCursor)
♦ unsetCursor()- отменяет изменение курсора мыши для компонента. В результате
  внешний вид курсора будет наследоваться от родителя;
♦ cursor() - возвращает объект класса QCursor, представляющий текущий курсор.
Управлять видом курсора сразу на уровне программы можно с помощью следующих
статических методов класса QApplication:
♦ setOverrideCursor(<Курсор>) - задает курсор мыши. В качестве параметра указывается
  объект класса QCursor или один из ранее описанных элементов перечисления CursorShape
  из модуля QtCore.Qt;
♦ restoreOverrideCursor() - отменяет изменение курсора мыши:
  QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
  # Выполняем длительную операцию
  QtWidgets.QApplication.restoreOverrideCursor()
♦ changeOverrideCursor(<Курсор>) - изменяет курсор мыши. Если до вызова этого метода
  не вызывался метод setOverrideCursor(), ничего не произойдет. В качестве параметра
  указывается объект класса QCursor или один из ранее описанных элементов перечисления
  CursorShape из модуля QtCore.Qt;
♦ overrideCursor() - возвращает объект класса QCursor, представляющий текущий курсор,
  или значение None, если таковой не бьш изменен.
Изменять курсор мыши на уровне программы следует на небольшой промежуток времени -
обычно при выполнения какой-либо операции, в процессе которой программа не может
нормально реагировать на действия пользователя. Обычно курсор изменяют на песочные
часы (элемент WaitCursor) или стрелку с песочными часами (элемент BusyCursor).
Метод setOverrideCursor() может быть вызван несколько раз. В этом случае курсоры
помещаются в стек. Каждый вызов метода restoreOverrideCursor() удаляет последний курсор,
добавленный в стек.Для нормальной работы программы необходимо вызывать методы
setOverrideCursor() и restoreOverrideCursor() одинаковое количество раз.
Класс QCursor позволяет использовать в качестве курсора изображение тобой формы. Чтобы
загрузить изображение, следует передать конструктору класса QPixmap путь к файлу изображения.
Для создания объекта курсора необходимо передать конструктору класса QCursor в первом
параметре объект класса QPixmap, а во втором и третьем параметрах - координаты «горячей»
точки будущего курсора. Вот пример создания и установки пользовательского курсора:
self.setCursor(QtGui.QCursor(QtGui.QPixmap("cursor.png"), О, О))
Класс QCursor поддерживает два статических метода:
♦ pos() - возвращает объект класса QPoint с координатами курсора мыши относительно экрана:
  р = QtGui.QCursor.pos()
  print(p.x(), р.у())
♦ setPos() - задает координаты курсора мыши. Форматы вызова:
  setPos(<X>, <У>)
  sеtРоs(<Координаты QPoint>)
"""
from PySide6.QtWidgets import (QMainWindow,
                               QLabel,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor

"""
Импорт из модуля PySide6.QWidgets класса главных окон QMainWindow, класса виджета ярлыка QLabel
класс виджета кнопки QPushButton, класса слоя для виджетов с их вертикальной организацией QVBoxLayout,
базового класса виджета QWidget

Импорт из модуля PySide6.QtCore класса перечислителя свойств виджетов Qt

Импорт из модуля PySide6.QtGui класса курсора мыши QCursor 
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
        self.setWindowTitle('Изменение курсора мыши')  # установка заголовка главного окна приложения
        self.resize(300, 300)  # установка исходного размера окна
        self.my_cursor = QCursor()  # создание экземпляра курсора мыши
        self.my_cursor.setShape(Qt.CrossCursor)  # изменение формы пользовательского курсора
        self.setCursor(self.my_cursor)  # привязка пользовательского курсора к компоненту интерфейса
        self.lbl = QLabel()  # создание экземпляра виджета ярлыка
        self.lbl.setStyleSheet("background-color:'red'")  # изменение фонового цвета ярлыка
        self.lbl.setText('Стрелка вверх')  # добавление текста на ярлык
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl.setCursor(Qt.CursorShape.UpArrowCursor)  # установка формы курсора мыши при наведении на ярлык
        self.btn = QPushButton('Смена курсора мыши')
        self.btn.clicked.connect(self.on_clicked)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.lbl)
        self.vbox.addWidget(QLabel())
        self.vbox.addWidget(self.btn)
        self.container = QWidget()
        self.container.setLayout(self.vbox)
        self.setCentralWidget(self.container)

    def on_clicked(self):
        if self.cursor().shape() == self.btn.cursor().shape():
            self.btn.setCursor(Qt.CursorShape.WaitCursor)
        else:
            self.btn.unsetCursor()


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    import sys
    from PySide6.QtWidgets import QApplication

    """
    Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
    к аргументам командной строки. Если использование аргументов командной строки не предполагается,
    то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
    в качестве аргумента передается пустой.
    Импорт из модуля PySide6.QWidgets класса управления приложением QApplication.
    """
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
