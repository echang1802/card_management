
from models.collection import Collection

def get_stats(tcg : str= None) -> dict:
    collection = Collection(tcg)
    return collection.get_stats()

def add_booster_to_collection(booster_filename : str) -> None:
    from models.booster import Booster

    booster = Booster(game = "pokemon", set = "Journey Together")
    booster.open(f"src/data/boosters/pokemon/{booster_filename}.csv")
    booster.get_booster_value()
    collection = Collection("pokemon")
    collection.add_booster(booster)