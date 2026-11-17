from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Projeto DevSecOps</title></head>
        <body>
            <h1>Aplicacao rodando para teste de Pipeline SAST e DAST!</h1>
            <p>Status: Online</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
