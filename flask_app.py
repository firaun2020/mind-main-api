from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def ping():

    status = 200
    if 1:
        status = 200
    else:
        status = 400
    response = {"status_code": status,
                "content": "We are Up & running!"}
    return jsonify(response)


# Route for writing data to the database
@app.route('/write', methods=['POST'])
def write_data():
    data = request.get_json()
    mood = data.get('mood')
    feel = data.get('feeling')
    timestamp = datetime.now()
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    # Insert the data into the database
    c.execute("INSERT INTO minddata (mood, feeling, timestamp) VALUES (?, ?, ?)", (mood, feel, timestamp))
    conn.commit()
    conn.close()
    return 'Data written to database!'


# Route for nuking whole table
@app.route('/nukemofo', methods=['GET'])
def nuke_all():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    # Delete all from minddata
    c.execute("DELETE from minddata")
    conn.commit()
    conn.close()
    return 'They all dead'


# Route for writing batch data to the database
@app.route('/batch_write', methods=['POST'])
def batch_write_data():
    data = request.get_json()
    moods = data.get('moods')
    feels = data.get('feelings')
    timestamp = datetime.now()
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    for m, f in zip(moods, feels):
    # Insert the data into the database
        c.execute("INSERT INTO minddata (mood, feeling, timestamp) VALUES (?, ?, ?)", (m, f, timestamp))
    conn.commit()
    conn.close()
    return 'Batch written to database!'

# Route for getting the mean value of all moods in the database
@app.route('/mood', methods=['GET'])
def get_mood():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT mood FROM minddata")
    numbers = c.fetchall()
    if len(numbers) > 0:
        mean = sum([x[0] for x in numbers]) / len(numbers)
    else:
        mean = 0
    conn.close()
    return jsonify({'mean': mean})

# Route for getting all moods & feels in the database
@app.route('/get_all', methods=['GET'])
def get_all():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('select mood, feeling from minddata')
    alldata = c.fetchall()
    if len(alldata) > 0:
        return jsonify(alldata)
    else:
        print("whatever")
    conn.close()
    return jsonify(alldata)


# Route to return last vote score
@app.route('/lastvote', methods=['GET'])
def get_last():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT mood FROM minddata ORDER BY timestamp DESC LIMIT 1")
    lastnumber = c.fetchone()
    c.execute("SELECT feeling FROM minddata ORDER BY timestamp DESC LIMIT 1")
    lastfeeling = c.fetchone()
    if len(lastnumber) > 0:
        response = {'latest': lastnumber,
                    'lastfeeling': lastfeeling}
    else:
        return jsonify({'response': "no data available"})
    conn.close()
    return jsonify(response)



if __name__ == '__main__':
    app.run()
