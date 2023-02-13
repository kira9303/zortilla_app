import numpy as np
from flask import Flask, request, redirect, render_template, jsonify, flash, session
import pickle
import jwt


app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
#app.config['SECRET_KEY'] = 'secret-key'

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/monday', methods=['POST', 'GET'])
def monday():
    return render_template('Monday.html')

@app.route('/tuesday', methods=['POST', 'GET'])
def tuesday():
    return render_template('Tuesday.html')

@app.route('/wed', methods=['POST', 'GET'])
def wednesday():
    return render_template(('Wednesday.html'))

@app.route('/thursday', methods=['POST', 'GET'])
def thursday():
    return render_template(('Thursday.html'))

@app.route('/friday', methods=['POST', 'GET'])
def friday():
    return render_template(('Friday.html'))

@app.route('/saturday', methods=['POST', 'GET'])
def saturday():
    return render_template(('Saturday.html'))

@app.route('/sunday', methods=['POST', 'GET'])
def sunday():
    return render_template('Sunday.html')

'''@app.route('/login', methods=['POST', 'GET'])
def login():

        import mysql.connector
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_tables"
        )

    # Insert user data into database
        cursor = conn.cursor()



        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        return render_template('Login.html')'''



#@app.route('/contact', methods=['POST', 'GET'])
#def contact_us():



@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if (request.method == "POST"):


        username = request.form.get("username")
        email = request.form.get("email")
        mobile = request.form.get("mobile_number")
        address = request.form.get("address")

        print(address)
        print(email)
        print(mobile)
        #password = request.form.get("password")
        #password2 = request.form.get("second_pass")

        #if password != password2:
            #return render_template("Signup.html", error_message="Passwords do not match")

    # Connect to database
        import mysql.connector
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_tables"
        )

    # Insert user data into database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO checkouts (Name, email, phone_number, address) VALUES (%s, %s, %s, %s)", (username, email, mobile, address))
        conn.commit()

        #print("print complete")
        #flash("Your data has been sent.")

        return redirect('/')
    return render_template("CheckOut.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if(request.method=="POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        #print(name)
        #print(email)

        #print(message)

        import mysql.connector
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_tables"
        )

        # Insert user data into database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedbacks (name, email, message) VALUES (%s, %s, %s)",
                       (name, email, message))
        conn.commit()

        return redirect('/')




@app.route('/signup', methods=['POST', 'GET'])
def signup():

    if (request.method == "POST"):


        username = request.form.get("username")
        email = request.form.get("email")
        mobile = request.form.get("mobile_number")
        password = request.form.get("password")
        password2 = request.form.get("second_pass")

        print(username)
        print(password)
        print(email)
        print(mobile)
        #print(usernaame)

        if password != password2:
            return render_template("Signup.html", error_message="Passwords do not match")

    # Connect to database
        import mysql.connector
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="food_tables"
        )

    # Insert user data into database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO registered (name, email, password, mobile_number) VALUES (%s, %s, %s, %s)", (username, email, password, mobile))
        conn.commit()

        return redirect('/')
    return render_template('Signup.html')



'''@app.route('/home',methods=['POST'])
def home():



    #list = []

    for x in request.form.values():
        list.append(x)
        print(x)


    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
   # prediction = model.predict([np.array(list(data.values()))])

    #output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)