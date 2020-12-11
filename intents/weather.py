from intents.library.df_msg_library import df_rich_responses
import json
import re
import sys
import requests
from flask import request, jsonify, Flask
from flask_simple_geoip import SimpleGeoIP
class weather():
    def getWeather(self,city):
        # print(city, file=sys.stderr)
        app = Flask(__name__)
        # https://ip-geolocation.whoisxmlapi.com/api/v1?apiKey=at_NMWXoFS2X4fDSmp2HrONG0vJRc5yi&ipAddress=8.8.8.8
        # app.config.update(GEOIPIFY_API_KEY='at_NMWXoFS2X4fDSmp2HrONG0vJRc5yi')
        # simple_geoip = SimpleGeoIP(app)
        
        url = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid=f99d6de2f556d78aa3ddc2bc03bc07fa'.format(city)
        # print(url)
        resp = requests.get(url).json()
        # print(resp)
        table_html = "<table border=1>"
        
        table_html += "<tr>" +\
                    "<th> Date and Time </th> " +\
                    "<th> Weather </th> " +\
                    "<th> Temperature </th> " +\
                    "<th> Pressure </th> " +\
                    "<th> Humidity </th> " +\
                    "</tr>"
        for c in resp["list"]:
            table_html += "<tr>" +\
                    "<td>" + c['dt_txt'] + "</td> " +\
                    "<td>" + c['weather'][0]['description']  +"</td> " +\
                    "<td>" + str(c['main']['temp']) + " </td> " +\
                    "<td>" + str(c['main']['pressure']) + " </td> " +\
                    "<td>" + str(c['main']['humidity']) + " </td> " +\
                    "</tr>"
           
        table_html += "</table>"
            
        lib = df_rich_responses()
        response = []
        table_response = lib.simple_accordion_response( table_html, "weather")
        # print(table_response)
        return lib.fulfillment_messages("Here is your Weather Forcast", [[table_response]])      