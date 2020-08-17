import discord

def poller():
    global ques
    global options

    pollstr = "?poll"  + ';' +ques 

    for answers in options:
        pollstr += ';' + answers

    return pollstr

while True:
    try:
        boom_no = int(input("Enter boom number(1 to 6): "))
    except ValueError:
        print("Wrong Input! Try Again!!", end="\n\n")
        continue
  
    if boom_no in {1,2,3,4,5,6}:
        print("?boom" + str(boom_no) + " SELECTED!", end="\n\n")
        break
    else:
        print("Boom number can be between 1 to 6 only, Try Again")


if boom_no == 1:
    listofpolls1 = []
elif boom_no == 2:
    listofpolls2 = []
elif boom_no == 3:
    listofpolls3 = []
elif boom_no == 4:
    listofpolls4 = []
elif boom_no == 5:
    listofpolls5 = []
else: 
    listofpolls6 = []


run2 = True
qcount = 1
while run2:
    ques = str(input("Enter the question(" +str(qcount) + "):" ))
    qcount += 1
    if ques == "":
        run2 = False
        run = False
    options = []

    run = True
    num = 1

    while run:
        inp = str(input("Enter option " +str(num)+ " : "))
        if inp == "":
            run = False
        options.append(inp)
        num += 1
    if ques != "":

        if boom_no == 1:
            listofpolls1.append(poller())
        elif boom_no == 2:
            listofpolls2.append(poller())
        elif boom_no == 3:
            listofpolls3.append(poller())
        elif boom_no == 4:
            listofpolls4.append(poller())
        elif boom_no == 5:
            listofpolls5.append(poller())
        else: 
            listofpolls6.append(poller())
    else:
        print()
        print("ALL POLLS SAVED!!!")
    
    if ques != "":    
        print()	
        print("SAVED!!")
        print(poller())
        print()

print("Waiting for Boom Activation...")


class MyClient(discord.Client):
    async def on_ready(self):
        print('------')
        print()
        print("?boom" + str(boom_no) + " Activated!!")
        print()
        print("ALL COMMANDS READY TO DEPLOY...BOOM IT")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        # if message.author.id == self.user.id:
        #     return


        if message.content.startswith('?status'):
            await message.channel.send('{0.author.mention}'.format(message) + " Boom " + str(boom_no) + " [RUNNING]" )
        
        if message.content.startswith('?boom') and len(message.content) == 5:
            await message.channel.send("<Invalid Request>\nType ?boom<boom no>")

        if message.content.startswith('?boom1'):
            if boom_no != 1:
                return
            for commands in range(len(listofpolls1)):
                await message.channel.send(listofpolls1[commands])  

        if message.content.startswith('?boom2'):
            if boom_no != 2:
                return
            for commands in range(len(listofpolls2)):
                await message.channel.send(listofpolls2[commands])  
 
        if message.content.startswith('?boom3'):
            if boom_no != 3:
                return
            for commands in range(len(listofpolls3)):
                await message.channel.send(listofpolls3[commands])    

        if message.content.startswith('?boom4'):
            if boom_no != 4:
                return
            for commands in range(len(listofpolls4)):
                await message.channel.send(listofpolls4[commands])  

        if message.content.startswith('?boom5'):
            if boom_no != 5:
                return
            for commands in range(len(listofpolls5)):
                await message.channel.send(listofpolls5[commands])  

        if message.content.startswith('?boom6'):
            if boom_no != 6:
                return
            for commands in range(len(listofpolls6)):
                await message.channel.send(listofpolls6[commands])     

client = MyClient()
try:
    client.run('NzQ0MTEyNTgyOTM1MTgzNDEz.Xzee2A.6c9LkX-Hc3AhB-y64DUoTeE3_wM')
except:
    print()
    print("There was some problem while connecting to Discord :(")
    print("Check your Internet Connection")
