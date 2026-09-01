from flask import Flask, render_template_string
import webbrowser
import threading

app = Flask(__name__)

# HTML file load karo
HTML_CODE = open("template/index.html", encoding="utf-8").read()

@app.route("/")
def home():
    return render_template_string(HTML_CODE)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    print("========================================")
    print("  Discount Rule Checker is starting...")
    print("  Open this link: http://127.0.0.1:5000")
    print("========================================")
    
    threading.Timer(1.0, open_browser).start()
    app.run(debug=False, port=5000)