from models.collection import Collection
from format_logger.logger import logger

def get_stats(log : logger, tcg : str = None) -> dict:
    collection = Collection(tcg)
    return collection.get_stats(log)

def add_booster_to_collection(booster_filename : str, tcg: str, log : logger) -> None:
    log = log.start_function("add_booster_to_collection")
    from models.booster import Booster    
    game = tcg.lower().replace(" ", "-")
    set_name = ''.join(filter(lambda x: not x.isdigit(), booster_filename.replace("_", "")))
    booster = Booster(game = game, set = set_name)
    booster.open(f"src/data/boosters/{tcg}/{booster_filename}.csv", log)
    log.INFO(f"Booster opened: {booster_filename} with value {booster.get_booster_value()}")
    collection = Collection(tcg)
    collection.add_booster(booster, log)
    log.end_function()