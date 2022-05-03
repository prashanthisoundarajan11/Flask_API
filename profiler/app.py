from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        iid = request.form['customer_Id']
        name = request.form['customer_Name']
        job = request.form['customer_Job']
        todos.insert_one({'customer_Id': iid, 'customer_Name': name,'customer_Job': job})
        return redirect(url_for('index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.route('/<int:user_id>',  methods=['GET'])
def get_user(user_id):
 	details = todos.find({'customer_Id': 1})
 	return render_template('userid.html', unique_customer=details)

