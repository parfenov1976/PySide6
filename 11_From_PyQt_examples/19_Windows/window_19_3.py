"""
Пример размещения окна точно по центру экрана, с учетом заголовка и толщины границ окна
Если требуется поместить окно точно в центре экрана, следует воспользоваться методом frameSize().
Однако этот метод возвращает корректные значения лишь после вывода окна.
Если код выравнивания по центру расположить после вызова метода show(),
окно вначале отобразится в одном месте экрана, а затем переместится в центр,
что вызовет неприятное мелькание. Чтобы исключить такое мелькание,
следует вначале вывести окно за пределами экрана, а затем переместить его в центр
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget

"""
Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
к аргументам командной строки. Если использование аргументов командной строки не предполагается,
то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
в качестве аргумента передается пустой.

Импорт из модуля PySide6.QWidgets класса управления приложением QApplication,
класса базового пустого виджета QWidget
"""

app = QApplication(sys.argv)  # создание основного цикла событий приложения
app.setStyle('Fusion')  # установка более красивой темы (стиля) для графического интерфейса
window = QWidget()  # создание окна
window.setWindowTitle('Вывод окна точно по центру экрана')  # установка заголовка окна
window.resize(300, 100)  # установка исходного размера окна
window.move(window.width() * 2, 0)  # установка положения окна за пределами экрана
window.show()  # показать окно, по умолчанию окно скрыто
screen_size = window.screen().availableSize()  # извлечение размера доступной области экрана без учета рабочей панели
x = (screen_size.width() - window.frameSize().width()) // 2
y = (screen_size.height() - window.frameSize().height()) // 2
window.move(x, y)  # установка положения окна относительно родителя с учетом размера заголовка и толщины границ
sys.exit(app.exec())  # Запуск основного цикла событий главного окна приложения.
# Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
# выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
