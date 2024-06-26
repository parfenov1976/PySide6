"""
Списки и таблицы. Роли элементов

Каждый элемент списка хранит набор величин, каждая из которых относится к определенной
роли: текст элемента, шрифт и цвет, которыми отображается элемент, текст всплывающей
подсказки и многое другое. Приведем роли элементов (элементы перечисления
ItemDataRole из модуля QtCore. Qt):
♦ DisplayRole - отображаемые данные (обычно текст);
♦ DecorationRole - изображение (обычно значок);
♦ EditRole - данные в виде, удобном для редактирования;
♦ ToolTipRole - текст всплывающей подсказки;
♦ StatusTipRole - текст для строки состояния;
♦ WhatsThisRole - текст для расширенной подсказки;
♦ FontRole - шрифт элемента (объект класса QFont);
♦ TextAlignmentRole - выравнивание текста внутри элемента;
♦ BackgroundRole - фон элемента (объект класса QBrush);
♦ ForegroundRole - цвет текста (объект класса QBrush);
♦ CheckStateRole - статус флажка. Могут быть указаны следующие элементы перечисления
  CheckState из модуля QtCore.Qt:
  • Unchecked - флажок сброшен;
  • PartiallyChecked - флажок частично установлен;
  • Checked - флажок установлен;
♦ AccessibleTextRole - текст, выводящийся специализированными устройствами вывода
  (например, системами чтения с экрана);
♦ AccessibleDescriptionRole - описание элемента, выводящееся специализированными
  устройствами вывода (например, системами чтения с экрана);
♦ SizeHintRole -рекомендуемый размер элемента (объект класса QSize);
♦ UserRole (32) - любые пользовательские данные (например, индекс элемента в базе
  данных). Можно сохранить несколько данных, указав их в роли с индексом более 32,
  например:
  comboBox.setItemData(O, 50, role=QtCore.Qt.ItemDataRole.UserRole)
  comboBox.setItemData(O, "Другие данные",
                            role=QtCore.Qt.ItemDataRole.UserRole + 1)
"""
from PySide6.QtWidgets import (QMainWindow,
                               QComboBox,
                               QTextEdit,
                               QVBoxLayout,
                               QWidget,
                               )
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


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
        # super().__init__(parent)  # вызов конструктора родительского класса через функцию super()
        self.setWindowTitle('Роли элементов списков и таблиц')  # установка заголовка главного окна
        self.statusBar()  # включение строки статуса
        self.resize(300, 300)  # установка исходного размера главного окна
        self.combobox = QComboBox()  # создание списка
        self.combobox.addItem('Data w/o role', 123)
        # данные отображается в UserRole, текст в DisplayRole
        self.combobox.addItem('Display Role')
        self.combobox.setItemData(1, 'Data', role=Qt.ItemDataRole.DisplayRole)
        # отображается вместо текста элемента в списке
        self.combobox.addItem('Decoration Role')
        self.combobox.setItemData(2, 'Decorator', role=Qt.ItemDataRole.DecorationRole)
        self.combobox.addItem('Edit Role')
        self.combobox.setItemData(3, 'Editing', role=Qt.ItemDataRole.EditRole)
        # отображается вместо текста элемента в списке
        self.combobox.addItem('Tool Tip Role')
        self.combobox.setItemData(4, 'Tips', role=Qt.ItemDataRole.ToolTipRole)
        # подсказка отображается при удержании курсора на элементе списка
        self.combobox.addItem('Status Tip Role')
        self.combobox.setItemData(5, 'Status', role=Qt.ItemDataRole.StatusTipRole)
        # автоматом в строку статуса ничего не попадает
        self.combobox.addItem('Whats this Role')
        self.combobox.setItemData(6, 'This is item', role=Qt.ItemDataRole.WhatsThisRole)
        self.combobox.addItem('Font Role')
        self.combobox.setItemData(7, QFont("Times"), role=Qt.ItemDataRole.FontRole)
        self.combobox.addItem('Check state role')
        self.combobox.setItemData(8, Qt.CheckState.Checked, role=Qt.ItemDataRole.CheckStateRole)

        self.combobox.activated.connect(self.activation)

        self.text_field = QTextEdit()  # создание текстового поля

        self.vbox = QVBoxLayout()  # создание вертикальной стопки для виджетов
        self.vbox.addWidget(self.combobox)  # добавление виджета в стопку
        self.vbox.addWidget(self.text_field)
        self.container = QWidget()  # создание контейнера для слоев с виджетами
        self.container.setLayout(self.vbox)  # размещение слоя с виджетами в контейнере
        self.setCentralWidget(self.container)  # размещение контейнера с виджетами в главном окне
        self.list_roles = {'Qt.ItemDataRole.DisplayRole': Qt.ItemDataRole.DisplayRole,
                           'Qt.ItemDataRole.UserRole': Qt.ItemDataRole.UserRole,
                           'Qt.ItemDataRole.DecorationRole': Qt.ItemDataRole.DecorationRole,
                           'Qt.ItemDataRole.EditRole': Qt.ItemDataRole.EditRole,
                           'Qt.ItemDataRole.ToolTipRole': Qt.ItemDataRole.ToolTipRole,
                           'Qt.ItemDataRole.StatusTipRole': Qt.ItemDataRole.StatusTipRole,
                           'Qt.ItemDataRole.WhatsThisRole': Qt.ItemDataRole.WhatsThisRole,
                           'Qt.ItemDataRole.FontRole': Qt.ItemDataRole.FontRole,
                           'Qt.ItemDataRole.CheckStateRole': Qt.ItemDataRole.CheckStateRole,
                           }

    def activation(self, index: int) -> None:
        """
        Обработчик выбора пункта выпадающего списка
        :param index: int - индекс элемента в списке
        :return: None
        """
        self.text_field.clear()
        self.text_field.append(f'Текст элемента: {self.combobox.itemText(index)}\n')
        self.text_field.append('Данные элемента по ролям')
        for el in self.list_roles.items():
            self.text_field.append(f'{el[0]}: {self.combobox.itemData(index, role=el[1])}')


if __name__ == '__main__':  # проверка условия запуска для предотвращения исполнения
    # кода верхнего уровня при импортировании данного файла как модуля
    from PySide6.QtWidgets import QApplication
    import sys

    """
    Импорт из модуля PySide6.QtWidgets класса управления приложением QApplication
    Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
    к аргументам командной строки. Если использование аргументов командной строки не предполагается,
    то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
    в качестве аргумента передается пустой.
    """
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # включение видимости окна, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
