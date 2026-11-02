from flask import Flask
import psycopg2

app= Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname = 'library2',
        user = 'postgres', 
        password = 'divu',
        host = 'localhost',     
        port = 5432       
    )
#create books table
@app.route('/create_table')
def create_table():
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
             CREATE TABLE IF NOT EXISTS book(
                  bid serial primary key,
                  title varchar(100),
                  author varchar(100),
                  price INT
             );
        """)
        conn.commit()
        cur.close()
        conn.close()

        return "Books Table created successfully"
    
    except Exception as e:
        return f"Error : {e}"
    
@app.route('/insert_records')
def insert_records():
    try:
        conn = db_connect()
        cur = conn.cursor()
    
        books=[
        ("Bhadrakali","Anant Tibile",1500),
        ("You Can Win","Shiv khera",295),
        ("Wings of Fire","Dr. A.P.J Abdul Kalam",299),
        ("Mann Mein hai vishwas","Vishwas Nangre Patil",500)
        ]
        cur.executemany( "INSERT INTO book(title,author,price) values(%s,%s,%s);",books)
            
        conn.commit()
        cur.close()
        conn.close()
        return"Records inserted Successfully in books table!"

    except Exception as e:
        return f"Error: {e}"

@app.route('/display_books')
def display_books():
     try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("SELECT title,author,price FROM book;")
        books = cur.fetchall()

        cur.close()
        conn.close()

        book_list = ""
        if not books:
         return "No books found! Please insert records first."
        for book in books:
             book_list += f"Title: {book[0]},Author:{book[1]},price:{book[2]}<br>"

        return book_list
     except Exception as e:
          return f"Error:{e}"
if __name__ =='__main__':
    app.run(debug=True)
