import pandas as pd

class Collection:

    def __init__(self, game : str = None):
        if game:
            self._data = pd.read_csv(f"src/data/Collection/{game}.csv")
        else:
            self._data = pd.DataFrame()
            for game in ["magic", "pokemon", "lorcana", "digimon"]:
                try:
                    data = pd.read_csv(f"src/data/Collection/{game}.csv")
                    self._data = pd.concat([self._data, data], ignore_index=True)
                except FileNotFoundError:
                    continue
            self._data.reset_index(drop=True, inplace=True)

    def add_booster(self, booster)-> None:
        for card in booster.cards:
            if card.name in self._data['name'].values:
                self._data.loc[self._data['name'] == card.name, 'quantity'] += 1
                self._data.loc[self._data['name'] == card.name, 'value'] = card.price
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

    def get_stats(self) -> dict:
        pos = self._data["value"] != -1
        total_value = (self._data.loc[pos]['value'] * self._data.loc[pos]['quantity']).sum()
        total_cards = self._data['quantity'].sum()
        return {
            'total_value': total_value,
            'total_cards': total_cards
        }
        