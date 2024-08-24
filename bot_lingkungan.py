import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'halo aku adalah bot {client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
    if message.content.startswith('$apa itu plastik?'):
        await message.channel.send("Plastik adalah salah satu makromolekul yang proses pembentukannya melalui tahap polimerisasi. Polimerisasi adalah suatu proses penggabungan dari beberapa molekul sederhana atau monomer menjadi molekul besar yang disebut makromolekul atau polimer melalui suatu proses kimia.")

        
client.run("TOKEN ADA DI VISUAL STUDIO CODE")
