from aiogram.dispatcher import FSMContext


from keyboards.default.user import user_main_menu
from load import dp, db
from aiogram import types



@dp.message_handler(text="Rasm joylash")
async def user_upload_photo(message: types.Message, state: FSMContext):
    photo = db.get_user_photo_by_chat_id(chat_id=message.chat.id)
    if photo:
        text = f"""
        Rasm alaqachon joylangan"""
        await message.answer_photo(photo=photo[2])
    else:
        text = "Iltimos yoqtirgan rasmingizni yuboring"
    await state.set_state("user-upload-photo")
    await message.answer(text=text)



@dp.message_handler(state="user-upload-photo", content_types=types.ContentTypes.PHOTO)
async def get_upload_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id, chat_id=message.chat.id)
    data = await state.get_data()

    if db.add_photo(data):
        text = f"Rasm qo'shildi"
    else:
        text = "Rasm qo'shilmadi"
    await message.answer(text=text)
    await state.finish()