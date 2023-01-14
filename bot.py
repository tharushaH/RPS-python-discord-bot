import discord
import responses

api_key = "41cab34c0ed6db700f035af8c25392bb"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

async def send_message(message, user_message, author, is_private):
    try:
        #Calls the function get_response which passes the truncated user message
        response = responses.get_response(user_message, author)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA2MjA5ODk2MDU2NDYyNTQ1OA.GSIhRz.9wyjzeQl8yLKjbIG5KffipZf9iYiCuEPirBz5A'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        #Make sure the bot does not reply to itself
        if message.author == client.user:
            return

        #Get the author, message, and message location
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
        if user_message.startswith('private ') :
            user_message = user_message[8:]
            await send_message(message, user_message, username, is_private=True)
        else:
            await send_message(message, user_message, username, is_private=False)

        
        
    client.run(TOKEN)