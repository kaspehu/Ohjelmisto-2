from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)

# http://127.0.0.1:3000/kentta/EFHK
@app.route('/kentta/<ICAO>')
def hae_kentta(ICAO):
    cursor = connection.cursor(dictionary=True)
    sql = 'SELECT gps_code AS "ICAO", name AS "Name", municipality AS "Municipality" FROM airport WHERE gps_code = %s'
    cursor.execute(sql, (ICAO,))
    tulos = cursor.fetchone()

    if tulos:
        return jsonify(tulos)
    else:
        return jsonify(f"The airport '{ICAO}' was not found.")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)