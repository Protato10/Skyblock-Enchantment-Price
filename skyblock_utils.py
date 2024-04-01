# Imports
import requests
import json


# # # Functions
#TEst to see if github works
# Returns GET request response from url
def get_info(call):
    r = requests.get(call)
    return r.json()


# Returns auction info from player uuid
#def get_auctions_from_player(uuid):
  #  return get_info(f"https://api.hypixel.net/skyblock/auction?key={API_KEY}&player={uuid}")


# Returns Bazaar data
def get_bazaar_data():
    return get_info("https://api.hypixel.net/skyblock/bazaar")


# Returns recently finished auctions data
def get_recently_ended_auctions():
    return get_info("https://api.hypixel.net/skyblock/auctions_ended")


# Returns a list of all active auctions
def get_auction_data():
    all_auctions = []

    first_page = get_info("https://api.hypixel.net/skyblock/auctions?page=0")

    auction_data = first_page.get("auctions", [])

    for page in range(1, first_page.get("totalPages", 0) + 1):
        current_page = get_info(f"https://api.hypixel.net/skyblock/auctions?page={page}")
        all_auctions += current_page.get("auctions", [])

    return all_auctions


# gets price of a specific item on bazaar

# Returns total coin count in buy orders on the bazaar
def get_bazaar_price(item_name):
    sum_coins = 0
    price_increase_threshold = 2
    buy_order_values = []
    item_sum_coins = 0

    # For every product
    for itemName, item_data in get_bazaar_data().get("products", {}).items():
        # print(itemName)

        if itemName == item_name:

            # For every buy offer
            for idx, buy_order in enumerate(item_data.get("buy_summary", [])):
                if (idx == 0):
                    item_sum_coins = buy_order.get("pricePerUnit")
                # if(buy_order.get("buyPrice")>item_sum_coins):
                # item_sum_coins = buy_order.get("pricePerUnit", 0)

    return item_sum_coins


