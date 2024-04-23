from pyrogram import Client, filters
api_id = hey_type_here_yourapi
api_hash "pleasekillme"
app = Client("MyAccountSession", api_id, api_hash)

@app.on_message(filters.command("spam", prefixes='.') & filters.me)
def spam(client, message):
    text = message.text.split(".spam ", maxsplit=1)[1]
    for _ in range(10):
        app.send_message(chat_id=message.chat.id, text=text)

app.run()
