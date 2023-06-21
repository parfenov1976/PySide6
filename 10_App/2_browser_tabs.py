"""
Пример приложения - браузер.
В основе лежит класс QWebEngineView, являющийся ядром браузера,
которое выполняет все функции просмотра веб страничек.
Данный пример дополнен поддержкой вкладок.
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
                               QTabWidget,
                               QMenu,
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
класс диалоговых окон для работы с файлами QFileDialog, класс виджета вкладок QTabWidget, класс виджета
всплывающих меню QMenu

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

        self.tabs = QTabWidget()  # создание объекта вкладок для главного окна приложения
        self.tabs.setDocumentMode(True)  # на macos отображает переключатель вкладки как ее часть, а не отдельно от нее
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)  # создание сигнала на двойной клик
        # с привязкой метода слота, открывающего новую вкладку
        self.tabs.currentChanged.connect(self.current_tab_changed)  # создание сигнала на изменение текущей вкладки
        # с привязкой метода слота, обновляющего адресную строку и заголовок окна
        self.tabs.setTabsClosable(True)  # добавляет возможность закрывать вкладки нажатием на крестик
        # рядом с названием вкладки
        self.tabs.tabCloseRequested.connect(self.close_current_tab)  # создание сигнала на закрытие вкладки
        # с привязкой метода слота, удаляющего вкладку
        self.setCentralWidget(self.tabs)  # размещение вкладки в главном окне приложения

        self.setContextMenuPolicy(Qt.NoContextMenu)  # запрет на вызов контекстного меню

        navtb = QToolBar('Navigation')  # создание экземпляра класса панели инструментов
        navtb.setIconSize(QSize(16, 16))  # установка размеров места для иконок
        navtb.setMovable(False)  # закрепить панель инструментов
        self.addToolBar(navtb)  # добавление на главное окно панели инструментов

        self.statusBar()  # включение в окне строки состояния

        back_btn = QAction(QIcon(os.path.join('icons', 'arrow-180.png')), 'Back', self)  # создание объекта инструмента
        # с кнопкой "Назад" с указанием имени кнопки, отображаемого во всплывающей подсказке
        back_btn.setStatusTip('Back to previous page')  # установка текста подсказки для отображения в строке состояния
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())  # создание сигнала на активацию кнопки
        # с привязкой метода слота, встроенного в класс ядра браузера с использованием анонимной функции
        # для предотвращения его автоматической отработки при создании экземпляра главного окна. К ядру браузера
        # обращаемся через ссылку, возвращаемую методом .currentWidget()
        navtb.addAction(back_btn)  # добавление инструмента (команды) на панель

        next_btn = QAction(QIcon(os.path.join('icons', 'arrow-000.png')), 'Forward', self)  # создание объекта
        # инструмента с кнопкой "Вперед" с указанием имени кнопки, отображаемого во всплывающей подсказке
        next_btn.setStatusTip('Forward to next page')  # установка текста подсказки для отображения в строке состояния
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())  # создание сигнала на активацию кнопки
        # с привязкой метода слота, встроенного в класс ядра браузера с использованием анонимной функции
        # для предотвращения его автоматической отработки при создании экземпляра главного окна. К ядру браузера
        # обращаемся через ссылку, возвращаемую методом .currentWidget()
        navtb.addAction(next_btn)  # добавление инструмента (команды) на панель

        reload_btn = QAction(QIcon(os.path.join('icons', 'arrow-circle-315.png')), 'Reload', self)  # создание объекта
        # инструмента с кнопкой "Обновление странички" с указанием имени кнопки, отображаемого во всплывающей подсказке
        reload_btn.setStatusTip('Reload page')  # установка текста подсказки для отображения в строке состояния
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())  # создание сигнала на активацию кнопки
        # с привязкой метода слота, встроенного в класс ядра браузера с использованием анонимной функции
        # для предотвращения его автоматической отработки при создании экземпляра главного окна. К ядру браузера
        # обращаемся через ссылку, возвращаемую методом .currentWidget()
        navtb.addAction(reload_btn)  # добавление инструмента (команды) на панель

        home_btn = QAction(QIcon(os.path.join('icons', 'home.png')), 'Home', self)  # создание объекта инструмента
        # с кнопкой "Домой" с указанием имени кнопки, отображаемого во всплывающей подсказке
        home_btn.setStatusTip('Go home')  # установка текста подсказки для отображения в строке состояния
        home_btn.triggered.connect(self.navigate_home)  # создание сигнала с привязкой метода слота
        navtb.addAction(home_btn)  # добавление инструмента (команды) на панель

        set_home_btn = QAction(QIcon(os.path.join('icons', 'gear.png')), 'Set home page URL', self)  # создание объекта
        # инструмента с кнопкой для установки адреса домашней странички
        set_home_btn.setStatusTip('Set home page URL')  # установка текста подсказки для отображения в строке состояния
        set_home_btn.triggered.connect(self.set_home_page)  # создание сигнала с привязкой метода слота
        navtb.addAction(set_home_btn)  # добавление инструмента (команды) на панель

        self.httpsicon = QLabel()  # создание ярлыка для изображения
        self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'lock-nossl.png')))  # создание изображения на ярлыке
        navtb.addWidget(self.httpsicon)  # размещение изображения на панели инструментов

        self.urlbar = QLineEdit()  # создание текстового поля для адреса странички
        self.urlbar.returnPressed.connect(self.navigate_to_url)  # создание сигнала на нажатие кнопки ввода
        # с привязкой метода слота перехода по адресу в строке
        navtb.addWidget(self.urlbar)  # размещение адресной строки на панели инструментов

        stop_btn = QAction(QIcon(os.path.join('icons', 'cross-circle.png')), 'Stop', self)  # создание объекта
        # инструмента с кнопкой стоп для остановки загрузки странички
        stop_btn.setStatusTip('Stop loading current page')  # установка текста подсказки для отображения
        # в строке состояния
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())  # создание сигнала на активацию кнопки
        # с привязкой метода слота, встроенного в класс ядра браузера с использованием анонимной функции
        # для предотвращения его автоматической отработки при создании экземпляра главного окна. К ядру браузера
        # обращаемся через ссылку, возвращаемую методом .currentWidget()
        navtb.addAction(stop_btn)  # добавление инструмента (команды) на панель

        self.menuBar().setNativeMenuBar(False)  # под macos перемещает панель меню непосредственно в окно приложения

        file_menu = self.menuBar().addMenu('&File')  # создание меню Файл

        new_tab_action = QAction(QIcon(os.path.join('icons', 'ui-tab--plus.png')), 'New Tab', self, shortcut='Ctrl+T')
        # создание объекта инструмента с кнопкой создать новую вкладку с указанием имени инструмента (в данном случае,
        # для меню, отображается как строка после иконки, а не как подсказка в облачке. Вероятно это связано
        # с вертикальной организацией пунктов меню)
        new_tab_action.setStatusTip('Open a New Tab')  # установка текста подсказки для отображения в строке состояния
        new_tab_action.triggered.connect(self.add_new_tab)  # создание сигнала на кнопку создания новой вкладки
        # с привязкой метода слота
        file_menu.addAction(new_tab_action)  # добавление инструмента в меню Файл

        open_file_action = QAction(QIcon(os.path.join('icons', 'disk--arrow.png')), 'Open file...', self,
                                   shortcut='Ctrl+O')  # создание объекта инструмента с кнопкой открыть файл
        # с указанием имени инструмента (в данном случае, для меню, отображается как строка после иконки,
        # а не как подсказка в облачке. Вероятно это связано с вертикальной организацией пунктов меню)
        open_file_action.setStatusTip('Open from file')  # установка текста подсказки для отображения в строке состояния
        open_file_action.triggered.connect(self.open_file)  # создание сигнала на кнопку открытия файла
        # с привязкой метода слота
        file_menu.addAction(open_file_action)  # добавление инструмента в меню Файл

        save_file_action = QAction(QIcon(os.path.join('icons', 'disk--pencil.png')), 'Save Page As...', self,
                                   shortcut='Ctrl+Shift+S')  # создание объекта инструмента с кнопкой сохранить в файл
        # с указанием имени инструмента (в данном случае, для меню, отображается как строка после иконки,
        # а не как подсказка в облачке. Вероятно это связано с вертикальной организацией пунктов меню)
        save_file_action.setStatusTip('Save current page to file')  # установка текста подсказки для отображения
        # в строке состояния
        save_file_action.triggered.connect(self.save_file)  # создание сигнала на кнопку открытия сохранения в файл
        # с привязкой метода слота
        file_menu.addAction(save_file_action)  # добавление инструмента в меню Файл

        print_action = QAction(QIcon(os.path.join('icons', 'printer.png')), 'Print...', self, shortcut='Ctrl+P')
        # создание объекта инструмента с кнопкой печати текущей странички
        print_action.setStatusTip('Print current page')  # указание текста подсказки для отображения в строке состояния
        print_action.triggered.connect(self.print_page)  # создание сигнала на нажатие кнопки печати с привязкой
        # метода слота
        file_menu.addAction(print_action)  # добавление инструмента печати в меню файл
        self.printer = QPrinter()  # создание экземпляра класса устройства вывода на принтер

        help_menu = self.menuBar().addMenu('&Help')  # создание меню помощи

        about_action = QAction(QIcon(os.path.join('icons', 'question.png')), 'About Mozzarella Ashbadger', self)
        # создание объекта инструмента вызова информации о браузере
        about_action.setStatusTip('Find out mort about Mozzarella Ashbadger')  # указание текста подсказки для
        # отображения в строке состояния
        about_action.triggered.connect(self.about)  # создание сигнала на нажатие кнопки вызова информации о браузере
        # и привязка метода слота вывода данной информации
        help_menu.addAction(about_action)  # добавление инструмента вызова информации о браузере в меню помощи

        navigate_mozzarella_action = QAction(QIcon(os.path.join('icons', 'lifebuoy.png')),
                                             'Mozzarella Ashbadger Homepage',
                                             self,
                                             )
        navigate_mozzarella_action.setStatusTip('Go to Mozzarella Ashbadger Homepage')  # указание текста подсказки для
        # отображения в строке состояния
        navigate_mozzarella_action.triggered.connect(self.navigate_mozzarella)  # создание сигнала на нажатие кнопки
        # перехода на домашнюю страничку и привязка метода слота
        help_menu.addAction(navigate_mozzarella_action)  # добавление инструмента перехода на домашнюю страничку
        # в меню помощи

        self.add_new_tab(QUrl(GO_HOME), 'Homepage')  # вызов метода добавления новой вкладки для создания 1-ой вкладки

        self.setWindowTitle('Mozzarella Ashbadger')  # установка заголовка главного окна приложения
        self.setWindowIcon(QIcon(os.path.join('icons', 'ma-icon-64.png')))  # установка иконки в строке заголовка
        # главного окна приложения

    def add_new_tab(self, qurl=None, label='Blank'):
        """
        Метод слот для добавления новой вкладки
        """
        if qurl is None:  # проверка наличия адреса веб странички в переданных аргументах
            qurl = QUrl('')  # установка пустой строки в качестве адреса на чала просмотра
        browser = WebTab(self)  # создание объекта представления веб странички с передачей ссылки на родительский объект
        browser.setUrl(qurl)  # указание адреса странички для представления
        i = self.tabs.addTab(browser, label)  # добавление вкладки с отображением веб странички
        # и сохранение в переменную i индекса вкладки, возвращенного методом добавления вкладки
        self.tabs.setCurrentIndex(i)  # установка в качестве текущей вкладки с индексом i
        browser.urlChanged.connect(lambda qurl, browser=browser: self.update_urlbar(qurl, browser))  # создание сигнала
        # на изменение адреса при переключении вкладок
        browser.loadFinished.connect(lambda _, i=i, browser=browser: self.tabs.setTabText(i, browser.page().title()))
        # создание сигнала завершения загрузки странички с привязкой встроенного слота, извлекающего название странички
        # и устанавливающего его в качестве наименования вкладки

    def tab_open_doubleclick(self, i) -> None:
        """
        Метод слота для создания вкладки по двойному щелчку мыши
        """
        if i == -1:  # если -1, то под курсором не было вкладок
            self.add_new_tab()  # вызов метода создания новой вкладке

    def current_tab_changed(self, _) -> None:
        """
        Метод слот для обновления заголовка окна и адресной строки при смете вкладки
        """
        qurl = self.tabs.currentWidget().url()  # извлечение ссылки из текущей вкладки (на которую переключились)
        self.update_urlbar(qurl, self.tabs.currentWidget())  # обновление адресной строки
        self.update_title(self.tabs.currentWidget())  # обновление заголовка главного окна

    def close_current_tab(self, i) -> None:
        """
        Метод слот удаления закрытой вкладки
        """
        if self.tabs.count() < 2:  # проверка количества открытых вкладок
            return
        self.tabs.removeTab(i)  # удаление вкладки по индексу

    def set_home_page(self) -> None:
        """
        Метод слот сигнала вызова диалогового окна для установки адреса домашней страницы
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
        Метод слот сигнала перехода на домашнюю страницу
        :return: None
        """
        self.tabs.currentWidget().setUrl(QUrl(GO_HOME))

    def navigate_to_url(self) -> None:
        """
        Метод слот для перехода по ссылке
        :return: None
        """
        q = QUrl(self.urlbar.text())  # извлечение текста из текстового поля, преобразование его в ссылку url
        # и ее сохранение в переменную
        if q.scheme() == '':  # проверка схемы ссылки
            q.setScheme('http')  # если схема пустая, то это значит что адрес относительный и нужно добавить схему
        self.tabs.currentWidget().setUrl(q)  # переход по ссылке

    def update_urlbar(self, q: QUrl, browser=None) -> None:
        """
        Метод слот на обновление содержимого адресной строки
        :param q: QUrl - ссылка с адресом странички
        :param browser: ссылка на текущую вкладку
        :return: None
        """
        if browser != self.tabs.currentWidget():
            # если сигнал поступил не из текущей вкладки, то он игнорируется
            return

        if q.scheme() == 'https':  # проверка схемы ссылки
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'lock-ssl.png')))  # установка иконки безопасного
            # соединения
        else:
            self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'lock-nossl.png')))  # установка иконки небезопасного
            # соединения
        self.urlbar.setText(q.toString())  # преобразование ссылки в текст и запись его в текстовое поле
        self.urlbar.setCursorPosition(0)  # смещение курсора в начало поля

    def update_title(self, browser=None) -> None:
        """
        Метод слот для изменения заголовка окна
        :param browser: ссылка на текущую вкладку
        :return: None
        """
        if browser != self.tabs.currentWidget():
            # если сигнал поступил не из текущей вкладки, то он игнорируется
            return
        title = self.tabs.currentWidget().page().title()  # извлечение заголовка странички
        self.setWindowTitle(f'{title} - Mozzarella Ashbadger')  # установка заголовка окна с заголовком странички

    def open_file(self):
        """
        Метод слот для загрузки файла странички с использованием встроенной функции для создания
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

            self.tabs.currentWidget().setHtml(html)  # передача содержимого переменной на отображение в ядро браузера
            self.urlbar.setText(filename)  # установка заголовка окна

    def save_file(self):
        """
        Метод слот для сохранения странички в файл с использованием встроенной функции для создания
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

            self.tabs.currentWidget().page().toHtml(writer)  # чтение кода странички и обратный вызов функции записи
            # с передачей ей кода

    def print_page(self) -> None:
        """
        Метод слот для вывода странички на принтер с использованием встроенной функции для создания
        диалогового окна для печати QPrintDialog()
        Для вывода странички используется метод self.browser.print().
        :return: None
        """
        dlg = QPrintDialog(self.printer)  # создание диалогового окна печати с привязкой устройства вывода
        if dlg.exec() == QDialog.Accepted:  # запуск цикла событий диалогового окна проверка условия,
            # что выбрана кнопка принять в диалоговом окне
            self.tabs.currentWidget().print(self.printer)  # вызов метода вывода странички на печать
            # и передача ему ссылки на устройство печати

    def navigate_mozzarella(self) -> None:
        """
        Метод слот перехода на домашнюю страничку
        :return: None
        """
        self.tabs.currentWidget().setUrl(QUrl('http://www.pythonguis.com/'))  # вызов метода перехода по ссылке

    @staticmethod
    def about() -> None:
        """
        Метод слот вызова информации о браузере
        :return: None
        """
        dlg = AboutDialog()  # создание экземпляра класса диалогового окна сведений о браузере
        dlg.exec()  # запуск цикла событий диалогового окна


class WebTab(QWebEngineView):
    """
    Подкласс представления странички для вкладки от супер класса представления веб страничек
    """

    def __init__(self, parent: MainWindow) -> None:
        """
        Конструктор представления веб странички для вкладки
        :param parent:  ссылка на родительский класс
        """
        QWebEngineView.__init__(self)  # явный вызов конструктора родительского класса
        self.parent = parent  # сохранение ссылки на родительский объект

    def contextMenuEvent(self, event) -> None:
        """
        Метод обработчик событий вызова контекстного меню.
        :param event: PySide6.QtGui.QContextMenuEvent
        :return: None
        """
        qurl = self.lastContextMenuRequest().linkUrl()  # извлечение ссылки из события вызова контекстного меню
        context_menu = QMenu(self)  # создание экземпляра класса контекстного меню
        open_in_new_tab = QAction('Open in new tab', self)  # создание объекта команды для контекстного меню
        open_in_new_tab.triggered.connect(lambda: self.parent.add_new_tab(qurl))  # создание сигнала на вызов пункта
        # меню с привязкой слота
        context_menu.addAction(open_in_new_tab)  # добавление объекта команды в контекстное меню
        context_menu.exec(event.globalPos())  # Запуск цикла событий контекстного меню. Метод .globalPos() обеспечивает
        # появление контекстного меню на месте курсора

    # FIXME - добиться работоспособности (открытие ссылки на новой вкладке по Ctrl+LBM)
    # этот вариант не перехватывает событие мыши в данной ситуации
    def mousePressEvent(self, event) -> None:
        """
        Метод обработчик событий PySide6.QtGui.QMouseEvent, отрабатывающий нажатие кнопки мыши
        :param: event - QWidget.mousePressEvent - событие специального обработчика событий мыши
        :return: None
        """
        print('000')
        if event.button() == Qt.LeftButton and event.modifiers()==Qt.ControlModifier:
            print('111')


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
    app.setApplicationName("Mozzarella Ashbadger")
    app.setOrganizationName("Mozzarella")
    app.setOrganizationDomain("mozzarella.org")
    window = MainWindow()  # создание главного окна приложения
    app.setStyle('Fusion')  # установка более красивого стиля интерфейса
    window.show()  # вызов метода главного окна, делающего его видимым (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий главного окна


if __name__ == '__main__':  # условие, предотвращающее запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода приложения верхнего уровня
