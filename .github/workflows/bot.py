import asyncio
import os
from datetime import datetime
import pytz
from telethon import TelegramClient
import logging

# Настройки из секретов
API_ID = os.getenv('API_ID', '2040')
API_HASH = os.getenv('API_HASH', 'b18441a1ff607e10a989891a5462e627')
BOT_TOKEN = os.getenv('BOT_TOKEN')
USER_CHAT_ID = int(os.getenv('USER_CHAT_ID', '0'))

# Список каналов (замените на свои)
CHANNELS = [
    'gubernator_46',
    'kursk_info46',
    'Alekhin_Telega',
    'rian_ru',
    'kursk_ak46',
    'zhest_kursk_146',
    'novosti_efir',
    'kursk_tipich',
    'seymkursk',
    'kursk_smi',
    'kursk_russia',
    'belgorod01',
    'kurskadm',
    'Avtokadr46',
    'kurskbomond',
    'prigranichie_radar1',
    'grohot_pgr',
    'kursk_nasv',
    'mchs_46',
    'patriot046',
    'kursk_now',
    'Hinshtein',
    'incidentkursk',
    'zhest_belgorod',
    'Pogoda_Kursk',
    'pb_032',
    'tipicl32',
    'bryansk_smi',

]

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

async def main():
    logger.info("🚀 Запуск бота")
    
    client = TelegramClient('github_bot', API_ID, API_HASH)
    
    try:
        await client.start(bot_token=BOT_TOKEN)
        logger.info("✅ Бот авторизован")
        
        # Отправляем тестовое сообщение
        await client.send_message(
            USER_CHAT_ID,
            f"🤖 Бот запущен!\n🕒 Время: {datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M %d.%m.%Y')}\n✅ Готов к работе!"
        )
        
        logger.info("✅ Тестовое сообщение отправлено")
        
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        
        try:
            # Пытаемся отправить сообщение об ошибке
            await client.send_message(USER_CHAT_ID, f"❌ Ошибка в боте: {str(e)[:100]}...")
        except:
            pass
            
    finally:
        await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
