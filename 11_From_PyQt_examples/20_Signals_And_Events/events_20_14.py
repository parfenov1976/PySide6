"""
События мыши. Нажатие и отпускание кнопок мыши

При нажатии и отпускании кнопок мыши вызываются следующие специальные методы:
♦ mousePressEvent(self, <event>) - вызывается при нажатии кнопки мыши в области
  компонента;.
♦ mouseReleaseEvent(self, <event>) - вызывается при отпускании ранее нажатой кнопки
  мыши;
♦ mouseDoubleClickEvent(self, <event>) - вызывается при двойном щелчке мышью.
  Следует учитывать, что двойному щелчку предшествуют другие события. Последовательность
  событий при двойном щелчке выглядит так:
  MouseButtonPress
  MouseButtonRelease
  MouseButtonDblClick
  MouseButtonPress
  MouseButtonRelease
  Задать интервал двойного щелчка в миллисекундах позволяет статический метод
  setDoubleClickInterval(<Интервал>) класса QApplication, а получить его текущее значение
  - статический метод doubleClickInterval() того же класса.
Через параметр <event> доступен объект класса QMouseEvent, хранящий дополнительную
информацию о событии. Он поддерживает такие методы:
♦ pos() - возвращает объект класса QPoint с целочисленными координатами в пределах
  компонента;
♦ position() - возвращает объект класса QPointF с вещественными координатами в пределах
  компонента;
♦ scenePosition() - возвращает объект класса QPointF с вещественными координатами
  в пределах окна или графической сцены;
♦ globalPosition() - возвращает объект класса QPointF с вещественными координатами
  в пределах экрана;
♦ button() - возвращает обозначение нажатой кнопки мыши в виде одного из следующих
элементов перечисления MouseButton из модуля QtCore.Qt (описаны не все элементы,
полный их список приведен на странице https://doc.qt.io/qt-6/qt.html#MouseButtonenum):
  • NoButton - ни одна кнопка не нажата. Это значение возвращается методом button()
    при перемещении курсора мыши;
  • LeftButton - левая кнопка;
  • RightButton - правая кнопка;
  • MiddleButton - средняя кнопка или колесико;
  • XButton1, ExtraButton1 и BackButton - первая из дополнительных кнопок;
  • XButton2, ExtraButton2 и ForwardButton - вторая из дополнительных кнопок;
♦ buttons() - возвращает обозначение всех нажатых кнопок мыши в виде комбинации
  элементов перечисления MouseButton:
  if e.buttons() & QtCore.Qt.MouseButton.LeftButton:
      print ("Нажата левая кнопка мыши")
♦ modifiers() - позволяет определить, какие клавиши-модификаторы (<Shift>, <Ctrl>,
  <Alt> и др.) были нажаты вместе с кнопкой мыши;
♦ flags () - возвращает дополнительные сведения о событии в виде значения одного из
  элементов перечисления MouseEventFlag из модуля QtCore или их комбинацию. По
  состоянию на сегодня перечисление содержит единственный элемент
  MouseEventCreatedDoubleClick, который устанавливается при возникновении события
  MouseButtonPress, если оно было вызвано-двойным щелчком;
♦ timestamp() - возвращает в виде числа отметку системного времени, в которое возникло
  событие.
Если событие было успешно обработано, следует вызвать метод accept() объекта события.
Чтобы родительский компонент мог получить событие, вместо метода accept() нужно вызвать
метод ignore().
Если у компонента элемент WA_NoMousePropagation перечисления WidgetAttribute из модуля
QtCore.Qt установлен в True, событие мыши не будет передаваться родительскому компоненту.
Значение атрибута можно изменить с помощью метода setAttribute(), вызванного
у этого компонента:
button.setAttribute(QtCore.Qt.WidgetAttribute.WA_NoMousePropagation, True)
По умолчанию событие мыши перехватывает компонент, над которым был произведен
щелчок м􀂲1шью. Чтобы перехватывать нажатие и отпускание мыши вне компонента, следу􀂳
ет захватить мышь вызовом метода grabMouse(). Освободить захваченную ранее мышь позволяет
метод releaseMouse().
"""
import sys
from PySide6.QtWidgets import (QApplication,
                               QPlainTextEdit,
                               )


class MainWindow(QPlainTextEdit):
    """
    Класс главного окна приложения от супер класса многострочного текстового поля
    """

    def __init__(self, parent=None) -> None:
        """
        Конструктор главного окна приложения
        :param parent: ссылка на родительский объект
        """
        QPlainTextEdit.__init__(self, parent)  # явный вызов конструктора родительского класса
        self.setWindowTitle('Нажатие и отпускание кнопок мыши')  # установка заголовка окна приложения
        self.resize(600, 300)  # установка исходного размера окна

    def mousePressEvent(self, event) -> None:
        """
        Обработчик события нажатия кнопки мыши
        :param event: объект события QMouseEvent
        :return: None
        """
        self.appendPlainText(f'Нажата кнопка {event.button()}, по координатам'
                             f' x={event.position().x()}, y={event.position().y()} в момент {event.timestamp()}')
        print(event.scenePosition())
        print(event.globalPosition())
        print(event.buttons())

    def mouseReleaseEvent(self, event) -> None:
        """
        Обработчик события отпускания кнопки мыши
        :param event: объект события QMouseEvent
        :return: None
        """
        self.appendPlainText(f'Отпущена кнопка {event.button()}')

    def mouseDoubleClickEvent(self, event) -> None:
        """
        Обработчик события двойного щелчка кнопки мыши
        :param event: объект события QMouseEvent
        :return: None
        """
        self.appendPlainText(f'Двойной клик кнопкой {event.button()}')


if __name__ == '__main__':  # проверка условия запуска данного файла для предотвращения запуска кода верхнего уровня
    # при импортировании данного файла как модуля
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля графического интерфейса
    window = MainWindow()  # создание главного окна приложения
    window.show()  # вывод окна на экран, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод sys.exit()
