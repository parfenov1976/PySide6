"""
Основные компоненты интерфейса. Поля для ввода целых и вещественных чисел

Для ввода целых чисел предназначен класс QSpinBox, для ввода вещественных чисел -
класс QDoubleSpinBox. Эти поля могут содержать две кнопки, которые позволяют щелчками
мыши увеличивать и уменьшать значение внутри поля.
Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QAbstractSpinBox - QSpinBox
(QObject, QPaintDevice) - QWidget - QAbstractSpinBox - QDoubleSpinBox
Форматы конструкторов классов QSpinBox и QDoubleSpinBox:
QSpinBox([parent=None])
QDoubleSpinBox([parent=None])
Классы QSpinBox и QDoubleSpinBox наследуют следующие методы из класса
QAbstractSpinBox (здесь приведены только основные - полный их список смотрите на
странице https://doc.qt.io/qt-6/qabstractspinbox.html):
♦ setButtonSymbols(<Режим>) - задает режим отображения кнопок, предназначенных для
  изменения значения поля. Можно указать следующие элементы перечисления
  ButtonSymbols из класса QAbstractSpinBox:
  • UpDownArrows - отображаются кнопки со стрелками;
  • PlusMinus - отображаются кнопки с символами + и -. Обратите внимание, что при использовании
    некоторых стилей это значение может быть проигнорировано;
  • NoButtons - кнопки не отображаются;
♦ setCorrectionMode(<Режим>) - задает режим преобразования введенных вручную недопустимых
  значений в допустимые в виде одного из следующих элементов перечисления
  CorrectionMode из класса QAbstractSpinBox:
  • CorrectToPreviousValue - преобразовывать в предыдущее допустимое значение;
  • CorrectToNearestValue - преобразовывать в ближайшее допустимое значение;
♦ setAccelerated(<Флаг>) - если в качестве параметра указано значение True, то при удержании
  какой-либо из кнопок нажатой скорость смены значений в поле увеличится;
♦ setAlignment(<Режим>) - задает режим выравнивания значения внутри поля;
♦ setWrapping(<Флаг>) - если в качестве параметра указано значение True, то значение
  внутри поля будет при нажатии кнопок изменяться по кругу: максимальное значение
  сменится минимальным и наоборот;
♦ setSpecialValueText(<Строка>) - задает строку, которая будет отображаться внутри
  поля вместо минимального значения;
♦ setReadOnly(<Флаг>) - если в качестве параметра указано значение True, поле будет
  доступно ТОЛЬКО для чтения;
♦ setFrame(<Флаг>) - если в качестве параметра указано значение False, поле будет
  отображаться без рамки;
♦ stepDown() - уменьшает значение на одно приращение. Метод является слотом;
♦ stepUp() - увеличивает значение на одно приращение. Метод является слотом;
♦ stepBy(<Количество>) - увеличивает (при положительном значении) или уменьшает
  (при отрицательном значении) значение поля на указанное количество приращений;
♦ text() - возвращает текст, содержащийся внутри поля;
♦ clear() - очищает поле. Метод является слотом;
♦ selectAll() - выделяет все содержимое поля. Метод является слотом.

Класс QAbstractSpinВox поддерживает сигнал editingFinished(), который генерируется
при потере полем фокуса ввода или при нажатии клавиши <Enter>.
Классы QSpinBox и QDouЬleSpinBox поддерживают следующие методы (здесь приведены
только основные - полные их списки доступны на страницах https://doc.qt.io/qt-6/
qspinbox.html и https://doc.qt.io/qt􀃜6/qdoublespinbox.html соответственно):
♦ setValue(<Число>) - задает значение поля. Метод является слотом, принимающим,
  в зависимости от компонента, целое или вещественное значение;
♦ value() - возвращает целое или вещественное число, содержащееся в поле;
♦ cleanText() - возвращает целое или вещественное число в виде строки, без дополнительного
  текста, заданного методами setPrefix() и setSuffix(), начальных и конечных
  пробелов;
♦ setRange(<Минимум>, <Максимум>) - задает минимальное и максимальное допустимые
  значения;
♦ setMinimum (<Минимум>) - задает минимальное значение;
♦ setMaximum (<Максимум>) - задает максимальное значение;
♦ setPrefix(<Текст>) - задает текст, который будет отображаться внутри поля перед значением;
♦ setSuffix(<Текст>) - задает текст, который будет отображаться внутри поля после значения;
♦ setSingleStep(<Число>) - задает число, которое будет прибавляться или вычитаться из
  текущего значения поля на каждом шаге.
Класс QDoubleSpinBox также поддерживает метод setDecimals(<Количество>), который задает
количество цифр после десятичной точки.
Классы QSpinВox и QDouЬleSpinBox поддерживают сигналы valueChanged(<Целое число>)
(в классе. QSpinBox), valueChanged(<Вещественное число>) (в классе QDoubleSpinBox) и
textChanged(<Строка>), которые генерируются при изменении значения внутри поля. Внутри
обработчика через параметр доступно новое значение в виде числа или строки.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QSpinBox,
                               QDoubleSpinBox,
                               QLabel,
                               QVBoxLayout,
                               QWidget,
                               QFrame,
                               )
from PySide6.QtCore import Qt
"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, класса виджета поля для
ввода целых чисел QSpinBox, класса виджета поля для ввода вещественных чисел QDoubleSpinBox,
класса виджета ярлыка QLabel, класса вертикальной стопки для виджетов QVBoxLayout, базового 
класса пустого виджета QWidget, класса рамки для виджетов QFrame

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt
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
        self.setWindowTitle('Поля для ввод чисел')  # установка заголовка главного окна приложения
        self.resize(300, 300)  # установка исходного размера окна
        self.spin_box = QSpinBox()  # создание поля для ввода целых чисел
        self.spin_box.setWrapping(True)  # установка режима перебора значений по кругу
        self.spin_box.setSpecialValueText('0 это минимум')  # установка сообщения для минимального значения
        self.spin_box.setValue(5)  # установка значения в поле
        self.spin_box.setRange(0, 10)  # установка диапазона значений поля
        self.spin_box.setSingleStep(1)  # установка величины приращения
        self.spin_box.setPrefix('Деньги  ')  # установка префикса перед значением
        self.spin_box.setSuffix('  руб')  # Установка суффикса после значения
        self.lbl_1 = QLabel()  # создание ярлыка для отображения значения
        self.lbl_1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания в ярлыке
        self.lbl_1.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)  # создание рамки вокруг ярлыка
        self.lbl_2 = QLabel()  # создание ярлыка для отображения значения
        self.lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания в ярлыке
        self.lbl_2.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Plain)  # создание рамки вокруг ярлыка
        self.spin_box.editingFinished.connect(self.spin_box_value_output)  # привязка обработчика
        # к сигналу о завершении ввода
        self.spin_box.valueChanged.connect(self.spin_box_value_changed)
        self.double_spin_box = QDoubleSpinBox()  # создание поля для ввода вещественных чисел
        self.double_spin_box.setDecimals(2)  # установка количества десятичных нулей
        self.double_spin_box.setSingleStep(0.01)  # установка величины приращения
        self.double_spin_box.setButtonSymbols(QDoubleSpinBox.ButtonSymbols.PlusMinus)
        self.double_spin_box.setFrame(False)

        self.vbox = QVBoxLayout()  # создание вертикальной стопки для виджетов
        self.vbox.addWidget(QLabel('Поле для ввода целых чисел'))  # добавление виджета в стопку
        self.vbox.addWidget(self.spin_box)
        self.vbox.addWidget(QLabel('Отображение значения по завершении ввода'))
        self.vbox.addWidget(self.lbl_1)
        self.vbox.addWidget(QLabel('Отображение изменения значения'))
        self.vbox.addWidget(self.lbl_2)
        self.vbox.addWidget(QLabel('Поле для вещественных чисел чисел'))
        self.vbox.addWidget(self.double_spin_box)

        self.container = QWidget()  # создание контейнера для стопок с виджетами
        self.container.setLayout(self.vbox)  # добавление стопки в контейнер
        self.setCentralWidget(self.container)  # добавление контейнера в главное окно приложения

    def spin_box_value_output(self) -> None:
        """
        Обработчик сигнала на завершение ввода
        :return: None
        """
        self.lbl_1.setText(self.spin_box.cleanText())  # перенос чистого текста на ярлык

    def spin_box_value_changed(self, value: int) -> None:
        """
        Обработчик сигнала на изменение значения в поле
        :param value: int - значение поля ввода
        :return: None
        """
        self.lbl_2.setText(str(value))  # перенос значения в ярлык с преобразованием в текст


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
