from discord import Intents

Token = 'YOUR_TOKEN'

intents = Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
