"""
Работа с растровыми изображениями

Библиотека PyQt включает несколько классов, позволяющих работать с растровыми изображениями
в контекстно-зависимом (классы QPixmap и QBitmap) и контекстно-независимом
(класс QImage) представлениях.
Получить список графических форматов, доступных для загрузки, позволяет статический
метод supportedImageFormats() класса QImageReader, возвращающий список с объектами
класса QByteArray. Получим список поддерживаемых форматов для чтения:
>> for i in QtGui.QImageReader.supportedImageFormats():
print(str(i, "ascii").upper(), end=" ")
ВМР CUR GIF ICNS ICO JPEG JPG РВМ PGM PNG РРМ SVG SVGZ TGA TIF TIFF WBMP
WEBP ХВМ ХРМ
Получить список графических форматов, доступных для сохранения, позволяет статический
метод supportedImageFormats() класса QImageWriter, возвращающий список с объектами
класса QByteArray. Получим список поддерживаемых форматов для записи:
>> for i in QtGui.QImageWriter .supportedImageFormats():
print(str(i, "ascii") .upper(), end=" ")
ВМР CUR ICNS ICO JPEG JPG РВМ PGM PNG РРМ TIF TIFF WBMP WEBP ХВМ ХРМ
Обратите внимание, что мы можем загрузить изображение в формате GIF, но не имеем возможности
сохранить изображение в этом формате, поскольку алгоритм сжатия, используемый
в нем, защищен патентом.
"""

# демонстрация данных классов представлены в примерах кода данного подраздела