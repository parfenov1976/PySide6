"""
Пример использований встроенного в PySide6 класса QProcess для запуска внешних процессов.
Для этого используем класс из модуля PySide6.QtCore:
QProcess - класс для запуска внешних процессов
В данном примере реализован менеджер внешних процессов
"""
import sys
import re
import uuid

from PySide6.QtWidgets import (QApplication,
                               QListView,
                               QMainWindow,
                               QPlainTextEdit,
                               QStyledItemDelegate,
                               QPushButton,
                               QVBoxLayout,
                               QWidget
                               )

from PySide6.QtCore import (QProcess,
                            QAbstractListModel,
                            QRect,
                            Qt,
                            QTimer,
                            Signal
                            )
from PySide6.QtGui import QPen, QColor, QBrush

"""
Модуль re для работы с регулярными выражениями.
Модуль для работы с уникальными идентификаторами uuid.
Модуль sys нужен для доступа к аргументам командной строки. Если использование аргументов
командной строки не предполагается, то импорт можно не выполнять. При этом, при создании
приложения в класс QApplication([]) в качестве аргумента передается пустой список.
Импорт из модуля PySide6.QtWidgets класса для управления приложением QApplication и класса слоев
для виджетов с вертикальной организацией QVBoxLayout, класса виджета кнопки QPushButton,
класс виджета индикатора прогресса QProgressBar, класс виджета многострочного редактируемого
текстового поля QPlainTextEdit, класс базового виджета QWidget, класс отображения списка для модели списка QListView,
класс QStyledItemDelegate предоставляет средства отображения и редактирования элементов данных из модели.
Импорт из модуля PySide6.QtCore класса для запуска внешних процессов и управления ими QProcess,
абстрактный класс модели списка QAbstractListModel, класс прямоугольника QRect, класса для работы с таймером QTimer,
класс сигнала Signal.
Qt - содержит различные идентификаторы, используемые в библиотеке Qt
Импорт из модуля PySide6.QtGui класс для установки размера пера (толщины линии)
и цвета для рисования QPen, класс объекта цветов QColor, класса кисти QBrush для закрашивания.
Другие виджеты можно найти по ссылке https://doc.qt.io/qt-5/widget-classes.html#basic-widget-classes
"""

STATUS_COLORS = {  # словарь цветов для обозначения состояний
    QProcess.NotRunning: '#b2df8a',
    QProcess.Starting: '#fbdf6f',
    QProcess.Running: '#33a02c'
}

STATES = {  # словарь состояний процессов
    QProcess.NotRunning: "Not running",
    QProcess.Starting: "Starting...",
    QProcess.Running: "Running..."
}

DEFAULT_STATE = {'progress': 0, 'status': QProcess.Starting}  # статус по умолчанию

progress_re = re.compile('Total complete: (\d+)%', re.M)


def simple_percent_parser(output: str) -> int:
    """
    Функция парсер для извлечения значения процента выполнения из строки статуса
    :param output:
    """
    m = progress_re.search(output)  # поиск в строке статуса процента выполнения
    if m:
        pc_complete = m.group(1)  # извлечение процента из матч объекта и запись в переменную
        return int(pc_complete)  # возврат процента выполнения в виде целого чиста


def extract_vars(l):
    """
    Функция парсер, извлекающая из строки результатов равенства и преобразующая их в элементы словаря
    и формирующая словарь результатов работы внешнего процесса
    :param l: строка результатов работы внешнего процесса
    """
    data = {}  # создание словаря для результатов
    for s in l.split():  # рзбиение строки проход по результатам разбиения
        if '=' in s:  # проверка, что подстрока является равенством
            name, value = s.split('=')  # разбиение равенства на подстроки
            data[name] = value  # запись ключа и значения в словарь результатов
    return data


