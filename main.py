from flask import Flask, request, make_response, jsonify, render_template
from datetime import datetime, timedelta
# from intents.soil_image import SoilImage
# from intents.show_crops import show_crops
from intents.weather import weather
import sys
import requests
from flask_simple_geoip import SimpleGeoIP
# initialize the flask app
app = Flask(__name__)
# default route
@app.route("/")
def index():
    return render_template("index.html")
# function for responses
def get_data():
    # build a request object
    req = request.get_json(force=True)
    print(req)
    # fetch action from json
    action = req.get('queryResult').get('action')
    # print('inside get data',file=sys.stderr)
    # image = ""
    # # if action == 'examine_soil_intent':
    # #     # print('inside examine soil',file=sys.stderr)
    # #     soilImage = SoilImage()
    # #     return soilImage.getImage(image)
    # # if action =='prediction_intent':
    # #     crops = show_crops()
    # #     return crops.prediction_summary(image)
    if action == 'weather':
        
        city = req['queryResult']['parameters']['city']
        print('request city: ',city)
        if city=='':
            if request.headers.getlist("X-Forwarded-For"):
                ip = request.headers.getlist("X-Forwarded-For")[0]
            else:
                ip = request.remote_addr
            geoip_data = requests.get('https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_mCfH3JRobVAsECzu4Uedqoby2ezZz&ipAddress='+ip).json() # simple_geoip.get_geoip_data()
            city = (geoip_data)['location']['city']
            print('ip: ',request.environ['REMOTE_ADDR'])
            print('city: ',city)
        wthr = weather()
        return wthr.getWeather(city)
# create a route for webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # return response
    # print('inside webhook',file=sys.stderr)
    print(get_data(), file=sys.stderr)
    return make_response(jsonify(get_data()))
if __name__ == '__main__':
    app.run(port=5000, debug=True)
