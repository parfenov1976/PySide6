"""
Обработка событий клавиатуры. Назначение клавиш быстрого доступа.
TODO: проверить под виндой
Клавиша быстрого доступа (или горячая клавиша) - это какая-либо из алфавитно-цифровых
клавиш, нажатие которой совместно с клавишей-модификатором (обычно <Alt>) устанавливает
фокус ввода на связанный с ней компонент. Если связанным компонентом является кнопка
(или пункт меню), она будет нажата.
У компонента, имеющего текстовую надпись (например, кнопки), указать клавишу быстрого
доступа можно, поставив в тексте надписи перед буквой, соответствующей указываемой
клавише, символ &. Чтобы вставить в надпись сам символ &, его следует продублировать.
Если компонент не имеет собственной текстовой надписи, придется создать надпись к нему
и связать ее с компонентом с помощью метода setBuddy(<Компонент>) объекта надписи.
Если же создать отдельную надпись у компонента не представляется возможным, можно
воспользоваться следующими методами класса QWidget:
♦ grabShortcut(<Клавиша> [, <Контекст>]) - регистрирует заданную клавишу быстрого
  доступа и возвращает идентификатор, с помощью которого можно управлять ею в дальнейшем.
  Клавиша указывается в виде объекта класса QKeySequence из модуля QtGui. Конструктор
  этого класса поддерживает следующие форматы вызова:
  QKeySequence(<Строка с обозначениями клавиш>)
  QKeySequence(<Числовое обозначение клавиши>)
  В первом формате в передаваемой строке обозначения клавиш указываются последовательно
  и отделяются друг от друга символами +. Во втором формате обозначение клавиши
  указывается в виде значения одного из элементов перечисления Кеу из модуля QtCore.Qt
  или комбинации значений через оператор +.
  Также можно воспользоваться статическим методом mnemonic(<Обозначение клавиши>)
  класса QKeySequence, где обозначение клавиши указывается в виде строки и предваряется
  символом &.
  Примеры создания объекта класса QKeySequence для комбинации клавиш <Alt>+<E>:
  QtGui.QKeySequence.mnemonic("&e")
  QtGui.QKeySequence("Alt+e")
  QtGui.QKeySequence(QtCore.Qt.Key.Key_F5)
  В качестве контекста можно указать следующие элементы перечисления ShortcutContext
  из модуля QtCore.Qt:
  • WidgetShortcut - клавиша быстрого доступа работает, когда родитель компонента имеет
    фокус ввода;
  • WidgetWithChildrenShortcut - клавиша быстрого доступа работает, когда его родитель
    компонента или любой из его потомков имеет фокус ввода;
  • WindowShortcut - клавиша быстрого доступа работает, когда окно, содержащее компонент,
    активно (значение по умолчанию);
  • ApplicationShortcut - клавиша быстрого доступа работает, когда программа активна;
♦ releaseShortcut(<Идентификатор>) - удаляет комбинацию с указанным идентификатором;
♦ setShortcutEnabled(<Идентификатор> [, <Состояние>]) - если в качестве состояния указано
  True (значение по умолчанию), клавиша быстрого доступа с заданным идентификатором
  разрешена. Состояние False запрещает использование клавиши быстрого доступа.
При нажатии клавиши быстрого доступа генерируется событие типа Туре.Shortcut,
которое можно обработать в методе event(self, <event>). Через параметр <event> доступен
объект класса QShortcutEvent, поддерживающий следующие методы:
♦ shortcutId() - возвращает идентификатор комбинации клавиш;
♦ isAmbiguous() - возвращает значение True, если нажатая клавиша быстрого доступа
  была указана сразу у нескольких компонентов, и False - в противном случае;
♦ key() - возвращает объект класса QKeySequence, представляющий нажатую клавишу
  быстрого доступа.
Для назначения клавиш быстрого доступа также можно воспользоваться классом QShortcut
из модуля QtGui. В этом случае назначение клавиши у первого текстового поля будет
выглядеть так:
self.line1 = QtWidgets.QLineEdit()
self.shc = QtGui.QShortcut(QtGui.QKeySequence.mnemonic("&e"), self)
self.shc.setContext(QtCore.Qt.ShortcutContext.WindowShortcut)
self.shc.activated.connect(self.line1.setFocus)
Еще можно использовать класс QAction из модуля QtGui. Назначение клавиши у второго
текстового поля выглядит следующим образом:
self.line2 = QtWidgets.QLineEdit()
self.act = QtGui.QAction(self)
self.act.setShortcut(QtGui.QKeySequence.mnemonic("&r"))
self.act.triggered.connect(self.line2.setFocus)
self.addAction(self.act)
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLineEdit,
                               QLabel,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import QEvent, Qt
from PySide6.QtGui import QKeySequence, QShortcut, QAction

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класс виджета кнопки QPushButton, класс слоя с вертикальной организацией виджетов QVBoxLayout,
базовый класс пустого виджета QWidget, класс редактируемого однострочного текстового поля QLindeEdit,
класс ярлыка QLabel

Импорт из модула PySide6.QtGui класса горячих клавиш QShortcut, класса сочетаний клавиш QKeySequence,
класса действий QAction

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt, класса событий QEvent
"""


