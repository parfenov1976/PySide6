"""
Обработка событий клавиатуры. Управление фокусом ввода.

Для управления фокусом ввода предназначены следующие методы класса QWidget:
♦ setFocus ([<Причина>]) - устанавливает фокус ввода, если компонент находится в активном
  окне. В качестве причины изменения фокуса ввода можно указать один из следующих
  элементов перечисления FocusReason из модуля QtCore. Qt:
    • MouseFocusReason - фокус изменен с помощью мыши; •
    • TabFocusReason - нажата клавиша <Tab>;
    • BacktabFocusReason - нажата комбинация клавиш <Shift>+<Tab>;
    • ActiveWindowFocusReason - окно стало активным или неактивным;
    • PopupFocusReason - открыто или закрыто всплывающее окно;
    • ShortcutFocusReason - нажата комбинация клавиш быстрого доступа;
    • MenuBarFocusReason - фокус ввода переместился на меню;
    • OtherFocusReason - другая причина;
♦ clearFocus() - убирает фокус ввода с текущего компонента;
♦ hasFocus() - возвращает значение True, если компонент имеет фокус ввода, и False -
  в противном случае;
♦ focusWidget() - возвращает ссылку на последний дочерний компонент, у которого вызывался
  метод setFocus(). Для компонентов верхнего уровня возвращается ссылка на
  компонент, который получит фокус после того, как окно станет активным;
♦ setFocusProxy(<Компонент>) - указывает компонент, который будет получать фокус
  ввода вместо текущего компонента;
♦ focusProxy() - возвращает ссылку на компонент, который получает фокус ввода вместо
  текущего компонента. Если такого компонента нет, возвращает значение None;
♦ focusNextChild() - передает фокус ввода следующему компоненту (аналогично нажатию
  клавиши <ТаЬ>). Возвращает значение True, если фокус ввода удалось передать,
  и False - в противном случае;
♦ focusPreviousChild() - передает фокус ввода предыдущему компоненту (аналогично
  нажатию комбинации клавиш <Shift>+<Tab>). Возвращает значение True, если фокус
  ввода удалось передать, и False - в противном случае;
♦ focusNextPrevChild(<Направление>) - если в параметре указано значение True, работает
  аналогично методу focusNextChild(), если указано False - аналогично методу
  focusPreviousChild();
♦ setTabOrder(<Компонент 1>, <Компонент 2>) - статический метод, задает последовательность
  смены фокуса при нажатии клавиши <ТаЬ>. В параметре <Компонент 2> указывается
  ссылка на компонент, на который переместится фокус с компонента <Компонент 1>.
  Вот пример указания цепочки перехода widget1 -> widget2 -> widget3 -> widget4:
  QtWidgets.QWidget.setTabOrder(widget1, widget2)
  QtWidgets.QWidget.setTabOrder(widget2, widget3)
  QtWidgets.QWidget.setTabOrder(widget3, widget4)
♦ setFocusPolicy(<Способ>) - задает способ получения фокуса текущим компонентом
  в виде одного из следующих элементов перечисления FocusPolicy из модуля QtCore.Qt:
    • NoFocus - компонент не может получать фокус;
    • TabFocus - с помощью клавиши <ТаЬ>;
    • ClickFocus - посредством щелчка мышью;
    • StrongFocus - с помощью клавиши <ТаЬ> и щелчка мышью;
    • WheelFocus - с· помощью клавиши <ТаЬ>, щелчка мышью и колесика мыши;
♦ focusPolicy() - возвращает текущий способ получения фокуса;
♦ grabKeyboard() - захватывает ввод с клавиатуры. Другие компоненты не будут
  получать события клавиатуры, пока не будет вызван метод releaseKeyboard();
♦ releaseKeyboard() - освобождает захваченный ранее ввод с клавиатуры.
Получить ссылку на компонент, находящийся в фокусе ввода, позволяет статический метод
focusWidget() класса QApplication. Если ни один компонент не имеет фокуса ввода, метод
возвращает значение None. Не путайте этот метод с одноименным методом из класса
QWidget.
Обработать получение и потерю фокуса ввода позволяют следующие специальные методы
класса QWidget:
♦ focusinEvent(self, <event>) - вызывается при получении фокуса ввода;
♦ focusOutEvent(self, <event>) - вызывается при потере фокуса ввода.
Через параметр <event> доступен объект класса QFocusEvent, который поддерживает следующие
методы:
♦ gotFocus() - возвращает значение True, если фокус ввода был получен, и False - если
  был потерян;
♦ lostFocus() - возвращает значение True, если фокус ввода был потерян, и False -
  если был получен;
♦ reason() - возвращает причину установки фокуса. Значение аналогично значению
  параметра <Причина> в методе setFocus().
Для назначения клавиш быстрого доступа также можно воспользоваться классом QShortcut
из модуля QtGui. В этом случае назначение клавиши у первого текстового поля будет выглядеть
так:
self.lineEdit1 = QtWidgets.QLineEdit()
self.shc = QtGui.QShortcut(QtGui.QKeySequence.mnemonic("&e"), self)
self.shc.setContext(QtCore.Qt.ShortcutContext.WindowShortcut)
self.shc.activated.connect(self.line1.setFocus)
Еще можно использовать класс QAction из модуля QtGui. Назначение клавиши у второго
текстового поля выглядит следующим образом:
self.lineEdit2 = QtWidgets.QLineEdit()
self.act = QtGui.QAction(self)
self.act.setShortcut(QtGui.QKeySequence.mnemonic("&r"))
self.act.triggered.connect(self.line2.setFocus)
self.addAction(self.act)
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLineEdit,
                               QPushButton,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtGui import (QShortcut,
                           QKeySequence,
                           QAction,
                           )
from PySide6.QtCore import Qt
"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication, класса главных окон QMainWindow,
класс виджета кнопки QPushButton, класс слоя с вертикальной организацией виджетов QVBoxLayout,
базовый класс пустого виджета QWidget, класс редактируемого однострочного текстового поля QLindeEdit

Импорт из модула PySide6.QtGui класса горячих клавиш QShortcut, класса сочетаний клавиш QKeySequence,
класса действий QAction

Импорт из модуля PySide6.QtCore класса перечислителя настроек виджетов Qt
"""


