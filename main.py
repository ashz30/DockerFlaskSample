# This is a sample Python script.
from flask import Flask, jsonify
import os
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)

@app.route("/")
def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, Ashish')  # Press Ctrl+F8 to toggle the breakpoint.
    return jsonify('"name":"Ashish"')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
