import random

import config
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def filter_messages(message: types.Message):

    chatId = message.chat.id
    text = message.text.lower()

    ### ГИБЛОЕ ДЕЛО ###
    if "дела " in text or "дело" in text:
        await bot.send_voice(chatId, open("sounds/1.mp3", 'rb'))

    ### ФАЕР ОЧЕНЬ ЛЮБИТ МЕТАЛ ###
    if 'метал' in text or 'песня' in text or 'музыка' in text:
        await bot.send_voice(chatId, open("sounds/любит метал.ogg", 'rb'))

    ### КОНЕЧНО ТЫ ЭТОГО НЕ ДЕЛАЛ ###
    if "делал" in text or "геноцид" in text or "резня" in text:
        await bot.send_voice(chatId, open("sounds/конечно ты этого не делал.ogg", 'rb'))

    ### КОНТЕНТ ###
    if "контент" in text:
        await bot.send_voice(chatId, open("sounds/дада мы тебя поняли конттент.ogg", 'rb'))

    ### МЛАДЕНЕЦ ###
    if "младенец" in text or 'ребеночек' in text or 'мальчик' in text or 'ребёночек' in text or 'слыш' in text:
        await bot.send_voice(chatId, open("sounds/дада мы тебя поняли конттент.ogg", 'rb'))

    ### НАЧАЛ И ЧЕ ###
    if "зачем ты" in text or "арсений зачем" in text or "зачем арсени" in text or "начинать" in text:
        await bot.send_voice(chatId, open("sounds/НУ НАЧАО И ЧЕ.ogg", 'rb'))

    ### ТЫ ТАКОЙ ОРИГИНАЛЬНЫЙ ###
    if "арсений ты лох" in text or "арсений ты чмо" in text or "твоя мам" in text or "жирная мамаша" in text in text or "оригинал" in text:
        await bot.send_voice(chatId, open("sounds/ой фаер ты такой оригинальный.ogg", 'rb'))

    ### ПОДДЕРЖИВАЮ ###
    if "войн" in text or 'спецоперация' in text:
        await bot.send_voice(chatId, open("sounds/ПОДДЕРЖИВАЮ.ogg", 'rb'))

    ### ПРОСТО ГЕНИЙ ###
    if "гений" in text or "гей" in text or "тимофе" in text or "200 iq" in text in text or "300 iq" in text:
        await bot.send_voice(chatId, open("sounds/ПРОСТО ГЕНИЙ.ogg", 'rb'))

    ### СВОИ ЛЮБИМЫЕ ПЕСНИ ###
    if 'метал' in text or 'песня' in text or 'музыка' in text or 'гиперпоп' in text or 'рок' in text:
        await bot.send_voice(chatId, open("sounds/СВОИ ЛЮБИМЫЕ ПЕСНИ.ogg", 'rb'))

    ### ТАК МЫ ТЕБЕ И ПОВЕРИЛИ ###
    if 'купил' in text or 'честно' in text or 'у меня есть' in text or 'это не я' in text:
        await bot.send_voice(chatId, open("sounds/так м ытебе и поверили.ogg", 'rb'))

    ### ЧЕ ТО ПРО ДЕВУШЕК ###
    if 'девушк' in text or 'девоч' in text or 'бронислава' in text or 'тяночк' in text:
        await bot.send_voice(chatId, open("sounds/че то про девушек.ogg", 'rb'))

    ### НЕ ПИСАЛ ###
    if 'какал' in text or 'какает' in text or 'писает' in text or 'писал' in text or 'писать' in text or 'какать' in text:
        await bot.send_voice(chatId, open("sounds/я там не писал.ogg", 'rb'))

    ### ФАЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕР ###
    if 'фаер' in text or 'леха' in text or 'леша' in text or 'fireholdest' in text:
        vrs = ['sounds/ФАЕР Я КОНЕЧНО ВСЕ ПОНИМАЮ.ogg', 'sounds/фаер какой же ты глупый.ogg', 'sounds/ты меня уже достал.ogg']
        choices = random.choices(vrs, k=1)
        await bot.send_voice(chatId, open(str(choices)[2:][:-2], 'rb'))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)