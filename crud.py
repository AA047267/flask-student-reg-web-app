from flask import *  
import sqlite3  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
    return render_template("index.html");  
 
@app.route("/add")  
def add():  
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    if request.method == 'POST':
        try:
            roll = request.form["roll"]
            name = request.form["name"]
            email = request.form["email"]
            country = request.form["country"]

            with sqlite3.connect("our_records.db") as con: 
                cur = con.cursor()  
                cur.execute("INSERT INTO students_info (roll, name, email, country) VALUES (?,?,?,?)",(roll,name,email,country))  
                con.commit()  
                msg = "Student Successfully Enrolled"  
            return render_template("success.html",msg = msg)

        except:
            con.rollback()
            msg = "Student Cannot Be Enrolled - Make Sure Enrollment ID is Unique" 
            return render_template("failure.html",msg = msg)

        finally:   
            con.close()  
                
@app.route("/view")
def view():
    with sqlite3.connect("our_records.db") as con: 
        con.row_factory = sqlite3.Row  
        cur = con.cursor()
        cur.execute("select * from students_info ")
        rows = cur.fetchall()  
    return render_template("view.html",rows = rows)  

@app.route("/delete/<roll_no>",methods = ["POST"])
def delete_record(roll_no):
    with sqlite3.connect("our_records.db") as con:
        cur = con.cursor()
        cur.execute("DELETE FROM students_info WHERE roll = ?", [roll_no])
        con.commit()
        msg = "Record Deleted For Enrollment No " + roll_no + " Successfully" 
    return render_template("delete_success.html", msg = msg )


if __name__ == "__main__":  
    app.run(debug = True)  
