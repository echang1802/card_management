import pandas as pd
from dataclasses import dataclass
from format_logger.logger import logger

from models.card import Card
from models.price_finder import PriceFinder

@dataclass
class Booster:
    game: str
    set: str
    file: str

    def open(self, log) -> iter:
        log = log.start_function("Booster.open")

        # Logic to open a booster pack and return the cards inside
        self.cards = []

        priceF = PriceFinder()

        booster = pd.read_csv(self.file)
        for idx, row in booster.iterrows():
            card = Card(
                name=row['card_name'],
                rarity=row['rarity'],
                type=row['card_type'],
                set=row['set'],
                game=self.game
            )
            if card in self.cards:
                card.price = [c.price for c in self.cards if c == card][0]
                message = "ok"
            else:
                card.price, message = priceF.find_card_price(card, log)
            if message == "DAILY_LIMIT_EXCEEDED":
                log.WARNING("Daily limit exceeded for JustTCG API. Skipping card price retrieval for remaining cards.")
                booster = booster.iloc[idx:]  # Stop processing further cards
                booster.to_csv(self.file, index=False)
                break
            self.cards.append(card)
            yield card, message
        log.end_function()

    def get_booster_value(self) -> float:
        # Calculate the total value of the booster pack
        return round(sum(card.price for card in self.cards), 2)

