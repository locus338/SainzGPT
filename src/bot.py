import asyncio
import re

from disnake import Message, Game, Status
from disnake.abc import Messageable
from disnake.ext.commands import InteractionBot

from .conversation import Conversation, ConversationStatus, Question

loading = "✅" 
cross = "❌" 

async def keep_typing(channel: Messageable):
    while True:
        await channel.trigger_typing()
        await asyncio.sleep(10)


class Bot(InteractionBot):
    def __init__(self, conversation: Conversation, *args, **kwargs):
        """
        :param conversation: Conversation instance
        :param args: args
        :param kwargs: kwargs
        """
        super().__init__(*args, **kwargs)

        self.conversation = conversation

        self.conversation.start_asking_loop(self.loop)

    async def on_ready(self):
        if self.conversation.status != ConversationStatus.PREPARED:
            await self.change_presence(activity=Game("準備中"), status=Status.dnd)

            await self.conversation.prepare()

            await self.change_presence(activity=Game("EK的電腦"), status=Status.online)

    async def on_message(self, message: Message):
        if message.author.bot:
            return

        if message.author.id == self.user.id:
            return

        if self.user not in message.mentions:
            return

        typing_task = self.loop.create_task(keep_typing(message.channel))
        
        await message.add_reaction(loading)
        
        try:
            pass
        except Exception as e: 
            print("==============================[ERROR]==============================")
            e = str(e)
            await message.remove_reaction(self.user)
            await message.add_reaction(cross)
        
        prompt = re.sub(r'<@([0-9]+)>', "", message.content)

        response = await self.conversation.ask(Question(prompt))

        typing_task.cancel()

        await message.reply(response)
