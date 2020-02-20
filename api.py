from flask import Flask,request,jsonify
from frequency_counter import word_counter


app = Flask(__name__)


@app.route("/api/get_frequency",methods=["POST"])
def get_frequency():
    """ Check Frequency of words using a posted value in json and return result in json """
    # Check if value is in json
    if request.is_json:
        content = request.get_json()
        if "text" in content:
            string = content["text"]
            if "sort" in content:
                besorted = content["sort"]
            else:
                besorted = 0
        else:
            return jsonify(message="Please supply a json with text as key and text to be analyzed as value"),400
        result = word_counter(string,besorted)
        return jsonify(result),200

    else:
        return jsonify(message="Please Send Your request in json"),400



app.run("0.0.0.0", debug=True)
