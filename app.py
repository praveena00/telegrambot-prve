from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client
aio = Client('prve', 'aio_IhIA80eg9c9KguplvfO4FCTEQi1D')

def demo1(bot,update):
   chat_id=bot.message.chat_id
   path='https://cdn1.vectorstock.com/i/1000x1000/91/20/i-am-ok-calligraphy-for-typography-vector-15589120.jpg'
   bot.message.reply_text('I am fine')
   update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
   bot.message.reply_text('My name is prvebot')
def turnonlight(bot,update):
   chat_id=bot.message.chat_id
   path='https://5.imimg.com/data5/WL/SG/MY-8835990/10w-gls-light-bulb-500x500.jpg'
   bot.message.reply_text('Light is turned on')
   update.bot.sendPhoto(chat_id=chat_id,photo=path)
   aio.send('bedroom-light', 1)
   data = aio.receive('bedroom-light')
   print(f'Received value: {data.value}')
def turnofflight(bot,update):
   chat_id=bot.message.chat_id
   path='https://cdn3.vectorstock.com/i/1000x1000/25/37/realistic-modern-light-bulb-off-vector-14042537.jpg'
   bot.message.reply_text('Light is turned off')
   update.bot.sendPhoto(chat_id=chat_id,photo=path)
   aio.send('bedroom-light', 0)
   data = aio.receive('bedroom-light')
   print(f'Received value: {data.value}')
def turnonfan(bot,update):
   chat_id=bot.message.chat_id
   path='https://thumbs.dreamstime.com/b/spinning-gray-ceiling-fan-picture-summer-134473260.jpg'
   bot.message.reply_text('Fan is turned on')
   update.bot.sendPhoto(chat_id=chat_id,photo=path)
   aio.send('bedroom-fan', 1)
   data = aio.receive('bedroom-fan')
   print(f'Received value: {data.value}')
def turnofffan(bot,update):
   chat_id=bot.message.chat_id
   path='https://5.imimg.com/data5/XS/MM/KF/SELLER-99661502/1200mm-electric-celling-fan-500x500.jpg'
   bot.message.reply_text('Fan is turned off')
   update.bot.sendPhoto(chat_id=chat_id,photo=path)
   aio.send('bedroom-fan', 0)
   data = aio.receive('bedroom-fan')
   print(f'Received value: {data.value}')
def main(bot,update):
  a=bot.message.text.lower()
  print(a)
  if a=="how are you?":
    demo1(bot,update)
  elif a=="what is your name?" or a=="name please":
    demo2(bot,update)
  elif a=="turn on light" or a=="light on":
    turnonlight(bot,update)
  elif a=="turn off light" or a=="light off":
    turnofflight(bot,update)
  elif a=="turn on fan" or a=="fan on":
    turnonfan(bot,update)
  elif a=="turn off fan" or a=="fan off":
    turnofffan(bot,update)
  else :
     bot.message.reply_text('invalid text')
BOT_TOKEN = '1871118778:AAFb3Y9z6DP2iC0vxY3pB84BYJuEls5GNx8'
u= Updater(BOT_TOKEN,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

