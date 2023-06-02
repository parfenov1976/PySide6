"""
Пример приложения - браузер.
В основе лежит класс QWebEngineView, являющийся ядром браузера,
которое выполняет все функции просмотра веб страничек.
Данный пример не содержит возможности использования вкладок.
"""

import sys
import os

from PySide6.QtCore import QUrl, QSize, Qt
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QToolBar,
                               QDialog,
                               QDialogButtonBox,
                               QVBoxLayout,
                               QLineEdit,
                               QLabel,
                               QFileDialog,
                               )
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QtWidgets.QApplication([]) в качестве аргумента передается пустой список.

Модуль os для извлечения путей операционной системы и работы с путями.

Импорт из модуля ядра библиотеки PySide6.QtCore класса для работы с Url-адресами QUrl, класса для объектов размеров
двухмерных объектов QSize, класса набора имен различных параметров Qt.

Импорт из модуля ядра веб виджетов PySide6.QtWebEngineWidgets класса ядра браузера
для отображения веб страничек QWebEngineView.

Модуль PySide6.QtWidgets предоставляет элементы пользовательского интерфейса для классических приложений на ПК.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета панели инструментов QToolBar, класс виджета диалогового окна QDialog,
класса кнопок для диалогового окна QDialogButtonBox, класс слоя для виджетов с вертикальной организацией QVBoxLayout,
класса виджета однострочного редактируемого текстового поля QLineEdit, класс виджета ярлыка QLabel,
класс диалоговых окон для работы с файлами QFileDialog

Модуль PySide6.QtGui предоставляет классы для интеграции оконной и графической системы, обработчика событий.
Импорт из модуля PySide6.QtGui класса абстракций пользовательских команд QAction, класса для работы и иконками QIcon,
класс представления изображения QPixmap.

