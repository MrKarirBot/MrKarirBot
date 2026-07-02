"""Handler perintah /help."""

from telegram import Update
from telegram.ext import ContextTypes


async def help_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    message = (
        "Perintah tersedia:\n"
        "/start - Membuka menu utama\n"
        "/help - Menampilkan bantuan"
    )

    if update.message:
        await update.message.reply_text(message)
