from flask import Flask, jsonify

app = Flask(__name__)

ships = [
    {"id": 1, "name": "Ever Given", "type": "Container", "tonnage": 220940, "port": "Kaohsiung"},
    {"id": 2, "name": "Formosa 1", "type": "Bulk", "tonnage": 85000, "port": "Kaohsiung"},
    {"id": 3, "name": "Ocean Star", "type": "Tanker", "tonnage": 95000, "port": "Taichung"},
]

@app.route("/")
def index():
    return jsonify({"message": "高雄港船舶資料 API", "version": "1.0", "total_ships": len(ships)})

@app.route("/ships")
def get_ships():
    return jsonify(ships)

@app.route("/ships/<int:ship_id>")
def get_ship(ship_id):
    ship = next((s for s in ships if s["id"] == ship_id), None)
    if ship:
        return jsonify(ship)
    return jsonify({"error": "找不到此船舶"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
