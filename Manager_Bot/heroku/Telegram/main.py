from telethon import TelegramClient, events


async def main(i):
    await client.send_message('me', str(i))


async def end():
    await client.send_message('me', 'END')


if __name__ == "__main__":
    with TelegramClient('MaxMesh', 1937357, '766afd98ce483cf336d71618ba57a847') as client:
        for i in range(10):
            client.loop.run_until_complete(main(i))
