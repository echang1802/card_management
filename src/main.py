from flask import Flask, render_template, request, jsonify

from utils.functions import get_stats, add_booster_to_collection

app = Flask(__name__)


@app.route("/")
def dashboard():
    collection_stats = get_stats()
    total_value, total_cards = collection_stats["total_value"], collection_stats["total_cards"]
    tcg_stats = [
        {"tcg": tcg, "count": get_stats(tcg)["total_cards"], "value": get_stats(tcg)["total_value"]}
        for tcg in ["magic", "pokemon", "lorcana", "digimon"]
    ]
    return render_template("dashboard.html", total_value=total_value, total_cards=total_cards, tcg_stats=tcg_stats)

@app.route("/add-booster", methods=["POST"])
def add_booster():
    booster_path = request.json.get("booster_path")
    add_booster_to_collection(booster_path)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)