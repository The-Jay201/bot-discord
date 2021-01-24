import discord, random
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print("Bot ready!!")

@commands.has_role("👌ADMIN👌")
@client.command()
async def kick(ext, member : discord.Member, alasan=None):
    try:
        await member.kick(reason=alasan)
        await ext.send("{} telah ter kick karena alasan {}".format(member.name, alasan))
    except:
        await ext.send("Maaf anda tidak bisa kick user dengan role anda, anda harus gunakan role 👌ADMIN👌 untuk bisa kick user!!")

@client.command()
async def role(ext, member : discord.Member):
    await ext.send("Role {} adalah {}".format(member.name, member.roles))

@client.command()
@commands.has_role("👌ADMIN👌")
async def ban(ext, member : discord.Member, alasan=None):
    try:
        await member.ban(reason=alasan)
        await ext.send("{} telah terban dari server karena {}!!".format(member.name, alasan))
    except:
        await ext.send("Maaf anda tidak bisa ban user dengan role anda, anda harus menggunakan role 👌ADMIN👌 untuk bisa ban user!!")

@client.command(aliases = ['q&a'])
async def qna(ext, *, message):
    respon = [
            'ya',
            'yes',
            'tidak',
            'kemungkinan',
            'mudah-mudahan',
            'gak akan',
            'pasti bisa',
            'gak tau',
            'tetap semangat',
            'semangat',
            'hacker',
            'mungkin bisa',
            'semoga beruntung',
            'hebat',
            'white hat hacker',
            'black hat hacker',
            'ethical hacker',
            'ethical hacking',
            'web hacking',
            'computer hacking',
            'cyber security',
            'komputer forensik',
            'wkwkwkwwk',
            'bisa lah',
            'gak guna',
            'hacker',
            'suatu hari',
            'mungkin suatu hari',
            'hacker terkenal'
            ]
    await ext.send("Pertanyaan: {}, Jawaban: {} ".format(message, random.choice(respon)))

client.run("NzQwOTI1MTg3MTg4MzI2NDQw.XywGWg.TEWu9JfzyZfhZW1C_umCuZ-7mRY")
