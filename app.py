from fastai.learner import load_learner
from flask import Flask
from classifiers import *
from flask_cors import CORS

BASE_PATH = os.getcwd()
IMAGES_PATH = os.path.join(BASE_PATH, "images")
MODELS_PATH = os.path.join(BASE_PATH, "models")
TEXTS_PATH = os.path.join(BASE_PATH, "texts")

ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
CORS(app)

# learner                     model path  model name
pet_breeds = load_learner(f"{MODELS_PATH}/pet_breeds.pkl")


@app.route("/pet-breeds", methods=["POST"])
def upload_images():
    return image_category_classifier(pet_breeds)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