class MyLineEdit(QLineEdit):
    """
    Пользовательский класс однострочного поля от супер класса однострочного редактируемого текстового поля
    """

    def __init__(self, id: int, parent=None) -> None:
        """
        Конструктор пользовательского класса однострочного редактируемого текстового поля
        :param id: int - аттрибут для хранения идентификатора поля
        :param parent: ссылка на родительский объект
        """
        QLineEdit.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.id = id  # аттрибут для хранения идентификатора

    def focusInEvent(self, event: QLineEdit.focusInEvent) -> None:
        """
        Обработчик события получения фокуса ввода
        :param event: QLineEdit.focusInEvent - событие получения фокуса ввода
        :return: None
        """
        print(f'Получен фокус ввода полем {self.id}')
        QLineEdit.focusInEvent(self, event)  # отправка события далее

    def focusOutEvent(self, event: QLineEdit.focusOutEvent) -> None:
        """
        Обработчик события потери фокуса ввода
        :param event: QLineEdit.focusOutEvent - событие потери фокуса ввода
        :return: None
        """
        print(f'Потерян фокус ввода полем {self.id}')
        QLineEdit.focusOutEvent(self, event)  # отправка события далее


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
        self.setWindowTitle('Обработка событий клавиатуры')  # установка заголовка главного окна
        self.resize(300, 100)  # установка исходного размера окна
        self.btn = QPushButton('Установить фокус на поле 2')  # создание виджета кнопки
        self.line1 = MyLineEdit(1)  # создание экземпляра пользовательского класса однострочного текстового поля
        self.line2 = MyLineEdit(2)  # создание экземпляра пользовательского класса однострочного текстового поля
        self.vbox = QVBoxLayout()  # создание слоя для виджетов
        self.vbox.addWidget(self.btn)  # размещение виджета кнопки в слое для виджетов
        self.vbox.addWidget(self.line1)  # размещение виджета текстового поля в слое
        self.vbox.addWidget(self.line2)  # размещение виджета текстового поля в слое
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение в контейнере слоя с виджетами
        self.setCentralWidget(self.container)  # размещение контейнера со слоями в главном окне приложения
        self.btn.clicked.connect(self.on_clicked)  # назначение обработчика сигналу на нажатие кнопки
        QMainWindow.setTabOrder(self.line1, self.line2)  # задаем порядок обхода с помощью клавиши <Tab>
        QMainWindow.setTabOrder(self.line2, self.btn)  # задаем порядок обхода с помощью клавиши <Tab>

        self.shc = QShortcut(QKeySequence.mnemonic("&e"), self)  # создание сочетания горячих клавиш <Alt>+<e>
        self.shc.setContext(Qt.ShortcutContext.WindowShortcut)  # добавление сочетания к контексту окна приложения
        self.shc.activated.connect(self.line1.setFocus)  # создание сигнала на активацию фокуса и привязка обработчика

        self.act = QAction(self)  # создание экземпляра класса действия
        self.act.setShortcut(QKeySequence.mnemonic('&r'))  # создание сочетания горячих клавиш <Alt>+<r>
        self.act.triggered.connect(self.line2.setFocus)  # создание сигнала на активацию фокуса и привязка обработчика
        self.addAction(self.act)  # добавление действия в экземпляр окна приложения

    def on_clicked(self) -> None:
        """
        Обработчика сигнала на нажатие кнопки
        :return: None
        """
        self.line2.setFocus()  # установка фокуса на поле 2


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
