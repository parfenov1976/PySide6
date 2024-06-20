"""
Основные компоненты интерфейса. Круговая шкала с ползунком

Класс QDial реализует круглую шкалу с ползунком, который можно перемещать по кругу
с помощью мыши или клавиатуры. Компонент, показанный ца рис. 22.6, напоминает регулятор,
используемый в различных устройствах для изменения каких-либо настроек. Иерархия
наследования:
(QObject, QPaintDevice) - QWidget - QAbstractSlider - QDial
Формат конструктора класса QDial:
QDial([parent=None])
Класс QDial наследует все методы и сигналы класса QAbstractSlider (здесь приведена
только часть методов - полный их список смотрите на странице https://doc.qt.io/qt-6/qdial.html):
♦ setValue(<Значение>) - задает новое целочисленное значение для шкалы. Метод является
  слотом;
♦ value() - возвращает текущее значение в виде числа;
♦ setSliderPosition(<Положение>) - задает текущее положение ползунка;
♦ sliderPosition() - возвращает текущее положение ползунка в виде числа. Если отслеживание
  перемещения ползунка включено (принято по умолчанию), то возвращаемое
  значение будет совпадать со значением, возвращаемым методом value(). Если отслеживание
  выключено, то при перемещении метод sliderPosition() вернет текущее положение,
  а метод value() - положение, которое имел ползунок до перемещения;
♦ setRange(<Минимум>, <Максимум>) - задает минимальное и максимальное значения,
  представленные целыми числами. Метод является слотом;
♦ setMinimum(<Минимум>) - задает минимальное значение в виде целого числа;
♦ setMaximum(<Максимум>) - задает максимальное значение в виде целого числа;
♦ setOrientation(<Ориентация>) - задает ориентацию шкалы. В качестве значения указываются
  элементы Horizontal (горизонтальная) или Vertical (вертикальная) перечисления
  Orientation из модуля QtCore.Qt. Метод является слотом;
♦ setSingleStep(<Значение>) - задает значение, на которое сдвинется ползунок при нажатии
  клавиш со стрелками;
♦ setPageStep(<Значение>) - задает значение, на которое сдвинется ползунок при нажатии
  клавиш <Page Up> и <Page Down>, повороте колесика мыши или щелчке мышью на
  шкале;
♦ setInvertedAppearance(<Флаг>) - если в качестве параметра указано значение True,
  направление увеличения значения будет изменено на противоположное (например, не
  слева направо, а справа налево - при горизонтальной ориентации);
♦ setInvertedControls(<Флаг>) - если в качестве параметра указано значение False, то
  при изменении направления увеличения значения будет изменено и направление перемещения
  ползунка при нажатии клавиш <Page Up> и <Page Down>, повороте колесика
  мыши и нажатии клавиш со стрелками вверх и вниз;
♦ setTracking(<Флаг>) - если в качестве параметра указано значение True, отслеживание
  перемещения ползунка будет включено (принято по умолчанию). При этом сигнал
  valueChanged() при перемещении ползунка станет генерироваться постоянно. Если в качестве
  параметра указано значение False, то сигнал valueChanged() будет сгенерирован
  только при отпускании ползунка;
♦ hasTracking() - возвращает значение True, если отслеживание перемещения ползунка
  включено, и False - в противном случае.
Класс QAbstractSlider поддерживает сигналы:
♦ actionTriggered(<Действие>) - генерируется, когда происходит взаимодействие с ползунком
  (например, при нажатии клавиши <PgUp>). Внутри обработчика через параметр
  доступно произведенное действие, которое описывается целым числом. Также можно
  использовать следующие элементы перечисления SliderAction из класса
  QAbstractSlider:
  • SliderNoAction - (0) нет взаимодействия с ползунком;
  • SliderSingleStepAdd - (1) увеличение значения путем щелчка на клавише-стрелке
    (какой именно, зависит от указанного направления увеличения значения);
  • SliderSingleStepSub - (2) уменьшение значения путем щелчка на клавише-стрелке;
  • SliderPageStepAdd - (3) увеличение значения путем щелчка на клавише <PgUp> или
    <PgDn> (какой именно, зависит от указанного направления увеличения значения);
  • SliderPageStepSub - (4) уменьшение значения путем щелчка на клавише <PgUp>
    или<PgDn>;
  • SliderToMinimum - (5) сдвиг ползунка в начало шкалы нажатием клавиши <Ноше>;
  • SliderToMaximum - (6) сдвиг ползунка в конец шкалы нажатием клавиши <End>;
  • SliderMove - (7) перемещение ползунка мышью;
♦ rangeChanged(<Минимум>, <Максимум>) -генерируется при изменении диапазона значений.
  Внутри обработчика через параметры доступны новые минимальное и максимальное
  значения, заданные целыми числами;
♦ sliderPressed() -генерируется при нажатии ползунка;
♦ sliderMoved(<Положение>) - генерируется постоянно при перемещении ползунка.
  Внутри обработчика через параметр доступно новое положение ползунка, выраженное
  целым числом;
♦ sliderReleased() - генерируется при отпускании ранее нажатого ползунка;
♦ valueChanged(<Значение>) - генерируется при изменении значения. Внутри обработчика
  через параметр доступно новое значение в виде целого числа.
Класс QDial дополнительно определяет следующие методы (здесь приведены только
основные - полный их список смотрите на странице https://doc.qt.io/qt-6/qdial.html):
♦ setNotchesVisible(<Флаг>) - если в качестве параметра указано значение True, будут
  отображены риски. По умолчанию риски не выводятся. Метод является слотом;
♦ setNotchTarget(<Значение>) - задает рекомендуемое расстояние между рисками в пикселах.
  В качестве параметра указывается вещественное число;
♦ setWrapping(<Флаг>) - если в качестве параметра указано значение True, то начало
  шкалы будет совпадать с ее концом. По умолчанию между началом шкалы и концом
  расположено пустое пространство. Метод является слотом.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QDial,
                               QLabel,
                               QGridLayout,
                               QWidget,
                               QPushButton,
                               )
from PySide6.QtGui import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, класса виджета круговой
шкалы с ползунком QDial, класса виджета ярлыка QLabel, класса слоя сетки для виджетов QGridLayout,
базового класса пустого виджета QWidget, класса кнопки QPushButton

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent:  ссылка на родительский объект
        """
        # QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        super().__init__(parent)  # вызов конструктора родительского класса с помощью функции super()
        self.setWindowTitle('Шкала с ползунком')  # установка заголовка главного окна
        self.resize(300, 150)  # установка исходного размера главного окна
        self.dial = QDial()  # создание экземпляра класса кругового регулятора
        self.dial.setFixedSize(200, 200)  # установка фиксированного размера
        self.dial.setRange(0, 50)  # установка диапазона значений регулятора
        self.dial.setSliderPosition(25)  # установка позиции регулятора
        self.dial.setSingleStep(2)  # установка шага слайдера для стрелочек
        self.dial.setPageStep(10)  # установка шага слайдера для колеса мыши и клавиш для листания страниц
        self.dial.setNotchesVisible(True)  # включение видимости рисок
        self.dial.setNotchTarget(25)  # задает рекомендуемое расстоянием между рисками
        self.lbl_1 = QLabel(f'Поз - {self.dial.sliderPosition()}')  # создание ярлыка для отображения
        # позиции регулятора
        self.lbl_1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания для ярлыка
        self.lbl_2 = QLabel('Пока ничего')  # создание ярлыка для отображения последнего действия
        self.lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания для ярлыка
        self.lbl_3 = QLabel(f'Значение - {self.dial.value()}')  # создание ярлыка для отображения значения регулятора
        self.lbl_3.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания для ярлыка
        self.dial.actionTriggered.connect(self.last_action)  # привязка обработчика на взаимодействие с регулятором
        self.dial.sliderMoved.connect(self.on_move_slider)  # привязка обработчика на перемещение слайдера !мышью!
        self.dial.valueChanged.connect(self.on_value_change)  # привязка обработчика на изменение значения регулятора
        self.btn_tracking = QPushButton(f'{self.dial.hasTracking()}')  # создание кнопки для переключения отслеживания
        self.btn_tracking.setCheckable(True)  # установка кнопки как переключателя
        self.btn_tracking.setChecked(True)  # установка кнопки в нажатое положение
        self.btn_tracking.clicked.connect(self.tracking_toggle)  # привязка обработчика на нажатие кнопки
        # переключения отслеживания
        self.btn_wrapping = QPushButton(f'{self.dial.wrapping()}')  # создание кнопки для переключения наличия
        # зазора между минимальным и максимальным положением регулятора
        self.btn_wrapping.setCheckable(True)  # установка кнопки как переключателя
        self.btn_wrapping.setChecked(False)  # установка кнопки в не нажатое положение
        self.btn_wrapping.clicked.connect(self.wrapping_toggle) # привязка обработчика на нажатие кнопки
        # переключения зазора

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(self.dial, 0, 0)  # размещение виджета в слое сетке
        self.grid.addWidget(self.lbl_1, 0, 1)
        self.grid.addWidget(QLabel('Последнее действие'), 1, 0)
        self.grid.addWidget(self.lbl_2, 1, 1)
        self.grid.addWidget(self.lbl_3, 2, 0, 1, 2)
        self.grid.addWidget(QLabel('Постоянное отслеживание'), 3, 0)
        self.grid.addWidget(self.btn_tracking, 3, 1)
        self.grid.addWidget(QLabel('Наличие зазора'), 4, 0)
        self.grid.addWidget(self.btn_wrapping, 4, 1)
        self.grid.addWidget(QLabel('Cлайдер можно перемещать мышью, '
                                   'колесом, стрелками, PgDn, PgUp, Home, End'), 5, 0, 1, 2)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя сетки в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне

    def last_action(self, action: int) -> None:
        """
        Обработчик сигнала на взаимодействие с регулятором
        :param action: int - код типа взаимодействия
        :return: None
        """
        self.lbl_2.setText(f'{QDial.SliderAction(action)} - {action}')

    def on_move_slider(self, position: int) -> None:
        """
        Обработчика сигнала на перемещение регулятора !мышью!
        :param position: Int - положение регулятора
        :return: None
        """
        self.lbl_1.setText(f'Поз - {position}')

    def on_value_change(self, value: int) -> None:
        """
        Обработчика сигнала на перемещение регулятора !мышью!
        :param value: Int - значение регулятора
        :return: None
        """
        self.lbl_3.setText(f'Значение - {value}')

    def tracking_toggle(self, checked: bool) -> None:
        """
        Обработчик сигнала нажатия на кнопку переключения отслеживания положения регулятора
        :param checked: bool - состояние кнопки "нажата"
        :return: None
        """
        self.dial.setTracking(checked)  # установка состояния отслеживания перемещения слайдера
        self.btn_tracking.setText(f'{self.dial.hasTracking()}')  # опрос состояния отслеживания и вывод на кнопку

    def wrapping_toggle(self, checked: bool) -> None:
        """
        Обработчик сигнала нажатия на кнопку переключения зазора
        :param checked: bool - состояние кнопки "нажата"
        :return: None
        """
        self.dial.setWrapping(checked)  # установка состояния отслеживания перемещения слайдера
        self.btn_wrapping.setText(f'{self.dial.wrapping()}')  # опрос состояния отслеживания и вывод на кнопку


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
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()