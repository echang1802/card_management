import pandas as pd
from dataclasses import dataclass
from format_logger.logger import logger

from models.card import Card
from models.price_finder import PriceFinder

@dataclass
class Booster:
    game: str
    set: str

    def open(self, booster_filename : str, log) -> None:
        log = log.start_function("Booster.open")

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
            card.price = priceF.find_card_price(card, log)
            self.cards.append(card)
            log.INFO(f"Card added: {card.name} with price {card.price}")
        log.end_function()

    def get_booster_value(self) -> float:
        # Calculate the total value of the booster pack
        return round(sum(card.price for card in self.cards), 2)

