from flask import Flask, jsonify, request

app = Flask(__name__)
print("SERVER IS RUNNING...")


@app.route("/returnjson", methods=["GET"])
def ReturnJSON():
    if request.method == "GET":
        data = {
            "Modules": 15,
            "Subject": "Data Structures and Algorithms",
        }

        return jsonify(data)


@app.route("/chat", methods=["GET"])
def chat():
    return jsonify({"a": 1, "b": 2})


if __name__ == "__main__":
    app.run(debug=True)
