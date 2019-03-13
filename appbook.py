from flask import Flask,render_template,url_for,request,jsonify
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from firebase import firebase
firebase = firebase.FirebaseApplication('https://tweet-of-thailand.firebaseio.com', None)
result = firebase.get('/region/ภาคกลาง', None)
'''
code ดึง model
'''
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong ja!!!!!!!!!!!!!')

@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })
'''
@app.route('/',methods=['POST'])
def predict():
    if request.method == 'POST': 
        comment = request.form['comment']
        firee = result
    return render_template('a.html',prediction = comment,fire=firee)
'''
if __name__ == '__main__':
    app.run(debug=True)