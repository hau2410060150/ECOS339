from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher



app = Flask(__name__)

caesar_cipher = CaesarCipher()
playfair_cipher = PlayfairCipher()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar")
def caesar_page():
    return render_template("caesar.html")

@app.route("/encrypt", methods=["POST"])
def encrypt_page():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    encrypt_page = caesar_cipher.encrypt_text(text, int(key))
    return f"text: {text} <br> key: {key} <br> encrypted text: {encrypt_page}"

@app.route("/decrypt", methods=["POST"])
def decrypt_page():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    decrypt_page = caesar_cipher.decrypt_text(text, int(key))
    return f"text: {text} <br> key: {key} <br> decrypted text: {decrypt_page}"


@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()
    if not data or "plain_text" not in data or "key" not in data:
        return jsonify({"error": "Invalid request"}), 400

    encrypted_text = caesar_cipher.encrypt_text(
        data["plain_text"], int(data["key"])
    )
    return jsonify({"encrypted_message": encrypted_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.get_json()
    if not data or "cipher_text" not in data or "key" not in data:
        return jsonify({"error": "Invalid request"}), 400

    decrypted_text = caesar_cipher.decrypt_text(
        data["cipher_text"], int(data["key"])
    )
    return jsonify({"decrypted_message": decrypted_text})


@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_creatematrix():
    data = request.get_json()
    if not data or "key" not in data:
        return jsonify({"error": "Invalid request"}), 400

    matrix = playfair_cipher.create_playfair_matrix(data["key"])
    return jsonify({"playfair_matrix": matrix})


@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.get_json()
    if not data or "plain_text" not in data or "key" not in data:
        return jsonify({"error": "Invalid request"}), 400

    matrix = playfair_cipher.create_playfair_matrix(data["key"])
    encrypted_text = playfair_cipher.playfair_encrypt(
        data["plain_text"], matrix
    )
    return jsonify({"encrypted_message": encrypted_text})


@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.get_json()
    if not data or "cipher_text" not in data or "key" not in data:
        return jsonify({"error": "Invalid request"}), 400

    matrix = playfair_cipher.create_playfair_matrix(data["key"])
    decrypted_text = playfair_cipher.playfair_decrypt(
        data["cipher_text"], matrix
    )
    return jsonify({"decrypted_message": decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
