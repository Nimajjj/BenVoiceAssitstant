import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'APIController'))

from APIController.ApiController import ApiController

if __name__ == "__main__":

    openWeatherMap_api_key = "2cbb8b39d24e5e49337a16318e7529fc"
    client_id = "9e96419c81944bea8c3368f71732f9b6"
    client_secret = "dcaf997d5b864a0e96371db0a6645ea8"
    redirect_url = "http://localhost:3000"

    apiControllerMetheo = ApiController(openWeatherMap_api_key, None, None)
    apiControllerMusic = ApiController(client_id, client_secret, redirect_url)

    #ville = input("Entrez le nom d'une ville : ")

    #resultat = apiController.get_temperature(ville)

    #print(resultat)

    track_name = input("Entrez le nom d'une musique ou d'un artist : ")
    resultat = apiControllerMusic.play_music(track_name)
    print(resultat)
