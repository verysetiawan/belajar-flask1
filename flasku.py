from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "IniSecretKeyKu2020"


if __name__ == "__main__":
    app.run (host='0.0.0.0', debug=True)