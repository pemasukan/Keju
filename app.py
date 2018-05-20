from flask import Flask,request,Response,jsonify
from peneliti import milo as ml, ml, mlo, mls
import scholarly,json

app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/peneliti/<nama>')
def apaajalah(nama):
    data = ml.cari(nama)
    return jsonify(data)

@app.route('peneliti/<nama>')
def coba2(nama):
    data = ml.coba(nama)
    return jsonify(data)

@app.route('/peneliti/<nama>')
def cobaapp(nama):
    data = mlo.checkmilo(nama)
    return jsonify(data)

@app.route('/peneliti/<nama>')
def sembarang(nama):
    data = mls.kampret(nama)
    return jsonify(data)