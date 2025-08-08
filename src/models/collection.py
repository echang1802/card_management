import pandas as pd

from utils.database import database

class Collection:

    def __init__(self, game : str = None) -> None:
        self._database = database()
        self._game = game.replace("-", "_") if game else None

    def add_booster(self, booster, save_stats : bool, log)-> None:
        log = log.start_function("Collection.add_booster")
        for card, message in booster.open(log):
            self._database.add_card_to_collection(card, message)
            log.INFO(f"Card added: {card.name} with price {card.price}")

        if save_stats:
            self._add_booster_stat(booster, log)
        log.end_function()

    def get_stats(self, log) -> dict:
        if self._game:
            return self._database.get_game_stats(self._game, log)
        else:
            total_value = 0
            total_cards = 0
            for game in ["magic_the_gathering", "pokemon", "disney_lorcana", "digimon"]:
                stats = self._database.get_game_stats(game, log)
                total_value += stats['total_value']
                total_cards += stats['total_cards']
            return {
                'total_value': round(total_value, 2),
                'total_cards': total_cards
            }

    def _add_booster_stat(self, booster, log) -> None:  
        self._database.add_booster_stat(booster)
        log.INFO(f"Booster stats added for {booster.game} - {booster.set}")
