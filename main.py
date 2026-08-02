from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from rahavard import get_price
from config import BOT_TOKEN

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
        "سلام 👋\n\nنماد را ارسال کنید.\nمثال:\nشسپا"
    )

async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text not in SYMBOLS:
        await update.message.reply_text("نماد پیدا نشد.")
        return

    try:
        data = get_price(SYMBOLS[text])

        msg = (
            f"📊 {text}\n\n"
            f"💰 آخرین قیمت: {data['last']}\n"
            f"📌 قیمت پایانی: {data['close']}\n"
            f"📈 تغییر: {data['change']}\n"
            f"📊 درصد: {data['percent']}%"
        )

        await update.message.reply_text(msg)

    except Exception as e:
        await update.message.reply_text(str(e))

def main():
    # ساخت اپلیکیشن با توکن
    app = Application.builder().token(BOT_TOKEN).build()

    # ثبت هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    print("Bot Started...")
    
    # اجرای ربات با متد استاندارد نسخه جدید
    app.run_polling()

if __name__ == "__main__":
    main()
