from flask import Flask, render_template, request
application = Flask(__name__)

@application.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@application.route("/")
def hello():
    return render_template('index.html') 

if __name__ == "__main__":
    application.run(host='127.0.0.1', debug='True')
