from flask import Flask, render_template
app = Flask(__name__, template_folder="template")


@app.route("/", methods=["GET"])
def base_html_get():
    # 根路径路由
    return render_template("index.html")
