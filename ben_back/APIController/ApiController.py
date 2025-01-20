from ModelApiMeteo import ModelApiMeteo

class ApiController:
    def __init__(self, openWeatherMap_api_key):
        
        self.modelApiMeteo = ModelApiMeteo(openWeatherMap_api_key)

    
    def get_temperature(self, ville):

        data = self.modelApiMeteo.metheo(ville)
        if 'error' in data:
            return data['error']
        else:
            nom_ville = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f"La température à {nom_ville} est de {temperature}°C, {description}."