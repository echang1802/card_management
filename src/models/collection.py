import pandas as pd

from utils.database import database

class Collection:

    def __init__(self, game : str = None):
        self._database = database()
        self._game = game.replace("-", "_") if game else None

    def add_booster(self, booster, log)-> None:
        log = log.start_function("Collection.add_booster")
        for card in booster.cards:
            self._database.add_card_to_collection(card)

            pos = (self._data['name'] == card.name) & (self._data['set'] == card.set) & (self._data['rarity'] == card.rarity) & (self._data['type'] == card.type)
            if pos.sum() > 0:
                self._data.loc[pos, 'quantity'] += 1
                self._data.loc[pos, 'value'] = card.price
            else:
                new_row = pd.DataFrame({
                    'name': [card.name], 
                    'rarity': [card.rarity],
                    'type': [card.type],
                    'set': [card.set],
                    'quantity': [1],                    
                    'value': [card.price]
                }, index = [self._data.shape[0]])
                self._data = pd.concat([self._data, new_row], ignore_index=True)

        self._data.to_csv(f"src/data/Collection/{booster.game}.csv", index=False)
        log.INFO(f"Cards added to {booster.game} collection")

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
