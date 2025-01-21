from APIController.ApiController import ApiController

if __name__ == "__main__":
    # Configuration des clés et paramètres
    openWeatherMap_api_key = "2cbb8b39d24e5e49337a16318e7529fc"
    client_id = "9e96419c81944bea8c3368f71732f9b6"
    client_secret = "dcaf997d5b864a0e96371db0a6645ea8"
    redirect_url = "http://localhost:3000"
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    email_address = "mail"
    email_password = "mdp"

    # Initialisation du contrôleur
    apiController = ApiController(
        openWeatherMap_api_key=openWeatherMap_api_key,
        client_id=client_id,
        client_secret=client_secret,
        redirect_url=redirect_url,
        smtp_server=smtp_server,
        smtp_port=smtp_port,
        email_address=email_address,
        email_password=email_password
    )

    # Test
    print("Options disponibles :")
    print("1. Meteo")
    print("2. Musique")
    print("3. Mail")
    choix = input("Choix : ")

    if choix == "1":
        ville = input("Entrez le nom d'une ville : ")
        print(apiController.get_temperature(ville))
    elif choix == "2":
        track_name = input("Entrez le nom d'une musique ou d'un artiste : ")
        print(apiController.play_music(track_name))
    elif choix == "3":
        destinataire = input("Mail du destinataire : ")
        objet = input("Objet du mail ")
        text = input("Contenu du mail ")
        print(apiController.send_email(destinataire, objet, text))
    else:
        print("Choix invalide.")
