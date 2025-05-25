from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функция, которая будет обрабатывать команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой бот. Напиши мне что-нибудь.')

# Функция для обработки обычных сообщений (не команд)
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text  # Получаем текст сообщения от пользователя
    response = f'Ты сказал: {user_message}'  # Формируем ответ
    update.message.reply_text(response)  # Отправляем ответ пользователю

# Основная функция для запуска бота
def main():
    # Токен вашего бота от BotFather
    token = 'YOUR_BOT_API_TOKEN'

    # Создаем объект Updater и передаем токен
    updater = Updater(token, use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчик для команды /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Регистрируем обработчик для обычных текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока вы его не остановите
    updater.idle()

if __name__ == '__main__':
    main()
