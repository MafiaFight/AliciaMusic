from pyrogram import Client as Aliciabot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from AliciaMusic.config import BOT_NAME as bn, BG_IMAGE




@Aliciabot.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start_(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}![๐ค]({BG_IMAGE})
        
I am ๐๐ฐ๐๐ฌ๐จ๐ฆ๐ ๐๐ฅ๐จ๐ฌ๐ฌ๐จ๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐๐จ๐ญ๐ถ๐ธ
I can play songs in your group's VC ๐ค
To listen songs add me to your group..
And don't forgot to promote me with all rights!๐ฅฐ
Otherwise I can't play songs!๐ฅบ๐๐
Use the buttons below to know more about me..๐
Add my assistant @A_B_Music_Assistant
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "โกCommandsโก", url="https://telegra.ph/MUSIC-BOT-COMMANDS-09-28")
                  ],[
                    InlineKeyboardButton(
                        "Owner๐", url="https://t.me/best_friends_official1"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Github๐ค", url="https://t.me/H1M4N5HU0P"
                    )],[
                    InlineKeyboardButton(
                        "โ Add To Your Group โ", url="https://t.me/Awesome_blossom_music_bot?startgroup=true"
                    )
                ]
            ]
        ),
    )

@Aliciabot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(client: Aliciabot, message: Message):
      await message.reply_text("""**๐๐ฐ๐๐ฌ๐จ๐ฆ๐ ๐๐ฅ๐จ๐ฌ๐ฌ๐จ๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐๐จ๐ญ๐ถ๐ธ is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner๐", url="https://t.me/best_friends_official1")
                ]
            ]
        )
   )


@Aliciabot.on_message(filters.command("help") & filters.private & ~filters.channel)
async def help(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.โก๐ฅ
        """)
        

@Aliciabot.on_message(filters.command("commands") & filters.private & ~filters.channel)
async def commands(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
          message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.โก๐ฅ
        """)
