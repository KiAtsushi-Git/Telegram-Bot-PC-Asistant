"""Пример простого Телеграм Бота - ПК асистента"""
from config import BotToken, AdminId, PyCharm_Path
from Dops.keyboards import menu_kb, start_programs_kb, stats_kb, volume_kb, different_kb
from Dops.audio import get_media_info
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import CallbackQuery
import pyautogui
import psutil
import webbrowser
import time
import subprocess
import os

bot = Bot(BotToken)
dp = Dispatcher(bot)


async def is_admin(chat_id):
    """Проверка на администратора"""
    return chat_id == AdminId


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    """Стартовая функция с основным управлением"""
    chatid = msg.chat.id

    if await is_admin(chatid):
        await bot.send_animation(
            chat_id=chatid,
            animation=open("./Static/start_msg.gif", "rb"),
            caption="Добро пожаловать в бота для удаленного администрирования персонального компьютера.",
            reply_markup=await menu_kb(),
        )
    else:
        pass


@dp.callback_query_handler(lambda c: True)
async def callback_handler(callback_query: CallbackQuery):
    """Обработчик inline ответов"""
    callback_data = callback_query.data
    chatid = callback_query.from_user.id

    if not await is_admin(chatid):
        pass

    elif callback_data == "volume_up":

        try:
            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Громкость +
