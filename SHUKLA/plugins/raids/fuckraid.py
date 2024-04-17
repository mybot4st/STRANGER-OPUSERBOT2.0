from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["fr", "rr", "rraid", "fuckraid"]))
@sudo_users_only
async def add_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 Processing ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Reply to a user's message or give username/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id

        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 How Fool, You Want To Activate Reply Raid On Your Own ID❓**"
            )
        
        fraid = await add_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**😁𝐎𝚈𝙴 𝚂𝚄𝙽 𝚁𝙰𝙽𝙸 𝙱𝙰𝙲𝙲𝙷𝙴😂🤣**"
            )
        return await aux.edit(
            "**😁𝐎𝚈𝙴 𝚂𝚄𝙽 𝚁𝙰𝙽𝙸 𝙱𝙰𝙲𝙲𝙷𝙴😂🤣**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dfr", "drr", "drraid", "dfuckraid"]))
@sudo_users_only
async def del_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 Processing ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Reply to a user's message or give username/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 How Fool, When I Activate Reply Raid On Your ID❓**"
            )
        
        fraid = await del_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**👻 𝙹𝙰𝙰 𝚂𝙰𝙹𝙽𝙰 𝚃𝚄𝙹𝙷𝙴 𝙲𝙷𝙾𝙳 𝙺𝙴 𝙳𝙵𝙽 𝙺𝚁 𝙳𝙸𝚈𝙰😻 #𝙵𝙴𝙴𝙻_4𝚂𝚃 😹.**"
            )
        return await aux.edit(
            "**👻 𝙹𝙰𝙰 𝚂𝙰𝙹𝙽𝙰 𝚃𝚄𝙹𝙷𝙴 𝙲𝙷𝙾𝙳 𝙺𝙴 𝙳𝙵𝙽 𝙺𝚁 𝙳𝙸𝚈𝙰😻 #𝙵𝙴𝙴𝙻_4𝚂𝚃 😹**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
