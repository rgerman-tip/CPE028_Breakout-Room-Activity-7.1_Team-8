import urllib.parse
import requests

# Accessing the API with a key
main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "AyRhfyHs9PM5gRGGoct61Xt40AyL9FiY"

def conversionFunc(origin,dest,state):
    url = main_api + urllib.parse.urlencode({"key": key, "from":origin, "to":dest})
    print("URL: " + (url))
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

print(conversionFunc("Marikina","Caloocan","normal"))