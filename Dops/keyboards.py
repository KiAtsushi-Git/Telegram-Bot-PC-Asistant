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

    DifferentBut = InlineKeyboardButton(
        text="[🖇] Разное", callback_data="different"
    )

    ShutdownBut = InlineKeyboardButton(
        text="[❌] Выключить устройство", callback_data="shutdown"
    )

    RefreshBut = InlineKeyboardButton(
        text="[🔄] Обновить меню", callback_data="refresh_menu"
    )

    keyboard.row(PreviousBut, PauseBut, NextBut)
    keyboard.row(VolumeUp, VolumeDown)
    keyboard.row(StartProgramsBut)
    keyboard.row(DifferentBut)
    keyboard.row(CheckStatistik)
    keyboard.row(ShutdownBut)
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

async def volume_kb(mode):
    """Клавитура блока звука"""
    target = "up"
    if mode == "down":
        target = "down"
    keyboard = InlineKeyboardMarkup()

    volume_2 = InlineKeyboardButton(text="2", callback_data=f"volume_2_{target}")
    volume_4 = InlineKeyboardButton(text="4", callback_data=f"volume_4_{target}")
    volume_6 = InlineKeyboardButton(text="6", callback_data=f"volume_6_{target}")
    volume_8 = InlineKeyboardButton(text="8", callback_data=f"volume_8_{target}")
    volume_10 = InlineKeyboardButton(text="10", callback_data=f"volume_10_{target}")
    volume_12 = InlineKeyboardButton(text="12", callback_data=f"volume_12_{target}")
    BackBut = InlineKeyboardButton(text="Назад", callback_data="back")

    keyboard.row(volume_2,volume_8)
    keyboard.row(volume_4,volume_10)
    keyboard.row(volume_6,volume_12)
    keyboard.add(BackBut)

    return keyboard

async def different_kb():
    """Клавитура блока разного"""
    keyboard = InlineKeyboardMarkup()

    RefreshBut = InlineKeyboardButton(text="[📸] Скриншот", callback_data="screenshot")
    BackBut = InlineKeyboardButton(text="Назад", callback_data="back")

    keyboard.row(RefreshBut)
    keyboard.add(BackBut)

    return keyboard