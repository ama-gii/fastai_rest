import os
from flask import jsonify, request
from werkzeug.utils import secure_filename


BASE_PATH = os.getcwd()
IMAGES_PATH = os.path.join(BASE_PATH, "images")
MODELS_PATH = os.path.join(BASE_PATH, "models")
TEXTS_PATH = os.path.join(BASE_PATH, "texts")

ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    """ Filter filenames to stop XSS problems """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def image_category_classifier(model):
    try:
        file = request.files["file"]
        if file and allowed_file(file.filename):
            file.save(os.path.join(IMAGES_PATH, secure_filename(file.filename)))
            result, _, _ = model.predict(f"{IMAGES_PATH}/{file.filename}")
            os.remove(os.path.join(IMAGES_PATH, secure_filename(file.filename)))
            return jsonify(result), 200
    except (KeyError, FileNotFoundError):
        return jsonify("An error occurred while processing the file."), 500


def image_multi_category_classifier(model):
    try:
        file = request.files["file"]
        if file and allowed_file(file.filename):
            file.save(os.path.join(IMAGES_PATH, secure_filename(file.filename)))
            result, _, _ = model.predict(f"{IMAGES_PATH}/{file.filename}")
            os.remove(os.path.join(IMAGES_PATH, secure_filename(file.filename)))
            if result is False:
                result = "Can't recognize image"
            return jsonify(" ".join(result)), 200
    except (KeyError, FileNotFoundError):
        return jsonify("An error occurred while processing the file."), 500
