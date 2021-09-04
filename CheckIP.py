import json
import requests,sys


if len(sys.argv) < 2:
    print("Usage : python3 test.py IP ")


else:
    API_KEY = ""

    ip = sys.argv[1]
    if len(API_KEY) == 0:
        print("Import your API KEY")
    else:

        url = "https://ipqualityscore.com/api/json/ip/"+API_KEY+"/"+ip+"?strictness=2&fast=1"
        s = requests.Session()
        d = s.get(url)
        f = open("out.json","w+")
        f.write(d.text)
        f.close()

        f = open("res.html","w")
        f.write("<!DOCTYPE html>\r\n")
        f.write("<html lang='fr'>\r\n")
        f.write("<meta http-equiv=Content-Type content='text/html; charset=utf-8'/>\r\n")
        f.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">')
        f.write("<script src='extensions/resizable/bootstrap-table-resizable.js'></script>\r\n")
        f.write('<style>.table{ width : 50%; margin-left:auto; margin-right: auto }</style>\r\n')
        f.write("<script src=\"https://code.jquery.com/jquery-3.5.1.js\"></script>\r\n")
        f.write("<script>setInterval(function(){ $( '#table' ).load( 'res.html #table' );}, 2000);</script>\r\n")
    
        f.write("<h2 style=text-align:center>Check IP</h2>\r\n")
        with open('out.json') as json_file:
            data = json.load(json_file)
            fraud = data['fraud_score']
            country = data['country_code']
            tor = data['tor']
            bot = data['bot_status']
            isp = data['ISP']
            city = data['city']
            color_fraud = "green"

        message = ""
        if fraud < 40:
            message = "Low Risk"
        elif fraud >= 75 and fraud < 85:
            color_fraud = "orange"
            message = "Suspicious"    
        elif fraud >= 85:
            color_fraud = "red"          
            message = "High risk"

        print("Score Fraud : "+str(fraud)+ " Pays : "+ country+" IP Tor:  "+str(tor)+" Bot: "+str(bot)+" ISP: "+isp+" City: "+city)
        f.write("<div id='table'>\r\n")
        f.write("<table class='table table-striped' data-show-columns=true  data-show-toggle=true data-pagination=true  data-resizable='true'><thead><tr><th>IP</th><th style=text-align:center>"+ip+"</th></tr></thead>\r\n")
        f.write("<tbody><tr><td>Score Fraud</td><td style=color:"+color_fraud+";text-align:center>"+str(fraud)+" : "+message+"</td></tr>\r\n")
        f.write("<tr><td>Pays</td><td style=text-align:center>"+str(country)+"</td></tr>\r\n")
        f.write("<tr><td>Ville</td><td style=text-align:center>"+str(city)+"</td></tr>\r\n")
        f.write("<tr><td>ISP</td><td style=text-align:center>"+str(isp)+"</td></tr>\r\n")
        f.write("<tr><td>IP tor</td><td style=text-align:center>"+str(tor)+"</td></tr>\r\n")
        f.write("<tr><td>Bot</td><td style=text-align:center>"+str(bot)+"</td></tr></tbody></table></div>\r\n")
        f.write("</html>")
        f.close()
        print("Your results are in res.html file")   
