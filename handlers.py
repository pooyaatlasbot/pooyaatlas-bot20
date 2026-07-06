from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_keyboard
from config import SCHOOL_NAME, PHONE, WEBSITE, ADDRESS


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"✈️ به {SCHOOL_NAME} خوش آمدید.",
        reply_markup=main_keyboard
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛩 معرفی آموزشگاه":
        await update.message.reply_text(
            "آموزشگاه خلبانی پویا اطلس برگزارکننده دوره‌های آموزش خلبانی فوق سبک، آموزش تئوری و آموزش عملی می‌باشد."
        )

    elif text == "✈️ دوره‌های آموزشی":
        await update.message.reply_text(
            """✈️ دوره‌های آموزشی

🛩 خلبانی فوق سبک

📘 آموزش تئوری

👨‍✈️ آموزش عملی"""
        )
    elif text == "✈️ دوره مقدماتی UL-PPL":
        await update.message.reply_text(
            "دوره مقدماتی UL-PPL"
        )

    elif text == "🚁 دوره پیشرفته UL-CPL":
        await update.message.reply_text(
            "دوره پیشرفته UL-CPL"
        )

    elif text == "👨‍✈️ استاد خلبانی UL-IP":
        await update.message.reply_text(
            "استاد خلبانی UL-IP"
        )
    elif text == "💰 شهریه":
        await update.message.reply_text(
            "برای اطلاع از شهریه لطفاً با آموزشگاه تماس بگیرید."
        )

    elif text == "📝 ثبت نام":
        await update.message.reply_text(
            "جهت ثبت‌نام با آموزشگاه تماس بگیرید."
        )

    elif text == "📍 آدرس":
        await update.message.reply_text(ADDRESS)

    elif text == "📞 تماس با ما":
        await update.message.reply_text(PHONE)

    elif text == "🌐 وب سایت":
        await update.message.reply_text(WEBSITE)

    else:
        await update.message.reply_text(
            "لطفاً یکی از گزینه‌های منو را انتخاب کنید."
        )