#!/bin/python3

import json
import urllib.request
import turtle
import time
import random

def consoleOutput():
#API wird wird nachgefragt und geladen
    url = 'http://api.open-notify.org/astros.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    
    print('People in Space: ', result['number'])
    people = result['people']
    for p in people:
        print(p['name'], 'in', p['craft'])
        
        
def getPosition():
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    print('Latitude', lat)
    print('Longitude', lon)
    
    return lon, lat
    

def createScreen() :

    screen = turtle.Screen()
    screen.setup(800, 400)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    screen.register_shape('iss.gif')
    iss= turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    
    iss.penup()
    iss.goto(getPosition())


def location() :
    #Buggingen / Malediven / Golf von Mexiko / Anchorage, Alaska / Falklandinseln / Sidney
    colors = ['yellow','ivory','lavenderblush','white','snow','lime','coral','gold','blue']
    lats = [47.8481234, 3.967374, 25.304304, 61.218056, -51.966642, -33.867487]
    lons = [7.6374895, 73.505465, -90.065918, -149.900284, -59.550039, 151.206990]
    
    i=0
    while i < len(lats) | len(lons):
        
        location = turtle.Turtle()
        location.penup()
        location.color(random.choice(colors))
        location.goto(lons[i], lats[i])
        location.dot(3)
        location.hideturtle()

        url = 'http://api.open-notify.org/iss-pass.json'
        url = url + '?lat=' + str(lats[i]) + '&lon=' + str(lons[i])
        response = urllib.request.urlopen(url)
        result = json.loads(response.read())
        over = result['response'][1]['risetime']
        #print(over)
        
        style = ('Arial', 9, 'bold')
        location.write(time.ctime(over), font=style)
        i+=1
    
consoleOutput()
createScreen()
location()

