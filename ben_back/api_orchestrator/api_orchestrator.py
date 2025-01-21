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
        self.controller_weather = ApiController("2cbb8b39d24e5e49337a16318e7529fc", None, None)
        self.controller_music = ApiController("9e96419c81944bea8c3368f71732f9b6", "dcaf997d5b864a0e96371db0a6645ea8", "http://localhost:3000")


    def execute(self, strategy: Strategy) -> dict:
        if strategy.action == Action.QUIT:
            print(f"[ERROR] API {strategy.action.to_str()} not implemented yet")
            return ERROR_API_NOT_IMPLEMENTED

        if strategy.action == Action.WEATHER:
            result = self.controller_weather.get_temperature(strategy.data["location"])
            return {
                "code": 0,
                "transcript": result
            }
        
        if strategy.action == Action.MUSIC:
            print(f"[ERROR] API {strategy.action.to_str()} not implemented yet")
            result = self.controller_music.play_music(strategy.data["song"])
            return {
                "code": 0,
                "transcript": result
            }

        if strategy.action == Action.EMAIL:
            print(f"[ERROR] API {strategy.action.to_str()} not implemented yet")
            return ERROR_API_NOT_IMPLEMENTED
        
        if strategy.action == Action.SEARCH:
            print(f"[ERROR] API {strategy.action.to_str()} not implemented yet")
            return ERROR_API_NOT_IMPLEMENTED

        return ERROR_UNKNOWN_ACTION