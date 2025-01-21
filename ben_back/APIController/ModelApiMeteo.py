import requests
# Doc : https://openweathermap.org/guide

class ModelApiMeteo:
    def __init__(self, openWeatherMap_api_key, openWeatherMap_api_url = "http://api.openweathermap.org/data/2.5/weather" ):
        self.openWeatherMap_api_key = openWeatherMap_api_key
        self.openWeatherMap_api_url = openWeatherMap_api_url
    
    def metheo(self, ville, units="metric", lang="fr"):
        param = {
            "q": ville,  
            "appid": self.openWeatherMap_api_key,
            "units": units,
            "lang": lang
        }
        try:
            reponse = requests.get(self.openWeatherMap_api_url, params=param)
            reponse.raise_for_status()
            return reponse.json() 
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}