from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {"id": 1, "name": "Idly", "price": 15},
    {"id": 2, "name": "Dosa", "price": 70},
    {"id": 3, "name": "Parotta", "price": 15},
    {"id": 4, "name": "Sivagangai Chicken Biriyani", "price": 200},
    {"id": 5, "name": "Sivagangai Mutton Biriyani", "price": 250}
]

@app.route("/")
def index():
    return render_template("index.html", menu=menu)

@app.route("/order", methods=["POST"])
def order():
    ordered_items = []
    total = 0

    for item in menu:
        qty = int(request.form.get(f"quantity{item['id']}", 0))
        if qty > 0:
            item_total = qty * item["price"]
            ordered_items.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": qty,
                "total": item_total
            })
            total += item_total

    return render_template("order.html", ordered_items=ordered_items, total=total)

if __name__ == '__main__git add app.py
    import os
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT env variable
    app.run(host='0.0.0.0', port=port)