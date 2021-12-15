 from app import app

from flask import Flask 

from flask import render_template

app = Flask(__name__)

@app.route("/")
def stars():
  return render_template('stars.html', name=name)

if __name__ == '__index__':
  app.run(debug=True)
