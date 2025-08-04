from flask import Flask
import threading
from main import run_all

app = Flask(__name__)

@app.route('/')
def index():
    return "Bot çalışıyor!"

if __name__ == "__main__":
    t = threading.Thread(target=run_all)
    t.start()
    app.run(host='0.0.0.0', port=10000)
