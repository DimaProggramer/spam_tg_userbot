text = ""

@app.on_message(filters.command("spam", prefixes='.') & filters.me)
async def spam(client, message):
    while True:
        await app.send_message(message.chat.id, text)

# im idiot N1