class JobManager(QAbstractListModel):
    """
    Класс менеджера внешних процессов для обработки активных процессов, вывода результатов и ошибок,
    а также результатов работы парсера прогресса
    """
    _jobs = {}  # создаем словарь для хранения ссылок на внешние рабочие процессы
    _state = {}  # создаем словарь для хранения состояний рабочих процессов
    _parsers = {}  # создаем словарь для хранения имен функций парсеров

    status = Signal(str)  # создание сигнала рабочего процесса о его статусе
    result = Signal(str, object)  # создание сигнала рабочего процесса с результатами его работы
    progress = Signal(str, int)  # создание сигнала рабочего процесса с прогрессом выполнения

    def __init__(self) -> None:
        """
        Конструктор менеджера внешних рабочих процессов
        """
        QAbstractListModel.__init__(self)  # явный вызов конструктора родительского класса
        self.status_timer = QTimer()  # создание таймера опроса статусов рабочих процессов
        self.status_timer.setInterval(100)  # установка длительности таймера
        self.status_timer.timeout.connect(self.notify_status)  # создание сигнала на истечение времени таймера
        # с привязкой метода ресивера
        self.status_timer.start()  # запуск таймера
        self.progress.connect(self.handle_progress)  # создание сигнала на получение данных сигнала
        # рабочего процесса о прогрессе его выполнения

    def notify_status(self) -> None:
        """
        Метод ресивер для сигнала об истечении таймера опроса статусов рабочих процессов
        :return: None
        """
        n_jobs = len(self._jobs)  # определение количества рабочих процессов
        self.status.emit(f'{n_jobs} jobs')  # передача данных о количестве рабочих процессов
        # сигналу на отображение количества рабочих процессов

    def execute(self, command: str, arguments: list, parsers=None) -> None:
        """
        Метод для запуска рабочих процессов
        :param command: команда запуска интерпретатора python
        :param arguments: список файлов с кодом для исполнения
        :param parsers: список парсеров, каждый парсер представляется в виде кортежа
                        (имя_функции, "наименование_сигнала")
        :return: None
        """
        job_id = uuid.uuid4().hex  # создание уникального идентификатора для внешнего процесса

        def fwd_signal(target):
            """
            По умолчанию сигналы не имеют доступа к какой-либо информации о процессе,
            который их отправил. Итак, мы используем этот конструктор для подписи
            каждого сигнала с помощью job_id.
            :param target: ссылка на функцию обработчика состояния
            :return: анонимная функция - вызов функции обработчика с идентификатором рабочего процесса,
                     принимающей аргументы
            """
            return lambda *args: target(job_id, *args)  # возвращение подписанного обработчика через анонимную функцию

        self._parsers[job_id] = parsers or []  # сохранение списка парсеров в словаре под ключом идентификатора процесса
        self._state[job_id] = DEFAULT_STATE.copy()  # сохранение состояния по умолчанию в словаре состояний под ключом
        # идентификатора процесса
        p = QProcess()  # создание объекта рабочего процесса
        p.readyReadStandardOutput.connect(fwd_signal(self.handle_output))  # создание сигнала стандартного вывода
        # результата с привязкой обработчика, который подписывается идентификатором процесса
        p.readyReadStandardError.connect(fwd_signal(self.handle_output))  # создание сигнала стандартного вывода ошибки
        # с привязкой обработчика, который подписывается идентификатором процесса
        p.stateChanged.connect(fwd_signal(self.handle_state))  # создание сигнала на изменение состояния
        # рабочего процесса с привязкой обработчика, который подписывается идентификатором процесса
        p.finished.connect(fwd_signal(self.done))  # создание сигнала на завершение выполнения рабочего процесса
        # с привязкой обработчика, который подписывается идентификатором процесса
        self._jobs[job_id] = p  # сохранение ссылки на рабочий процесс в словаре под ключом идентификатора процесса
        p.start(command, arguments)  # запуск рабочего процесса на выполнение
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def handle_output(self, job_id: str) -> None:
        """
        Метод ресивер - обработчика стандартного вывода из рабочего процесса
        :param job_id: идентификатор рабочего процесса
        :return: None
        """
        p = self._jobs[job_id]  # извлечение ссылки на рабочий процесс из словаря по его идентификатору
        stderr = bytes(p.readAllStandardError()).decode('utf8')  # извлечение и декодирования текста ошибки
        # из рабочего процесса
        stdout = bytes(p.readAllStandardOutput()).decode('utf8')  # извлечение и декодирование текста вывода
        # из рабочего процесса
        output = stderr + stdout  # сборка полного вывода
        parsers = self._parsers.get(job_id)  # извлечение списка парсеров по идентификатору рабочего процесса
        for parser, signal_name in parsers:  # цикл по списку парсеров для использования одного за проход
            result = parser(output)  # использование парсера на выводе и сохранение результата в переменной
            if result:  # если результаты есть
                signal = getattr(self, signal_name)  # извлечение имени сигнала из объекта менеджера процессов
                signal.emit(job_id, result)  # передача данных для сигнала из списка сигналов по его имени

    def handle_progress(self, job_id: str, progress: int | str) -> None:
        """
        Метод ресивер - обработчик изменения прогресса выполнения
        :param job_id: идентификатор рабочего процесса
        :param progress: значение прогресса выполнения рабочего процесса
        :return: None
        """
        self._state[job_id]['progress'] = progress  # сохранение прогресса выполнения в словаре состояний
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def handle_state(self, job_id: str, state: str) -> None:
        """
        Метод ресивер - обработчик изменения состояния рабочего процесса
        :param job_id: идентификатор рабочего процесса
        :param state: состояние рабочего процесса
        :return: None
        """
        self._state[job_id]["status"] = state  # сохранение состояния рабочего процесса в словаре состояний
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def done(self, job_id: str, exit_code, exit_status) -> None:
        """
        Метод ресивер - обработчик завершения выполнения процесса
        :param job_id: идентификатор рабочего процесса
        :param exit_code: код выхода процесса
        :param exit_status: состояние выхода
        :return: None
        """
        del self._jobs[job_id]  # удаление рабочего процесса из словаря с ссылками по завершении выполнения
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    def cleanup(self) -> None:
        """
        Метод очистки словаря от сбойных и завершенных рабочих процессов
        :return: None
        """
        for job_id, s in list(self._state.items()):  # проход по словарю с рабочими процессами
            if s['status'] == QProcess.NotRunning:  # проверка состояния рабочего процесса
                del self._state[job_id]  # удаление рабочего процесса из словаря по его идентификатору
        self.layoutChanged.emit()  # передача данных для сигнала на обновление отображения модели

    # Интерфейс модели
    def data(self, index, role: int) -> tuple:
        """
        Метод извлечения данных из модели данных
        :param index: QModelIndex - объект индексирования модели
        :param role: роль данных
        :return: кортеж вида (идентификатор_процесса, состояние)
        """
        if role == Qt.DisplayRole:
            job_ids = list(self._state.keys())  # извлечение идентификаторов рабочих процессов и сохранение их в списке
            job_id = job_ids[index.row()]  # извлечение идентификатора рабочего процесса по объекту 0индексирования
            return job_id, self._state[job_id]  # возврат идентификатора процесса и его состояния (кортеж)

    def rowCount(self, index) -> int:
        """
        Метод подсчета количества активных рабочих процессов
        :param index: QModelIndex объект индексирования модели
        :return: количество активных рабочих процессов
        """
        return len(self._state)


