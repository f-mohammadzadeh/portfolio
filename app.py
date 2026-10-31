import sqlite3
from flask import Flask, render_template, request

app = Flask (__name__)      #ساختن برنامه اصلی وب با فلسک 

def init_db():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')        #  تعریف آدرس صفحه اصلی سایت (Route)

def home():
    return render_template('index.html')

@app.route('/contact', methods=["POST"])  
def contact():
    user_name = request.form['name']
    user_email = request.form['email']
    user_message = request.form['message']

    conn = sqlite3.connect('portfolio.db')                # اتصال به دیتابیس و اجرای دستور INSERT در SQL
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages(name, email, message) 
        VALUES(?, ?, ?)''', (user_name, user_email, user_message))
    conn.commit()
    conn.close()

    return render_template('index.html', success_message="Thank you! Your message has been saved to the database.")


if __name__ == '__main__':
    app.run(debug=True)
