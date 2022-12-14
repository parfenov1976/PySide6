from PySide6.QtWidgets import QApplication, QMainWindow
# Импорт из модуля QtWidgets PySide6 класса для управления приложением QApplication и
# класса виджетов окон QMainWindow.

import sys
# данный модуль нужен для доступа к аргументам командной строки

app = QApplication(sys.argv)
"""
На одно приложение нужен только один экземпляр QApplication.
Передача sys.argv нужна, чтобы обеспечить возможность использования аргументов командной строки для приложения.
Если использование аргументов командной строки не предполагается, то QApplication([]) тоже будет работать. 
[] - пустой список.
"""

window = QMainWindow()  # Создает виджет окна приложения из класса виджетов окон.
window.show()  # Метод для вывода главного окна. По умолчанию окно спрятано.

app.exec()  # Запуск цикла событий, при помощи метода управления приложением.

# Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
# выход и цикл событий не будет остановлен.
