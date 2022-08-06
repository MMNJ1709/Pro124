from flask import Flask,jsonify,request
app=Flask(__name__)

list = [
        {
        "id":1,
        "name":u"Rahul",
        "done":False,
        "contact":u"9876543210"
    },
    {
        "id":2,
        "name":u"Ram",
        "done":False,
        "contact":u"8735743519"
    }
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    contact={
        "id":list[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("contact",""),
        "done":False
    }
    list.append(contact)
    return jsonify({
        "status":"success","message":"contacts added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":list
    })
if(__name__=="__main__"):
    app.run(debug=True)