import pickle
import requests

class PriceFinder:

    def __init__(self):
        with open("src/utils/justtcg.pkl", "rb") as file:
            self._key = pickle.load(file)

        self._base_url = "https://api.justtcg.com/v1"
        self._cards_endpoint = "cards"
        self._headers = {
            "X-API-Key": self._key,
            "Content-Type" : "application/json"
        }
        self._price_function_switch = {
            "pokemon" : lambda results, card: self._get_pokemon_card_price(results, card),
            "disney-lorcana" : lambda results, card: self._get_pokemon_card_price(results, card)
        }

    def find_card_price(self, card, log):
        params = {
            "q" : card.name,
            "game" : card.game,
            "condition" : "Near Mint"
        }
        url = f"{self._base_url}/{self._cards_endpoint}"
        response = requests.get(url, headers=self._headers, params=params)
        response = response.json()
        if "error" in response.keys():
            log.ERROR(f"Error fetching card price: {response['error']}")
            price = 0
        elif response["meta"]["total"] == 0:
            log.WARNING(f"No results found for card: {card.name} in game: {card.game}")
            price = 0
        else:
            results = response["data"]
            price = self._price_function_switch[card.game](results, card)
        return price

    def _get_pokemon_card_price(self, results, card):
        best_result = {
            "score" : -1,
            "result" : None
        }
        for result in results:
            score = 0
            if card.set in result["set"]:
                score += 1
            if card.rarity == result["rarity"]:
                score += 1
            if score >= best_result["score"]:
                best_result = {
                    "score" : score,
                    "result" : result
                }
        price = 0
        for variant in best_result["result"]["variants"]:
            if variant["condition"] != "Near Mint":
                continue
            if not card.type in variant["printing"]:
                continue
            price = variant["avgPrice"]
        return price
    
    