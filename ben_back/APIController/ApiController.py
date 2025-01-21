from APIController.ModelApiMeteo import ModelApiMeteo
from APIController.ModelApiMusic import ModelApiMusic
from APIController.ModelApiMail import ModelApiMail

class ApiController:
    def __init__(self, openWeatherMap_api_key=None, client_id=None, client_secret=None, redirect_url=None, 
                 smtp_server=None, smtp_port=None, email_address=None, email_password=None):
        if openWeatherMap_api_key:
            self.modelApiMeteo = ModelApiMeteo(openWeatherMap_api_key)
        if client_id and client_secret and redirect_url:
            self.modelApiMusic = ModelApiMusic(client_id, client_secret, redirect_url)
        if smtp_server and smtp_port and email_address and email_password:
            self.modelApiMail = ModelApiMail(smtp_server, smtp_port, email_address, email_password)

    # Fonction pour avoir la météo
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

    # Fonction pour jouer de la musique
    def play_music(self, track_name):
        if not hasattr(self, 'modelApiMusic'):
            raise AttributeError("This ApiController instance is not configured for music API")
        return self.modelApiMusic.search_and_play(track_name)

    # Fonction pour l'envoie de mail
    def send_email(self, destinataire, subject, body):
        if not hasattr(self, 'modelApiMail'):
            raise AttributeError("This ApiController instance is not configured for mail API")
        return self.modelApiMail.send_email(destinataire, subject, body)
