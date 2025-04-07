from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
   return "<h1> Welcome To Render Flask,/h1>"

if __name__ == '__main__':
   app.run()
