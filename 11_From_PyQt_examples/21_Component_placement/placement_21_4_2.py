"""
Размещение компонентов интерфейса в окне. Управление размерами компонентов.

Если в вертикальный контейнер большой высоты добавить надпись и кнопку, то кнопка
займет пространство, совпадающее с рекомендуемыми размерами (которые возвращает
метод sizeHint()), а под надпись будет выделено все остальное место. Управление
размерами компонентов внутри контейнера определяется правилами, установленными с
помощью объектов класса QSizePolicy. Установить эти правила для компонента можно с
помощью метода setSizePolicy(<Правило QSizePolicy>) класса QWidget, а получить их
вызовом метода sizePolicy().
Формат конструктора класса QSizePolicy:
QSizePolicy([<Правило для горизонтали>, <Правило для вертикали>[,
                                                <Тип компонента>]])
Если параметры не заданы, размер компонента будет точно соответствовать размерам,
возвращаемым методом sizeHint(). В первом и втором параметрах указывается один из
следующих элементов перечисления Policy из класса QSizePolicy:
♦ Fixed - размеры компонента будут точно соответствовать размерам, возвращаемым
  методом sizeHint();
♦ Minimum - размеры, возвращаемые методом sizeHint(), станут минимальными для компонента
  и могут быть увеличены при необходимости;
♦ Maximum - размеры, возвращаемые методом sizeHint(), станут максимальными для
  компонента и могут быть уменьшены при необходимости;
♦ Preferred - размеры, возвращаемые методом sizeHint(), являются предпочтительными
  и могут быть как увеличены, так и уменьшены;
♦ Expanding - размеры, возвращаемые методом sizeHint(), могут быть как увеличены,
  так и уменьшены. Компонент займет все свободное пространство в контейнере;
♦ MinimumExpanding - размеры, возвращаемые методом sizeHint(), являются минимальным
  для компонента. Компонент займет все свободное пространство в контейнере;
♦ Ignored - размеры, возвращаемые методом sizeHint(), игнорируются. Компонент займет
  все свободное пространство в контейнере.
В качестве типа компонента указывается один из следующих элементов перечисления
ControlType из класса QSizePolicy: DefaultType (нет какого-либо специфического типа -
значение по умолчанию), ButtonBox (набор кнопок диалогового окна, представленный объектом
класса QDialogButtonBox), CheckBox (флажок), ComboBox (раскрывающийся список),
Frame (панель с рамкой), GroupBox (группа), Label (надпись), Line (панель с рамкой, выводящаяся
в виде горизонтальной или вертикальной линии), LineEdit (поле ввода), PushButton (кнопка),
RadioButton (переключатель), Slider (шкала с ползунком), SpinBox (поле для ввода
целых чисел), TabWidget (панель с вкладками) или ToolButton (кнопка панели инструментов).
Пример:
sp = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum,
                           QtWidgets.QSizePolicy.Policy.Fixed,
                           QtWidgets.QSizePolicy.ControlType.Frame)
Изменить правила управления размерами уже после создания объекта класса QSizePolicy
позволяют методы setHorizontalPolicy(<Правило для горизонтали>) и setVerticalPolicy(<Правило
для вертикали>).
Изменить тип компонента после создания объекта класса QSizePolicy позволяет метод
setControlType(<Tип компонента>).
С помощью методов setHorizontalStretch(<Фактор для горизонтали>) и setVerticalStretch(<Фактор
для вертикали>) можно указать фактор растяжения. Чем больше указанное значение относительно
значения, заданного в других компонентах, тем больше места будет выделяться под текущий компонент.
Можно указать, что предпочтительная высота компонента зависит от его ширины. Для этого
необходимо передать значение True в метод setHeightForWidth(<Флаг>). Кроме того, следует
в классе компонента переопределить метод heightForWidth(<Ширина>) - переопределенный
метод должен возвращать высоту компонента для указанной в параметре ширины.
Метод setRetainSizeWhenHidden(<Флаг>) позволяет указать поведение контейнера при
скрытии компонента. Значение False параметра предписывает контейнеру полностью убирать
как сам скрытый компонент, так и пространство, занятое скрытым компонентом, а значение True
- убирать лишь компонент, оставляя занятое им пространство свободным.
"""
from PySide6.QtWidgets import (QMainWindow,
                               QPushButton,
                               QPlainTextEdit,
                               QVBoxLayout,
                               QWidget,
                               QSizePolicy,
                               )

"""
Импорт из модуля PySide6.QtWidgets класса главного окна приложения QMainWindow,
класса контейнера вертикальной стопки QVBoxLayout, класса виджета кнопки QPushButton, 
базового класса пустого виджета QWidget, класса политик управления размерами QSizePolicy,
класса виджета многострочного текстового поля QPlainTextEdit
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
        self.setWindowTitle('Управление размера компонентов')  # установка заголовка окна
        self.resize(600, 600)  # установка исходного размера окна
        self.txt_edit = QPlainTextEdit()  # создание экземпляра текстового поля
        self.btn = QPushButton('Кнопка')  # создание экземпляра кнопки
        self.vbox = QVBoxLayout()  # создание контейнера стопки
        self.vbox.addWidget(self.txt_edit)  # размещение в стопке текстового поля
        self.vbox.addWidget(self.btn)  # размещение в стопке кнопки
        self.container = QWidget()  # создание контейнера окна для контейнеров с виджетами
        self.container.setLayout(self.vbox)  # размещение в контейнере окна контейнера с виджетами
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне
        self.sp_text = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)  # создание политики размера
        self.txt_edit.setSizePolicy(self.sp_text)  # применение политики размера к компоненту
        self.txt_edit.appendPlainText(str(self.btn.sizeHint()))
        self.txt_edit.appendPlainText(str(self.btn.sizePolicy()))


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
