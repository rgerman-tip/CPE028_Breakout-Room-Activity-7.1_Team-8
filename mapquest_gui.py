from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "AyRhfyHs9PM5gRGGoct61Xt40AyL9FiY"
def convertDistance(amount):
    #Meter to Miles
    return amount/1609 
dataType = 1
def conversionFunc(origin,dest,state):
    url = main_api + urllib.parse.urlencode({"key": key, "from":origin, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    temp = []
    if json_status == 0:
        if state != 'down':
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                temp.append(each["narrative"])
            x = "\n".join(temp)
            print(x)
            output = "API Status: " + str(json_status) + " = A successful route call.\n" + "Directions from " + (origin) + " to " + (dest) + "\n" + "Trip Duration: " + (json_data["route"]["formattedTime"]) + "\n" + "Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + "\n\nDIRECTION\n\n" + x
        else:
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                temp.append(each["narrative"])
            x = "\n".join(temp)
            output = "API Status: " + str(json_status) + " = A successful route call.\n" + "Directions from " + (origin) + " to " + (dest) + "\n" + "Trip Duration: " + (json_data["route"]["formattedTime"]) + "\n" + "Miles:      " + str("{:.2f}".format(convertDistance((json_data["route"]["distance"])*1.61))) + "\n\nDIRECTION\n\n" + x

    if json_status == 402: 
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

    return output


LabelBase.register(name = "Nunito", fn_regular= "BebasNeue-Regular.otf")
  
class MapQuest(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('main.kv')
        
    def calc(self,origin,destination,state):
        self.screen.ids.output.ids.textoutput.text =  conversionFunc(origin,destination,state)
    def build(self):
        return self.screen
    
if __name__ == '__main__':
    MapQuest().run()