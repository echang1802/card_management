import pandas as pd
from dataclasses import dataclass

from models.card import Card
from models.price_finder import PriceFinder

@dataclass
class Booster:
    game: str
    set: str

    def open(self, booster_filename : str) -> None:
        # Logic to open a booster pack and return the cards inside
        self.cards = []

        priceF = PriceFinder()

        booster = pd.read_csv(booster_filename)
        for _, row in booster.iterrows():
            card = Card(
                name=row['card_name'],
                rarity=row['rarity'],
                type=row['card_type'],
                set=self.set,
                game=self.game
            )
            card.price = priceF.find_card_price(card)
            self.cards.append(card)

    def get_booster_value(self) -> float:
        # Calculate the total value of the booster pack
        return sum(card.price for card in self.cards)
        
        

        
        
