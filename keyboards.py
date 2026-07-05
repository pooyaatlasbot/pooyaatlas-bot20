from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["🛩 معرفی آموزشگاه"],
        ["✈️ دوره‌های آموزشی", "💰 شهریه"],
        ["📝 ثبت نام", "📍 آدرس"],
        ["📞 تماس با ما", "🌐 وب سایت"],
    ],
    resize_keyboard=True
)