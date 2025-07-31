from dataclasses import dataclass

@dataclass
class Card:
    name: str
    rarity: str
    type: str
    set : str
    game : str
