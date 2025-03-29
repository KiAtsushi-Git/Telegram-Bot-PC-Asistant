from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def menu_kb():
    """Iline клавиатура с основным управлением"""
    keyboard = InlineKeyboardMarkup()

    PreviousBut = InlineKeyboardButton(text="⏪", callback_data="previous")
    PauseBut = InlineKeyboardButton(text="[⏯️] Пауза", callback_data="pause")
    NextBut = InlineKeyboardButton(text="⏩", callback_data="next")

    VolumeUp = InlineKeyboardButton(text="➕", callback_data="volume_up")
    VolumeDown = InlineKeyboardButton(text="➖", callback_data="volume_down")

    StartProgramsBut = InlineKeyboardButton(
        text="[🗳] Запуск приложений", callback_data="start_programs"
    )
    CheckStatistik = InlineKeyboardButton(
        text="[🖥] Производительность", callback_data="stats"
    )

    RefreshBut = InlineKeyboardButton(
        text="[🔄] Обновить меню", callback_data="refresh_menu"
    )

    keyboard.row(PreviousBut, PauseBut, NextBut)
    keyboard.row(VolumeUp, VolumeDown)
    keyboard.row(StartProgramsBut)
    keyboard.row(CheckStatistik)
    keyboard.row(RefreshBut)

    return keyboard


async def start_programs_kb():
    """Клавиатура для запуска сайтов и приложений"""
    keyboard = InlineKeyboardMarkup()

    Stringbut = InlineKeyboardButton(text="――――――――――――――――――――", callback_data="None")
    EmptyBut = InlineKeyboardButton(text="ㅤ", callback_data="None")

    SiteBut = InlineKeyboardButton(text="Сайты:", callback_data="None")
    GoogleBut = InlineKeyboardButton(text="Google", callback_data="start_google")
    YandexBut = InlineKeyboardButton(text="Яндекс", callback_data="start_yandex")
    ChatGptBut = InlineKeyboardButton(text="ChatGPT", callback_data="start_chatgpt")
    YoutubeBut = InlineKeyboardButton(text="YouTube", callback_data="start_youtube")

    ProgramsBut = InlineKeyboardButton(text="Программы:", callback_data="None")
    PyCharmBut = InlineKeyboardButton(text="PyCharm", callback_data="start_pycharm")
    CmdBut = InlineKeyboardButton(text="Cmd", callback_data="start_cmd")

    BackBut = InlineKeyboardButton(text="Назад", callback_data="back")

    keyboard.row(Stringbut)
    keyboard.row(SiteBut)
    keyboard.row(GoogleBut, YandexBut)
    keyboard.row(ChatGptBut, YoutubeBut)
    keyboard.row(Stringbut)

    keyboard.row(ProgramsBut)
    keyboard.row(PyCharmBut, CmdBut)

    keyboard.row(Stringbut)
    keyboard.add(BackBut)

    return keyboard


async def stats_kb():
    """Клавитура блока статистики"""
    keyboard = InlineKeyboardMarkup()

    RefreshBut = InlineKeyboardButton(text="Обновить", callback_data="stats_refresh")
    BackBut = InlineKeyboardButton(text="Назад", callback_data="back")

    keyboard.row(RefreshBut)
    keyboard.add(BackBut)

    return keyboard
