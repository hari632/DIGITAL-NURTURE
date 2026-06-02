import json

def save_config(config):

    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

    print("Configuration Saved")


def load_config():

    with open("config.json", "r") as file:
        config = json.load(file)

    print("Configuration Loaded")
    print(config)


settings = {
    "theme": "dark",
    "language": "English",
    "notifications": True
}

save_config(settings)
load_config()