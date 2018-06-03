from flask import Flask,request,jsonify
from peneliti import milo as ml
import scholarly,json
from flask_mysqldb import MySQL
import pymysql

db = pymysql.connect("localhost", "root", "", "author")

app = Flask(__name__)
mysql = MySQL(app)

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

@app.route('/peneliti/<nama>', methods=['GET'])
def apaajalah(nama):
    search_query = scholarly.search_author(nama)
    return str(next(search_query))

@app.route('/aut')
def hehe():
    cursor = db.cursor()
    sql = "SELECT * FROM service"
    cursor.execute(sql)
    results = cursor.fetchall()
    return str(results)

@app.route('/cobaan')
def cobain():
   cursor = db.cursor()
   sql = "SELECT * FROM service WHERE id=180"
   cursor.execute(sql)
   results = cursor.fetchall()
   return jsonify(results)