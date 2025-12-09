from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result")
def result():
    images = [
    {
        "file": "Elbow Method for Optimal k.png",
        "title": "Elbow Method for Optimal k",
        "desc": "Menentukan jumlah cluster (k) optimal berdasarkan WCSS."
    },
    {
        "file": "KMeans Clusters Visualized PCA.png",
        "title": "KMeans Clusters Visualized PCA",
        "desc": "Visualisasi cluster dalam 2D menggunakan PCA."
    },
    {
        "file": "Cluster Feature Means (Profile Heatmap).png",
        "title": "Cluster Feature Means (Profile Heatmap)",
        "desc": "Heatmap rata-rata fitur pada setiap cluster."
    },
    {
        "file": "Cluster Profiles for Key Customer Features.png",
        "title": "Cluster Profiles for Key Customer Features",
        "desc": "Perbandingan fitur kunci untuk tiap cluster."
    },
]

    return render_template("result.html", images=images)


if __name__ == "__main__":
    # Jalankan app
    app.run(debug=True)
