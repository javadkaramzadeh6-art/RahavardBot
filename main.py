from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from rahavard import get_price
from config import BOT_TOKEN

# شناسه نمادها
SYMBOLS = {
    "شسپا": 478,
    "شپنا": 484,
    "شتران": 637,
    "شبندر": 485,
    "شبریز": 492,
    "شراز": 696,
    "شاوان": 710,
    "شرانل": 672,
    "ونفت": 337,
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "نماد را ارسال کنید.\n"
        "مثال:\n"
        "شسپا"
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text not in SYMBOLS:
        await update.message.reply_text("نماد پیدا نشد.")
        return

    try:
        data = get_price(SYMBOLS[text])

        msg = f"""
📊 {text}

💰 آخرین قیمت: {data['last']}
📌 قیمت پایانی: {data['close']}
📈 تغییر: {data['change']}
📊 درصد: {data['percent']}%
"""
        await update.message.reply_text(msg)

    except Exception as e:
        await update.message.reply_text(str(e))

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

from telegram.ext import MessageHandler, filters
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

print("Bot Started...")
app.run_polling()
