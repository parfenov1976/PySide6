"""
Работа с растровыми изображениями. Класс QPixmap

Класс QPixmap предназначен для работы с изображениями в контекстно-зависимом представлении.
Данные хранятся в виде, позволяющем отображать изображение на экране наиболее
эффективным способом, поэтому класс QPixmap часто используется для предварительного
рисования графики перед выводом ее на экран. Иерархия наследования:
QPaintDevice - QPixmap
Поскольку класс QPixmap наследует класс QPaintDevice, мы можем использовать его как
поверхность для рисования. Вывести изображение позволяет метод drawPixmap() класса
QPainter (см 25_2_3_draw_pics.py).
Форматы конструктора класса:
QPixmap()
QPixmap(<Ширина>, <Высота>)
QPixmap(<Размеры QSize>)
QPixmap(<Путь к файлу>[, format=None] [, flags=Image.ConversionFlag.AutoColor])
QPixmap(<Исходный объект QPixmap>)
Первый формат создает пустой объект изображения. Второй и третий форматы позволяют
указать размеры изображения - если размеры равны нулю, то будет создан пустой объект.
Четвертый формат предназначен для загрузки изображения из файла. Во втором параметре
указывается тип изображения в виде строки (например, "PNG")- если он не указан, то
формат будет определен по расширению загружаемого файла. Пятый конструктор создает
копию указанного изображения.
Класс QPixmap поддерживает следующие методы (здесь приведены только основные - полный
их список можно найти на странице https://doc.qt.io/qt-6/qpixmap.html):
♦ isNull() - возвращает значение True, если объект является пустым, и False - в противном
  случае;
♦ load() - загружает изображение из файла с указанным путем. Формат метода:
  load(<Путь к файлу>[, format=None] [, flags=ImageConversionFlag.AutoColor])
  Во втором параметре можно задать формат файла в виде строки - если он не указан,
  формат определяется по расширению файла. Необязательный параметр flags задает тип
  преобразования цветов. Метод возвращает значение True, если изображение успешно
  загружено, и False - в противном случае;
♦ loadFromData() - загружает изображение из заданного объекта класса QByteArray.
  Формат метода:
  loadFromData(<Объект QByteArray или bytes> [, format=None] [,
               flags=ImageConversionFlag.AutoColor])
  Метод возвращает значение True, если изображение успешно загружено, и False -
  в противном случае;
♦ save(<Путь к файлу>[, format=None] [, quality=-1]) - сохраняет изображение в файл
  с указанным путем. Во втором параметре можно задать формат файла в виде строки -
  если он не указан, формат будет определен по расширению файла. Необязательный
  параметр quality позволяет задать качество изображения. Можно передать значение
  в диапазоне от О до 100, значение -1 указывает качество по умолчанию. Метод возвращает
  значение True, если изображение успешно сохранено, и False - в противном случае;
♦ convertFromImage() - преобразует заданный объект класса QImage в объект класса
  QPixmap. Формат метода:
  convertFromImage(<Изображение QImage>[, flags=ImageConversionFlag.AutoColor])
  Метод возвращает значение True, если изображение успешно преобразовано, и False -
  в противном случае;
♦ fromImage() - статический, преобразует заданный объект класса QImage в объект класса
  QPixmap, который и возвращает. Формат метода:
  fromImage(<Изображение QImage>[, flags=ImageConversionFlag.AutoColor])
♦ toImage() - преобразует текущее изображение в объект класса QImage и возвращает его;
♦ fill([color=GlobalColor.white]) - производит заливку изображения указанным цветом;
♦ width() - возвращает ширину изображения;
♦ height() - возвращает высоту изображения;
♦ size() -возвращает объект класса QSize с размерами изображения;
♦ rect() - возвращает объект класса QRect с координатами и размерами прямоугольной
  области, ограничивающей изображение;
♦ depth() - возвращает глубину цвета;
♦ isQBitmap() - возвращает значение True, если глубина цвета равна одному биту (т. е.
  это монохромное изображение), и False - в противном случае;
♦ createMaskFromColor(<Цвет QColor>[, mode=MaskMode.MaskInColor]>) - создает на основе
  текущего изображения маску в виде объекта класса QBitmap и возвращает ее. Первый
  параметр задает цвет - области, закрашенные этим цветом, будут на маске либо
  прозрачными, либо непрозрачными. Необязательный параметр mode задает режим создания
  маски в виде следующих элементов перечисления MaskMode из модуля QtCore.Qt:
  • MaskInColor - области, закрашенные указанным цветом, будут прозрачными;
  • MaskOutColor - области, закрашенные указанным цветом, будут непрозрачными;
♦ setMask(<Маска QBitmap>) - устанавливает маску;
♦ mask() - возвращает объект класса QBitmap с маской изображения;
♦ сору() - возвращает объект класса QPixmap с фрагментом изображения. Если параметр
  rect не указан, изображение копируется полностью. Форматы метода:
  copy([rect=QRect()])
  сору(<Х>, <Y>, <Ширина>, <Высота>)
♦ scaled() - изменяет размер изображения и возвращает результат в виде объекта класса
  QPixmap. Исходное изображение не изменяется. Форматы метода:
  scaled(<Ширина>, <Высота>[,
         aspectRatioMode=AspectRatioMode.IgnoreAspectRatio] [,
         transformMode=TransformationMode.FastTransformation])
  scaled (<Размеры QSize>[, aspectRatioMode=AspectRatioMode.IgnoreAspectRatio] [,
          transformMode=TransformationMode.FastTransformation])
  В необязательном параметре aspectRatioMode могут быть указаны следующие элементы
  перечисления AspectRatioMode из модуля QtCore.Qt:
  • IgnoreAspectRatio - изменяет размеры без сохранения пропорций сторон;
  • KeepAspectRatio - изменяет размеры с сохранением пропорций сторон. При этом
    часть области нового изображения может оказаться незаполненной;
  • KeepAspectRatioByExpanding - изменяет размеры с сохранением пропорций сторон.
    При этом часть нового изображения может выйти за пределы его области.
    В необязательном параметре transformMode могут быть указаны следующие элементы
    перечисления TransformationMode из модуля QtCore.Qt:
  • FastTransformation - сглаживание выключено;
  • SmoothTransformation - сглаживание включено;
♦ scaledToWidth() - изменяет ширину изображения и возвращает результат в виде объекта
  класса QPixmap. Формат метода:
  scaledToWidth(<Ширина>[, mode=TransformationMode.FastTransformation])
  Высота изображения изменяется пропорционально. Исходное изображение не изменяется.
  Параметр mode аналогичен параметру transformMode в методе scaled();
♦ scaledToHeight() - изменяет высоту изображения и возвращает результат в виде объекта
  класса QPixmap. Формат метода:
  scaledToHeight (<Высота> [, mode=TransformationMode.FastTransformation])
  Ширина изображения изменяется пропорционально. Исходное изображение не изменяется.
  Параметр mode аналогичен параметру transformMode в методе scaled();
♦ transformed() - производит трансформацию изображения (например, поворот) и возвращает
  результат в виде объекта класса QPixmap. Формат метода:
  transformed(<Трансформация QTransform>[, mode=TransformationMode.FastTransformation])
  Исходное изображение не изменяется. Параметр mode аналогичен параметру
  transformMode в методе scaled();
♦ swap(<Изображение QPixmap>) - заменяет текущее изображение указанным в параметре;
♦ hasAlpha() - возвращает True, если изображение имеет прозрачные области, и False -
  в противном случае;
♦ hasAlphaChannel() - возвращает True, если формат изображения поддерживает прозрачность,
  и False - в противном случае.
"""
import os

