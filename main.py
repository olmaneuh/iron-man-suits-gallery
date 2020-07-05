import os
from flask import Flask, render_template, request
from flask_uploads import UploadSet, IMAGES, configure_uploads
from PilLite import Image

app = Flask(__name__)
app.config["UPLOADED_IMG_DEST"] = "static/uploads/img"
app.config["UPLOADED_THUMB_DEST"] = "static/uploads/thumbs"

img = UploadSet("img", IMAGES)
configure_uploads(app, img)

THUMBS_SIZE = (195, 368)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "image" in request.files:
        uploaded_img = request.files["image"]

        img.save(uploaded_img)
        create_thumb(uploaded_img.filename)

        images = get_all_img()
        return render_template("index.html", images=images)

    images = get_all_img()
    return render_template("index.html", images=images)


def create_thumb(filename):
    uploaded_img_thumb = Image.open("/".join((app.config["UPLOADED_IMG_DEST"], filename)))
    uploaded_img_thumb.thumbnail(THUMBS_SIZE)
    uploaded_img_thumb.save("/".join((app.config["UPLOADED_THUMB_DEST"], filename)))


def get_all_img():
    return os.listdir(app.config["UPLOADED_IMG_DEST"])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
