import requests
from datetime import datetime
from pprint import pprint

APP_ID="0d97f1ed"
API_KEY="fbaae007dbb76e4b37424a7c324a409c"


headers={
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text=input("What did you do?")

body={
    "query": exercise_text,
    "weight_kg": 98,
    "height_cm": 185,
    "age": 23
}

response = requests.post(url=f"https://trackapi.nutritionix.com/v2/natural/exercise", data=body, headers=headers)

exercises = response.json()["exercises"]

GOOGLE_SHEET="https://api.sheety.co/dbcf9e222bbf35399b7bc1d5aa5daee0/workoutsLovro/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercises:
    pprint(exercise)
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    google_sheet_response = requests.post(url=f"{GOOGLE_SHEET}", json=sheet_inputs)
    pprint(google_sheet_response)


#print(google_sheet_response.json())