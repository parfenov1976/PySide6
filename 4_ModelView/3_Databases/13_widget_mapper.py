"""
Пример использования модели таблиц и представления (маппера) QDataWidgetMapper,
которое позволяет выполнять ввод и редактирование данных, а также реализация
необходимого для этого управления.
В данном примере в качестве структуры данных для таблицы будет файл базы данных sqlite.
"""

import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import (QApplication,
                               QComboBox,
                               QDataWidgetMapper,
                               QDoubleSpinBox,
                               QFormLayout,
                               QLabel,
                               QLineEdit,
                               QMainWindow,
                               QSpinBox,
                               QWidget,
                               QHBoxLayout,
                               QVBoxLayout,
                               QPushButton
                               )

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса выпадающего списка QComboBox, класса спин бокса
с плавающей точкой QDoubleSpinBox и спин бокса для целых чисел QSpinBox, класса слоев для 
построчной организации виджетов в форму QFormLayout, класса ярлыка QLabel,
однострочного редактируемого текстового поля QLideEdit, класса базового пустого виджета QWidget,
класс слоя c горизонтальной организацией виджетов QHBoxLayout, класс слоя c вертикальной
организацией виджетов QHBoxLayout, класс кнопки QPushButton.
Импорт из модула PySide6.QtCore класса размеров двухмерных объектов QSize и класса Qt,
содержащего различные идентификаторы, используемые в библиотеке Qt.
Импорт из модуля PySide6.QtSql класса для установления связи с базой данных QSqlDatabase, 
класса модели таблиц QSqlTableModel.
"""

db = QSqlDatabase('QSQLITE')  # создание экземпляра объекта базы данных с присвоением имени
db.setDatabaseName('chinook.sqlite')  # указание имени файл базы данных
db.open()  # команда на открытие базы данных


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        form = QFormLayout()  # создание экземпляра класса слоев с построчной организацией
        # виджетов в форму (похоже на слой с вертикальной организацией QVBoxLayout)
        self.track_id = QSpinBox()  # создание экземпляра спин бокса для установки номера трека
        self.track_id.setRange(0, 2147483647)  # установка диапазона возможных значений
        self.track_id.setDisabled(True)  # отключение возможности ввода значения в ручную в поле
        self.name = QLineEdit()  # создание экземпляра текстового поля для ввода название трека
        self.album = QComboBox()  # создание экземпляра выпадающего списка с выбором названия альбома
        self.media_type = QComboBox()  # создание экземпляра выпадающего списка с выбором типа носителя
        self.genre = QComboBox()  # создание экземпляра выпадающего списка с выбором музыкального жанра
        self.composer = QLineEdit()  # создание экземпляра текстового поля для ввода имени композитора
        self.milliseconds = QSpinBox()  # создание спин бокса для установки продолжительности трека
        self.milliseconds.setRange(0, 2147483647)  # установка диапазона возможных значений
        self.milliseconds.setSingleStep(1)  # установка шага изменения значений
        self.bytes = QSpinBox()  # создание спин бокса для установки размера файла трека в байтах
        self.bytes.setRange(0, 2147483647)  # установка диапазона возможных значений
        self.bytes.setSingleStep(1)  # установка шага изменения значений
        self.unit_price = QDoubleSpinBox()  # создание экземпляра класса спин бокса для установки стоимости трека
        self.unit_price.setRange(0, 999)  # установка диапазона значений
        self.unit_price.setSingleStep(0.01)  # установка шага изменений значения
        self.unit_price.setPrefix('$')  # установка префикса для значений поля
        form.addRow(QLabel('Track ID'), self.track_id)  # вставка в форму строки из ярлыка и поля с ID трека
        form.addRow(QLabel('Track name'), self.name)  # вставка в форму строки из ярлыка и поля с названием трека
        form.addRow(QLabel('Composer'), self.composer)  # вставка в форму строки из ярлыка и поля с именем композитора
        form.addRow(QLabel('Milliseconds'), self.milliseconds)  # вставка в форму строки из ярлыка и поля с
        # продолжительностью трека
        form.addRow(QLabel('Bytes'), self.bytes)  # вставка в форму строки из ярлыка и поля с размером файла в байтах
        form.addRow(QLabel('Unit Price'), self.unit_price)  # вставка в форму строки из ярлыка и поля с ценой трека
        self.model = QSqlTableModel(db=db)  # создание модели таблицы с установкой связи с базой данных
        self.mapper = QDataWidgetMapper()  # создание экземпляра маппера для работы с таблицей базы данных
        self.mapper.setModel(self.model)  # привязка модели таблицы к мапперу
        self.mapper.addMapping(self.track_id, 0)  # установка связи поля и колонки таблицы
        self.mapper.addMapping(self.name, 1)  # установка связи поля и колонки таблицы
        self.mapper.addMapping(self.composer, 5)  # установка связи поля и колонки таблицы
        self.mapper.addMapping(self.milliseconds, 6)  # установка связи поля и колонки таблицы
        self.mapper.addMapping(self.bytes, 7)  # установка связи поля и колонки таблицы
        self.mapper.addMapping(self.unit_price, 8)
        self.model.setTable('Track')  # выбор таблицы из модели для передачи в маппер
        self.model.select()  # чтение данных из таблицы базы данных в модель
        self.mapper.toFirst()  # установка курсора маппера на первую запись
        self.setMinimumSize(QSize(400, 400))  # установка минимального размера главного окна приложения
        controls = QHBoxLayout()  # создание экземпляра класса слоя в горизонтальной организацией виджетов
        prev_rec = QPushButton('Previous')  # создание кнопки для перемещения курсора на предыдущую запись
        prev_rec.clicked.connect(self.mapper.toPrevious)  # создание сигнала на переход к предыдущей записи
        next_rec = QPushButton('Next')  # создание кнопки для перемещения курсора к следующей записи
        next_rec.clicked.connect(self.mapper.toNext)  # создание сигнала на переход к следующей записи
        save_rec = QPushButton('Save Changes')  # создание кнопки для записи изменений
        save_rec.clicked.connect(self.mapper.submit)  # создание сигнала на запись изменений в базу
        controls.addWidget(prev_rec)  # размещение виджета кнопки на слое
        controls.addWidget(next_rec)  # размещение виджета кнопки на слое
        controls.addWidget(save_rec)  # размещение виджета кнопки на слое
        layout = QVBoxLayout()  # создание слоя с вертикальной организацией элементов
        layout.addLayout(form)  # размещение на слое слоя форм
        layout.addLayout(controls)  # размещение на слое слоя с кнопками управления
        widget = QWidget()  # создание контейнера для размещения слоя с виджетами
        widget.setLayout(layout)  # размещение слоя в контейнере
        self.setCentralWidget(widget)  # размещение контейнера в главном окне приложения


def main() -> None:
    """
    Функция запуска кода верхнего уроня приложения
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий главного окна приложения
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # установка видимости окна, по умолчанию окно скрыто
    app.exec()  # запуск основного цикла событий главного окна приложения


if __name__ == '__main__':  # конструкция для предотвращения запуска кода верхнего уровня при импортировании
    # данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
