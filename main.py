from fastai.learner import load_learner
from flask import Flask
from classifiers import *
from flask_cors import CORS


# Creating text and image path just to be sure
os.makedirs(IMAGES_PATH, exist_ok=True)
os.makedirs(TEXTS_PATH, exist_ok=True)


app = Flask(__name__)
# Register your website for CORS
CORS(app, resources={r"/api/*": {"origins": ["YOUR-WEBSITE"]}})

# learner                     model path  model name
learner = load_learner(f"{MODELS_PATH}/export.pkl")


@app.route("/api/end-point", methods=["POST"])
def classify_image():
    return image_category_classifier(learner)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
