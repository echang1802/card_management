from models.collection import Collection
from format_logger.logger import logger

def get_stats(log : logger, tcg : str = None) -> dict:
    collection = Collection(tcg)
    return collection.get_stats(log)

def add_cards_to_collection(booster_filename : str, tcg: str, is_booster: bool, log : logger) -> None:
    log = log.start_function("add_booster_to_collection")
    from models.booster import Booster    
    game = tcg.lower().replace(" ", "-")
    set_name = ''.join(filter(lambda x: not x.isdigit(), booster_filename.replace("_", "")))
    booster = Booster(game = game, set = set_name, file = f"src/data/boosters/{tcg}/{booster_filename}.csv")
    collection = Collection(tcg)
    collection.add_booster(booster, is_booster, log)    
    log.INFO(f"Booster opened: {booster_filename} with value {booster.get_booster_value()}")    
    log.end_function()