from flask import Flask

app = Flask(__name__)

@app.route('/')
def portal():
    return 'portal stuff'

if __name__=='__main__':
   app.run()