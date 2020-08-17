import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        # if message.author.id == self.user.id:
        #     return


        if message.content.startswith('?hi'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('?poll'):
 
            vals = message.content.split(";")
            if vals[-1] == "":
                vals.pop(-1)
            
            await message.delete()

            if len(vals) > 12:
                await message.channel.send("Cannot handle more than ten options :(")
                return

            if len(vals) != 6:     
                reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
            else:
                reactions = ['\N{REGIONAL INDICATOR SYMBOL LETTER A}' , '\N{REGIONAL INDICATOR SYMBOL LETTER B}', "\N{REGIONAL INDICATOR SYMBOL LETTER C}", "\N{REGIONAL INDICATOR SYMBOL LETTER D}"]

            options = ""
            for x in range(len(vals) - 2):
                options += reactions[x] + " " + vals[x+2] + "\n"
            # embedVar = discord.Embed(title= vals[1], description=options, color=0x00ff00)
            embedVar = discord.Embed(title= vals[1], description=options, color=0xFF7700)
            # embedVar = discord.Embed(title= vals[1], description=options, color=message.author.color)
            embedVar.set_author(name=f"{message.author}", icon_url=message.author.avatar_url)
            # embedVar.set_thumbnail(url=message.author.avatar_url)
            
            poll = await message.channel.send(embed=embedVar)
            for x in range(len(vals) - 2):
                await poll.add_reaction(reactions[x])

            

client = MyClient()
client.run('NzQ0MTEyNTgyOTM1MTgzNDEz.Xzee2A.6c9LkX-Hc3AhB-y64DUoTeE3_wM')


