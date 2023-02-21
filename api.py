from flask import Flask, jsonify , request
import csv

all_articles=[]

with open('articles.csv','r',encoding='UTF8') as f:
    dataframe=csv.reader(f)
    df=list(dataframe)
    all_articles=df[1:]

liked_articles=[]
not_liked_articles=[]

app=Flask(__name__)

@app.route("/get-article")
def get_articles():
    return jsonify({
        "data":all_articles,
        "status":"success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not_liked-article",methods=['POST'])
def not_liked_article():
    article=all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status":"success"
    }),201

if __name__ == "__main__":
    app.run()