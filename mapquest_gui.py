from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.text import LabelBase
import urllib.parse
import requests
from datetime import datetime

# Accessing the API with a key
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "AyRhfyHs9PM5gRGGoct61Xt40AyL9FiY"


# Conversion Function Based On The Lab Activity MapQuest 7.1
def conversionFunc(origin,dest,state):
    url = main_api + urllib.parse.urlencode({"key": key, "from":origin, "to":dest})
    # print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    temp = []
    if json_status == 0: 
        if state != 'down':  # output if the checkbox is not clicked
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                temp.append(each["narrative"])
            x = "\n".join(temp)
            print(x)
            output = "API Status:    " + str(json_status) + " A successful route call.\n" + "Directions from " + (origin) + " to " + (dest) + "\n" + "Trip Duration:     " + (json_data["route"]["formattedTime"]) + "\n" + "Kilometers:    " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + "\n\nDIRECTION\n\n" + x
        else: # output if the checkbox is not clicked
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                temp.append(each["narrative"])
            x = "\n".join(temp)
            output = "API Status:    " + str(json_status) + " A successful route call.\n" + "Directions from " + (origin) + " to " + (dest) + "\n" + "Trip Duration:     " + (json_data["route"]["formattedTime"]) + "\n" + "Miles:    " + str("{:.2f}".format((json_data["route"]["distance"]))) + "\n\nDIRECTION\n\n" + x

    elif json_status == 402: # output if status 402
        output = "Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations."
    elif json_status == 611: # output if status 611
        output = "Status Code: " + str(json_status) + "; Missing an entry for one or both locations."
    else: # output if not found
        output = "For Staus Code: " + str(json_status) + "; Refer to: \n" + "https://developer.mapquest.com/documentation/directions-api/status-codes"
    return output


LabelBase.register(name = "Nunito", fn_regular= "BebasNeue-Regular.otf")

class MapQuest(MDApp): # Kivy Main Class For The GUI
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('main.kv')
        self.read_object = open('LOGS.txt', 'r')
        self.logs = self.read_object.read()
        self.read_object2 = open('recent.txt', 'r')
        self.recentlist = self.read_object2.read()
        
    def calc(self,origin,destination,state):
        self.screen.ids.output.ids.textoutput.text = conversionFunc(origin,destination,state)
        # Grabing the inputs from the text fields
    
    def log(self,message):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        file_object = open('LOGS.txt', 'a')
        file_object.write(f"{dt_string} {message}\n")
    
    def openLogs(self):
        self.read_object = open('LOGS.txt', 'r')
        self.logs = self.read_object.read()
        self.screen.ids.logs.ids.logs.text = self.logs
    
    def recent(self,o,d):
        file_object = open('recent.txt', 'a')
        if d != '' and o != '':
            file_object.write(f"{o} To {d}\n")
    
    def history(self):
        self.read_object2 = open('recent.txt', 'r')
        self.recentlist = self.read_object2.read()
        self.screen.ids.recent.ids.recent.text = self.recentlist
    
    def clear(self):
        self.screen.ids.front.ids.Destination.text = ""
        self.screen.ids.front.ids.Origin.text = ""

    def build(self):
        return self.screen
    
if __name__ == '__main__':
    MapQuest().run() # Running the main app