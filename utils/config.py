from pathlib import Path
import yaml

def load_config():
    config_path=Path("config/config.yaml")

    with open(config_path,"r") as file:
        return yaml.safe_load(file)
    

    
from utils.config import load_config

config = load_config()