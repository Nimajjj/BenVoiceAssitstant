from APIController.ModelApiMeteo import ModelApiMeteo
from APIController.ModelApiMusic import ModelApiMusic

class ApiController:
    def __init__(self, client_id=None, client_secret=None, redirect_url=None):
        if client_id and client_secret and redirect_url:
            self.modelApiMusic = ModelApiMusic(client_id, client_secret, redirect_url)
        elif client_id:  
            self.modelApiMeteo = ModelApiMeteo(client_id)
        else:
            raise ValueError("Invalid initialization parameters for ApiController")

    def get_temperature(self, ville):
        if not hasattr(self, 'modelApiMeteo'):
            raise AttributeError("This ApiController instance is not configured for weather API")
        data = self.modelApiMeteo.metheo(ville)
        if 'error' in data:
            return data['error']
        else:
            nom_ville = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f"La température à {nom_ville} est de {temperature}°C, {description}."

    def play_music(self, track_name):
        if not hasattr(self, 'modelApiMusic'):
            raise AttributeError("This ApiController instance is not configured for music API")
        return self.modelApiMusic.search_and_play(track_name)
