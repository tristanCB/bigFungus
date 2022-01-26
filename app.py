from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    # context = ('cert.pem', 'key.pem') #certificate and key files  // ssl_context=context
    app.run(host='0.0.0.0', port=5000, debug=True)
    # serve(app, host='0.0.0.0', port=5000, url_scheme='https')