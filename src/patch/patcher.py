import os
import shutil

def main():
    source_file = "game-data.ts"
    destination_dir = "../src/system/"
    destination_file = os.path.join(destination_dir, source_file)

    try:
        if os.path.exists(destination_file):
            os.remove(destination_file)

        shutil.move(source_file, destination_dir)
        shutil.copy2(destination_file, source_file)
        print("Patch successful")
    except Exception as e:
        print("Patch unsuccessful:", e)

    input("Press any key to exit...")

if __name__ == "__main__":
    main()