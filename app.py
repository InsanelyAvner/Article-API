from flask import Flask,jsonify,request
import csv

app = Flask(__name__)

all_articles = []
liked_articles = []
not_liked_articles = []


with open("articles.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

@app.route("/get-article")
def get_article():
    return jsonify({
        "data": all_articles[0],
        "status":"success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.apppend(article)

    return jsonify({
        "status":"success"
    }), 201


@app.route("/not-liked-articles", methods=["POST"])
def not_liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.apppend(article)
    
    return jsonify({
        "status":"success"
    }), 201

if __name__ == "__main__":
    app.run(port = 5000)