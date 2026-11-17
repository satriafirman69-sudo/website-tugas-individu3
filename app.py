
from flask import Flask, render_template

app = Flask(__name__)

# Daftar username yang sudah terdaftar
USERNAME_TERDAFTAR = ["andi", "budi", "citra", "satria"]


# Halaman Beranda
@app.route("/")
def home():
    return render_template("index.html")


# Halaman Pengecekan Username
@app.route("/cek/<username>")
def cek_username(username):

    username = username.lower()

    # Memeriksa panjang username
    valid = len(username) >= 4

    # Memeriksa ketersediaan username
    tersedia = valid and username not in USERNAME_TERDAFTAR

    return render_template(
        "cek.html",
        username=username,
        valid=valid,
        tersedia=tersedia
    )


# Halaman Daftar Username
@app.route("/data")
def data_username():

    daftar_username = [
        {"nama": "andi", "status": "Terdaftar"},
        {"nama": "budi", "status": "Terdaftar"},
        {"nama": "citra", "status": "Terdaftar"},
        {"nama": "satria", "status": "Terdaftar"}
    ]

    return render_template(
        "data.html",
        daftar=daftar_username
    )


if __name__ == "__main__":
    app.run(debug=True)