class ProgressBarDelegate(QStyledItemDelegate):
    """
    Класс индикатора прогресса от супер-класса, предоставляющего
    средства отображения и редактирования элементов данных из модели
    """

    def paint(self, painter, option, index) -> None:
        """
        Метод для отрисовки индикатора прогресса
        """
        job_id, data = index.model().data(index, Qt.DisplayRole)  # извлечение из объекта индекса модели
        # идентификатора рабочего потока и словаря состояний, который содержит статус и прогресс, в переменные
        if data['progress'] > 0:
            color = QColor(STATUS_COLORS[data['status']])  # создание объекта цвета для строки
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


class MainWindow(QMainWindow):
    """
    Класс главного окна приложения от супер класса главных окон
    """

    def __init__(self) -> None:
        """
        Конструктор главного окна приложения
        """
        QMainWindow.__init__(self)  # явный вызов конструктора родительского класса
        self.job = JobManager()  # создание экземпляра менеджера рабочих процессов
        self.job.status.connect(self.statusBar().showMessage)  # создание сигнала на вывод состояния рабочих процессов
        # в строку статуса главного окна приложения
        self.job.result.connect(self.display_result)  # создание сигнала результата с привязкой метода ресивера
        layout = QVBoxLayout()  # создание экземпляра слоя для виджетов с вертикальной организацией
        self.progress = QListView()  # создание представления таблицы для вывода прогресса выполнения
        self.progress.setModel(self.job)  # привязка модели к представлению
        delegate = ProgressBarDelegate()  # создание экземпляра класса индикатора прогресса
        self.progress.setItemDelegate(delegate)  # подключение делегата к модели
        layout.addWidget(self.progress)  # размещение представления в слое для виджетов
        self.text = QPlainTextEdit()  # создание текстового многострочного поля
        self.text.setReadOnly(True)  # установка поля в состояние только для чтения
        button = QPushButton("Run a command")  # создание кнопки на запуск команды
        button.pressed.connect(self.run_command)  # создание сигнала на нажатие кнопки с привязкой ресивера
        clear = QPushButton("Clear")  # создание кнопки на очистку
        clear.pressed.connect(self.job.cleanup)  # создание сигнала на очистку с привязкой ресивера
        layout.addWidget(self.text)  # размещение текстового поля в слое для виджетов
        layout.addWidget(button)  # размещение кнопки в слое для виджетов
        layout.addWidget(clear)  # размещение кнопки в слое для виджетов
        w = QWidget()  # создание контейнера для слоев
        w.setLayout(layout)  # размещение слоя в контейнере
        self.setCentralWidget(w)  # размещение контейнера в главном окне приложения

    def run_command(self) -> None:
        """
        Метод ресивер на запуск команды на выполнение кода рабочего процесса
        :return: None
        """
        self.job.execute(
            "python",
            ["dummy_script.py"],
            parsers=[
                (simple_percent_parser, "progress"),
                (extract_vars, "result"),
            ],
        )

    def display_result(self, job_id: str, data: dict) -> None:
        """
        Метод ресивер на отображение результатов работы рабочего процесса
        :param job_id: идентификатор рабочего процесса
        :param data:
        :return: None
        """
        self.text.appendPlainText(f"WORKER {job_id}: {data}")


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
