from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["lr", "lraid", "loveraid"]))
@sudo_users_only
async def add_love_raid(client, message):
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
                "**🤣 How Fool, You Want To Activate Love Raid On Your Own ID❓**"
            )
        
        lraid = await add_loveraid_user(user_id)
        if lraid:
            return await aux.edit(
                "** 👀 𝙾𝚈𝙴 𝚂𝚄𝙽 🤧💗 .**"
            )
        return await aux.edit(
            "**🤖 Hey, Love Raid Already Active On This User❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dlr", "dlraid", "dloveraid"]))
@sudo_users_only
async def del_love_raid(client, message):
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
                "**🤣 How Fool, When I Activate Love Raid On Your ID❓**"
            )
        
        lraid = await del_loveraid_user(user_id)
        if lraid:
            return await aux.edit(
                "**👀 𝙳𝙼 𝙺𝙰𝚁𝙾𝙶𝙴 𝚈𝙰 𝙸 𝙻𝙾𝚅𝙴 𝚄𝙷 𝙱𝙾𝙻𝙾𝙶𝙴..?💕.**"
            )
        return await aux.edit(
            "**🤖 Hey, Love Raid Not Active On This User❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
