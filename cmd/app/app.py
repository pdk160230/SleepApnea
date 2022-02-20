from flask import Flaskapp = Flask(__name__)@app.route('/')
def portal():
    return 'portal stuff to come!'if __name__=='__main__':
   app.run()