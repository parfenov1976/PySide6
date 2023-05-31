"""
Пример приложения - браузер.
В основе лежит класс QWebEngineView, являющийся ядром браузера,
которое выполняет все функции просмотра веб страничек.
Данный пример не содержит возможности использования вкладок.
"""

import sys
import os

from PySide6.QtCore import QUrl, QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QToolBar,
                               QDialog,
                               QDialogButtonBox,
                               QVBoxLayout,
                               QLineEdit,
                               QLabel,
                               )
from PySide6.QtGui import QAction, QIcon, QPixmap

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QtWidgets.QApplication([]) в качестве аргумента передается пустой список.

Модуль os для извлечения путей операционной системы и работы с путями.

Импорт из модуля ядра библиотеки PySide6.QtCore класса для работы с Url-адресами QUrl.

Импорт из модуля ядра веб виджетов PySide6.QtWebEngineWidgets класса ядра браузера
для отображения веб страничек QWebEngineView, класса для создания объектов для размеров
двухмерных объектов QSize.

Модуль PySide6.QtWidgets предоставляет элементы пользовательского интерфейса для классических приложений на ПК.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета панели инструментов QToolBar, класс виджета диалогового окна QDialog,
класса кнопок для диалогового окна QDialogButtonBox, класс слоя для виджетов с вертикальной организацией QVBoxLayout,
класса виджета однострочного редактируемого текстового поля QLineEdit, класс виджета ярлыка QLabel.

Модуль PySide6.QtGui предоставляет классы для интеграции оконной и графической системы, обработчика событий.
Импорт из модуля PySide6.QtGui класса абстракций пользовательских команд QAction, класса для работы и иконками QIcon,
класс представления изображения QPixmap.
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

    def set_home_page(self) -> None:
        """
        Метод ресивер сигнала вызова диалогового окна для установки адреса домашней страницы
        :return: None
        """
        global GO_HOME  # создание ссылки на глобальную переменную
        dlg = SetHomeDialog(self)  # создание диалогового окна
        dlg.url_line.setText(GO_HOME)  # считывание текущего адреса домашней страницы в текстовое поле
        if dlg.exec():  # проверка условия нажатия на кнопки
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
