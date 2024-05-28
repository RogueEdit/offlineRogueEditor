import json

import getpass

from modules.rogueClass import Rogue

if __name__ == '__main__':

    with open("./data/data.json") as f:
         data = json.loads(f.read())

    print(data["startup_message"])

    rogue = Rogue()

    func = {
        "1": rogue.unlock_all_starters,
        "2": rogue.starter_edit,
        "3": rogue.pokedex,
        "4": rogue.moves,
        "5": rogue.biomes,
        "6": rogue.hatch_all_eggs,
        "7": rogue.edit_pokemon_party,
        "8": rogue.ticket,
        "9": rogue.unlock_all_achievements,
        "10": rogue.unlock_all_gamemodes,
        "11": rogue.unlock_all_vouchers
    }

    term = [
        "**************************** COMMANDS ****************************",
        "1: Unlock all starters",
        "2: Edit a starter",
        "3: Show all pokemon IDs",
        "4: Show all moves IDs",
        "5: Show all biomes IDs",
        "6: Hatch all eggs",
        "7: Edit pokemon party",
        "8: Edit tickets",
        "9: Unlock all achievements",
        "10: Unlock all gamemodes",
        "11: Unlock all vouchers",
        "--------------------------------------------------------------------"
    ]

    while True:
        print("\n".join(term))
        command = input("Command: ")

        if command in func:
            func[command]()
        elif command == "exit":
            quit()
        else:
            print("Command not found")