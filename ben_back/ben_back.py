import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'APIController'))

from APIController.ApiController import ApiController
from APIController.ModelApiMeteo import ModelApiMeteo

if __name__ == "__main__":

    openWeatherMap_api_key = "2cbb8b39d24e5e49337a16318e7529fc"
    apiController = ApiController(openWeatherMap_api_key)

    ville = input("Entrez le nom d'une ville : ")

    resultat = apiController.get_temperature(ville)

    print(resultat)