class MyLineEdit(QLineEdit):
    """
    Пользовательский класс однострочного поля от супер класса однострочного редактируемого текстового поля
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор пользовательского однострочного поля
        """
        QLineEdit.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.id = None  # создание аттрибута для хранения идентификатора быстрой клавиши

    def event(self, event: QEvent) -> bool | QEvent:
        """
        Обработчик события установки фокуса ввода
        """
        print(self.id)
        if event.type() == QEvent.Type.Shortcut:  # проверка типа события на принадлежность к быстрым клавишам
            if self.id == event.shortcut_id():  # проверка соответствия идентификатора быстрой клавиши
                self.setFocus(Qt.FocusReason.ShortcutFocusReason)  # установка фокуса ввода на поле
                return True
        return QLineEdit.event(self, event)  # проброс события далее


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Назначение быстрых клавиш')  # установка заголовка главного окна приложения
        self.resize(300, 100)  # установка исходного размера главного окна
        self.lbl = QLabel('Установить фокус ввода на поле 1')  # создание экземпляра виджета ярлыка с надписью
        self.line_edit_1 = QLineEdit()  # создание экземпляра виджета однострочного текстового поля
        self.lbl.setBuddy(self.line_edit_1)  # связывание ярлыка с надписью и текстового поля
        self.line_edit_2 = MyLineEdit()  # создание текстового поля из пользовательского класса
        self.line_edit_2.id = self.line_edit_2.grabShortcut(QKeySequence.mnemonic('&w'))  # регистрация и
        # передача идентификатор быстрой клавиши <Alt + w>
        self.btn = QPushButton('&Убрать фокус с поля 1')  # создание кнопки с надписью привязка быстрой клавиши
        self.btn.clicked.connect(self.on_clicked)  # назначение обработчика на нажатие кнопки
        self.vbox = QVBoxLayout()  # создание слоя для виджтеов с вертикальной организацией
        self.vbox.addWidget(self.lbl)  # размещение виджета на слое
        self.vbox.addWidget(self.line_edit_1)
        self.vbox.addWidget(self.line_edit_2)
        self.vbox.addWidget(self.btn)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера с виджетами в главном окне приложения

        self.shc = QShortcut(QKeySequence.mnemonic("&e"), self)  # создание сочетания горячих клавиш <Alt>+<e>
        self.shc.setContext(Qt.ShortcutContext.WindowShortcut)  # добавление сочетания к контексту окна приложения
        self.shc.activated.connect(self.line_edit_1.setFocus)  # создание сигнала на активацию фокуса и
        # привязка обработчика

        self.act = QAction(self)  # создание экземпляра класса действия
        self.act.setShortcut(QKeySequence.mnemonic('&r'))  # создание сочетания горячих клавиш <Alt>+<r>
        self.act.triggered.connect(self.line_edit_2.setFocus)  # создание сигнала на активацию фокуса и
        # привязка обработчика
        self.addAction(self.act)  # добавление действия в экземпляр окна приложения

    def on_clicked(self):
        """
        Обработчик сигнала на нажатие кнопки на снятия фокуса ввода с поля 1
        """
        self.line_edit_1.clearFocus()  # снятие фокуса ввода с поля 1


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
