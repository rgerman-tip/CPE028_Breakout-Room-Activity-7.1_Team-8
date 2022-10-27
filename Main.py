import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "AyRhfyHs9PM5gRGGoct61Xt40AyL9FiY"
def convertDistance(amount):
    #Meter to Miles
    return amount/1609 
dataType = 1

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    dataType = input("[1] Meters or \n[2] Miles: ")
    if dataType == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]


    if json_status == 0:
        if dataType == 1:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
            print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
            #Added information
            print("Mode of Transportation: " + (json_data["route"]["legs"][0]["maneuvers"][0]["transportMode"]))
            print("=============================================")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) +"    km)"))
            print("=============================================\n")
        else:
            print("API Status: " + str(json_status) + " = A successful route call.\n")
            print("=============================================")
            print("Directions from " + (orig) + " to " + (dest))
            print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
            print("Miles:      " + str("{:.2f}".format(convertDistance((json_data["route"]["distance"])*1.61))))
            print("=============================================")
            for each in json_data["route"]["legs"][0]["maneuvers"]:
                print((each["narrative"]) + " (" + str("{:.2f}".format(convertDistance((each["distance"])*1.61) +"    km)")))
            print("=============================================\n")

           
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


