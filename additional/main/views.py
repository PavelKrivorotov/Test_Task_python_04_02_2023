from .models import RocketSQL, LaunchSQL, MissionSQL, make_insertion
from .shemas import Rocket, Launch, Mission, get_validated_data
from .utils import get_response

def create_content_view():
    raw = get_response()["data"]

    rockets = get_validated_data(Rocket, raw["rockets"])
    launces = get_validated_data(Launch, raw["launches"])
    missions = get_validated_data(Mission, raw["launches"])

    for rocket in rockets:
        make_insertion(RocketSQL, **rocket.dict())

    for launch in launces:
        data = launch.dict()
        make_insertion(
            LaunchSQL,
            id=data["id"],
            rocket_id = data["rocket"]["rocket"]["id"],
            details=data["details"]
        )

    for mission in missions:
        data = mission.dict()
        make_insertion(
            MissionSQL,
            id=data["mission_id"][0],
            launc_id=data["id"],
            name=data["mission_name"]
        )

    return None