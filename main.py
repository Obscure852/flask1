from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route("/")
def home():
    name = "Thato Obuseng"
    return render_template("index.html", content=name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
