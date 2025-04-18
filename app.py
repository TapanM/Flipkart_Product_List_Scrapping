from flask import Flask, render_template, request
import glob
import csv

from flipkart_scrapper import run

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    products = []
    if request.method == "POST":
        search_item = request.form.get("search")
        if search_item:
            products = run(search_item)
    return render_template("index.html", items=products)

if __name__ == "__main__":
    app.run()