dictOfEnchantments = {'Bank 5': 'ENCHANTMENT_ULTIMATE_BANK_5',
                      'Combo 5': 'ENCHANTMENT_ULTIMATE_COMBO_5',
                      'Swarm 1': 'ENCHANTMENT_ULTIMATE_SWARM_1',
                      'Swarm 2': 'ENCHANTMENT_ULTIMATE_SWARM_2',
                      'Swarm 3': 'ENCHANTMENT_ULTIMATE_SWARM_3',
                      'Swarm 4': 'ENCHANTMENT_ULTIMATE_SWARM_4',
                      'Swarm 5': 'ENCHANTMENT_ULTIMATE_SWARM_5',
                      'Chimera 1': 'ENCHANTMENT_ULTIMATE_CHIMERA_1',
                      'Chimera 2': 'ENCHANTMENT_ULTIMATE_CHIMERA_1',
                      'Chimera 3': 'ENCHANTMENT_ULTIMATE_CHIMERA_1',
                      'Chimera 4': 'ENCHANTMENT_ULTIMATE_CHIMERA_1',
                      'Chimera 5': 'ENCHANTMENT_ULTIMATE_CHIMERA_1',
                      'Inferno 1': 'ENCHANTMENT_ULTIMATE_INFERNO_1',
                      'Inferno 2': 'ENCHANTMENT_ULTIMATE_INFERNO_1',
                      'Inferno 3': 'ENCHANTMENT_ULTIMATE_INFERNO_1',
                      'Inferno 4': 'ENCHANTMENT_ULTIMATE_INFERNO_1',
                      'Inferno 5': 'ENCHANTMENT_ULTIMATE_INFERNO_1',
                      'Duplex 1:': 'ENCHANTMENT_ULTIMATE_REITERATE_1',
                      'Duplex 2:': 'ENCHANTMENT_ULTIMATE_REITERATE_2',
                      'Duplex 3:': 'ENCHANTMENT_ULTIMATE_REITERATE_3',
                      'Duplex 4:': 'ENCHANTMENT_ULTIMATE_REITERATE_4',
                      'Duplex 5:': 'ENCHANTMENT_ULTIMATE_REITERATE_5',
                      'Rend 1': 'ENCHANTMENT_ULTIMATE_REND_1',
                      'Rend 2': 'ENCHANTMENT_ULTIMATE_REND_2',
                      'Rend 3': 'ENCHANTMENT_ULTIMATE_REND_3',
                      'Rend 4': 'ENCHANTMENT_ULTIMATE_REND_4',
                      'Rend 5': 'ENCHANTMENT_ULTIMATE_REND_5',
                      "Bobbin' Time 1": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_1',
                      "Bobbin' Time 2": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_2',
                      "Bobbin' Time 3": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_3',
                      "Bobbin' Time 4": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_4',
                      "Bobbin' Time 5": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_5',
                      "Bobbin Time 1": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_1',
                      "Bobbin Time 2": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_2',
                      "Bobbin Time 3": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_3',
                      "Bobbin Time 4": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_4',
                      "Bobbin Time 5": 'ENCHANTMENT_ULTIMATE_BOBBIN_TIME_5',
                      'Flash 1': 'ENCHANTMENT_ULTIMATE_FLAST_1',
                      'Flash 2': 'ENCHANTMENT_ULTIMATE_FLAST_2',
                      'Flash 3': 'ENCHANTMENT_ULTIMATE_FLAST_3',
                      'Flash 4': 'ENCHANTMENT_ULTIMATE_FLAST_4',
                      'Flash 5': 'ENCHANTMENT_ULTIMATE_FLAST_5',
                      'Legion 1': 'ENCHANTMENT_ULTIMATE_LEGION_1',
                      'Legion 2': 'ENCHANTMENT_ULTIMATE_LEGION_2',
                      'Legion 3': 'ENCHANTMENT_ULTIMATE_LEGION_3',
                      'Legion 4': 'ENCHANTMENT_ULTIMATE_LEGION_4',
                      'Legion 5': 'ENCHANTMENT_ULTIMATE_LEGION_5',
                      'One For All': 'ENCHANTMENT_ULTIMATE_ONE_FOR_ALL_1',
                      'Fatal Tempo 1': 'ENCHANTMENT_ULTIMATE_FATAL_TEMPO_1',
                      'Fatal Tempo 2': 'ENCHANTMENT_ULTIMATE_FATAL_TEMPO_1',
                      'Fatal Tempo 3': 'ENCHANTMENT_ULTIMATE_FATAL_TEMPO_1',
                      'Fatal Tempo 4': 'ENCHANTMENT_ULTIMATE_FATAL_TEMPO_1',
                      'Fatal Tempo 5': 'ENCHANTMENT_ULTIMATE_FATAL_TEMPO_1',
                      'Habanero Tactics 4': 'ENCHANTMENT_ULTIMATE_HABANERO_TACTICS_4',
                      'Habanero Tactics 5': 'ENCHANTMENT_ULTIMATE_HABANERO_TACTICS_5',
                      'Last Stand 5': 'ENCHANTMENT_ULTIMATE_LAST_STAND_5',
                      'Soul Eater 5': 'ENCHANTMENT_ULTIMATE_SOUL_EATER_5',
                      'Dragon Hunter 1': 'ENCHANTMENT_DRAGON_HUNTER+1',
                      'Dragon Hunter 2': 'ENCHANTMENT_DRAGON_HUNTER+2',
                      'Dragon Hunter 3': 'ENCHANTMENT_DRAGON_HUNTER+3',
                      'Dragon Hunter 4': 'ENCHANTMENT_DRAGON_HUNTER+4',
                      'Dragon Hunter 5': 'ENCHANTMENT_DRAGON_HUNTER+5',
                      'Ultimate Wise 5': 'ENCHANTMENT_ULTIMATE_ULTIMATE_WISE_5',
                      'Wisdom 5': 'ENCHANTMENT_ULTIMATE_WISDOM_5', 'Execute 6': 'ENCHANTMENT_EXECUTE_6',
                      'Champion 1': 'ENCHANTMENT_COMPACT_1', 'Hecatomb 1': 'ENCHANTMENT_HECATOMB_1',
                      'Angler 6': 'ENCHANTMENT_ANGLER_6', 'Bane Of Arthropods 7': 'ENCHANTMENT_BANE_OF_ARTHROPODS_7',
                      'Blast Protection 7': 'ENCHANTMENT_BLAST_PROTECTION_7', 'Caster 6': 'ENCHANTMENT_CASTER_6',
                      'Charm 6': 'ENCHANTMENT_CHARM_5', 'Counter-Strike 5': 'ENCHANTMENT_COUNTER_STRIKE_5',
                      'Critical 7': 'ENCHANTMENT_CRITICAL_7', "Chance 5": 'ENCHANTMENT_CHANCE_5',
                      'Cleave 6': 'ENCHANTMENT_CLEAVE_6', 'Divine Gift 1': 'ENCHANTMENT_DIVINE_GIFT_1',
                      'Divine Gift 2': 'ENCHANTMENT_DIVINE_GIFT_2', 'Divine Gift 3': 'ENCHANTMENT_DIVINE_GIFT_3',
                      'Power 7': 'ENCHANTMENT_POWER_7', 'Cubism 6': 'ENCHANTMENT_CUBISM_6',
                      'Ender Slayer 7': 'ENCHANTMENT_ENDER_SLAYER_7', 'Experience 5': 'ENCHANTMENT_EXPERIENCE_5',
                      'Feather Falling 10': 'ENCHANTMENT_FEATHER_FALLING_10', 'Big Brain 3': 'ENCHANTMENT_BIG_BRAIN_3',
                      'Big Brain 2': 'ENCHANTMENT_BIG_BRAIN_2', 'Big Brain 1': 'ENCHANTMENT_BIG_BRAIN_1',
                      'Fire Aspect 3': 'ENCHANTMENT_FIRE_ASPECT_3', 'First Strike 5': 'ENCHANTMENT_FIRST_STRIKE_5',
                      'Fortune 4': 'ENCHANTMENT_FORTUNE_4', 'Rejuvenate 5': 'ENCHANTMENT_REJUVENATE_5',
                      'Smoldering 5': 'ENCHANTMENT_SMOLDERING_5', 'Smoldering 4': 'ENCHANTMENT_SMOLDERING_4',
                      'Smoldering 3': 'ENCHANTMENT_SMOLDERING_3', 'Smoldering 2': 'ENCHANTMENT_SMOLDERING_2',
                      'Smoldering 1': 'ENCHANTMENT_SMOLDERING_1', 'Thunderlord 7': 'ENCHANTMENT_THUNDERLORD_7',
                      'Ferocious Mana 10': 'ENCHANTMENT_Ferocious_MANA_10',
                      'Ferocious Mana 9': 'ENCHANTMENT_Ferocious_MANA_9',
                      'Ferocious Mana 8': 'ENCHANTMENT_Ferocious_MANA_8',
                      'Ferocious Mana 7': 'ENCHANTMENT_Ferocious_MANA_7',
                      'Ferocious Mana 6': 'ENCHANTMENT_Ferocious_MANA_6',
                      'Ferocious Mana 5': 'ENCHANTMENT_Ferocious_MANA_5',
                      'Ferocious Mana 4': 'ENCHANTMENT_Ferocious_MANA_4',
                      'Ferocious Mana 3': 'ENCHANTMENT_Ferocious_MANA_3',
                      'Ferocious Mana 2': 'ENCHANTMENT_Ferocious_MANA_2',
                      'Ferocious Mana 1': 'ENCHANTMENT_Ferocious_MANA_1',
                      'Hardened Mana 10': 'ENCHANTMENT_HARDENED_MANA_10',
                      'Hardened Mana 9': 'ENCHANTMENT_HARDENED_MANA_9',
                      'Hardened Mana 8': 'ENCHANTMENT_HARDENED_MANA_8',
                      'Hardened Mana 7': 'ENCHANTMENT_HARDENED_MANA_7',
                      'Hardened Mana 6': 'ENCHANTMENT_HARDENED_MANA_6',
                      'Hardened Mana 5': 'ENCHANTMENT_HARDENED_MANA_5',
                      'Hardened Mana 4': 'ENCHANTMENT_HARDENED_MANA_4',
                      'Hardened Mana 3': 'ENCHANTMENT_HARDENED_MANA_3',
                      'Hardened Mana 2': 'ENCHANTMENT_HARDENED_MANA_2',
                      'Hardened Mana 1': 'ENCHANTMENT_HARDENED_MANA_1',
                      'Infinite Quiver 10': 'ENCHANTMENT_INFINITE_QUIVER_10', 'Lethality 6': 'ENCHANTMENT_LETHALITY 6',
                      'Life Steal 5': 'ENCHANTMENT_LIFE_STEAL_5', 'Luck 7': 'ENCHANTMENT_LUCK_7',
                      'Giant Killer 6':'ENCHANTMENT_GIANT_KILLER_6','Giant Killer 7':'ENCHANTMENT_GIANT_KILLER_7',
                      'Looting 5': 'ENCHANTMENT_LOOTING_5', 'Luck Of The Sea 5': 'ENCHANTMENT_LUCK_OF_THE_SEA_5',
                      'Magnet 6': 'ENCHANTMENT_MAGNET_6', 'Mana Vampire 10': 'ENCHANTMENT_MANA_VAMPIRE_10',
                      'Mana Vampire 9': 'ENCHANTMENT_MANA_VAMPIRE_9', 'Mana Vampire 8': 'ENCHANTMENT_MANA_VAMPIRE_8',
                      'Mana Vampire 7': 'ENCHANTMENT_MANA_VAMPIRE_7', 'Mana Vampire 6': 'ENCHANTMENT_MANA_VAMPIRE_6',
                      'Mana Vampire 5': 'ENCHANTMENT_MANA_VAMPIRE_5', 'Mana Vampire 4': 'ENCHANTMENT_MANA_VAMPIRE_4',
                      'Mana Vampire 3': 'ENCHANTMENT_MANA_VAMPIRE_3', 'Mana Vampire 2': 'ENCHANTMENT_MANA_VAMPIRE_2',
                      'Mana Vampire 1': 'ENCHANTMENT_MANA_VAMPIRE_1', 'Piscary 6': 'ENCHANTMENT_PISCARY_6',
                      'Overload 1': 'ENCHANTMENT_OVERLOAD_1', 'Overload 2': 'ENCHANTMENT_OVERLOAD_2',
                      'Overload 3': 'ENCHANTMENT_OVERLOAD_3', 'Overload 4': 'ENCHANTMENT_OVERLOAD_4',
                      'Overload 5': 'ENCHANTMENT_OVERLOAD_5', 'Prosperity 1': 'ENCHANTMENT_PROSPERITY_1',
                      'Prosperity 2': 'ENCHANTMENT_PROSPERITY_2', 'Prosperity 3': 'ENCHANTMENT_PROSPERITY_3',
                      'Prosperity 4': 'ENCHANTMENT_PROSPERITY_4', 'Prosperity 5': 'ENCHANTMENT_PROSPERITY_5',
                      'Pristine 5': 'ENCHANTMENT_PRISTINE_5', 'Protection 6': 'ENCHANTMENT_PROTECTION_6',
                      'Protection_7': 'ENCHANTMENT_PROTECTION_7', 'Replenish 1': 'ENCHANTMENT_REPLENISH_1',
                      'Prosecute 6': 'ENCHANTMENT_PROSECUTE_6', 'Mana Steal 3': 'ENCHANTMENT_MANA_STEAL_3',
                      'Mana Steal 2': 'ENCHANTMENT_MANA_STEAL_2', 'Mana Steal 1': 'ENCHANTMENT_MANA_STEAL_1',
                      'Respite 5': 'ENCHANTMENT_RESPITE_5', 'Sharpness 7': 'ENCHANTMENT_SHARPNESS_7',
                      'Smarty Pants 5': 'ENCHANTMENT_SMARTY_PANTS_5', 'Smarty Pants 4': 'ENCHANTMENT_SMARTY_PANTS_4',
                      'Smarty Pants 3': 'ENCHANTMENT_SMARTY_PANTS_3', 'Smarty Pants 2': 'ENCHANTMENT_SMARTY_PANTS_2',
                      'Smarty Pants 1': 'ENCHANTMENT_SMARTY_PANTS_1', 'Smite 7': 'ENCHANTMENT_SMITE_7',
                      'Snipe 4': 'ENCHANTMENT_SNIPE_4', 'Strong Mana 10': 'ENCHANTMENT_STRONG_MANA_10',
                      'Strong Mana 9': 'ENCHANTMENT_STRONG_MANA_9', 'Strong Mana 8': 'ENCHANTMENT_STRONG_MANA_8',
                      'Strong Mana 7': 'ENCHANTMENT_STRONG_MANA_7', 'Strong Mana 6': 'ENCHANTMENT_STRONG_MANA_6',
                      'Strong Mana 5': 'ENCHANTMENT_STRONG_MANA_5', 'Strong Mana 4': 'ENCHANTMENT_STRONG_MANA_4',
                      'Strong Mana 3': 'ENCHANTMENT_STRONG_MANA_3', 'Strong Mana 2': 'ENCHANTMENT_STRONG_MANA_2',
                      'Strong Mana 1': 'ENCHANTMENT_STRONG_MANA_1', 'Tabasco 2': 'ENCHANTMENT_TABASCO_2',
                      'Syphon 5': 'ENCHANTMENT_SYPHON_5', 'Scavenger 5': 'ENCHANTMENT_SCAVENGER_5',
                      'Tabasco 3': 'ENCHANTMENT_TABASCO_3', 'Thunderbolt 6': 'ENCHANTMENT_THUNDERBOLT_6',
                      'Titan Killer 7': 'ENCHANTMENT_TITAN_KILLER_7', 'Triple Strike 5': 'ENCHANTMENT_TRIPLE_STRIKE_5',
                      'Turbo-Cacti 5': 'ENCHANTMENT_TURBO_CACTI_5', 'Turbo-Potato 5': 'ENCHANTMENT_TURBO_POTATO_5',
                      'Turbo-Melon 5': 'ENCHANTMENT_TURBO_MELON_5', 'Turbo-Carrot 5': 'ENCHANTMENT_TURBO_CARROT_5',
                      'Turbo-Wart 5': 'ENCHANTMENT_TURBO_WART_5', 'Turbo Cacti 5': 'ENCHANTMENT_TURBO_CACTI_5',
                      'Turbo Potato 5': 'ENCHANTMENT_TURBO_POTATO_5', 'Turbo Melon 5': 'ENCHANTMENT_TURBO_MELON_5',
                      'Turbo Carrot 5': 'ENCHANTMENT_TURBO_CARROT_5', 'Turbo Wart 5': 'ENCHANTMENT_TURBO_WART_5',
                      'Venomous 6': 'ENCHANTMENT_VENOMOUS_6', 'Compact 1': 'ENCHANTMENT_COMPACT_1',
                      'Vicious 3': 'ENCHANTMENT_VICIOUS_3', 'Vicious 4': 'ENCHANTMENT_VICIOUS_4',
                      'Vicious 5': 'ENCHANTMENT_VICIOUS_5', 'Dedication 4': 'ENCHANTMENT_DEDICATION_4',
                      'Green Thumb 1': 'ENCHANTMENT_GREEN_THUMB_1', 'Green Thumb 2': 'ENCHANTMENT_GREEN_THUMB_2',
                      'Green Thumb 3': 'ENCHANTMENT_GREEN_THUMB_3', 'Green Thumb 4': 'ENCHANTMENT_GREEN_THUMB_4',
                      'Green Thumb 5': 'ENCHANTMENT_GREEN_THUMB_5', 'Pesterminator 1': 'ENCHANTMENT_PESTERMINATOR_1',
                      'Growth 6': 'ENCHANTMENT_GROWTH_6', 'Growth 7': 'ENCHANTMENT_GROWTH_7',
                      'Pesterminator 2': 'ENCHANTMENT_PESTERMINATOR_2',
                      'Pesterminator 3': 'ENCHANTMENT_PESTERMINATOR_3',
                      'Pesterminator 4': 'ENCHANTMENT_PESTERMINATOR_4',
                      'Pesterminator 5': 'ENCHANTMENT_PESTERMINATOR_5',
                      'Quantum 3': 'ENCHANTMENT_QUANTUM_3', 'Cayenne 4': 'ENCHANTMENT_CAYENNE_4',
                      'Cayenne 5': 'ENCHANTMENT_CAYENNE_5',
                      'Quantum 4': 'ENCHANTMENT_QUANTUM_4', 'Quantum 5': 'ENCHANTMENT_QUANTUM_5',
                      'Reflection 1': 'ENCHANTMENT_REFLECTION_1', 'Reflection 2': 'ENCHANTMENT_REFLECTION_2',
                      'Reflection 3': 'ENCHANTMENT_REFLECTION_3', 'Reflection 4': 'ENCHANTMENT_REFLECTION_4',
                      'Reflection 5': 'ENCHANTMENT_REFLECTION_5', 'Refrigerate 1': 'ENCHANTMENT_ULTIMATE_REFRIGERATE_1',
                      'Refrigerate 2': 'ENCHANTMENT_ULTIMATE_REFRIGERATE_2',
                      'Refrigerate 3': 'ENCHANTMENT_ULTIMATE_REFRIGERATE_3',
                      'Refrigerate 4': 'ENCHANTMENT_ULTIMATE_REFRIGERATE_4',
                      'Refrigerate 5': 'ENCHANTMENT_ULTIMATE_REFRIGERATE_5', 'Sunder 6': 'ENCHANTMENT_SUNDER_6',
                      'The One 4': 'ENCHANTMENT_ULTIMATE_THE_ONE_4', 'The One 5': 'ENCHANTMENT_ULTIMATE_THE_ONE_5'}


