import json
import os
import random

from dotenv import load_dotenv

def pick_new_background(backgrounds_path, current_background):
    chosen_background_path = backgrounds_path + random.choice(os.listdir(backgrounds_path))
    while current_background == chosen_background_path:
        chosen_background_path = backgrounds_path + random.choice(os.listdir(backgrounds_path))

    return chosen_background_path

def set_background(settings_path, background_path):
    with open(settings_path, "r") as file:
        data = json.load(file)
        data["profiles"]["defaults"]["backgroundImage"] = background_path
        
    with open(settings_path, "w") as file:
        json.dump(data, file, indent=4)

def get_current_background(settings_path):
    with open(settings_path, "r") as file:
        data = json.load(file)
        return data["profiles"]["defaults"]["backgroundImage"]

def main():
    load_dotenv()
    backgrounds_path = os.getenv("BACKGROUNDS_PATH") 
    settings_path = os.getenv("SETTINGS_PATH") 

    background_image_path = pick_new_background(backgrounds_path, get_current_background(settings_path))
    set_background(settings_path,background_image_path)


if __name__ == "__main__":
    main()
