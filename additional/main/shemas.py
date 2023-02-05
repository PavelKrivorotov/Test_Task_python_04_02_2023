from pydantic import BaseModel, parse_obj_as


class Rocket(BaseModel):
    id: str
    name: str | None = None
    country: str |None = None
    company: str | None = None
    type: str | None = None


class Launch(BaseModel):
    id: str
    rocket: dict[str, dict] | None = None
    details: str | None = None


class Mission(BaseModel):
    mission_id: list[str] | None = None
    mission_name: str | None = None
    id: str | None = None


def get_validated_data(
        shema: Rocket | Launch | Mission,
        data: dict
    ) -> list[object] | None:

    return parse_obj_as(list[shema], data)