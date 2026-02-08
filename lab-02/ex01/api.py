from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
playfair_cipher = PlayfairCipher()


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