"""
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await volume_kb("up"),
                parse_mode="HTML"
            )

        except ValueError:
            pass

    elif callback_data == "volume_2_up":
        pyautogui.press("volumeup")

    elif callback_data == "volume_4_up":
        for i in range(2):
            pyautogui.press("volumeup")

    elif callback_data == "volume_6_up":
        for i in range(3):
            pyautogui.press("volumeup")

    elif callback_data == "volume_8_up":
        for i in range(4):
            pyautogui.press("volumeup")

    elif callback_data == "volume_10_up":
        for i in range(5):
            pyautogui.press("volumeup")

    elif callback_data == "volume_12_up":
        for i in range(6):
            pyautogui.press("volumeup")

    elif callback_data == "volume_down":
        try:
            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Громкость -
            """
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await volume_kb("down"),
                parse_mode="HTML"
            )
        except ValueError:
            pass

    elif callback_data == "volume_2_down":
        pyautogui.press("volumedown")

    elif callback_data == "volume_4_down":
        for i in range(2):
            pyautogui.press("volumedown")

    elif callback_data == "volume_6_down":
        for i in range(3):
            pyautogui.press("volumedown")

    elif callback_data == "volume_8_down":
        for i in range(4):
            pyautogui.press("volumedown")

    elif callback_data == "volume_10_down":
        for i in range(5):
            pyautogui.press("volumedown")

    elif callback_data == "volume_12_down":
        for i in range(6):
            pyautogui.press("volumedown")

    elif callback_data == "pause":
        pyautogui.press("playpause")
        try:

            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Пауза
            """
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await menu_kb(),
                parse_mode="HTML"
            )
        except ValueError:
            pass

    elif callback_data == "next":
        pyautogui.press("nexttrack")
        try:
            time.sleep(1)
            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Следующий трек
                        """
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await menu_kb(),
                parse_mode="HTML"
            )
        except ValueError:
            pass

    elif callback_data == "previous":
        pyautogui.press("prevtrack")
        pyautogui.press("prevtrack")
        try:
            time.sleep(1)
            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Предыдущий трек
                        """
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await menu_kb(),
                parse_mode="HTML"
            )
        except ValueError:
            pass

    elif callback_data == "refresh_menu":
        try:
            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Обновление меню
                        """
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await menu_kb(),
                parse_mode="HTML"
            )
        except ValueError:
            pass

    elif callback_data == "start_programs":
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Меню программ",
                reply_markup=await start_programs_kb(),
            )
        except ValueError:
            pass

    elif callback_data == "back":
        try:
            track_info = await get_media_info()
            caption_text = f"""
<b>Сейчас играет:</b>
{track_info or 'Ничего не играет'}

<b>Последние действие:</b>
  ▸ Назад
"""
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=caption_text,
                reply_markup=await menu_kb(),
                parse_mode="HTML"
            )
        except ValueError:
            pass

    elif callback_data == "start_google":
        webbrowser.open("https://www.google.com/")
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Открытие Google",
                reply_markup=await start_programs_kb(),
            )
        except ValueError:
            pass

    elif callback_data == "start_yandex":
        webbrowser.open("https://ya.ru/")
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Открытие Яндекс",
                reply_markup=await start_programs_kb(),
            )
        except ValueError:
            pass

    elif callback_data == "start_chatgpt":
        webbrowser.open("https://chatgpt.com/")
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Открытие ChatGPT",
                reply_markup=await start_programs_kb(),
            )
        except ValueError:
            pass

    elif callback_data == "start_youtube":
        webbrowser.open("https://www.youtube.com")
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Открытие YouTube",
                reply_markup=await start_programs_kb(),
            )
        except ValueError:
            pass

    elif callback_data == "start_pycharm":
        subprocess.Popen(PyCharm_Path)
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Запуск PyCharm",
                reply_markup=await start_programs_kb(),
            )
        except ValueError:
            pass

    elif callback_data == "start_cmd":
        subprocess.Popen(["start", "cmd.exe"], shell=True)
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption="Последние действие:\n  ▸ Запуск Cmd",
                reply_markup=await start_programs_kb(),
            )
        except Exception:
            pass

    elif callback_data == "stats":
        Free_Space = psutil.disk_usage("C:\\").free / (1024 * 1024 * 1024)  # в GB
        UpTime = time.time() - psutil.boot_time()
        uptime = time.gmtime(UpTime)
        days = UpTime // (24 * 3600)
        UptimeCor = f"{int(days)} д {uptime.tm_hour:02} ч {uptime.tm_min:02} м {uptime.tm_sec:02} с"
        cpu_percent = psutil.cpu_percent(interval=1)
        virtual_memory = psutil.virtual_memory()
        free_memory = virtual_memory.available / (1024 * 1024 * 1024)
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=f"""
Последние действие: 
 ▸ Открытие статистики
    
  ▸ <b>Время с запуска:</b> {UptimeCor}
  ▸ <b>Свободно на диске C:</b> {Free_Space:.2f} GB
  ▸ <b>Нагрузка CPU:</b> {cpu_percent}%
  ▸ <b>Свободно ОЗУ:</b> {free_memory:.2f} GB
    """,
                reply_markup=await stats_kb(),
                parse_mode="HTML",
            )
        except ValueError:
            pass


    elif callback_data == "shutdown":
        await bot.edit_message_caption(
            message_id=callback_query.message.message_id,
            chat_id=chatid,
            caption=f"Последние действие:\n ▸ Выключение устройства",
            reply_markup=await menu_kb(),
            parse_mode="HTML",
        )
        os.system("shutdown /s /t 5")


    elif callback_data == "different":
        await bot.edit_message_caption(
            message_id=callback_query.message.message_id,
            chat_id=chatid,
            caption=f"Последние действие:\n ▸ Разное",
            reply_markup=await different_kb(),
            parse_mode="HTML",
        )

    elif callback_data == "screenshot":
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)

        with open(screenshot_path, "rb") as photo:
            await bot.send_photo(chat_id=chatid, photo=photo, caption="📸 Скриншот экрана")

    elif callback_data == "stats_refresh":
        Free_Space = psutil.disk_usage("C:\\").free / (1024 * 1024 * 1024)  # в GB
        UpTime = time.time() - psutil.boot_time()
        uptime = time.gmtime(UpTime)
        days = UpTime // (24 * 3600)
        UptimeCor = f"{int(days)} д {uptime.tm_hour:02} ч {uptime.tm_min:02} м {uptime.tm_sec:02} с"
        cpu_percent = psutil.cpu_percent(interval=1)
        virtual_memory = psutil.virtual_memory()
        free_memory = virtual_memory.available / (1024 * 1024 * 1024)
        try:
            await bot.edit_message_caption(
                message_id=callback_query.message.message_id,
                chat_id=chatid,
                caption=f"""
Последние действие: 
 ▸ Обновление статистики

  ▸ <b>Время с запуска:</b> {UptimeCor}
  ▸ <b>Свободно на диске C:</b> {Free_Space:.2f} GB
  ▸ <b>Нагрузка CPU:</b> {cpu_percent}%
  ▸ <b>Свободно ОЗУ:</b> {free_memory:.2f} GB
        """,
                reply_markup=await stats_kb(),
                parse_mode="HTML",
            )
        except ValueError:
            pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
