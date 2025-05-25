import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,      # Для создания и запуска бота
    CommandHandler,         # Для обработки команд (например, /start)
    MessageHandler,         # Для обработки обычных сообщений
    ContextTypes,           # Типы контекста для современных хендлеров
    filters                 # Для фильтрации сообщений (текст, команды и др.)
)

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен бота из переменной окружения TELEGRAM_BOT_TOKEN
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# -------------------------
# Обработчик команды /start
# -------------------------
# При вводе пользователем команды /start эта функция отправит приветственное сообщение.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Отправляем ответное сообщение пользователю
    await update.message.reply_text('Привет! Я твой бот. Напиши мне что-нибудь.')


# -------------------------
# Обработчик текстовых сообщений
# -------------------------
# Бот будет просто повторять (эхо) любое полученное текстовое сообщение.
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Получаем текст из сообщения пользователя
    user_message = update.message.text
    
    # Отправляем обратно тот же текст
    await update.message.reply_text(user_message)


# -------------------------
# Главная функция запуска бота
# -------------------------
def main():
    # Проверяем, что токен действительно получен
    if not TOKEN:
        print("❌ Токен не найден. Проверь файл .env и переменную TELEGRAM_BOT_TOKEN.")
        return

    # Создаем объект приложения бота с указанным токеном
    app = ApplicationBuilder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    app.add_handler(CommandHandler('start', start))

    # Регистрируем обработчик для обычных текстовых сообщений,
    # исключая команды (т.е. все текстовые сообщения без слэша в начале)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ Бот запущен и готов к работе!")
    
    # Запускаем цикл получения обновлений и обработки сообщений
    app.run_polling()


# Точка входа в программу
if __name__ == '__main__':
    main()
