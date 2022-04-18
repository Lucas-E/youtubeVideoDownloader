from flask import Flask, request, render_template, redirect, url_for
from main import downloadVideo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=["POST"])
def download():
    link = request.form.get('link')
    downloadVideo(link)
    return render_template('index.html', downloaded = True)
if __name__ == "__main__":
    app.run(debug=True)