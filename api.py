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
                to_sort = content["sort"]
            else:
                to_sort = 0
        else:
            return jsonify(message="Please supply a json with text as key and text to be analyzed as value"),400
        client_ip = request.environ.get("HTTP_X_FORWARDED_FOR")
        loadbalancer_ip = request.environ.get("REMOTE_ADDR")
        worker_ip = request.environ.get("HTTP_HOST")
        result = word_counter(string,to_sort)
        return jsonify(result,{"Client_IP":client_ip,"Loadbalancer_IP":loadbalancer_ip,"Worker_IP":worker_ip}),200

    else:
        return jsonify(message="Please Send Your request in json"),400



app.run("0.0.0.0", debug=True,threaded=True)
