import requests

class Weather:

    def get_weather(self):

        try:

            url = "https://wttr.in/Chennai?format=j1"

            response = requests.get(url)

            if response.status_code == 404:
                print("Error: City not found")
                return

            response.raise_for_status()

            data = response.json()

            temperature = data["current_condition"][0]["temp_C"]
            condition = data["current_condition"][0]["weatherDesc"][0]["value"]

            print("Weather Report")
            print("----------------")
            print(f"Temperature : {temperature}°C")
            print(f"Condition   : {condition}")

        except requests.exceptions.ConnectionError:
            print("Network Error")

        except requests.exceptions.RequestException as e:
            print("API Error:", e)


weather = Weather()

weather.get_weather()