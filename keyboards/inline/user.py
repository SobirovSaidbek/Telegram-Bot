from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

user_like_data = CallbackData('like', 'act', 'photo_id')
user_dislike_data = CallbackData('dislike', 'act', 'photo_id')

async def user_like_button_def(likes, dislikes, photo_id):
    user_like_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=f"{likes} 👍", callback_data=user_like_data.new(act="like", photo_id=photo_id)),
                InlineKeyboardButton(text=f"{dislikes} 👎", callback_data=user_dislike_data.new(act="dislike", photo_id=photo_id))
            ]
        ]
    )
    return user_like_button

