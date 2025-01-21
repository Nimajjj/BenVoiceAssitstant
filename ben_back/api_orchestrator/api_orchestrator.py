from APIController.ApiController import ApiController

from strategy.strategy import Action, Strategy

ERROR_UNKNOWN_ACTION = {
    "code": -1,
    "transcript": "Unknown action."
}

ERROR_API_NOT_IMPLEMENTED = {
    "code": -3,
    "transcript": "Something unexpected happened."
}

class APIOrchestrator:
    def __init__(self):
            # Configuration des clés et paramètres
        openWeatherMap_api_key = "2cbb8b39d24e5e49337a16318e7529fc"
        client_id = "d163ee9c9f96439e9a0374617bb38fcf"
        client_secret = "b7a1b3ada3074a228d96bcd9a1bb4fa9"
        redirect_url = "http://localhost:3000"
        smtp_server = "smtp.office365.com"
        smtp_port = 587
        email_address = "mail"
        email_password = "mdp"

        # Initialisation du contrôleur
        self.controller = ApiController(
            openWeatherMap_api_key=openWeatherMap_api_key,
            client_id=client_id,
            client_secret=client_secret,
            redirect_url=redirect_url,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            email_address=email_address,
            email_password=email_password
        )
        self.controller_weather = ApiController("2cbb8b39d24e5e49337a16318e7529fc", None, None)
        self.controller_music = ApiController("9e96419c81944bea8c3368f71732f9b6", "dcaf997d5b864a0e96371db0a6645ea8", "http://localhost:3000")


    def execute(self, strategy: Strategy) -> dict:
        if strategy.action == Action.QUIT:
            print(f"[ERROR] API {strategy.action.to_str()} not implemented yet")
            return ERROR_API_NOT_IMPLEMENTED

        if strategy.action == Action.WEATHER:
            result = self.controller.get_temperature(strategy.data["location"])
            return {
                "code": 0,
                "transcript": result
            }
        
        if strategy.action == Action.MUSIC:
            print(strategy)
            result = self.controller.play_music(strategy.data["song"])
            return {
                "code": 0,
                "transcript": result
            }

        if strategy.action == Action.EMAIL:
            print(f"[ERROR] API {strategy.action.to_str()} not implemented yet")
            return ERROR_API_NOT_IMPLEMENTED
        
        if strategy.action == Action.SEARCH:
            result: str = strategy.data["answer"]
            return {
                "code": 0,
                "transcript": result
            }

        return ERROR_UNKNOWN_ACTION