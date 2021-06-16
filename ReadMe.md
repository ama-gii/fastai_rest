**Docker ready fastai RestAPI**

---

After exporting your models with learn.export( ) put your .pkl files in models directory.

Register models at app.py like this:

`learner = load_learner(f"{MODELS_PATH}/export.pkl")`

Use models at endpoints like this:

    @app.route("/end-point", methods=["POST"])

    def classify():
        return image_classifier(learner)

For deployment run

`docker build -t fastai .`

`docker run -p 5000:5000 -d fastai`

And run your container on any service provider.
