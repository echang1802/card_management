from flask import Flask, render_template, request, jsonify
from format_logger.logger import logger

from utils.functions import get_stats, add_cards_to_collection

app = Flask(__name__)


@app.route("/")
def dashboard():
    log = logger("card_management", "dashboard")
    collection_stats = get_stats(log)
    total_value, total_cards = collection_stats["total_value"], collection_stats["total_cards"]
    tcg_stats = [
        {
            "tcg": tcg.replace("-", " "), 
            "count": get_stats(log, tcg)["total_cards"],
            "value": get_stats(log, tcg)["total_value"]
        }
        for tcg in ["magic-the-gathering", "pokemon", "disney-lorcana", "digimon"]
    ]
    log.end_function()
    return render_template("dashboard.html", total_value=total_value, total_cards=total_cards, tcg_stats=tcg_stats)

@app.route("/add-booster", methods=["POST"])
def add_booster():
    log = logger("card_management", "add_booster")
    booster_path = request.json.get("booster_path")
    tcg = request.json.get("tcg")
    is_booster = request.json.get("booster", True)  # Checkbox value from modal

    add_cards_to_collection(booster_path, tcg.lower(), is_booster,log)

    log.end_function()
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)