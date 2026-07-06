from telegram import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    [
        ["🛩 معرفی آموزشگاه"],
        ["✈️ دوره‌های آموزشی"],
        ["✈️ دوره مقدماتی UL-PPL"],
        ["🛩 دوره پیشرفته UL-CPL"],
        ["👨‍✈️ استاد خلبانی UL-IP"],
        ["💰 شهریه", "📝 ثبت نام"],
        ["📍 آدرس", "📞 تماس با ما"],
        ["🌐 وب سایت"],
    ],
    resize_keyboard=True
)