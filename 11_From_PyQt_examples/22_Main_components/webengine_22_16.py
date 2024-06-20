"""
Основные компоненты интерфейса. Веб-браузер

Веб-браузер реализуется классом QWebEngineView из модуля QtWebEngineWidgets.
Иерархия наследования:
(QObject, QPaintDevice) - QWidget - QWebEngineView

Формат конструктора класса QWebEngineView:
QWebEngineView([parent=None])
Класс QWebEngineView поддерживает следующие полезные для нас методы (полный их список
смотрите на странице https://doc.qt.io/qt-6/qwebengineview.html):
♦ load(<Интернет-адрес>) и sеtUrl(<Интернет-адрес>) - загружают и выводят страницу
с указанным в параметре адресом, который задается в виде объекта класса QUrl из модуля
QtCore:
web.load(QtCore.QUrl('https://www.google.ru/'))
♦ url() - возвращает адрес текущей страницы в виде объекта класса QUrl;
♦ title() - возвращает заголовок (содержимое тега <title>) текущей страницы;
♦ setHtml(<НТМL-код> [, baseUrl=QUrl()]) - задает НТМL-код страницы, которая будет
  отображена в компоненте.
  Необязательный параметр baseUrl указывает базовый адрес, относительно которого
  будут отсчитываться относительные адреса в гиперссылках, ссылках на файлы изображений,
  таблицы стилей, файлы сценариев и пр. Если этот параметр не указан, в качестве
  значения по умолчанию используется «пустой» объект класса QUrl, и относительные
  адреса будут отсчитываться от каталога, где находится сам файл страницы. Пример:
  wv.setHtml("<hl>Заголовок</hl>")
  # Файл page2.html будет загружен с сайта http://www.somesite.ru/
  webview.setHtml("<a href='page2.html'>Вторая страница</а>",
                    QtCore.QUrl('http://www.somesite.ru/'))
♦ selectedText() - возвращает выделенный текст или пустую строку, если ничего не было
  выделено;
♦ hasSelection() - возвращает True, если какой-либо фрагмент страницы был выделен,
  и False - в противном случае;
♦ setZoomFactor(<Множитель>) - задает масштаб самой страницы. Значение 1 указывает,
  что страница будет выведена в оригинальном масштабе, значение меньше единицы -
  в уменьшенном, значение больше единицы - увеличенном масштабе;
♦ zoomFactor() - возвращает масштаб страницы;
♦ back() -загружает предыдущий ресурс из списка истории. Метод является слотом;
♦ forward() - загружает следующий ресурс из списка истории. Метод является слотом;
♦ reload() -перезагружает страницу. Метод является слотом;
♦ stop() - останавливает загрузку страницы. Метод является слотом;
♦ icon() - возвращает в виде объекта класса QIcon значок, заданный для страницы;
♦ findText(<Искомый текст>[, options= {}] [, resultCallback=0]) - ищет на странице
  заданный фрагмент текста. Все найденные фрагменты будут выделены желтым фоном
  непосредственно в компоненте.
  Необязательный: параметр option задает дополнительные параметры в виде одного из
  следующих элементов перечисления FindFlag класса QWebEnginePage из модуля
  QtWebEngineCore (или их комбинации через оператор |):
  • FindBackward - выполнять поиск в обратном, а не в прямом направлении;
  • FindCaseSensitively - поиск с учетом регистра символов (по умолчанию выполняется
    поиск без учета регистра).
  В необязательном параметре resultCallback можно указать функцию, которая будет вызвана
  по окончании поиска. Эта функция должна принимать в качестве единственного
  параметра объект класса QWebEngineFindTextResult из модуля QtWebEngineCore. Этот
  класс поддерживает следующие методы:
  • numЬerOfMatches() - возвращает количество совпавших фрагментов;
  • activeMatch() - индекс выделенного в текущий момент совпавшего фрагмента.
  Пример поиска с учетом регистра и выделением всех найденных совпадений:
  web.findText('Python', options=QtWebEngineCore.QWebEnginePage.FindFlag.FindBackward |
                    QtWebEngineCore.QWebEnginePage.FindFlag.FindCaseSensitively)
♦ triggerPageAction(<Действие>[, checked=False]) - выполняет над страницей указанное
  действие. В качестве действия задается один из элементов перечисления WebAction
  класса QWebEnginePage из модуля QtWebEngineCore - этих атрибутов очень много, и все
  они приведены на странице https://doc.qt.io/qt-6/qwebenginepage.html#WebActionenum.
  Необязательный параметр checked имеет смысл указывать лишь для действий,
  принимающих логический флаг:
  # Выделение всей страницы
  web.triggerPageAction(QtWebEngineCore.QWebEnginePage.WebAction.SelectAll)
  # Копирование выделенного фрагмента страницы
  web.triggerPageAction(QtWebEngineCore.QWebEnginePage.WebAction.Copy)
  # Перезагрузка страницы, минуя кеш
  web.triggerPageAction(QtWebEngineCore.QWebEnginePage.WebAction.ReloadAndBypassCache)
♦ page() - возвращает объект класса QWebEnginePage из модуля QtWebEngineCore, представляющий
  открытую веб-страницу (описан далее);
♦ print(<Принтер>) - печатает содержимое открытой страницы на заданном принтере
  (указывается в виде объекта класса QPrinter);
♦ printToPdf() - преобразует страницу в формат PDF. Форматы метода:
  printToPdf(<Путь к файлу>,
                pageLayout=QPageLayout(QPageSize(QPageSize.PageSizeId.A4),
                QPageLayout.Orientation.Portrait, QMarginsF()),
                ranges={})
  printТоРdf(<Функция>,
                pageLayout=QPageLayout(QPageSize(QPageSize.PageSizeId.A4),
                QPageLayout .Orientation .Portrait,
                QMarginsF()),
                ranges= {})
  Первый формат сразу сохраняет преобразованную страницу в файле, чей путь указан
  первым параметром. Второй формат после преобразования вызывает указанную в первом
  параметре функцию, передавая ей в качестве единственного параметра. преобразованную
  страницу в виде объекта класса QByteArray.
  Параметр pageLayout задает настройки страницы в виде объекта класса QPageLayout.
  Если параметр не указан, будет выполнена печать на бумаге типоразмера
  А4, в портретной ориентации, без отступов.
  Параметр ranges задает номера страниц, которые попадут в формируемый РDF-документ,
  в виде множества. Если он не указан, в документ попадут все страницы.
Класс QWebEngineView поддерживает следующий набор полезных сигналов (полный их список
смотрите на странице https://doc.qt.io/qt-6/qwebengineview.html):
♦ iconChanged(<Значок QIcon>) - генерируется после загрузки или изменения значка, заданного
  для страницы. В параметре, передаваемом обработчику, доступен полученный значок;
♦ loadFinished(<Флаг>) - генерируется по окончании загрузки страницы. Значение True
  параметра указывает, что загрузка выполнена без проблем, False - что при загрузке
  произошли ошибки;
♦ loadProgress(<Процент выполнения>) - периодически генерируется в процессе загрузки
  страницы. В качестве параметра передается целое число от 0 до 100, показывающее процент
  загрузки;
♦ loadStarted() - генерируется после начала загрузки страницы;
♦ selectionChanged() - генерируется при выделении нового · фрагмента содержимого
  страницы;
♦ titleChanged(<Текст>) - генерируется при изменении текста заголовка страницы (содержимого
  тега <title>). В параметре, передаваемом обработчику, доступен этот текст
  в виде строки;
♦ urlChanged(<Интернет-адрес QUrl>) - генерируется при изменении интернет-адреса
  текущей страницы, что может быть вызвано, например, загрузкой новой страницы. Параметр
  - новый интернет-адрес.
Класс QWebEnginePage, представляющий открытую в веб-браузере страницу, поддерживает
следующие полезные методы (полный их список смотрите на странице
https://doc.qt.io/qt-6/qwebenginepage.html):
♦ save(<Путь к файлу>, format=SaveFormatPage.MimeHtmlSaveFormat) - сохраняет страницу
  в файле, чей путь указан в первом параметре. Параметр format задает формат файла
  в виде одного из следующих элементов перечисления SavePageFormat класса
  QWebEngineDownloadRequest из модуля QtWebEngineCore:
  • SingleHtmlSaveFormat - обычный НТМL-файл. Связанные со страницей файлы
    (изображения, аудио- и видеоролики, таблицы стилей и пр.) не сохраняются;
  • CompleteHtmlSaveFormat - то же самое, только связанные файлы будут сохранены
    в каталоге, находящемся там же, где и файл со страницей, и имеющем то же имя;
  • MimeHtmlSaveFormat - страница и все связанные файлы сохраняются в одном файле;
♦ contentsSize() - возвращает объект класса QSizeF, хранящий размеры содержимого
  страницы;
♦ scrollPosition() - возвращает объект класса QPointF, хранящий позицию прокрутки
  содержимого страницы;
♦ setAudioMuted(<Флаг>) - если с параметром передать значение True, все звуки, воспроизводящиеся
  на странице, будут приглушены. Чтобы снова сделать их слышимыми, нужно передать значение False;
♦ isAudioMuted() - возвращает True, если все звуки, воспроизводящиеся на странице,
  приглушены, и False - в противном случае;
♦ setBackgroundColor(<Цвет QColor>) - задает для страницы фоновый цвет;
♦ backgroundColor() - возвращает фоновый цвет страницы в виде объекта класса QColor.
"""

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QMainWindow,
                               QGridLayout,
                               QWidget,
                               QLineEdit,
                               QProgressBar,
                               )
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon

