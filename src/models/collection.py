import pandas as pd
from datetime import datetime

class Collection:

    def __init__(self, game : str = None):
        if game:
            self._data = pd.read_csv(f"src/data/Collection/{game}.csv")
        else:
            self._data = pd.DataFrame()
            for game in ["magic-the-gathering", "pokemon", "disney-lorcana", "digimon"]:
                try:
                    data = pd.read_csv(f"src/data/Collection/{game}.csv")
                    self._data = pd.concat([self._data, data], ignore_index=True)
                except FileNotFoundError:
                    continue
            self._data.reset_index(drop=True, inplace=True)

    def add_booster(self, booster, log)-> None:
        log = log.start_function("Collection.add_booster")
        for card in booster.cards:
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

    def get_stats(self) -> dict:
        pos = self._data["value"] != -1
        total_value = (self._data.loc[pos]['value'] * self._data.loc[pos]['quantity']).sum()
        total_cards = self._data['quantity'].sum()
        return {
            'total_value': round(total_value, 2),
            'total_cards': total_cards
        }

    def _add_booster_stat(self, booster, log) -> None:
        booster_stats = pd.read_csv("src/data/Collection/boosters.csv")
        booster_stats = pd.concat([booster_stats, pd.DataFrame({
            'game': booster.game,
            'set': booster.set,
            'date_added' : datetime.now().strftime("%Y-%m-%d"),
            'value': booster.get_booster_value()
        }, index = [booster_stats.shape[0]])], ignore_index=True)
        booster_stats.to_csv("src/data/Collection/boosters.csv", index=False)
        log.INFO(f"Booster stats added for {booster.game} - {booster.set}")
