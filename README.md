# Anime Hybrid Recommender

> **Hybrid (Collaborative + Content)** Anime recommendation engine — Flask web app with containerized deployment and CI/CD.

---

## 🧠 Purpose

To recommend the **top n anime titles** for a given `user_id` by:

* Using similar users’ preferences (**collaborative filtering**)
* Finding similar anime based on content (**content-based filtering**)
* Combining both with adjustable weights through a **hybrid approach**

This ensures recommendations are both **personalized** and **diverse**, balancing what similar users enjoy with anime that share content characteristics.

---

## 📦 Tech Stack

* **Python** (pandas, numpy, scikit-learn, TensorFlow/Keras)
* **Flask**, HTML, Jinja2 templating for web app
* **Docker** for containerization
* **Jenkins** for CI/CD automation
* **Google Kubernetes Engine (GKE)** for deployment
* **Google Container Registry (GCR)** to store images
* **Google Cloud Storage (GCS)** for data ingestion
* **DVC** for data versioning (to manage large data files (dvc add anime_list.csv) and push to remote storage (GCS) so the repo remains lightweight and reproducible)
* **GitHub** for code versioning
* **CometML** for experiment tracking and monitoring

---

## 📂 Data Sources

All datasets were sourced from **Kaggle** and uploaded to GCP buckets:

* `anime_list.csv` (sampled \~5M rows from \~70M)
* `anime_with_synopsis.csv`
* `anime.csv`

Selective data ingestion was applied to handle scale efficiently.

---

## 🎯 Key Highlights

* Built **content-based filtering** and **user/collaborative filtering**, then combined them into a **hybrid recommender**.
* Deployed the final app on a **Kubernetes cluster** for scalability.
* Used **CometML** for tracking experiments, hyperparameters, and metrics online.
* Achieved a smooth **CI/CD pipeline** with Jenkins, Docker, and GCP services.
* Designed an **interactive web interface**: given a `user_id`, the app recommends anime and displays them in grid cards.

---
Note on data sampling: only a subset of the large anime_list.csv was used in experiments (roughly 5M rows sampled from ~70M). This sampling reduced training time but affected recommendation quality & coverage 

---
## 🧠 Models & training

Collaborative model (embedding / neural CF)

Architecture: RecommenderNet() — user and anime embedding layers (embedding size = 128) with a Dot similarity followed by a Dense(1) + sigmoid output. This is a matrix‑factorization style model implemented in Keras.

*Loss / metrics*: **binary_crossentropy loss**; *metrics logged during training*: **mae, mse**.

Training: model.fit(...) was used with epochs = 20 and a custom learning‑rate schedule, model checkpoint, Early Stopping. 

LR schedule: start_lr, max_lr, min_lr, ramup_epochs, exp_decay

## 📹 Demo Video

👉 [Watch the project demo here](https://vimeo.com/1116553003)

---

This project demonstrates how blending **collaborative filtering** with **content-based filtering** creates a powerful and scalable anime recommendation system.
