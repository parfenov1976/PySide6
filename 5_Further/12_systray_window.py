"""
Пример создания иконки для лотка (трея) панели задач с привязкой к ней меню действий.
В данном примере представлен вариант полного приложения.
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QMenu,
                               QSystemTrayIcon,
                               QTextEdit
                               )
from PySide6.QtGui import QAction, QIcon

"""
Модуль os нужен для создания путей к файлам для разных платформ.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля QtCore класса QSize для управления размерами объектов и класса
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
класса основного окна QMainWindow, класса виджета панели инструментов меню, класса виджета
иконки для лотка (трея) панели задач QSystemTrayIcon, класса виджета многострочного текстового
поля QTextEdit.
Импорт из модуля QtGui класса эффектов действия QAction, класса для создания иконок QIcon.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


class MainWindow(QMainWindow):
    """
    Подкласс главного окна приложения с наследованием от супер класса главных окон
    """

    def __init__(self, app: QApplication) -> None:
        """
        Конструктор главного окна приложения
        :param app:  ссылка на экземпляр основного цикла главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        app.setQuitOnLastWindowClosed(False)  # Устанавливает возможность продолжения работы приложения
        # при закрытии его окон
        icon = QIcon('animal-penguin.png')  # создание иконки из графического файла
        self.tray = QSystemTrayIcon()  # создание экземпляра класса виджета иконки для лотка (трея) панели задач
        self.tray.setIcon(icon)  # привязка иконки к виджету иконки лотка панели задач
        self.tray.setVisible(True)  # разрешение видимости иконки для панели задач
        self.tray.activated.connect(self.activate)
        app.aboutToQuit.connect(self.save)
        self.editor = QTextEdit()  # создание экземпляра класса многострочного текстового поля
        self.load()  # вызов метода загрузки текста из файла
        menu = self.menuBar()  # создание панели меню в главном окне приложения
        file_menu = menu.addMenu('&File')  # добавление на панель меню Файл
        self.reset = QAction('&Reset')  # создание экземпляра класса эффекта действия с указанием его наименования
        self.reset.triggered.connect(self.editor.clear)  # создание сигнала для эффекта действия, выполняющего команду
        # очистки текстового поля
        file_menu.addAction(self.reset)  # добавление в меню Файл действия на очистку текстового поля
        self.quit = QAction('&Quit')  # создание экземпляра класса эффекта действия с указанием его наименования
        self.quit.triggered.connect(app.quit)  # создание сигнала для эффекта действия, выполняющего команду выхода
        file_menu.addAction(self.quit)
        self.setCentralWidget(self.editor)
        self.setWindowTitle('PenguinNotes')

    def load(self) -> None:
        """
        Метод ресивер (слот), который загружает текст из файла в текстовое поле
        :return: None
        """
        with open('notes.txt', 'r') as f:  # Открытие файла на чтение с помощью менеджера контекста
            # если файл не существует, будет выброшено исключение
            text = f.read()  # чтение текст из файла в переменную
        self.editor.setPlainText(text)  # передача текста из переменной в текстовое поле

    def save(self) -> None:
        """
        Метод ресивер (слот), который сохраняет текст в файл из текстового поля
        :return: None
        """
        text = self.editor.toPlainText()  # чтение текста из текстового поля в переменную
        with open('notes.txt', 'w') as f:  # открытие файла на запись с помощью менеджера контекста
            f.write(text)  # запись файла из переменной в файл

    def activate(self, reason: QSystemTrayIcon) -> None:
        """
        Метод ресивер (слот), при активации выводящий окно приложения
        :param reason:  QSystemTrayIcon - событие активации (клика на иконке приложения в лотке панели задач)
        :return: None
        """
        if reason == QSystemTrayIcon.Trigger:  # проверка условия активации
            if self.isVisible():  # проверка условия видимости окна приложения
                self.hide()  # спрятать окно приложения
            else:
                self.show()  # показать окно приложения


def main() -> None:
    """
    Функция запуска кода верхнего уроня приложения
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра основного цикла главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window = MainWindow(app)  # создание экземпляра главного окна приложения
    app.exec()  # запуска основного цикла главного окна приложения


if __name__ == '__main__':  # данное условие нужно для предотвращения запуска кода верхнего уровня при
    # импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
