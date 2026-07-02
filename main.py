"""Entry point MrKarirBot."""

import logging

from telegram.ext import Application, CommandHandler

from app.config import settings
from app.handlers.help import help_handler
from app.handlers.start import start_handler


def build_application() -> Application:
    if not settings.bot_token:
        raise RuntimeError(
            "BOT_TOKEN belum diatur. Tambahkan token di environment variable."
        )

    application = Application.builder().token(settings.bot_token).build()
    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_handler))
    return application


def main() -> None:
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    application = build_application()
    logging.info("MrKarirBot mulai berjalan.")
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
