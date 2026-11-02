from flask import Flask,request,render_template
import psycopg2
app=Flask(__name__)
def dbconnect():
    return psycopg2.connect(
        dbname='fsd',
        user='postgres',
        password='divu',
        host='localhost',
        port=5432)
@app.route('/createtable')
def createtable():
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS std(id serial primary key,name varchar(100),course varchar(100));
                ''')
    conn.commit()
    cur.close()
    conn.close()
    return"table created sucessfully!!"
@app.route('/addstudent',methods=['GET','POST'])
def addstudent():
    if request.method=='POST':
        n=request.form.get('name')
        c=request.form.get('course')
        conn=dbconnect()
        cur=conn.cursor()
        cur.execute("INSERT INTO std(name,course)VALUES (%s,%s);",(n,c))
        conn.commit()
        cur.close()
        conn.close()
        return"STUDENT ADDES SUCCESSFULLY!!"
    return render_template('index.html')
@app.route('/getallrec')
def getallrec():
    conn=dbconnect()
    cur=conn.cursor()
    cur.execute("SELECT id,name,course FROM std;")
    details=cur.fetchall()
    cur.close()
    conn.close()
    all=""
    for s in details:
        all+=f"ID:{s[0]},NAME:{s[1]},COURSE:{s[2]}<br>"
    return all
app.run(debug=True)