Импорт из модуля поддержки принтеров PySide6.QtPrintSupport класса диалогового окна для печати QPrintDialog,
класса устройства вывода на принтер QPrinter.  
"""
GO_HOME = 'https://www.yandex.ru'


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супе-класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.browser = QWebEngineView()  # создание экземпляра класса ядра браузера дял отображения веб страниц
        self.browser.setUrl(QUrl(GO_HOME))  # установка начального адреса для просмотра
        self.browser.urlChanged.connect(self.update_urlbar)  # создание сигнала на изменение адреса странички при клике
        # по ссылке с привязкой метода ресивера на обновление адресной строки
        self.browser.loadFinished.connect(self.update_title)  # создание сигнала на завершение загрузки странички
        # с привязкой метода ресивер на обновление заголовка окна
        self.setCentralWidget(self.browser)  # размещение представления веб страницы в главном окне приложения

        navtb = QToolBar('Navigation')  # создание экземпляра класса панели инструментов
        navtb.setIconSize(QSize(16, 16))  # установка размеров места для иконок
        navtb.setMovable(False)  # закрепить панель инструментов
        self.addToolBar(navtb)  # добавление на главное окно панели инструментов

        self.statusBar()  # включение в окне строки состояния

        back_btn = QAction(QIcon(os.path.join('icons', 'arrow-180.png')), 'Back', self)  # создание объекта инструмента
        # с кнопкой "Назад" с указанием имени кнопки, отображаемого во всплывающей подсказке
        back_btn.setStatusTip('Back to previous page')  # установка текста подсказки для отображения в строке состояния
        back_btn.triggered.connect(self.browser.back)  # создание сигнала на активацию кнопки с привязкой метода
        # ресивера, встроенного в класс ядра браузера
        navtb.addAction(back_btn)  # добавление инструмента (команды) на панель

        next_btn = QAction(QIcon(os.path.join('icons', 'arrow-000.png')), 'Forward', self)  # создание объекта
        # инструмента с кнопкой "Вперед" с указанием имени кнопки, отображаемого во всплывающей подсказке
        next_btn.setStatusTip('Forward to next page')  # установка текста подсказки для отображения в строке состояния
        next_btn.triggered.connect(self.browser.forward)  # создание сигнала на активацию кнопки с привязкой метода
        # ресивера, встроенного в класс ядра браузера
        navtb.addAction(next_btn)  # добавление инструмента (команды) на панель

        reload_btn = QAction(QIcon(os.path.join('icons', 'arrow-circle-315.png')), 'Reload', self)  # создание объекта
        # инструмента с кнопкой "Обновление странички" с указанием имени кнопки, отображаемого во всплывающей подсказке
        reload_btn.setStatusTip('Reload page')  # установка текста подсказки для отображения в строке состояния
        reload_btn.triggered.connect(self.browser.reload)  # создание сигнала на активацию кнопки с привязкой метода
        # ресивера, встроенного в класс ядра браузера
        navtb.addAction(reload_btn)  # добавление инструмента (команды) на панель

        home_btn = QAction(QIcon(os.path.join('icons', 'home.png')), 'Home', self)  # создание объекта инструмента
        # с кнопкой "Домой" с указанием имени кнопки, отображаемого во всплывающей подсказке
        home_btn.setStatusTip('Go home')  # установка текста подсказки для отображения в строке состояния
        home_btn.triggered.connect(self.navigate_home)  # создание сигнала с привязкой метода ресивера
        navtb.addAction(home_btn)  # добавление инструмента (команды) на панель

        set_home_btn = QAction(QIcon(os.path.join('icons', 'gear.png')), 'Set home page URL', self)  # создание объекта
        # инструмента с кнопкой для установки адреса домашней странички
        set_home_btn.setStatusTip('Set home page URL')  # установка текста подсказки для отображения в строке состояния
        set_home_btn.triggered.connect(self.set_home_page)  # создание сигнала с привязкой метода ресивера
        navtb.addAction(set_home_btn)  # добавление инструмента (команды) на панель

        self.httpsicon = QLabel()  # создание ярлыка для изображения
        self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'lock-nossl.png')))  # создание изображения на ярлыке
        navtb.addWidget(self.httpsicon)  # размещение изображения на панели инструментов

        self.urlbar = QLineEdit()  # создание текстового поля для адреса странички
        self.urlbar.returnPressed.connect(self.navigate_to_url)  # создание сигнала на нажатие кнопки ввода
        # с привязкой метода ресивера перехода по адресу в строке
        navtb.addWidget(self.urlbar)  # размещение адресной строки на панели инструментов

        stop_btn = QAction(QIcon(os.path.join('icons', 'cross-circle.png')), 'Stop', self)  # создание объекта
        # инструмента с кнопкой стоп для остановки загрузки странички
        stop_btn.setStatusTip('Stop loading current page')  # установка текста подсказки для отображения
        # в строке состояния
        stop_btn.triggered.connect(self.browser.stop)  # создание сигнала на остановку загрузки странички
        # с привязкой метода ресивера, встроенного в класс ядра браузера
        navtb.addAction(stop_btn)  # добавление инструмента (команды) на панель

        file_menu = self.menuBar().addMenu('&File')  # создание меню Файл

        open_file_action = QAction(QIcon(os.path.join('icons', 'disk--arrow.png')), 'Open file...', self)  # создание
        # объекта инструмента с кнопкой открыть файл с указанием имени инструмента (в данном случае, для меню,
        # отображается как строка после иконки, а не как подсказка в облачке. Вероятно это связано с вертикальной
        # организацией пунктов меню)
        open_file_action.setStatusTip('Open from file')  # установка текста подсказки для отображения в строке состояния
        open_file_action.triggered.connect(self.open_file)  # создание сигнала на кнопку открытия файла
        # с привязкой метода ресивера
        file_menu.addAction(open_file_action)  # добавление инструмента в меню Файл

        save_file_action = QAction(QIcon(os.path.join('icons', 'disk--pencil.png')), 'Save Page As...', self)
        # создание объекта инструмента с кнопкой сохранить в файл с указанием имени инструмента (в данном случае,
        # для меню, отображается как строка после иконки, а не как подсказка в облачке. Вероятно это связано
        # с вертикальной организацией пунктов меню)
        save_file_action.setStatusTip('Save current page to file')  # установка текста подсказки для отображения
        # в строке состояния
        save_file_action.triggered.connect(self.save_file)  # создание сигнала на кнопку открытия сохранения в файл
        # с привязкой метода ресивера
        file_menu.addAction(save_file_action)  # добавление инструмента в меню Файл

        print_action = QAction(QIcon(os.path.join('icons', 'printer.png')), 'Print...', self)  # создание объекта
        # инструмента с кнопкой печати текущей странички
        print_action.setStatusTip('Print current page')  # указание текста подсказки для отображения в строке состояния
        print_action.triggered.connect(self.print_page)  # создание сигнала на нажатие кнопки печати с привязкой
        # метода ресивера
        file_menu.addAction(print_action)  # добавление инструмента печати в меню файл
        self.printer = QPrinter()  # создание экземпляра класса устройства вывода на принтер

        help_menu = self.menuBar().addMenu('&Help')  # создание меню помощи

        about_action = QAction(QIcon(os.path.join('icons', 'question.png')), 'About Mozzarella Ashbadger', self)
        # создание объекта инструмента вызова информации о браузере
        about_action.setStatusTip('Find out mort about Mozzarella Ashbadger')  # указание текста подсказки для
        # отображения в строке состояния
        about_action.triggered.connect(self.about)  # создание сигнала на нажатие кнопки вызова информации о браузере
        # и привязка метода ресивера вывода данной информации
        help_menu.addAction(about_action)  # добавление инструмента вызова информации о браузере в меню помощи

        navigate_mozzarella_action = QAction(QIcon(os.path.join('icons', 'lifebuoy.png')),
                                             'Mozzarella Ashbadger Homepage',
                                             self,
                                             )
        navigate_mozzarella_action.setStatusTip('Go to Mozzarella Ashbadger Homepage')  # указание текста подсказки для
        # отображения в строке состояния
        navigate_mozzarella_action.triggered.connect(self.navigate_mozzarella)  # создание сигнала на нажатие кнопки
        # перехода на домашнюю страничку и привязка метода ресивера
        help_menu.addAction(navigate_mozzarella_action)  # добавление инструмента перехода на домашнюю страничку
        # в меню помощи

    def set_home_page(self) -> None:
        """
        Метод ресивер сигнала вызова диалогового окна для установки адреса домашней страницы
        :return: None
        """
        global GO_HOME  # создание ссылки на глобальную переменную
        dlg = SetHomeDialog(self)  # создание диалогового окна
        dlg.url_line.setText(GO_HOME)  # считывание текущего адреса домашней страницы в текстовое поле
        if dlg.exec():  # запуск цикла событий диалогового окна и проверка условия нажатия на кнопки
            GO_HOME = dlg.url_line.text()  # установка содержимого текстового поля в переменную
            # для адреса домашней страницы

    def navigate_home(self) -> None:
        """
        Метод ресивер сигнала перехода на домашнюю страницу
        :return: None
        """
        self.browser.setUrl(QUrl(GO_HOME))

    def navigate_to_url(self) -> None:
        """
        Метод ресивер для перехода по ссылке
        :return: None
        """
        q = QUrl(self.urlbar.text())  # извлечение текста из текстового поля, преобразование его в ссылку url
        # и ее сохранение в переменную
        if q.scheme() == '':  # проверка схемы ссылки
            q.setScheme('http')  # если схема пустая, то это значит что адрес относительный и нужно добавить схему
        self.browser.setUrl(q)  # переход по ссылке

    def update_urlbar(self, q: QUrl) -> None:
        """
        Метод ресивер на обновление содержимого адресной строки
        :param q: QUrl - ссылка с адресом странички
        :return: None
        """
        if q.scheme() == 'https':  # проверка схемы ссылки
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'lock-ssl.png')))  # установка иконки безопасного
            # соединения
        else:
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'lock-nossl.png')))  # установка иконки небезопасного
            # соединения
        self.urlbar.setText(q.toString())  # преобразование ссылки в текст и запись его в текстовое поле
        self.urlbar.setCursorPosition(0)  # смещение курсора в начало поля

    def update_title(self) -> None:
        """
        Метод ресивер для изменения заголовка окна
        :return: None
        """
        title = self.browser.page().title()  # извлечение заголовка странички
        self.setWindowTitle(f'{title} - Mozzarella Ashbadger')  # установка заголовка окна с заголовком странички

    def open_file(self):
        """
        Метод ресивер для загрузки файла странички с использованием встроенной функции для создания
        диалогового окна для открытия файла QFileDialog.getOpenFileName()
        :return: None
        """
        # создание диалогового окна на открытие файла
        # в _ передается выбор фильтра файлов в диалоговом окне
        filename, _ = QFileDialog.getOpenFileName(
            self,
            'Open file',
            '',
            'Hypertext Markup Language (*,htm *.html);;' 'All Files (*.*)',
        )
        if filename:  # проверка условия выбран ли файла
            with open(filename, 'r') as f:  # открытие файла на чтение
                html = f.read()  # чтение файла в переменную

            self.browser.setHtml(html)  # передача содержимого переменной на отображение в ядро браузера
            self.urlbar.setText(filename)  # установка заголовка окна

    def save_file(self):
        """
        Метод ресивер для сохранения странички в файл с использованием встроенной функции для создания
        диалогового окна для открытия файла QFileDialog.getSaveFileName()
        Для получения странички используется метод self.browser.page().toHtml(). Это асинхронный метода и это
        подразумевает, что страничке не будет получена немедленно. Вместо этого нужно передать метод обратного вызова,
        который получит страничку, как только она будет готова. Для этого нужно создать простую функцию записи, которая
        выполнит данную работу, используя имя файла из локально области видимости.
        :return: None
        """
        # создание диалогового окна на запись файла
        # в _ передается выбор фильтра файлов в диалоговом окне
        filename, _ = QFileDialog.getSaveFileName(
            self,
            'Save Page As',
            '',
            'Hypertext Markup Language (*,htm *.html);;' 'All Files (*.*)',
        )
        if filename:  # проверка условия задано ли имя файла
            def writer(html: str) -> None:
                """
                Функция записи конда страничка в файл
                Не работает со страничками из интернета
                :param html: код html странички
                :return: None
                """
                with open(filename, 'w') as f:  # открытие файла на запись, если файла нет, то он создается
                    f.write(html)  # запись кода страничка в файл

            self.browser.page().toHtml(writer)  # чтение кода странички и обратный вызов функции записи
            # с передачей ей кода

    def print_page(self) -> None:
        """
        Метод ресивер для вывода странички на принтер с использованием встроенной функции для создания
        диалогового окна для печати QPrintDialog()
        Для вывода странички используется метод self.browser.print().
        :return: None
        """
        dlg = QPrintDialog(self.printer)  # создание диалогового окна печати с привязкой устройства вывода
        if dlg.exec() == QDialog.Accepted:  # запуск цикла событий диалогового окна проверка условия,
            # что выбрана кнопка принять в диалоговом окне
            self.browser.print(self.printer)  # вызов метода вывода странички на печать
            # и передача ему ссылки на устройство печати

    def navigate_mozzarella(self) -> None:
        """
        Метод ресивер перехода на домашнюю страничку
        :return: None
        """
        self.browser.setUrl(QUrl('http://www.pythonguis.com/'))  # вызов метода перехода по ссылке

    def about(self) -> None:
        """
        Метод ресивер вызова информации о браузере
        :return: None
        """
        dlg = AboutDialog()  # создание экземпляра класса диалогового окна сведений о браузере
        dlg.exec()  # запуск цикла событий диалогового окна


class AboutDialog(QDialog):
    """
    Класс диалогового окна сведений о браузере от супер-класса диалоговых окон
    """
    def __init__(self) -> None:
        """
        Конструктор диалогового окна сведений о браузере
        """
        QDialog.__init__(self)  # явный вызов конструктора родительского класса

        ok_btn = QDialogButtonBox.Ok  # создание кнопки ОК для диалогового окна
        self.button_box = QDialogButtonBox(ok_btn)  # создание блока кнопок и размещение кнопки в нем
        self.button_box.accepted.connect(self.accept)  # создание сигнала на нажатие кнопки
        self.button_box.rejected.connect(self.reject)  # создание сигнала на отказ нажатия кнопки

        layout = QVBoxLayout()  # создание слоя для виджетов с вертикальной организаций
        title = QLabel('Mozzarella Ashbadger')  # создание ярлыка с надписью
        font = title.font()  # создание объекта настроек шрифта
        font.setPointSize(20)  # установка высоты шрифта
        title.setFont(font)  # применение настроек шрифта к ярлыку

        layout.addWidget(title)  # добавление ярлыка на слой

        logo = QLabel()  # создание пустого ярлыка для последующего размещения изображения
        logo.setPixmap(QPixmap(os.path.join('icons', 'ma-icon-128.png')))  # добавление на ярлык изображения
        layout.addWidget(logo)  # добавление ярлыка с лого на слой

        layout.addWidget(QLabel('Version 23.35.211.233232'))  # добавление ярлыка с версией
        layout.addWidget(QLabel('Copyright 2015 Mozzarella Inc'))  # добавления ярлыка объекта авторского права

        for i in range(0, layout.count()):  # цикл прохода по индексам элементов в слое
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)  # выравнивание элемента слоя по центру

        layout.addWidget(self.button_box)  # добавление на слой блока кнопок

        self.setLayout(layout)  # размещение слоя с виджетами в диалоговом окне


class SetHomeDialog(QDialog):
    """
    Класс диалогового окна для настройки адреса домашней страницы от супер-класса диалоговых окон
    """

    def __init__(self, parent: QMainWindow = None) -> None:
        """
        Конструктор диалогового окна
        :param parent: ссылка на родительский объект
        """
        QDialog.__init__(self, parent)  # явный вызов родительского класса
        self.setWindowTitle('Set home page URL')  # установка названия диалогового окна
        self.setMinimumSize(QSize(500, 75))  # установка минимального размера диалогового окна
        self.url_line = QLineEdit()  # создание строки для ввода адреса домашней странички
        self.url_line.setPlaceholderText('Enter home page URL')  # установка текста, который отображается в пустом поле
        self.buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel  # создание списка кнопок диалогового окна
        # из стандартного пространства имен класса QDialogButtonBox
        self.button_box = QDialogButtonBox(self.buttons)  # создание кнопок диалогового окна из списка
        self.button_box.setCenterButtons(True)  # центровка кнопок
        self.button_box.accepted.connect(self.accept)  # создание сигнала для кнопки OK
        self.button_box.rejected.connect(self.reject)  # создание сигнала для кнопки Cancel
        self.layout = QVBoxLayout()  # создание слоя для виджетов
        self.layout.addWidget(self.url_line)  # добавление на слой диалогового окна строки для адреса
        self.layout.addWidget(self.button_box)  # добавление кнопок на слой диалогового окна
        self.setLayout(self.layout)  # размещение слоя в диалоговом окне
        # self.show()  # метод для установки видимости диалогового окна, если далее в коде будет
        # метод запуска .exec() для данного окна, то данный вызов не требуется


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    """
    app = QApplication(sys.argv)  # создание основного цикла событий главного окна
    window = MainWindow()  # создание главного окна приложения
    app.setStyle('Fusion')  # установка более красивого стиля интерфейса
    window.show()  # вызов метода главного окна, делающего его видимым (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий главного окна


if __name__ == '__main__':  # условие, предотвращающее запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода приложения верхнего уровня
