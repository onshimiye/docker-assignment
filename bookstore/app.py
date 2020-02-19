from flask import Flask, render_template, g, request
import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('database.db')
print('Opened database successfully')

conn.execute('CREATE TABLE IF NOT EXISTS books (book TEXT, author TEXT, quantity INTEGER)')
print('Table created successfully')
conn.close()

@app.route('/')
def home():
    return '<h1> Hi there!</h1> <a href = "/add">add new</a> <br> <a href = "/list">view all</a> '

@app.route('/add', methods= ['POST', 'GET'])
def add():
    if request.method == 'POST':
        book = request.form['book']
        author = request.form['author']
        quantity = request.form['quantity']
    
        with sql.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO books (book, author, quantity) \
                    VALUES (?,?,?)", (book,author,quantity) )

            con.commit()
            print("Recorded successfully")

    return render_template('add.html')
    conn.close()

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
   
    cur = con.cursor()
    cur.execute("select * from books")
   
    rows = cur.fetchall() 
    return render_template("view.html",rows = rows)

if __name__ == '__main__':
    app.run()


