import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello_to_Alfred(ctx):
    await ctx.send(f'Я {bot.user}, ваш любимый преподаватель по физике и математике. Думаю, мы с тобой подружимся.')

@bot.command()
async def talk_to_Alfred(ctx):
    talk_to_Alfred = ["У нас сегодня открытая пара, не забудьте свои тетради.", "Вечером состоится финал игр волейбола между преподавателями. Нет, я не настаиваю на том, чтобы ты голосовал(а) за меня... Я и Кайн будем играть против Сэм и Альфреда. Уверен, мы справимся.", "Что? Сэм боится пауков? Это хороший повод подшутить...", "Надо бы взять отпуск.", "Не хотите сходить на прогулку? Высадимся на Землю возле какого-нибудь моря. Считайте это школьной поездкой.", "Сэм просила передать, чтобы вы ей не мешали.", "Звездный Скиталец отправит вам ваше домашнее задание на сегодня. Будьте добры быть готовыми к следующему уроку. Поблажек не будет!", "Зачем Кайн передал мне эти ключи?.."]
    await ctx.send(random.choice(talk_to_Alfred))

@bot.command()
async def lesson_about_math(ctx):
    lesson_about_math = ["Миг — это количество времени равное 0,01 секунды.", "Знаменитый профессор математики Стивен Хокинг, наш современник, неоднократно говорил о том, что он обучался математике только в школе. Когда же Стивен преподавал в университете, он просто заранее читал учебник, по которому собирался учить студентов.", "Эвклид оставил после своей жизни множество трудов по математике, которыми мы пользуемся до сих пор. Интересен факт, что сведений о самом Эвклиде не обнаружено.", "Сечение — это изображение фигуры, получающееся при мысленном рассечении предмета секущей плоскостью.", "Факториал числа — это произведение натуральных чисел от 1 до а.", " В мире квантовой физики, частицы могут находиться в состоянии суперпозиции, находясь одновременно в нескольких местах. Этот феномен лежит в основе многих квантовых технологий, включая квантовые компьютеры.", "Абсолютный ноль. Это теоретический предел, при котором все молекулярное движение должно прекратиться. В термодинамике абсолютный ноль равен минус 273.15 градусов Цельсия или ноль градусов по шкале Кельвина.", "Свет может проявлять себя как волна и как частица (фотон). Этот двойственный характер света – одна из ключевых особенностей квантовой механики.", "Физические законы не изменяются со временем. Один из основополагающих принципов физики гласит, что фундаментальные законы физики не изменяются со временем. Это приводит к таким понятиям, как сохранение энергии и момента.", "Скорость света является пределом скорости. В соответствии с теорией относительности Эйнштейна, ничто не может двигаться быстрее света. Это значит, что информация и влияние не могут передаваться быстрее света."]
    await ctx.send(random.choice(lesson_about_math))

bot.run("")
