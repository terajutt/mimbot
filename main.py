import logging
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater, Dispatcher
from apscheduler.schedulers.background import BackgroundScheduler
import os

# Replace with your token from @BotFather
BOT_TOKEN = "8173195584:AAEdchH7-DokXiVStDiBxH1kAmtufYYG5gc"

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher: Dispatcher = updater.dispatcher
logging.basicConfig(level=logging.INFO)

# Store group IDs where the bot is added
groups = set()

# Start command (private chat)
def start(update, context):
    update.message.reply_text("Hello! I'm alive.")

# Track group joins
def handle_new_chat_members(update, context):
    chat_id = update.effective_chat.id
    if update.effective_chat.type in ['group', 'supergroup']:
        groups.add(chat_id)
        context.bot.send_message(chat_id=chat_id, text="Thanks for adding me!")

# Scheduled message
def send_group_messages():
    for group_id in groups:
        try:
            bot.send_message(chat_id=group_id, text="This is your scheduled message.")
        except Exception as e:
            print(f"Failed to send to {group_id}: {e}")

# Flask route to keep it alive
@app.route('/')
def home():
    return 'Bot is running!'

# Telegram webhook route (not needed for polling but required by Render)
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Register handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", start))
dispatcher.add_handler(CommandHandler("ping", start))
dispatcher.add_handler(CommandHandler("alive", start))
dispatcher.add_handler(CommandHandler("status", start))
dispatcher.add_handler(CommandHandler("info", start))
dispatcher.add_handler(CommandHandler("groupinfo", start))
dispatcher.add_handler(CommandHandler("settings", start))
dispatcher.add_handler(CommandHandler("commands", start))
dispatcher.add_handler(CommandHandler("startbot", start))
dispatcher.add_handler(CommandHandler("stop", start))
dispatcher.add_handler(CommandHandler("pause", start))
dispatcher.add_handler(CommandHandler("resume", start))
dispatcher.add_handler(CommandHandler("restart", start))
dispatcher.add_handler(CommandHandler("uptime", start))
dispatcher.add_handler(CommandHandler("about", start))
dispatcher.add_handler(CommandHandler("version", start))
dispatcher.add_handler(CommandHandler("support", start))
dispatcher.add_handler(CommandHandler("credits", start))
dispatcher.add_handler(CommandHandler("license", start))
dispatcher.add_handler(CommandHandler("donate", start))
dispatcher.add_handler(CommandHandler("contact", start))
dispatcher.add_handler(CommandHandler("feedback", start))
dispatcher.add_handler(CommandHandler("report", start))
dispatcher.add_handler(CommandHandler("bug", start))
dispatcher.add_handler(CommandHandler("issue", start))
dispatcher.add_handler(CommandHandler("suggestion", start))
dispatcher.add_handler(CommandHandler("feature", start))
dispatcher.add_handler(CommandHandler("feature_request", start))
dispatcher.add_handler(CommandHandler("feature_suggestion", start))
dispatcher.add_handler(CommandHandler("new_feature", start))
dispatcher.add_handler(CommandHandler("feature_idea", start))
dispatcher.add_handler(CommandHandler("idea", start))
dispatcher.add_handler(CommandHandler("feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_issue", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_suggestion", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_idea", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_bug", start))
dispatcher.add_handler(CommandHandler("feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_request_feature_issue", start))

dispatcher.add_handler(CommandHandler("groupjoin", handle_new_chat_members))

# Schedule repeated messages
scheduler = BackgroundScheduler()
scheduler.add_job(send_group_messages, 'interval', minutes=1)
scheduler.start()

if __name__ == '__main__':
    updater.start_polling()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
