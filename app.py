import handlers, middlewares, filters
from load import dp, db
from aiogram import executor


async def on_startup(dispatcher):
    #db.create_tables()
    pass

async def on_shutdown(dispatcher):
    db.conn.close()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_shutdown=on_shutdown, on_startup=on_startup)