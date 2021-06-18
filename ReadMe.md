**Docker And GCloud Run ready fastai RestAPI**

---

After exporting your models with learn.export( ) put your .pkl files in models directory.

Register models at app.py like this:

`learner = load_learner(f"{MODELS_PATH}/export.pkl")`

**Use models at endpoints like this:**

    @app.route("/end-point", methods=["POST"])

    def classify():
        return image_classifier(learner)

**For Docker build and deployment**

`docker build -t fastai .`

`docker run -p 8080:8080 -d fastai`

**And run your container on any service provider.**

---

**For gcloud build and deployment**

**If you're using gcloud deploy your models one model at a time**

`gcloud builds submit --tag gcr.io/PROJECT-ID/PROJECT-NAME`

`gcloud run deploy --image gcr.io/PROJECT-ID/PROJECT-NAME`

---
