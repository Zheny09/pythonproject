# This is a sample Python script.
import os
from flask import Flask, render_template

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
