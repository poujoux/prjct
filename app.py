#from predict import EducateIt
from flask import Flask, request, render_template, jsonify
from modules.apisendai import sendai # relative imports from same package
from dotenv import load_dotenv



app = Flask(__name__, template_folder="templates")

@app.route("/")
def main():
    return render_template("index.html")



@app.route("/educateit", methods=["POST"])
def educate():
    imgs = request.files.getlist("efiles")
    name = request.form.get("name")

    if not imgs:
        return jsonify({"No images uploaded"}), 400

    if not name:
        return jsonify({"No plant name provided"}), 400


    """
    obj = EducateIt(imgs, name)
    result = obj.putfiles()
    
    if result == -1:
        return jsonify({"msg": "Error"}), 400
    """

    return jsonify({"msg": "Training completed"}), 200



@app.route("/predictit", methods=["POST"])
def predict():
    img = request.files.get("efiles")
    if not img:
        return jsonify({"No plant name provided"}), 400

    print("The image:", img, end="\n")

    """
    obj = EducateIt(img)
    Weather = obj.predict()
    """

    Weather = "sunny"

    load_dotenv()

    api_key = os.getenv("api_key")
    apikeym = os.getenv("mastodon_api_key")


    role = (
            """Put the sample above. Later explain which places will be {Weather}.
                Sample: 
                'The weather is {Weather}. (emoji)
                (explaining)'
                """
                )

    context = f"The weather today is: {Weather}"

    responseobj = sendai(api_key, 1.3, 60) #Creating the object
    result = responseobj.sendmessage(role, context)

    print("\n--- AI RESPONSE ---\n")
    print(result)

    print("Sending to Mastodon....")

    objp = sendpost(apikeym)
    returnei = objp.cppost(txtresult)

    print("its a: ", returnei.status_code) 

    text = f"The message has boen sended with the info of {Weather}"
                    
    return jsonify({"msg": text}), 200

if __name__ == "__main__":
    app.run(debug=True)
    
