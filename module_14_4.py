from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

mainkeyb = ReplyKeyboardMarkup(resize_keyboard = True)
mainbutton1 = KeyboardButton(text = "Расчет калорий по формуле Миффлина-Сан Жеора")
mainbutton2 = KeyboardButton(text = "Купить продукты для здоровья")
mainkeyb.add(mainbutton1)
mainkeyb.add(mainbutton2)

countkeyb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text = "Рассчитать норму калорий", callback_data='calories')
button2 = InlineKeyboardButton(text = "Формулы расчета", callback_data='formulas')
countkeyb.row(button1, button2)

pbkeyb = InlineKeyboardMarkup()
button1 = InlineKeyboardButton(text="Product 1", callback_data='product_buying')
button2 = InlineKeyboardButton(text="Product 2", callback_data='product_buying')
button3 = InlineKeyboardButton(text="Product 3", callback_data='product_buying')
button4 = InlineKeyboardButton(text="Product 4", callback_data='product_buying')
pbkeyb.row(button1, button2, button3, button4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий вашему здоровью.", reply_markup = mainkeyb)

@dp.message_handler(text = ['Расчет калорий по формуле Миффлина-Сан Жеора'])
async def main_menu(message):
    await message.answer("Выберите опцию.", reply_markup = countkeyb)

@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer("Для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()

@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer("Введите свой возраст.")
    await UserState.age.set()
    await call.answer()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer("Введите свой рост.")
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer("Введите свой вес.")
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    norm = (10 * int(data['weight'])) + (6.25 * int(data['growth'])) - (5 * int(data['age'])) - 161
    await message.answer(f"Ваша норма калорий: {norm}")
    await state.finish()

@dp.message_handler(text = ['Купить продукты для здоровья'])
async def get_buying_list(message):
    products = crud_functions.get_all_products()
    for product in products:
        await message.answer(f"Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}")
    await message.answer("Выберите продукт для покупки.", reply_markup=pbkeyb)


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")

@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

crud_functions.initiate_db()
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)