import settings

from vkbottle.bot import Bot, Message


async def getid(pattern):
    pattern = str(pattern)
    if pattern.isdigit(): return pattern
    elif "vk.com/" in pattern:
        uid = (await bot.api.users.get(user_ids=pattern.split("/")[-1]))[0]
        return uid.id
    elif "[id" in pattern:
        uid = pattern.split("|")[0]
        uid = (await bot.api.users.get(user_ids=uid.replace("[id", "")))[0]
        return uid


async def getUser(user_id):
    try: return (await bot.api.users.get(user_ids=user_id))[0]
    except: return None


bot = Bot(settings.TOKEN)


@bot.on.message(text=["/setr", "/setr <domain>", "/setr <domain> <role>"][::-1])
async def set_user_role(event: Message, domain = None, role = None):
    if domain is None or role is None or "@" not in domain or ":/" not in domain or not domain.isdigit():
        return await event.answer(
            message="/setr <<@Пользователь>> <<Назначаемая роль>>",
        )

    if "@" in domain:
        member = await getid(domain)
    else:
        member = await getUser(await getid(domain))

    if member is None:
        return await event.answer(
            message="/setr <<@Пользователь>> <<Назначаемая роль>>",
        )
    
    # Запрос в бд на поисk пользователя
    # res = db

    user = db.request(f"SELECT * FROM `users` WHERE user_id = '{member.id}'", 'fetchone')
    if user is None:
        return await event.answer(
            message="Пользователь незарегестрирован!"
        )
    
    # Запрос в бд на добавление записи и обновление

    db.request(f"UPDATE `users` SET role = '{role}' WHERE vk = '{member.id}'")

    await event.answer(
        message=f"Пользователь [id{member.id}|{member.first_name} {member.last_name}] получил роль <<{role}>>"
    )



bot.run_forever()