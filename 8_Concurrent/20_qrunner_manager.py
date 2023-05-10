"""
Пример менеджера потоков для управления рабочими потоками
и отслеживания их состояния.
Для этого используем два класса из модуля PySide6.QtCore:
QRunnable - контейнер для кода, который необходимо выполнить
QThreadPool - менеджер рабочих потоков.
Также понадобиться класс декоратора Slot и класс сигнала Signal
"""
import subprocess
import sys
import time
import uuid
import random
import traceback

from PySide6.QtWidgets import (QApplication,
                               QListView,
                               QPlainTextEdit,
                               QVBoxLayout,
                               QMainWindow,
                               QPushButton,
                               QWidget,
                               QProgressBar,
                               QStyledItemDelegate
                               )
from PySide6.QtCore import (QRunnable,
                            Qt,
                            Slot,
                            QThreadPool,
                            Signal,
                            QObject,
                            QAbstractListModel,
                            QTimer,
                            QRect,
                            )
from PySide6.QtGui import QPen, QColor, QBrush

"""
Модуль subprocess для работы с внешними процессами
Модуль traceback для работы с трассировками стека программы.
Модуль для работы со случайностью random
Модуль uuid для генерации уникальных идентификаторов
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс виджета многострочного редактируемого текстового поля QLineEdit, класс базового виджета QWidget,
класс виджета индикатора прогресса QProgressBar, класс отображения списка для модели списка QListView,
класс QStyledItemDelegate предоставляет средства отображения и редактирования элементов данных из модели.
Импорт из модуля PySide6.QtCore класс контейнера для исполняемого кода QRunnable,
класс менеджера потоков QThreadPool, класс декоратора Slot, класс сигнала Signal, класс базового объекта QObject,
класса для работы с таймером QTimer, абстрактный класс модели списка QAbstractListModel, класс прямоугольника QRect
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля PySide6.QtGui класс для установки размера пера (толщины линии)
и цвета для рисования QPen, класс объекта цветов QColor, класса кисти QBrush для закрашивания.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

STATUS_WAITING = 'waiting'
STATUS_RUNNING = 'running'
STATUS_ERROR = 'error'
STATUS_COMPLETE = 'complete'

STATUS_COLOR = {
    STATUS_RUNNING: '#33a02c',
    STATUS_ERROR: '#e31a1c',
    STATUS_COMPLETE: '#b2bf8a'
}

DEFAULT_STATE = {'progress': 0, 'status': STATUS_WAITING}


class WorkerSignals(QObject):
    """
    Класс сигналов рабочего потока, определяющий набор сигналов
    Перечень поддерживаемых сигналов:
    finished - нет данных или произвольная строка
    error - кортеж вида (exctype, value, traceback.format_exc()) где элементы являются строками
    result - любой объект
    progress - целое число или строка - процент выполнения
    status - строка
    """
    finished = Signal(str)
    error = Signal(str, str)
    result = Signal(str, object)
    progress = Signal(str, int)
    status = Signal(str, str)


class Worker(QRunnable):
    """
    Рабочий поток - подкласс контейнера для исполняемого кода.
    Наследуется от супер класса QRannable для управления рабочими потоками, сигналами c
    результатами работы.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Конструктор рабочего потока.
        :param args: аргументы для передачи на обработку рабочему потоку
        :param args: ключевые аргументы для передачи на обработку рабочему потоку
        """
        QRunnable.__init__(self)  # явный вызов конструктора родительского класса
        self.signals = WorkerSignals()  # создание экземпляра класса сигналов рабочего потока
        self.job_id = str(uuid.uuid4())  # создание уникального идентификатора рабочего потока
        self.args = args  # сохранение аргументов в аттрибуте рабочего потока
        self.kwargs = kwargs  # сохранение ключевых аргументов в аттрибуте рабочего потока
        self.signals.status.emit(self.job_id, STATUS_WAITING)  # передача данных рабочего потока при его создании
        # сигналу получения статуса. При создании рабочему потоку присваивается статус Ожидает

    @Slot  # данный декоратор помечает метод как слот с кодом для исполнения
    def run(self):
        """
        Код, который необходимо выполнить помещаем в метод с именем run()
        Данный код имеет заложенную вероятность возникновения ошибки при делении на ноль
        """
        self.signals.status.emit(self.job_id, STATUS_RUNNING)  # передача данных рабочего потока при его запуске
        # сигналу получения статуса. При запуске рабочему потоку присваивается статус Выполняется
        x, y = self.args  # распаковка аргументов в переменные
        try:  # блок обработки исключений
            value = random.randint(0, 100) * x  # создание случайной величины
            delay = random.random() / 10  # создание случайной величины задержки
            result = []  # создание списка для хранения результата
            for n in range(100):  # создание цикла вычислительной нагрузки и генерации результата
                value = value / y  # вычисление некоего значения, при y=0 будет сгенерировано исключение
                y -= 1
                result.append(value)  # сохранение вычисленного значения в списке результатов
                self.signals.progress.emit(self.job_id, n + 1)  # передача данных о прогрессе выполнения
                # сигналу о его изменении
                time.sleep(delay)  # запуск задержки выполнения
        except Exception as e:  # перехват исключения
            print(e)  # вывод текста ошибки
            self.signals.error.emit(self.job_id, str(e))  # передача данных об ошибке сигналу получения ошибки
            self.signals.status.emit(self.job_id, STATUS_ERROR)  # передача данных рабочего потока
            # при возникновении ошибки сигналу о получении статуса рабочего процесса
        else:  # блок если ошибки не возникло
            self.signals.result.emit(self.job_id, result)  # передача результатов работы рабочего потока
            # сигналу о получении результата
            self.signals.status.emit(self.job_id, STATUS_COMPLETE)  # передача данных рабочего потока
            # при его успешном завершении сигналу о получении статуса

        self.signals.finished.emit(self.job_id)  # передача идентификатора рабочего потока сигналу
        # о завершении его выполнения


class WorkerManager(QAbstractListModel):
    """
    Класс менеджера потоков, образованный от абстрактного класса модели списка.
    Менеджер потоков управляет очередью рабочих потоков и обрабатывает их состояния.
    Также менеджер потоков выполняет функцию модели данных для отображения
    индикации прогресса выполнения для каждого потока
    """
    _workers = {}  # создание словаря для хранения ссылок на рабочие потоки
    _state = {}  # создание словаря для хранения состояний рабочих потоков
    status = Signal(str)  # создание сигнала рабочего потока о его состоянии

    def __init__(self):
        """
        Конструктор менеджера потоков и модели данных
        """
        QAbstractListModel.__init__(self)  # явный вызов конструктора родительского класса
        self.threadpool = QThreadPool()  # создание экземпляра менеджера рабочих потоков
        self.max_threads = self.threadpool.maxThreadCount()  # получение информации о
        # максимально возможном количестве рабочих потоков для конкретной системы
        print(f'Multithreading with maximum {self.max_threads} threads')  # вывод числа потоков
        self.status_timer = QTimer()  # создание таймера статуса для менеджера потоков
        self.status_timer.setInterval(100)  # установка интервала вывода состояния потоков (загрузки системы)
        self.status_timer.timeout.connect(self.notify_status)  # создание сигнала на истечение
        # таймера статуса потоков и привязка метода для его передачи сигналу на вывод
        self.status_timer.start()  # запуск таймера опроса статуса потоков (загрузки системы)

    def notify_status(self) -> None:
        """
        Метод для формирования и передачи состояния потоков по загрузке рабочими потоками
        :return: None
        """
        n_workers = len(self._workers)  # определение общего количества рабочих потоков, переданных менеджеру
        running = min(n_workers, self.max_threads)  # вычисление количества выполняющихся потоков
        waiting = max(0, n_workers - self.max_threads)  # вычисление количества потоков, ожидающих в очереди
        self.status.emit(f'{running} running, {waiting} waiting, {self.max_threads} threads')
        # передача данных о состоянии потоков (загрузки системы) сигналу рабочего потока

    def enqueue(self, worker: QRunnable) -> None:
        """
        Метод для постановки рабочего потока в очередь на выполнение
        путем передачи его менеджеру потоков QThreadPoll
        :param worker: объект рабочего потока
        :return: None
        """
        worker.signals.error.connect(self.receive_error)  # создание сигнала об ошибке с привязкой метода ресивера
        worker.signals.status.connect(self.receive_status)  # создание сигнала о статусе с привязкой метода ресивера
        worker.signals.progress.connect(self.receive_progress)  # создание сигнала о прогрессе выполнения
        # с привязкой метода ресивера
        worker.signals.finished.connect(self.done)  # создание сигнала о завершении потока с привязкой метода ресивера
        self.threadpool.start(worker)  # запуск рабочего потока на выполнение
        self._workers[worker.job_id] = worker  # сохранение ссылки на рабочий поток
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def receive_status(self, job_id: str, status: str) -> None:
        """
        Метод для получения и сохранения статуса рабочего потока
        :param job_id: - уникальный идентификатор рабочего потока
        :param status: - статус рабочего потока
        :return: None
        """
        self._state[job_id]['status'] = status  # сохранение информации о состоянии потока
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def receive_progress(self, job_id: str, progress: int) -> None:
        """
        Метод для получения и сохранения прогресса выполнения рабочего потока
        :param job_id: - уникальный идентификатор рабочего потока
        :param progress: - прогресс выполнения рабочего потока
        :return: None
        """
        self._state[job_id]['progress'] = progress  # сохранение информации о состоянии потока
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    @staticmethod
    def receive_error(job_id: str, message: str) -> None:
        """
        Метод для получения и вывода сообщения об ошибке рабочего потока
        :param job_id: - уникальный идентификатор рабочего потока
        :param message: - сообщение об ошибке рабочего потока
        :return: None
        """
        print(job_id, message)

    def done(self, job_id: str) -> None:
        """
        Метод по завершении рабочего потока удаляет его из словаря с активными рабочими потоками
        В словаре состояний информации о потоке не удаляется для обеспечения возможности индикации
        выполненных рабочих потоков
        :param job_id: уникальный идентификатор рабочего потока
        :return: None
        """
        del self._workers[job_id]
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def cleanup(self) -> None:
        """
        Метод для удаления всех выполненных или сбойных рабочих потоков из словаря состояний
        :return:
        """
        for job_id, s in list(self._state.items()):
            if s['status'] in (STATUS_COMPLETE, STATUS_ERROR):
                del self._state[job_id]
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def data(self, index, role: int) -> str:
        """
        Метод, возвращающий статус рабочего потока
        :param index: QModelIndex или QPersistentModelIndex объект индексации модели данных
        :param role: код роли рабочего потока
        :return: str
        """
        if role == Qt.DisplayRole:  # проверка наличия роли отображения
            job_ids = list(self._state.keys())  # создание списка идентификаторов рабочих процессов
            job_id = job_ids[index.row()]
            return job_id, self._state[job_id]

    def rowCount(self, index) -> int:
        """
        Метод для подсчета количества зарегистрированных потоков
        :param index: QModelIndex или QPersistentModelIndex объект индексации модели данных
        :return: - количество строк
        """
        return len(self._state)


class ProgressBarDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        job_id, data = index.model().data(index, Qt.DisplayRole)  # извлечение из объекта индекса модели
        # идентификатора рабочего потока и словаря состояний, который содержит статус и прогресс, в переменные
        if data['progress'] > 0:
            color = QColor(STATUS_COLOR[data['status']])  # создание объекта цвета для строки
            brush = QBrush()  # создание экземпляра класса кисти для закрашивания
            brush.setColor(color)  # установка цвета закрашивания
            brush.setStyle(Qt.SolidPattern)  # установка стиля (узора) закрашивания - сплошной
            width = option.rect.width() * data['progress'] / 100  # вычисление ширины области закрашивания
            rect = QRect(option.rect)  # создание экземпляра класса прямоугольника для закрашивания
            rect.setWidth(width)  # установка ширины области закрашивания для строки
            painter.fillRect(rect, brush)  # закрашивание прямоугольника согласно настройками кисти
        pen = QPen()  # создание экземпляра класса пера
        pen.setColor(Qt.black)  # установка цвета пера
        painter.drawText(option.rect, Qt.AlignLeft, job_id)  # вывод уникального идентификатора рабочего потока
        # в прямоугольник для закрашивания


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла событий приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    app.setStyle('Fusion')  # более интересная глобальная кроссплатформенна тема Fusion
    window.show()  # установка видимости главного окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
