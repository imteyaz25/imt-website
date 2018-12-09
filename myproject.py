from flask import Flask, render_template, request
application = Flask(__name__)

@application.route("/")
def hello():
    return render_template('index.html') 

if __name__ == "__main__":
    application.run(host='172.104.216.83')
