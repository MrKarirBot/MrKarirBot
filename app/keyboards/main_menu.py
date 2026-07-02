"""Keyboard menu utama Telegram."""

from telegram import ReplyKeyboardMarkup


def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = [
        ["🔍 Cari Lowongan", "📄 Buat CV ATS"],
        ["🎤 Interview AI", "📊 Tracker Lamaran"],
        ["👤 Profil Saya", "⚙️ Pengaturan"],
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