def missing_enchantments():
    value = input("Please enter the names of the enchantment you need in a comma seperated list, capitulation and "
                  "spelling matter. (Most enchantments only have their max\n")
    lst = list(value.split(","))
    sum_of_coins = 0
    for i in range(len(lst)):
        lst[i] = lst[i].strip(" ")
        if lst[i] not in dictOfEnchantments:
            print(
                "Unable to find " + lst[i] + '. Please make sure the spelling is EXACTLY the same (use numbers not '
                                             'roman numerals and have correct spacing')
        if lst[i] in dictOfEnchantments:
            if lst[i] == "Chimera 5" or lst[i] == "Fatal Tempo 5" or lst[i]=="Bobbin' Time 5"or lst[i]=="Bobbin Time 5":
                total = get_bazaar_price(dictOfEnchantments[lst[i]]) * 2
                sum_of_coins += total
                print(lst[i] + ": " + str(total))
            elif lst[i] == "Chimera 5" or lst[i] == "Fatal Tempo 5" or lst[i]=="Bobbin' Time 5"or lst[i]=="Bobbin Time 5":
                total = get_bazaar_price(dictOfEnchantments[lst[i]]) * 4
                sum_of_coins += total
                print(lst[i] + ": " + str(total))
            elif lst[i] == "Chimera 5" or lst[i] == "Fatal Tempo 5" or lst[i]=="Bobbin' Time 5"or lst[i]=="Bobbin Time 5":
                total = get_bazaar_price(dictOfEnchantments[lst[i]]) * 8
                sum_of_coins += total
                print(lst[i] + ": " + str(total))
            elif lst[i] == "Chimera 5" or lst[i] == "Fatal Tempo 5" or lst[i]=="Bobbin' Time 5"or lst[i]=="Bobbin Time 5":
                total = get_bazaar_price(dictOfEnchantments[lst[i]])*16
                sum_of_coins += total
                print(lst[i] + ": " + str(total))
            else:
                total = get_bazaar_price((dictOfEnchantments[lst[i]]))
                print(lst[i] + ": " + str(total))
                sum_of_coins += get_bazaar_price(dictOfEnchantments[lst[i]])


    print("Total cost for all enchantments are " + str(round((sum_of_coins / 1000000), 5)) + " million coins")
    return


