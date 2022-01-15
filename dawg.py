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
    if ctx.channel.id == :
        member = ctx.message.author
        roles = member.roles
        clear = True
        for role in roles:
            for real_role in roles_list:
                if role == real_role:
                    clear = False
        if clear:
            if cred == 'guild':
                response = requests.get("https://gameinfo.albiononline.com/api/gameinfo/guilds//members")
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
                response = requests.get("https://gameinfo.albiononline.com/api/gameinfo/alliances/")
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


if __name__ == "__main__":
    bot.run(TOKEN)
