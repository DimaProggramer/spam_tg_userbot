from pyrogram import Client, filters
api_id = hey_type_here_yourapi
api_hash "pleasekillme"
app = Client("MyAccountSession", api_id, api_hash)

text = ""

@app.on_message(filters.command("spam", prefixes='.') & filters.me)
async def spam(client, message):
    while True:
        await app.send_message(message.chat.id, text)

# im idiot N1
app.run()
