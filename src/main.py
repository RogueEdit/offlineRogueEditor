# Authors
# Organization: https://github.com/rogueEdit/
# Repository: https://github.com/rogueEdit/OnlineRogueEditor
# Contributors: https://github.com/claudiunderthehood https://github.com/JulianStiebler/
# Date of release: 04.06.2024 


import logging
import getpass
import requests
from modules.rogueClass import Rogue
from colorama import Fore, Style, init

init()

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    session = requests.Session()

    rogue = Rogue()
    
    while True:
        print(Fore.GREEN + "\n<PyRogue Offline>" + Style.RESET_ALL)
    
        func = {
            "1": rogue.starter_edit,
            "2": rogue.unlock_all_starters,
            "3": rogue.add_ticket,
            "4": rogue.edit_pokemon_party,
            "5": rogue.unlock_all_achievements,
            "6": rogue.unlock_all_gamemodes,
            "7": rogue.edit_vouchers,
            "8": rogue.add_candies,
            "9": rogue.edit_money,
            "10": rogue.edit_pokeballs,
            "11": rogue.edit_biome,
            "12": rogue.generate_eggs,
            "13": rogue.edit_hatchWaves,
            "14": rogue.edit_account_stats,
            "15": rogue.unlock_all_features,
            "16": rogue.create_backup,
            "17": rogue.restore_backup,
            "18": rogue.print_pokedex,
            "19": rogue.print_biomes,
            "20": rogue.print_moves,
            "21": rogue.print_vouchers,
            "22": rogue.print_natures,
            "23": rogue.print_natureSlot,
            "24": rogue.print_help,
        }

        title = "************************ PyRogue Offline *************************"
        working_status = "(Working)"

        formatted_title = f"{Fore.GREEN}{Style.BRIGHT}{title}{Style.RESET_ALL}"
        formatted_working_status = f"{Fore.GREEN}{Style.BRIGHT}{working_status}{Style.RESET_ALL}"

        term = [
            f"{formatted_title}",
            f"1: Edit a starter{' ' * 32}{formatted_working_status}",
            f"2: Unlock all starters{' ' * 27}{formatted_working_status}",
            f"3: Edit your egg-tickets{' ' * 25}{formatted_working_status}",
            f"4: Edit CURRENT Pokemon Party{' ' * 20}{formatted_working_status}",
            f"5: Unlock all achievements{' ' * 23}{formatted_working_status}",
            f"6: Unlock all gamemodes{' ' * 26}{formatted_working_status}",
            f"7: Edit vouchers{' ' * 33}{formatted_working_status}",
            f"8: Add candies to a pokemon{' ' * 21}{formatted_working_status}",
            f"9: Edit money amount{' ' * 28}{formatted_working_status}",
            f"10: Edit pokeballs amount{' ' * 24}{formatted_working_status}",
            f"11: Edit biome{' ' * 35}{formatted_working_status}",
            f"12: Generate eggs{' ' * 32}{formatted_working_status}",
            f"13: Set your eggs to hatch{' ' * 23}{formatted_working_status}",
            f"14: Edit account stats{' ' * 27}{formatted_working_status}",
            f"15: Unlock Everything{' ' * 28}{formatted_working_status}",
            Fore.GREEN + Style.BRIGHT + "----------------------------------------------------------" + Style.RESET_ALL,
            f"16: Create a backup{' ' * 30}{formatted_working_status}",
            f"17: Recover your backup{' ' * 26}{formatted_working_status}",
            f"18: Show all Pokemon ID{' ' * 26}{formatted_working_status}",
            f"19: Show all Biome IDs{' ' * 27}{formatted_working_status}",
            f"20: Show all Move IDs{' ' * 28}{formatted_working_status}",
            f"21: Show all Vouchers IDs{' ' * 24}{formatted_working_status}",
            f"22: Show all Natures IDs{' ' * 25}{formatted_working_status}",
            f"23: Show all NaturesSlot IDs{' ' * 21}{formatted_working_status}",
            Fore.LIGHTYELLOW_EX + Style.BRIGHT + "-- You can always edit your json by yourself! --" + Style.RESET_ALL,
            f"24: >> Print help and program information{' ' * 17}",
            f"{formatted_title}",
        ]


        while True:
            print("")
            for line in term:
                print(Fore.GREEN + "* " + Style.RESET_ALL + line + Fore.GREEN + " *" + Style.RESET_ALL)
            command = input("Command: ")

            if command in func:
                func[command]()
            elif command == "exit":
                quit()
            else:
                print("Command not found")