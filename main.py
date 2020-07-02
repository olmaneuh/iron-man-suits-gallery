from flask import Flask, render_template, request
from flask_uploads import UploadSet, IMAGES, configure_uploads

img = UploadSet("img", IMAGES)

app = Flask(__name__)
app.config["UPLOADED_IMG_DEST"] = "uploads/img"

configure_uploads(app, img)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "image" in request.files:
        img.save(request.files["image"])
        return "Suit uploaded"

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
