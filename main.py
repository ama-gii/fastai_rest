from fastai.learner import load_learner
from flask import Flask
from classifiers import *
from flask_cors import CORS


# Creating text and image path just to be sure
os.makedirs(IMAGES_PATH, exist_ok=True)
os.makedirs(TEXTS_PATH, exist_ok=True)


app = Flask(__name__)
CORS(app)

# learner                     model path  model name
pet_breeds = load_learner(f"{MODELS_PATH}/pet_breeds.pkl")


@app.route("/pet-breeds", methods=["POST"])
def upload_images():
    return image_category_classifier(pet_breeds)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
