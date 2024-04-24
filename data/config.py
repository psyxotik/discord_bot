from discord import Intents

Token = 'MTIxMTMzNTUyMjAyNzQzODE3MQ.GINbBW.MoPwurhStdhnmNCHT5VTNrmKBH1Lf3NA6BiENY'

intents = Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True