from flask import Flask, render_template, request, jsonify
from scrap import scrap_data

from fetche_weather import weather

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def flask_app():

    new_data = scrap_data()
    return render_template('index.html', new_data=new_data)

@app.route("/weather")
def return_weather():
    args = request.args.get("city")

    #print("City : ", args)

    return jsonify(weather(args))



if __name__ == '__main__':
    app.run(debug=True)


    
