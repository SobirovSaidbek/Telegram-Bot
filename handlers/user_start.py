from aiogram.dispatcher import FSMContext

from keyboards.default.user import user_main_menu
from load import dp, db
from aiogram import types


from states.states import RegisterStates


@dp.message_handler(commands=['start'])
async def user_start(message: types.Message):
    if db.get_user_by_chat_id(chat_id=message.chat.id):
        text = "Asslamo alaykum, xush kelibsz"
        await message.answer(text=text, reply_markup=user_main_menu)
    else:
        text = "Asslamo alaykum, ismingizni kiriting"
        await message.answer(text=text)
        await RegisterStates.full_name.set()


@dp.message_handler(state=RegisterStates.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text, chat_id=message.chat.id)
    text = "Telfon Raqamni kiriting "
    await message.answer(text=text)
    await RegisterStates.phone_number.set()


@dp.message_handler(state=RegisterStates.phone_number)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    text = "Manzil joyllashuv "
    await message.answer(text=text)
    await RegisterStates.location.set()


@dp.message_handler(state=RegisterStates.location)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)

    data = await state.get_data()
    if db.add_user(data):
        text = "Muvafaqiyatli qoshildi  ✅"
    else:
        text = "Xalotik bor ❌"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()