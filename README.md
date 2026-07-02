# MrKarirBot

MrKarirBot adalah AI Career Assistant berbasis Telegram untuk membantu pengguna:

- mencari lowongan kerja,
- membuat CV ATS,
- menyiapkan surat lamaran,
- latihan interview,
- memeriksa indikasi penipuan lowongan,
- dan melacak proses lamaran kerja.

## Menjalankan secara lokal

1. Salin `.env.example` menjadi `.env`.
2. Isi `BOT_TOKEN`.
3. Instal dependensi:

```bash
pip install -r requirements.txt
```

4. Jalankan bot:

```bash
python main.py
```

## Status

Fondasi proyek dan handler `/start` serta `/help` sudah disiapkan.
Fitur lainnya akan dikembangkan bertahap.
