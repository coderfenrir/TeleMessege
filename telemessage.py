# This Python script
# is used to send a specific
# message to a particular user on
# Telegram a certain number of times.
# The owner of this script is coderfenrir.

import os
import time
import asyncio
from telethon import TelegramClient
from telethon.tl.types import User

print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Instagram / github @coderfenrir")
time.sleep(2)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m TeleMessage V3.1-BETA")
time.sleep(2)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Kullanıcıya sınırsız mesaj gonderme programı. \033[0m")
time.sleep(2)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m TeleMessage programı başlatılıyor... \033[0m")
time.sleep(5)

# Renkli banner
def banner():
    os.system("clear")
    print("""\033[0;96m
        _
       / \      _-'/
     _/|  \-''- _ /
__-' { |          \)
    /             \)
    /       "o.  |o }
    |            \ ;
                  ',
       \_         __)
         ''-_    \.//
           / '-____'
          /
        _'
      _-'\033[0m
\033[0;32m
┏┳┓┏┓┓ ┏┓┳┳┓┏┓┏┓┏┓┏┓┏┓┏┓
 ┃ ┣ ┃ ┣ ┃┃┃┣ ┗┓┗┓┣┫┃┓┣
 ┻ ┗┛┗┛┗┛┛ ┗┗┛┗┛┗┛┛┗┗┛┗┛
          \033[0m
\033[1;35mİnstagram: coderfenrir
\033[1;36mGithub: coderfenrir
\033[1;31mVersion: 3.1-BETA
\033[0m""")

async def main():
    # Giriş bilgileri
    banner()
    api_id = input("\033[34m[⌯]\033[0m\033[36m API ID girin: \033[0m")
    api_hash = input("\033[34m[⌯]\033[0m\033[36m API Hash girin: \033[0m")
    phone_number = input("\033[34m[⌯]\033[0m\033[36m Telefon numarası (ülke kodu ile): \033[0m")

    # Telegram client
    client = TelegramClient('session', api_id, api_hash)

    # Giriş
    await client.start(phone_number)

    # Kullanıcıları bul
    users = []
    async for dialog in client.iter_dialogs():
        if isinstance(dialog.entity, User):
            users.append(dialog.entity)

    # Kullanıcıları listele
    banner()
    for i, user in enumerate(users):
        print(f"\033[1;33m{i+1}. {user.first_name} {user.last_name if user.last_name else ''} (@{user.username})\033[0m")

    # Kullanıcı seçimi
    user_index = int(input("\033[36m[::] Kullanıcı numarası girin: \033[0m"))
    user = users[user_index - 1]

    # Mesaj ve gönderme adedi
    message = input("\033[35mGönderilecek mesajı giriniz: \033[0m")
    count = int(input("\033[35mKaç defa göndermek istiyorsunuz: \033[0m"))

    # Mesaj gönderme
    for _ in range(count):
        await client.send_message(user, message)
        await asyncio.sleep(0.1)

    # Başarı mesajı
    print("\033[1;32mMesajlar başarıyla gönderildi!\033[0m")

asyncio.run(main())
