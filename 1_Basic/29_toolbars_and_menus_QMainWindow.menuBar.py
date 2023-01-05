"""
Пример создания меню с использованием метода QMainWindow.menuBar() класса основных окон.
Ниже указано, где данный пример начинается.
"""
import sys
import os
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLabel,
                               QToolBar,
                               QStatusBar,
                               QCheckBox
                               )
from PySide6.QtGui import QAction, QIcon, QKeySequence

"""
Модуль os нужен для создания путей к файлам для разных платформ.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtCore класса QSize для управления размерами объектов и класса
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета ярлыков (надписей) QLabel, класса виджета
панели инструментов QToolBar.
Импорт из модуля QtGui класса эффектов действия QAction, класса для создания иконок QIcon
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

basedir = os.path.dirname(__file__)  # извлечение пути до директории, из которой запущено приложение


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения с наследованием от класса виджета главного окна.
    """

    def __init__(self):
        """
        Конструктор главного окна приложения.
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.setWindowTitle('My App')  # присвоение имени главному окну приложения
        self.label = QLabel('Hello!')  # создание экземпляра класса виджета ярлыка с надписью
        self.label.setAlignment(Qt.AlignCenter)  # установка настройки с центральным расположением надписи
        self.setCentralWidget(self.label)  # размещение надписи в главном окне приложения
        self.toolbar = QToolBar('My main toolbar')  # создание экземпляра панели инструментов с указанием имени панели
        self.toolbar.setIconSize(QSize(16, 16))  # установка размера иконки
        self.addToolBar(self.toolbar)  # размещение панели инструментов в главном окне приложения
        self.button_action = QAction(QIcon(os.path.join(basedir, 'data', 'bug.png')), '&Your button', self)
        """
        Создание эффекта для кнопки панели инструментов. Данный эффект можно подключать к разным элементам интерфейса,
        которые выполняют одну и туже функцию для избежания многократного дублирования определения действий. 
        Текстовая строка задает имя кнопки. QIcon устанавливает иконку для кнопки. Текст по умолчанию будет
        отображаться в облачке с подсказкой при удержании курсора над иконкой.
        """
        self.button_action.setStatusTip('This is your button')  # установка строки подсказки, выводимой в панели статуса
        # при наведении курсора на кнопку
        self.button_action.triggered.connect(self.on_my_tool_bar_button_click)  # создание сигнала с привязкой
        # метода ресивера
        self.button_action.setCheckable(True)  # Устанавливает кнопку в режим переключателя. Если данный режим
        # не установлен, то при нажатии на кнопку сигнал всегда будет передавать False.
        self.toolbar.addAction(self.button_action)  # привязка эффекта к панели инструментов
        """
        Пример созданию сочетания клавиш для быстрого вызова инструмента
        """
        self.button_action.setShortcut(QKeySequence("Ctrl+p"))  # установка сочетания клавиш для вызова эффекта кнопки
        self.toolbar.addSeparator()  # добавление разделителя между кнопками
        # далее повторяем код для создания второй кнопки
        self.button_action2 = QAction(QIcon(os.path.join(basedir, 'data', 'bug.png')), 'Your &second button', self)
        self.button_action2.setStatusTip('This is your second button')
        self.button_action2.triggered.connect(self.on_my_tool_bar_button_click)
        self.button_action2.setCheckable(True)
        self.toolbar.addAction(self.button_action2)
        self.toolbar.addWidget(QLabel('Hello world!!!'))  # добавляет виджет ярлыка с надписью на панель инструментов
        # self.toolbar.addWidget(QCheckBox())  # добавляет чек бокс на панель инструментов
        self.checkbox_widget = QCheckBox('Your checkbox')
        self.checkbox_widget.setStatusTip('This is your checkbox')
        self.toolbar.addWidget(self.checkbox_widget)
        self.setStatusBar(QStatusBar(self))  # Создание экземпляра виджета панели статуса и
        # его размещение в главном окне приложения. При наведении курсора на кнопку панели инструментов
        # в статусе будет отображаться строка статуса кнопки
        """
        Пример с выпадающими меню начинается отсюда. Для его реализации используем ранее созданные эффекты для кнопок
        панели инструментов.
        """
        menu = self.menuBar()  # создание панели меню в главном окне приложения
        file_menu = menu.addMenu('&File')  # создание выпадающего меню на панели меню. Добавление амперсанда
        # позволяет вызывать меню и его пункты по нажатию клавиши с буквой, перед которой он был размещен.
        # (не работает в макос)
        file_menu.addAction(self.button_action)  # помещение в выпадающее меню эффекта ранее созданной кнопки
        file_menu.addSeparator()  # добавление сепаратора в выпадающее меню
        file_menu.addAction(self.button_action2)  # помещение в выпадающее меню эффекта ранее созданной кнопки
        file_submenu = file_menu.addMenu('Submenu')  # создание подменю
        file_submenu.addAction(self.button_action)  # помещение в подменю эффекта ранее созданной кнопки
        file_submenu.addAction(self.button_action2)  # помещение в подменю эффекта ранее созданной кнопки


    @staticmethod
    def on_my_tool_bar_button_click(s: bool) -> None:
        """
        Метод ресивер (слот) для получения сигнала и его вывода.
        :param s: bool - содержимое сигнала от виджета
        :return: None
        """
        print('click', s)


def main() -> None:
    """
    Функция запуска кода верхнего уровня приложения.
    """
    app = QApplication(sys.argv)  # Создание экземпляра класса основного цикла событий приложения.
    window = MainWindow()  # Создание главного окна приложения.
    window.show()  # Метод вывода главного окна приложения (по умолчанию окно спрятано).
    app.exec()  # Запуск основного цикла событий главного окна приложения.


if __name__ == '__main__':  # Данное условие предотвращает запуск кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня
