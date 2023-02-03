"""
Пример приложения списка дел с использованием архитектуры QT Model/View (специфичного
для PyQt и PySide варианта архитектуры Model View Controller (MVC))
"""

import sys
from MainWindow import Ui_MainWindow  # импорт скомпилированного в питон файла UI из Qt Designer
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QAbstractListModel

"""
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и
класса основного окна QMainWindow, класса ярлыка QLabel.
Импорт из модула PySide6.QtCore абстрактного класса QAbstractListModel, предоставляющего стандартный 
интерфейс для моделей, которые представляют свои данные в виде простой неиерархической 
последовательности элементов (списка). Он не используется напрямую, но должен быть подклассом.
Qt из модуля PySide6.QtCore содержит различные идентификаторы, используемые в библиотеке Qt.
"""


# tag::model[]
class TodoModel(QAbstractListModel):
    """
    Подкласс модели списка дел от абстрактного супер-класса моделей списков
    """

    def __init__(self, todos: list = None) -> None:
        """
        Конструктор класса модели списков дел
        :param todos: список
        """
        QAbstractListModel.__init__(self)  # явный запуск конструктора родительского класса
        self.todos = todos or []  # создание атрибута для хранения списка дел с инициализацией
        # списком, подаваемым в качестве аргумента при создании экземпляра класса модели списка
        # или пустым списком

    def data(self, index, role: int) -> str:
        """
        Метод для обработки запросов из представления на выборку данных из списка
        :param index: координаты запрашиваемых данных предоставляемых методами .row() и .column()
        в списке index.column() всегда выдает 0. index является экземпляром классов QModelIndex
        QPersistentModelIndex из библиотеки PySide6.QtCore.
        :param role: int - код типа данных. Подробнее https://doc.qt.io/qt-5/qt.html#ItemDataRole-enum
        :return: str - наименование запрошенного дела
        """
        if role == Qt.DisplayRole:  # проверка соответствия данных роли текстовой строки (role=0)
            status, text = self.todos[index.row()]  # извлечение данных из записи - статуса и наименования дела
            return text

    def rowCount(self, index) -> int:
        """
        Метод подсчета количества записей в списке дел
        :param index:
        :return: int - количество записей
        """
        return len(self.todos)


# tag::model[]

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        # Вызывать конструктор Ui_MainWindow не нужно так как у этого супер-класса его нет
        self.setupUi(self)  # вызов метода сборки интерфейса из модуля главного окна MainWindow
        self.model = TodoModel()  # создание экземпляра класса модели списка дел
        self.todo_view.setModel(self.model)  # привязка модели к виджету списка подкласса главного окна
        self.add_button.pressed.connect(self.add)  # создание сигнала кнопки добавить и привязка метода ресивера

    def add(self) -> None:
        """
        Метода добавления записи в список дел
        :return: None
        """
        text = self.todo_edit.text()  # извлечение строки из однострочного редактируемого поля в переменную
        text = text.strip()  # удаление пробелов с концов строки
        if text:  # проверка, что строка не пустая воз избежания добавления пустых записей
            self.model.todos.append((False, text))  # добавление записи в список в виде кортежа из статуса
            # и наименования дела
            self.model.layoutChanged.emit()  # подача сигнала для представления об изменении данных
            self.todo_edit.setText('')  # создание пустой строки в качестве разделителя пунктов списка


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла событий главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # метод показа главного окна приложения (по умолчанию окно скрыто)
    app.exec()  # запуск основного цикла события главного окна приложения


if __name__ == '__main__':  # конструкция, предотвращающая запуск кода приложения верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода приложения верхнего уровня
