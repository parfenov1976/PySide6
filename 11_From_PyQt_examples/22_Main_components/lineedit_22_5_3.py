"""
Основные компоненты интерфейса. Поле ввода, контроль с помощью валидаторов

Валидатор - механизм, проверяющий соответствие введенного в поле значения заданным
правилам.
Валидатор у поля ввода задается методом setValidator(<Валидатор>). В качестве параметра
указывается объект класса, производного от класса QValidator из модуля QtGui. Существуют
следующие стандартные классы валидаторов:
♦ QIntValidator - допускает ввод только целых чисел. Функциональность класса зависит
  от настройки локали. Форматы конструктора:
  QIntValidator([parent=None])
  QIntValidator(<Минимальное значение>, <Максимальное значение>[, parent=None])
  Пример ограничения ввода диапазоном целых чисел от 0 до 100:
  lineEdit.setValidator(QtGui.QIntValidator(0, 100, parent=window))
♦ QDoubleValidator - допускает ввод только вещественных чисел. Функциональность
  класса зависит от настройки локали. Форматы конструктора:
  QDoubleValidator([parent=None])
  QDoubleValidator(<Минимальное значение>, <Максимальное значение>,
                   <Количество цифр после точки>[, parent=None])
  Пример ограничения ввода диапазоном вещественных чисел от о. 0 до 100. о и двумя
  цифрами после десятичной точки:
  lineEdit.setValidator(QtGui.QDoubleValidator(0.0, 100.0, 2, parent=window))
  Чтобы позволить вводить числа в экспоненциальной форме, необходимо передать в метод
  setNotation(<Tип записи>) элемент ScientificNotation перечисления Notation из
  класса QDoubleValidator. Если передать методу элемент StandardNotation того же перечисления,
  будет разрешено вводить числа только в десятичной форме. Пример:
  validator = QtGui.QDoubleValidator(0.0, 100.0, 2, parent=window)
  validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
  lineEdit.setValidator(validator)
♦ QRegularExpressionValidator - позволяет проверить данные на соответствие заданному
  регулярному выражению. Форматы конструктора:
  QRegularExpressionValidator([parent=None])
  QRegularExpressionValidator(<Регулярное выражение>[, parent=None])
  Регулярное выражение указывается в виде объекта класса QRegularExpression из модуля
  QtCore. Пример ввода только цифр от О до 9:
  validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[0-9]+"),
                                                parent=window)
  lineEdit.setValidator(validator)
  Обратите внимание, что здесь производится проверка полного соответствия шаблону,
  поэтому символы ^ и $ явным образом указывать не нужно.
Проверить корректность введенных данных позволяет метод hasAcceptableInput(). Если
данные корректны, метод возвращает значение True, а в противном случае - False.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QLineEdit,
                               QLabel,
                               QGridLayout,
                               QWidget,
                               )
from PySide6.QtCore import Qt
from PySide6.QtGui import (QIntValidator,
                           QDoubleValidator,
                           QRegularExpressionValidator,
                           )

"""
Импорт из модуля PySide6.QtWidgets класса главного окна приложения QMainWindow,
класса однострочного редактируемого текстового поля QLineEdit, класса виджета ярлыка QLabel,
класса контейнера сетки QGridLayout, класса пустого базового виджета QWidget 

Импорт из модуля PySide6.QtCort класса перечислителя настроек виджетов Qt

Импорт из модуля PySide6.QtGui класса валидатора для целых чисел QIntValidator,
класса валидатора для вещественных чисел QDoubleValidator, класса валидатора на основе
регулярных выражений QRegularExpressionValidator
"""


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от класса главных окон
    """

    def __init__(self, parent=None):
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.resize(400, 300)  # установка исходного размера окна
        self.setWindowTitle('Валидаторы')  # установка заголовка главного окна приложения
        self.grid = QGridLayout()  # создание контейнера сетки для размещения виджетов

        self.lbl_1 = QLabel('Целы числа от 1 до 50')  # создание ярлыка с надписью
        self.line_edit_1 = QLineEdit()  # создание редактируемого текстового поля
        self.line_edit_1.setPlaceholderText('Введите целое число')  # размещение подсказки в поле ввода
        self.line_edit_1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # настройка выравнивания в поле
        self.line_edit_1.setValidator(QIntValidator(0, 50))  # установка валидатора на поле ввода
        state_1 = QLabel('!!!!!')  # создание ярлыка для отображения результатов проверки валидности
        # создание сигнала на редактирование поле и привязка обработчика для проверки валидности ввода
        # и вывода результата
        self.line_edit_1.textEdited.connect(lambda: self.check_valid_input(self.line_edit_1, state_1))

        self.lbl_2 = QLabel('Вещественные числа от 0.00 до 10.00')
        self.line_edit_2 = QLineEdit()
        self.line_edit_2.setPlaceholderText('Введите вещественное число')
        self.line_edit_2.setAlignment(Qt.AlignmentFlag.AlignRight)
        validator = QDoubleValidator(0.0, 10.0, 2)  # создание валидатора
        self.line_edit_2.setValidator(validator)  # установка валидатора на поле ввода
        state_2 = QLabel('!!!!!')
        self.line_edit_2.textEdited.connect(lambda: self.check_valid_input(self.line_edit_2, state_2))

        self.lbl_3 = QLabel('Текст с русскими буквами')
        self.line_edit_3 = QLineEdit()
        self.line_edit_3.setPlaceholderText('Ведите слово')
        self.line_edit_3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.validator = QRegularExpressionValidator('[а-яА-Я ]{1,30}')  # создание валидатора
        self.line_edit_3.setValidator(self.validator)  # установка валидатора на поле ввода
        state_3 = QLabel('!!!!!')
        self.line_edit_3.textEdited.connect(lambda: self.check_valid_input(self.line_edit_3, state_3))

        # размещение элементов интерфейса в сетке
        self.grid.addWidget(self.lbl_1, 0, 0)
        self.grid.addWidget(self.line_edit_1, 0, 1)
        self.grid.addWidget(state_1, 0, 2)
        self.grid.addWidget(self.lbl_2, 1, 0)
        self.grid.addWidget(self.line_edit_2, 1, 1)
        self.grid.addWidget(state_2, 1, 2)
        self.grid.addWidget(self.lbl_3, 2, 0)
        self.grid.addWidget(self.line_edit_3, 2, 1)
        self.grid.addWidget(state_3, 2, 2)

        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение сетки в контейнере для слоев
        self.setCentralWidget(self.container)  # размещение контейнера со слоями в главном окне приложения

    @staticmethod
    def check_valid_input(field, state):
        """
        Обработчик сигнала редактирования поля с проверкой валидности ввода
        :param field: ссылка на поле ввода
        :param state: ссылка на ярлык для отображения результатов проверки валидности
        :return: None
        """
        if field.hasAcceptableInput():
            state.setText('OK')
        else:
            state.setText('!!!!!')


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
