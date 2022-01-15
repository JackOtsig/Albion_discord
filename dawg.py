import os,  pathlib, discord, requests
from dotenv import load_dotenv
from discord.ext import commands



path = str(pathlib.Path(__file__).parent.resolve())
os.chdir(path)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents, activity=discord.Game(name='amogus'))
kills_list = []
timer = False



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

#id n2dLeMAmS7u-nna6svhyAg
@bot.command()
async def verify(ctx, cred, username):
    member_role = discord.utils.find(lambda r: r.name == 'Member', ctx.message.guild.roles)
    recruit_role = discord.utils.find(lambda r: r.name == 'Recruit', ctx.message.guild.roles)
    alliance_role = discord.utils.find(lambda r: r.name == 'Alliance', ctx.message.guild.roles)
    officer_role = discord.utils.find(lambda r: r.name == 'Officer', ctx.message.guild.roles)
    rh_role = discord.utils.find(lambda r: r.name == 'The Right Hand', ctx.message.guild.roles)
    roles_list = [
        recruit_role,
        member_role,
        alliance_role,
        officer_role,
        rh_role,
    ]
    if ctx.channel.id == 931293831582855189:
        member = ctx.message.author
        roles = member.roles
        clear = True
        for role in roles:
            for real_role in roles_list:
                if role == real_role:
                    clear = False
        if clear:
            if cred == 'guild':
                response = requests.get("https://gameinfo.albiononline.com/api/gameinfo/guilds/n2dLeMAmS7u-nna6svhyAg/members")
                match = False
                for user in response.json():
                    if username.lower() == user['Name'].lower():
                        match = True
                        break
                if match == True:
                    await member.add_roles(roles_list[0])
                    await ctx.send('Verified!')
                else:
                    await ctx.send("Sorry, couldn't verify!")
            elif cred == 'alliance':
                response = requests.get("https://gameinfo.albiononline.com/api/gameinfo/alliances/Yzq8-LgPTIm-9SMVdyAN8w")
                guilds = response.json()['Guilds']
                alliance_member_list = []
                id_list = []
                for guild in guilds:
                    id_list.append(guild['Id'])
                    for id in id_list:
                        response = requests.get("https://gameinfo.albiononline.com/api/gameinfo/guilds/"+id+"/members")
                        for user in response.json():
                            alliance_member_list.append(user['Name'])
                for user in alliance_member_list:
                    if username.lower() == user.lower():
                        match = True
                        break
                if match == True:
                    await member.add_roles(roles_list[2])
                    await ctx.send('Verified!')
                else:
                    await ctx.send("Sorry, couldn't verify!")
            else:
                await ctx.send('not a valid parameter')
        else:
            await ctx.send("you don't need this lol")
    else:
        await ctx.send('wrong channel!')

# def get_sent():
#     f = open('sent.json','r')
#     sent_list = json.load(f)
#     f.close()
#     return sent_list

# def save_sent(id):
#     f = open('sent.json', 'w')
#     old_list = get_sent()
#     old_list.append(id)
#     new_list_json = json.dumps(old_list)
#     f.write(new_list_json)
#     return

# async def kills():
#     global kills_list
#     print('refreshing kills')
#     response = requests.get('https://gameinfo.albiononline.com/api/gameinfo/events?limit=40&offset=0&guildId=n2dLeMAmS7u-nna6svhyAg')
#     print('response gotten')
#     for kill in response.json():
#         event_id = kill['EventId']
#         killer = {
#             'name' : kill['Killer']['Name'], 
#             'gear' : kill['Killer']['Equipment'], 
#             'guild' : [kill['Killer']['GuildName'], kill['Killer']['GuildId']],
#             'alliance' : [kill['Killer']['AllianceName'], kill['Killer']['AllianceId']]
#         }
#         victim = {
#             'name' : kill['Victim']['Name'], 
#             'gear' : kill['Victim']['Equipment'], 
#             'guild' : [kill['Victim']['GuildName'], kill['Victim']['GuildId']],
#             'alliance' : [kill['Victim']['AllianceName'], kill['Victim']['AllianceId']]
#         }
#         kills_list.append({'id' : event_id, 'killer' : killer, 'victim' : victim, 'recap' : killer['name']+' killed '+victim['name']})
#         while len(kills_list) > 5:
#             kills_list.pop(0)
#     print('kills updated')
#     return kills_list

# async def kills_not():
#     print('starting notification')
#     channel = bot.get_channel(927270590140792884)
#     print('got channel')
#     printed = get_sent()
#     print('sent list gotten')
#     match = False
#     print('match set to false')
#     kills_list = await kills()
#     print('kills awaited')
#     print('got kills')
#     for kill in kills_list:
#         if not printed:
#             await channel.send(kill['recap'])
#             save_sent(kill['id'])
#         else:
#             for log in printed:
#                 if kill['id'] == log:
#                     match = True
#             if not match:
#                 await channel.send(kill['recap'])
#                 save_sent(kill['id'])
#     return printed

# @tasks.loop(seconds=15)
# async def kbl():
#     await kills_not()
#     print('looped')
# kbl.start()

if __name__ == "__main__":
    bot.run(TOKEN)
