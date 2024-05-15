import requests
from datetime import datetime

API_ID = "c8967cfa"
API_KEY = "a7d1ad092028323d50d34daf5852dcde"
sheet_Endpoint = "https://api.sheety.co/28c216e5910f1796dc27ae0cc9f28cf6/myWorkout/sheet1"

Headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

User_params = {
    "query": input("What workout did you do today: ")
}

Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=Endpoint,json=User_params,headers=Headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_Endpoint, json=sheet_inputs)

    print(sheet_response.text)

