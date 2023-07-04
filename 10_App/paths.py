"""
Данные модуль содержит настройки путей к ресурсам Moonsweeper метод загрузчик файлов ресурсов
"""

import os  # импорт модуля библиотеки для работы с переменными среды


class Paths:
    """
    Класс настроек пути к ресурсам приложения
    """
    base = os.path.dirname(__file__)  # извлечение пути до модуля с кодов верхнего уровня
    icons = os.path.join(base, 'icons')  # присоединение к пути папки с ресурсами

    @classmethod
    def icon(cls, filename: str) -> os.path:
        """
        Метод загрузчик файлов ресурсов
        :param filename: имя файла
        :return: путь к файлу
        """
        return os.path.join(cls.icons, filename)
