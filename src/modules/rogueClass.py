import json, requests, random, os, time

class Rogue:
    def __init__(self) -> None:
        with open("./data/pokemon.json") as f:
            self.pokemon_id_by_name = json.loads(f.read())
        
        with open("./data/biomes.json") as f:
            self.biomes_by_id = json.loads(f.read())

        with open("./data/moves.json") as f:
            self.moves_by_id = json.loads(f.read())
        
        with open("./data/data.json") as f:
            self.extra_data = json.loads(f.read())
    
    def load_data(self, mode):

        check = self.check_or_rename_json_file(mode)

        if check:
            pass
        else:
            return
        
        if mode == 0:
            with open("data_Guest.json") as f:
                data = json.loads(f.read())
        else:
            with open("sessionData_Guest.json") as f:
                data = json.loads(f.read())
        
        return data
    
    def write_data(self, data, mode):

        if mode == 0:
            with open("data_Guest.json", "w") as f:
                json.dump(data, f, indent=2)
        else:
            with open("sessionData_Guest.json", "w") as f:
                json.dump(data, f, indent=2)
    

    def check_or_rename_json_file(self, mode):
        current_dir = os.getcwd()  # Get the current directory
        json_files = [file for file in os.listdir(current_dir) if file.startswith('data_') and file.endswith('.json')]
        json_files1 = [file for file in os.listdir(current_dir) if file.startswith('sessionData_') and file.endswith('.json')] 

        if mode == 0:
            if not json_files:  # Check if json_files is empty
                print("No JSON files found.")
                return False
            if 'data_Guest.json' in json_files:  # Check if "data_Guest.json" already exists
                # This recursively gets called whenever we just enter a command aswell. We might just want to opt out rather than always printing?
                # If the file exists everything is okay anyway and doesn't need a response i think
                # print("The file 'data_Guest.json' already exists.")
                return True
            else:
                for file in json_files:
                    if file != 'data_Guest.json':  # If a JSON file exists but isn't named "data_Guest.json"
                        try:
                            os.rename(file, 'data_Guest.json')  # Rename the file to "data_Guest.json"
                            print(f"File '{file}' renamed to 'data_Guest.json'")
                            return True  # Exit loop after renaming the first file found
                        except OSError as e:
                            print(f"Error: {e}")
                            return False
                else:
                    print("No JSON file found to rename.")
                    return False
        else:
            if not json_files1:  # Check if json_files1 is empty
                print("No JSON files found.")
                return False
            if 'sessionData_Guest.json' in json_files1:  # Check if "sessionData_Guest.json" already exists
                print("The file 'sessionData_Guest.json' already exists.")
                return True
            else:
                for file in json_files1:
                    if file != 'sessionData_Guest.json':  # If a JSON file exists but isn't named "sessionData_Guest.json"
                        try:
                            os.rename(file, 'sessionData_Guest.json')  # Rename the file to "sessionData_Guest.json"
                            print(f"File '{file}' renamed to 'sessionData_Guest.json'")
                            return True  # Exit loop after renaming the first file found
                        except OSError as e:
                            print(f"Error: {e}")
                            return False
                else:
                    print("No JSON file found to rename.")
                    return False





    def unlock_all_starters(self):

        data = self.load_data(0)

        if not data:
            return None
        total_caught = 0
        total_seen = 0
        for entry in data["dexData"].keys():
            caught = random.randint(150, 250)
            seen = random.randint(150, 350)
            total_caught += caught
            total_seen += seen
            data["dexData"][entry] = {
                "$sa": 479,
                "$ca": 255,
                "$na": 67108862,
                "$s": seen,
                "$c": caught,
                "$hc": 0,
                "$i": [31, 31, 31, 31, 31, 31]
            }
            data["starterData"][entry] = {
                "$m": None,
                "$em": 15,
                "$x": caught + 20,
                "$a": 7,
                "$pa": 0,
                "$vr": 0
            }
            data["gameStats"]["battles"] = total_caught + random.randint(1, total_caught)
            data["gameStats"]["pokemonCaught"] = total_caught
            data["gameStats"]["pokemonSeen"] = total_seen
            data["gameStats"]["shinyPokemonCaught"] = len(data["dexData"]) * 2

            self.write_data(data, 0)


    def pokedex(self):
        dex = [f"{value}: {key}" for key, value in self.pokemon_id_by_name['dex'].items()]
        print("\n".join(dex))

        
    def starter_edit(self, dexId=None):
        data = self.load_data(0)
        if not data:
            return None
        if not dexId:
            dexId = input("Enter Pokemon (Name / ID): ")
            if dexId.isnumeric():
                if dexId not in data["starterData"]:
                    print(f"No Pokemon with ID: {dexId}")
                    return
            else:
                dexId = self.pokemon_id_by_name["dex"].get(dexId.lower())
                if not dexId:
                    print(f"No Pokemon with ID: {dexId}")
                    return
        is_shiny = int(input("Make the Pokemon shiny? (1: Yes, 2: No): "))
        caught_attr = 255 if is_shiny == 1 else 253
        nature_attr = 67108862
        caught = int(input("How many of this Pokemon have you caught?: "))
        hatched = int(input("How many of this Pokemon have hatched from eggs?: "))
        seen_count = int(input("How many of this Pokemon have you seen?: "))
        ivs = [int(input("SpA IVs: ")), int(input("DEF IVs: ")), int(input("Attack IVs: ")),
               int(input("HP IVs: ")), int(input("Spe IVs: ")), int(input("Def IVs: "))]
        data["dexData"][dexId] = {
            "$sa": 479,
            "$ca": caught_attr,
            "$na": nature_attr,
            "$s": seen_count,
            "$c": caught,
            "$hc": hatched,
            "$i": ivs
        }
        data["starterData"][dexId] = {
            "$m": None,
            "$em": 15,
            "$x": caught + (hatched * 2),
            "$a": 7,
            "$pa": 0,
            "$vr": 0
        }
        
        self.write_data(data, 0)
    
    def ticket(self):
        data = self.load_data(0)
        if not data:
            return None
        voucher_counts = {
            "0": int(input("How many common vouchers do you want?: ")),
            "1": int(input("How many rare vouchers do you want?: ")),
            "2": int(input("How many epic vouchers do you want?: ")),
            "3": int(input("How many legendary vouchers do you want?: "))
        }
        data["voucherCounts"] = voucher_counts
        
        self.write_data(data, 0)

    def hatch_all_eggs(self):
        data = self.load_data(0)
        if not data:
            return None
        eggs = data.get("eggs", [])
        if not eggs:
            print("No eggs to hatch")
            return
        for egg in eggs:
            egg["hatchWaves"] = 0
        data["eggs"] = eggs
        self.write_data(data, 0)


    def edit_pokemon_party(self):
        data = self.load_data(1)
        
        if data is None:
            return
        
        options = [
            "1: Change species",
            "2: Set it shiny",
            "3: Set Level",
            "4: Set Luck",
            "5: Set IVs",
            "6: Change a move on a pokemon in your team"
        ]
        
        party_num = int(input("Select the party slot of the Pokémon you want to edit (0-4): "))
        if party_num < 0 or party_num > 5:
            print("Invalid party slot")
            return
        
        print("**************************** OPTIONS ****************************")
        print("\n".join(options))
        print("--------------------------------------------------------------------")
        
        command = int(input("Option: "))
        if command < 1 or command > 6:
            print("Invalid option")
            return
        
        if command == 1:
            poke_id = int(input("Choose the pokemon you'd like by ID: "))
            data["party"][party_num]["species"] = poke_id
        elif command == 2:
            data["party"][party_num]["shiny"] = True
            variant = int(input("Choose the shiny variant (from 0 to 2): "))
            if variant < 0 or variant > 2:
                print("Invalid shiny variant")
                return
            data["party"][party_num]["variant"] = variant
        elif command == 3:
            level = int(input("Choose the level: "))
            if level < 1:
                print("Invalid level")
                return
            data["party"][party_num]["level"] = level
        elif command == 4:
            luck = int(input("What luck level do you desire? (from 1 to 14): "))
            if luck < 1 or luck > 14:
                print("Invalid luck")
                return
            data["party"][party_num]["luck"] = luck
        elif command == 5:
            data["party"][party_num]["ivs"] = [31, 31, 31, 31, 31, 31]
        elif command == 6:
            move_slot = int(input("Select the move you want to change (from 0 to 3): "))
            if move_slot < 0 or move_slot > 3:
                print("Invalid move slot")
                return
            move = int(input("What move do you want (ID)? "))
            if move < 0 or move > 919:
                print("Invalid move")
                return
            data["party"][party_num]["moveset"][move_slot]["moveId"] = move

        self.write_data(data, 1)
    
    def unlock_all_gamemodes(self):
        try:
            data = self.load_data(0)
            unlocked_modes = data.get("unlocks", {})
            if not unlocked_modes:
                print("Unable to find data entry: unlocks")
                return

            for mode in unlocked_modes:
                unlocked_modes[mode] = True

            self.write_data(data, 0)
            print("All gamemodes have been unlocked!")
        
        except Exception as e:
            print(f"Error on unlock_all_gamemodes() -> {e}")
    
    def unlock_all_achievements(self):
        
        try:
            data = self.load_data(0)
            current_time_ms = int(time.time() * 1000) 
            min_time_ms = current_time_ms - 3600 * 1000  

            achievements = self.extra_data["achievements"]
            data["achvUnlocks"] = {
                achievement: random.randint(min_time_ms, current_time_ms)
                for achievement in achievements
            }

            self.write_data(data, 0)
            print("All achievements have been unlocked!")

        except Exception as e:
            print(f"Error on unlock_all_achievements -> {e}")
    
    def unlock_all_vouchers(self):
        try:
            data = self.load_data(0)

            current_time_ms = int(time.time() * 1000) 
            min_time_ms = current_time_ms - 3600 * 1000  

            vouchers = self.extra_data.get("vouchers", [])
            voucher_unlocks = {}
            for voucher in vouchers:
                random_time = min_time_ms + random.randint(0, current_time_ms - min_time_ms)
                voucher_unlocks[voucher] = random_time
            data["voucherUnlocks"] = voucher_unlocks

            self.write_data(data, 0)
            print("All vouchers have been unlocked!")

        except Exception as e:
            print(f"Error on unlock_all_vouchers -> {e}")
    
    def biomes(self):
        biomes = [f"{value}: {key}" for key, value in self.biomes_by_id['biomes'].items()]
        print("\n".join(biomes))

    def moves(self):
        moves = [f"{value}: {key}" for key, value in self.moves_by_id['moves'].items()]
        print("\n".join(moves))
