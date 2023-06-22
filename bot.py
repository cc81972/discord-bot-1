import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    except Exception as e:
        print(e)
        
def run_discord_bot():
    TOKEN = 'MTExNzk2OTkxMjc0OTY0MTc1OA.GZMBVN.naD7PL-55LUs50GV3NmeR0DsfIC82OCUx4uJ0I'
    TARGET_USER_ID = [780933023620268042]
    TARGET_VOICE_CHANNEL_ID = 871828353374621706
    TARGET_TEXT_CHANNEL_ID = 879940992013332521
    intents = discord.Intents.default()  # Create a default intents object
    intents.message_content = True  # Disable typing events if you don't need them
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now runnning!')
        
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
    @client.event
    async def on_voice_state_update(member, before, after):
        if member.id in TARGET_USER_ID and after.channel and after.channel.id == TARGET_VOICE_CHANNEL_ID:
            guild = member.guild
            channel = guild.get_channel(TARGET_TEXT_CHANNEL_ID)
            await channel.send("Sam the rizzler has joined vc!")
    
    client.run(TOKEN)
