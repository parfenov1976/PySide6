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

from PySide6.QtWidgets import (QApplication,
                               QPlainTextEdit,
                               QVBoxLayout,
                               QMainWindow,
                               QPushButton,
                               QWidget,
                               QProgressBar
                               )
from PySide6.QtCore import (QRunnable,
                            Qt,
                            Slot,
                            QThreadPool,
                            Signal,
                            QObject,
                            QAbstractListModel,
                            QTimer
                            )

"""
Модуль subprocess для работы с внешними процессами
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс виджета многострочного редактируемого текстового поля QLineEdit, класс базового виджета QWidget,
класс виджета индикатора прогресса QProgressBar.
Импорт из модуля PySide6.QtCore класс контейнера для исполняемого кода QRunnable,
класс менеджера потоков QThreadPool, класс декоратора Slot, класс сигнала Signal, класс базового объекта QObject,
класса для работы с таймером QTimer, абстрактный класс модели списка QAbstractListModel
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""


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


def main() -> None:
    """
    Функция запуска кода приложения верхнего уровня
    :return: None
    """
    app = QApplication(sys.argv)  # создание экземпляра класса основного цикла событий приложения
    window = MainWindow()  # создание экземпляра класса главного окна приложения
    window.show()  # установка видимости главного окна (по умолчанию окно спрятано)
    app.exec()  # запуск основного цикла событий приложения


if __name__ == '__main__':  # данная конструкция предотвращает запуск кода верхнего уровня
    # при импортировании данного файла как модуля
    main()  # вызов функции запуска кода верхнего уровня приложения
