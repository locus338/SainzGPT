import asyncio
from os import getenv

from disnake import Intents
from revChatGPT.V1 import Chatbot

from src.bot import Bot
from src.conversation import Conversation, Question


config = {
  "email":"locus338@gmail.com",
  "password":"",
  "access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJsb2N1czMzOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZX0sImh0dHBzOi8vYXBpLm9wZW5haS5jb20vYXV0aCI6eyJ1c2VyX2lkIjoidXNlci00b3VDQjJMcnhnS3M3emRPS3lTQWRQZVkifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEzOTUzOTM4MzkzODQ0MzQzODM3IiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY4MzIxMDUyMSwiZXhwIjoxNjg0NDIwMTIxLCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.IpBsg5uSLv6OjCeO6L6DUDGbJP7_boasSJlM_pftJvY6Rk-PwatWY0LC9Ar72Wl18UZ3-R7dWFhTy_jiZ8St0k8ikL85CU2hrmx0-CJ-SGVdexfCgz2fpXq0rhaUBOFmYy8C4vA4hQsU_D5UM4BA2AxkZnQtjlVeaMnxgCGSE1c2PCBk2ZAOlEVwPm_y0KKttz_gyRx2U7G93v5PNPN4nCi-RSHqCuFsMq9IlVgjRF9MRDsMlnmOoFGfNXg34fD2FqLYFQLeAC7Zjg7ePI2sg6b7mwDW5cB66w1xrrpUg87il21TaglfsnRqSi6TXUCCWlYQZvCiSQGCxdy0zKJz8w"
}

def main():
    conversation = Conversation(
        Chatbot(config=config),
        load_brainwash()
    )

    bot = Bot(conversation, intents=Intents.all())

    try:
        bot.run(getenv("DISCORD_TOKEN"))
    except KeyboardInterrupt:
        conversation.close()

        asyncio.get_event_loop().close()


def load_brainwash() -> list[Question]:
    """
    Load brainwash messages from brainwash.txt
    :return: A list of Question
    """
    with open(getenv("BRAINWASH_PATH", "./brainwash.txt"), "r", encoding='utf-8') as f:
        return [Question(line) for line in f.readlines()]


if __name__ == "__main__":
    main()
