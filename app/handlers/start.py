"""Handler perintah /start."""

from telegram import Update
from telegram.ext import ContextTypes

from app.keyboards.main_menu import get_main_menu


async def start_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    user = update.effective_user
    first_name = user.first_name if user else "Teman"

    message = (
        f"Halo {first_name} 👋\n\n"
        "Selamat datang di MrKarirBot.\n"
        "Asisten karier untuk mencari lowongan, membuat CV ATS, "
        "latihan interview, dan melacak lamaran kerja."
    )

    if update.message:
        await update.message.reply_text(
            message,
            reply_markup=get_main_menu(),
        )
