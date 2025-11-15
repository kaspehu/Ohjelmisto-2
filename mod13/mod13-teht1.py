from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:3000/alkuluku/45
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    if luku <= 1:
        return f"Antamasi luku {luku} ei ole alkuluku."

    for i in range(2, luku):
        if luku % i == 0:
            return f"Antamasi luku {luku} ei ole alkuluku."

    return f"Antamasi luku {luku} on alkuluku."

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)





