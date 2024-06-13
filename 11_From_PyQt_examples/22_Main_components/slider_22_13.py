"""
Основные компоненты интерфейса. Шкала с ползунком

Класс QSlider реализует шкалу с ползунком. Иерархия наследования выглядит так:
(QObject, QPaintDevice) - QWidget - QAbstractSlider - QSlider
Форматы конструктора класса QSlider:
QSlider([parent=None])
QSlider(<Ориентация>[, parent=None])
В качестве значения параметра <Ориентация> указываются элементы Horizontal (горизонтальная)
или Vertical (вертикальная - значение по умолчанию) перечисления Orientation
из модуля QtCore.Qt.
Класс QSlider наследует следующие методы из класса QAbstractSlider (здесь· приведены
только основные - полный их список смотрите на странице https://doc.qt.io/qt-2/qabstractslider.html):
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
Класс QSlider дополнительно определяет следующие методы (здесь приведены только
основные - полный их список смотрите на странице https://doc.qt.io/qt-6/qslider.html):
♦ setTickPosition (<Позиция>) - задает позицию рисок. В качестве параметра указываются
  следующие элементы перечисления TickPosition из класса QSlider:
  • NoTicks - без рисок;
  • TicksBothSides - риски по обе стороны;
  • TicksAbove - риски выводятся сверху;
  • TicksBelow - риски выводятся снизу;
  • TicksLeft - риски выводятся слева;
  • TicksRight - риски выводятся справа;
♦ setTickInterval(<Расстояние>) - задает расстояние между отдельными рисками.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QSlider,
                               QLabel,
                               QGridLayout,
                               QWidget,
                               QPushButton,
                               )
from PySide6.QtGui import Qt

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, класса виджета шкалы 
с ползунком QSlider, класса виджета ярлыка QLabel, класса слоя сетки для виджетов QGridLayout,
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
        self.slider_1 = QSlider(Qt.Orientation.Horizontal)  # создание экземпляра класса слайдера
        self.slider_1.setFixedWidth(200)  # установка фиксированного размера
        self.slider_1.setRange(0, 50)  # установка диапазона значений слайдера
        self.slider_1.setSliderPosition(25)  # установка позиции слайдера
        self.slider_1.setSingleStep(2)  # установка шага слайдера для стрелочек
        self.slider_1.setPageStep(10)  # установка шага слайдера для колеса мыши и клавиш для листания страниц
        self.slider_1.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.lbl_1 = QLabel(f'Поз - {self.slider_1.sliderPosition()}')  # создание ярлыка для отображения
        # позиции слайдера
        self.lbl_1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания для ярлыка
        self.lbl_2 = QLabel('Пока ничего')  # создание ярлыка для отображения последнего действия
        self.lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания для ярлыка
        self.lbl_3 = QLabel(f'Значение - {self.slider_1.value()}')  # создание ярлыка для отображения значения слайдера
        self.lbl_3.setAlignment(Qt.AlignmentFlag.AlignCenter)  # установка настроек выравнивания для ярлыка
        self.slider_1.actionTriggered.connect(self.last_action)  # привязка обработчика на взаимодействие со слайдером
        self.slider_1.sliderMoved.connect(self.on_move_slider)  # привязка обработчика на перемещение слайдера !мышью!
        self.slider_1.valueChanged.connect(self.on_value_change)  # привязка обработчика на изменение значения ползунка
        self.btn = QPushButton(f'{self.slider_1.hasTracking()}')  # создание кнопки для переключения отслеживания
        self.btn.setCheckable(True)  # установка кнопки как переключателя
        self.btn.setChecked(True)  # установка кнопки в нажатое положение
        self.btn.clicked.connect(self.tracking_toggle)  # привязка обработчика на нажатие кнопки
        # переключения отслеживания

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(self.slider_1, 0, 0)  # размещение виджета в слое сетке
        self.grid.addWidget(self.lbl_1, 0, 1)
        self.grid.addWidget(QLabel('Последнее действие'), 1, 0)
        self.grid.addWidget(self.lbl_2, 1, 1)
        self.grid.addWidget(self.lbl_3, 2, 0, 1, 2)
        self.grid.addWidget(QLabel('Постоянное отслеживание'), 3, 0)
        self.grid.addWidget(self.btn, 3, 1)
        self.grid.addWidget(QLabel('Cлайдер можно перемещать мышью, колесом, стрелками, PgDn, PgUp, Home, End'), 4, 0,
                            1, 2)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя сетки в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне

    def last_action(self, action: int) -> None:
        """
        Обработчик сигнала на взаимодействие со слайдером
        :param action: int - код тип взаимодействия
        :return: None
        """
        self.lbl_2.setText(f'{QSlider.SliderAction(action)} - {action}')

    def on_move_slider(self, position: int) -> None:
        """
        Обработчика сигнала на перемещение слайдера !мышью!
        :param position: Int - положение слайдера
        :return: None
        """
        self.lbl_1.setText(f'Поз - {position}')

    def on_value_change(self, value: int) -> None:
        """
        Обработчика сигнала на перемещение слайдера !мышью!
        :param value: Int - значение слайдера
        :return: None
        """
        self.lbl_3.setText(f'Значение - {value}')

    def tracking_toggle(self, checked: bool) -> None:
        """
        Обработчик сигнала начатия на кнопку переключения отслеживания положения слайдера
        :param checked: bool - состояние кнопки "нажата"
        :return: None
        """
        self.slider_1.setTracking(checked)  # установка состояния отслеживания перемещения слайдера
        self.btn.setText(f'{self.slider_1.hasTracking()}')  # опрос состояния отслеживания и вывод на кнопку


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