from PySide6.QtWidgets import (QMainWindow,
                               )
from PySide6.QtGui import (QPainter,
                           QPixmap,
                           QImage,
                           Qt,
                           QColor,
                           QTransform,
                           )
"""
Импорт модуля os для работы с переменными интерпретатора 

Импорт из модуля PySide6.QtWidgets класса главных окон QMainWindow

Импорт из модуля PySide6.QtGui класса рисовальщика QPainter,
класса для работы с изображениями в контекстно-зависимом представлении QPixmap,
класса для работы с изображениями в контекстно-независимом представлении QImage,
класса перечислителя настроек виджетов Qt, класса цветов QColor,
класса преобразований изображений QTransform
"""

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
        self.resize(1000, 600)  # установка исходных размеров главного окна приложения
        self.setWindowTitle('Класс QPixmap')  # установка имени главного окна приложения
        self.pix_1 = QPixmap(os.path.join('data', 'photo.jpg'))  # создание объекта изображения из файла

       # --== Загрузка изображения из массива байтов
        self.img = QImage()  # создание объекта файла изображения
        f = open(os.path.join('data', 'photo.jpg'), 'rb')  # открытие файла на чтение в режиме байтов
        self.img = f.read()  # чтение файла изображения в аттрибут
        f.close()  # закрытие файла
        self.pix_2 = QPixmap()  # создание объекта изображения
        self.pix_2.loadFromData(self.img, 'jpg')  # загрузка в объект изображения байтовых данных

        # --== Загрузка изображения из файла
        self.pix_3 = QPixmap()  # создание объекта изображения
        print(self.pix_3.load(os.path.join('data', 'photo.jpg')))  # загрузка изображения из файла

        # --== Сохранение изображения в файл
        self.pix_3.save(os.path.join('data', 'photo.png'), 'png')  # сохранение изображения в файл

        # --== Преобразование объекта QImage в объект QPixmap
        self.img = QImage(os.path.join('data', 'photo.jpg'))  # создание объекта изображения из файла
        self.pix_4 = QPixmap()  # создание объекта изображения
        print(self.pix_4.convertFromImage(self.img))  # конвертация объекта изображения
        self.pix_5 = QPixmap.fromImage(self.img)

        # --== Преобразование объекта QPixmap в объект QImage
        self.img_2 = QPixmap.toImage(self.pix_5)

        # --== Заливка изображения цветом
        self.pix_6 = QPixmap(os.path.join('data', 'photo.jpg'))  # создание объекта изображения из файла
        self.pix_6.fill(fillColor='blue')  # заливка изображения цветом (цвет может быть задан очень по разному)

        # --== Извлечение данные об изображении
        print(f'Ширина изображения: {self.pix_6.width()}')
        print(f'Высота изображения: {self.pix_6.height()}')
        print(f'Размеры прямоугольника, описывающего изображение: {self.pix_6.rect().width()} x {self.pix_6.rect().height()}')
        print(f'Глубина цвета изображения: {self.pix_6.depth()} бит')
        print(f'Изображение монохромное: {self.pix_6.isQBitmap()}')
        print(f'Изображение имеет прозрачные области: {self.pix_6.hasAlpha()}')
        print(f'Изображение поддерживает прозрачность: {self.pix_6.hasAlphaChannel()}')

        # --== Маска изображения
        self.mask = self.pix_5.createMaskFromColor(QColor('white'), mode=Qt.MaskMode.MaskOutColor)
        print(self.mask)

        # --== Копирование части изображения
        self.pix_7 = self.pix_5.copy(50, 50, 75, 75)

        # --== Изменение масштаба изображения
        self.pix_8 = self.pix_5.scaled(100, 150, aspectMode=Qt.AspectRatioMode.IgnoreAspectRatio)
        self.pix_9 = self.pix_5.scaledToWidth(100, mode=Qt.TransformationMode.SmoothTransformation)
        self.pix_10 = self.pix_5.scaledToHeight(100, mode=Qt.TransformationMode.SmoothTransformation)

        # --== Трансформация изображения
        rotation = QTransform()  # создание объекта трансформации
        rotation.rotate(45.0)  # указание поворота в качестве трансформации
        self.pix_11 = self.pix_5.transformed(rotation)  #  применение трансформации к изображению


    def paintEvent(self, event) -> None:
        """
        Обработчик события рисования
        :param event: событие рисования
        :return: None
        """
        painter = QPainter(self)  # создание объекта рисовальщика с подключением поверхности рисования
        painter.drawPixmap(0, 0, self.pix_1)  # вывод изображения в область рисования
        painter.drawPixmap(250, 0, self.pix_2)  # вывод изображения в область рисования
        painter.drawPixmap(500, 0, self.pix_3)  # вывод изображения в область рисования
        painter.drawPixmap(0, 200, self.pix_4)  # вывод изображения в область рисования
        painter.drawPixmap(250, 200, self.pix_5)  # вывод изображения в область рисования
        painter.drawImage(500, 200, self.img_2)  # вывод изображения в область рисования
        painter.drawPixmap(0, 400, self.pix_6)  # вывод изображения в область рисования
        painter.drawPixmap(250, 400, self.mask)  # вывод изображения в область рисования
        painter.drawPixmap(500, 400, self.pix_7)  # вывод изображения в область рисования
        painter.drawPixmap(600, 400, self.pix_8)  # вывод изображения в область рисования
        painter.drawPixmap(550, 500, self.pix_9)  # вывод изображения в область рисования
        painter.drawPixmap(650, 500, self.pix_10)  # вывод изображения в область рисования
        painter.drawPixmap(750, 0, self.pix_11)  # вывод изображения в область рисования


if __name__ == '__main__':  # проверка условия запуска для предотвращения
    # запуска кода верхнего уровня при импортировании данного файла как модуля
    from PySide6.QtWidgets import QApplication
    import sys
    """
    Импорт из модуля PySide6.QtWidgets класса управления приложением QApplication
    Импорт модуля sys, предоставляющего доступ к объекта интерпретатора, нужен для доступа
    к аргументам командной строки. Если использование аргументов командной строки не предполагается,
    то импорт можно не выполнять. При этом, при создании приложения в класс QtWidgets.QApplication([])
    в качестве аргумента передается пустой список.
    """
    app = QApplication(sys.argv)  # создание основного цикла событий приложения
    app.setStyle('Fusion')  # установка более красивого стиля оформления виджетов
    window = MainWindow()  # создание экземпляра главного окна приложения
    window.show()  # включение видимости окна, по умолчанию окно спрятано
    sys.exit(app.exec())  # Запуск основного цикла событий приложения.
    # Код ниже метода запуска цикла событий не будет достигнут и выполнен пока не будет выполнен
    # выход и цикл событий не будет остановлен. Не обязательно оборачивать запуск цикла в метод выхода