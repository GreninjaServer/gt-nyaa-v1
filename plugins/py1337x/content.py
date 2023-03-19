from pyrogram import Client, filters


@Client.on_message(filters.regex('getLink'))
async def results(Client, message):
    user_lang = await Client.MISC.user_lang(message)
    torrent_id = message.text.split('_')[1]
    response = Client.py1337x.info(torrentId=torrent_id)

    text = Client.STRUCT.content_message(response, user_lang)

    await Client.send_message(
        chat_id=message.chat.id,
        text=text,
        reply_markup=Client.KB.torrent_info(response.get('infoHash')),
    )