"""
Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow, 
класс однострочного редактируемого поля QLineEdit, класс слоя сетки для виджетов QGridLayout,
класса пустого базового виджета QWidget

Импорт из модуля PySide6.QtWebEngineWidgets класса окна представления веб движка QWebEngineView

Импорт из модуля PySide6.QtCort класса веб объекта url-адресов QUrl

Импорт из модуля PySide.QtGui класса иконок QIcon
"""


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
        self.setWindowTitle('Веб-браузер')  # установка заголовка главного окна приложения
        self.resize(800, 600)  # установка исходного размера главного окна приложения
        self.web_view = QWebEngineView()  # создание веб представления для отображения страницы
        self.web_view.load(QUrl('https://www.ya.ru/'))  # загрузка страницы по адресу
        self.web_view.iconChanged.connect(self.icon_change)  # привязка обработчика на изменение значка страницы
        self.web_view.urlChanged.connect(self.url_change)  # привязка обработчика сигнала изменения адреса страницы
        self.web_view.loadProgress.connect(lambda value: self.progress_bar.setValue(value))
        self.url_line = QLineEdit()  # создание виджета адресной строки
        self.url_line.setText('https://www.ya.ru/')  # размещение в адресной строке адреса по умолчанию
        self.url_line.returnPressed.connect(self.url_change)  # привязка обработчика на ввод нового адреса
        self.progress_bar = QProgressBar()  # создание шкалы прогресса загрузки
        self.progress_bar.setRange(0, 100)  # установка диапазона значение прогресса

        self.grid = QGridLayout()  # создание слоя сетки для виджетов
        self.grid.addWidget(self.url_line, 0, 0)  # размещение виджета в сетке
        self.grid.addWidget(self.web_view, 1, 0)
        self.grid.addWidget(self.progress_bar, 2, 0)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.grid)  # размещение слоя в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера в главном окне приложения

    def icon_change(self, item: QIcon) -> None:
        """
        Обработчика сигнала о смене значка страницы
        :param item: QIcon - значок страницы
        :return: None
        """
        self.setWindowIcon(item)  # установка иконки странички в заголовок окна приложения

    def url_change(self, url: QUrl = None) -> None:
        """
        Обработчик изменения адреса страницы
        :param url: QUrl - объект нового адреса
        :return: None
        """
        if url:
            self.url_line.setText(url.toString())  # размещение нового адреса в адресной строке
        else:
            self.web_view.load(QUrl(self.url_line.text()))  # загрузка страницы по введенному адресу


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