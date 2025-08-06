
import psycopg2
import pickle
from numpy import round

class database:

    def __init__(self):
        with open("src/data/creds/database.pkl", "rb") as file:
            creds = pickle.load(file)
        self.conn = psycopg2.connect(**creds)

    def test_connection(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT version();")
            version = cur.fetchone()
            print("PostgreSQL version:", version)
            cur.close()
        except Exception as e:
            print("Database connection failed:", e)

    def get_game_stats(self, game : str, log) -> dict:
        cur = self.conn.cursor()
        query = f"""
        SELECT SUM(value * quantity) AS total_value, SUM(quantity) AS total_cards
        FROM collections.{game};
        """
        cur.execute(query)
        result = cur.fetchone()
        cur.close()
        if result:
            log.INFO(f"Stats for {game} retrieved, total value: {result[0]}, total cards: {result[1]}")
            return {
                'total_value': round(result[0], 2) if result[0] is not None else 0,
                'total_cards': result[1] if result[1] is not None else 0
            }
        return {
            'total_value': 0,
            'total_cards': 0
        }
    
    def add_card_to_collection(self, card) -> None:
        cur = self.conn.cursor()
        query = f"""
        INSERT INTO collections.{card.game} (name, rarity, type, set, quantity, value)
        VALUES (%s, %s, %s, %s, 1, %s)
        ON CONFLICT (name, rarity, type, set) DO UPDATE SET
            quantity = collections.{card.game}.quantity + 1,
            value = %s
        """
        cur.execute(query, (card.name, card.rarity, card.type, card.set, card.price, card.price))
        self.conn.commit()
        cur.close()

    def add_booster_stat(self, booster) -> None:
        cur = self.conn.cursor()
        query = """
        INSERT INTO boosters.history (game, set, date_added, value)
        VALUES (%s, %s, CURRENT_DATE, %s);
        """
        cur.execute(query, (booster.game, booster.set, booster.get_booster_value()))
        self.conn.commit()
        cur.close()

    def close_connection(self):
        if self.conn:
            self.conn.close()
    