# Sorts and displays a list of buy order items by total value
def sort_bazaar_buy_orders_by_value(buy_order_values):
    # Sort items by values
    buy_order_values.sort(key=lambda x: -x[1])

    # Display items and values
    for (item_name, item_sum_coins) in buy_order_values:
        print(f"{item_name.ljust(30, ' ')} | {round(item_sum_coins):,}")

    return


# Returns total coin count in recently ended auctions
def get_ended_auctions_value(ended_auctions_data):
    sum_coins = 0

    # For every auction object
    for auction_obj in ended_auctions_data.get("auctions", {}):
        # Add the sale price to the sum
        sum_coins += auction_obj.get("price", 0)

    return sum_coins


# Returns auction items after passing them through the filter
def filter_auction_items(auction_data, item_filters):
    filtered_items = []

    # For every auction object
    for auction in auction_data:

        # For every individual filter
        for item_filter in item_filters:

            # For every filter argument
            for filter_property, filter_value in item_filter.items():

                # String filters (item_name)
                if (type(filter_value) == type("")):
                    if (filter_value not in auction.get(filter_property, "")):
                        break

                # Boolean filters (bin)
                elif (type(filter_value) == type(True)):
                    if (filter_value != auction.get(filter_property, False)):
                        break

                # If all subfilters have passed
                filtered_items.append(auction)

    # filtered_items = sorted(filtered_items, key=lambda x: x['price'])

    return filtered_items


# Displays top x items from y list of auction objects
def display_top_auction_items(filtered_items, amount):
    for i in range(min(amount, len(filtered_items))):
        print(
            f"\n#{i + 1} {filtered_items[i]['item_name']}\n - {filtered_items[i]['starting_bid']:,}\n- /viewauction {filtered_items[i]['uuid']}")


# Variables
# API_FILE = open("API_KEY.json", "r")
# API_KEY = json.loads(API_FILE.read())["API_KEY"]
# example_player_uuid = "6a61acfe47c04f038ca6be4ae358e259"
# item_filters = (
# {"item_name": "Drill", "bin": True},
# )

# Code
# print(f"Bazaar Buy Order Eco: {get_bazaar_buy_order_value(get_bazaar_data()):,}")

# print(f"Finished Auctions (60s) Eco: {get_ended_auctions_value(get_recently_ended_auctions()):,}")

# auction_data = get_auction_data()

# print(f"Amount of auction items: {len(auction_data):,}")

# filtered_items = filter_auction_items(auction_data, item_filters)

# print(f"Filtered auction items: {len(filtered_items):,}")

# display_top_auction_items(filtered_items, 3)

missing_enchantments()
