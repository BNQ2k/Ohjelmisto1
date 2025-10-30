from flask import Flask, jsonify
app = Flask(__name__)

def onko_alkuluku(luku):
    if luku <= 1:
        return False
    i = 2
    while i * i <= luku:
        if luku % i == 0:
            return False
        i += 1
    return True

@app.route('/alkuluku/<int:luku>', methods=['GET'])
def tarkista_alkuluku(luku):
    on_alkuluku = onko_alkuluku(luku)
    vastaus = {
        "Number": luku,
        "isPrime": on_alkuluku
    }

    return jsonify(vastaus)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)