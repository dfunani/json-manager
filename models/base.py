from requests import get, Response
from json import dump
from enum import Enum
from logging import error, info


class ResponseType(Enum):
    error = 0
    success = 1


class DevCMS:
    __CMSURL__ = "http://devcms.ayoba.me/jsonapi/15c1ad2ea0d3/taxonomy_term/"

    @staticmethod
    def write(object: dict, filename: str) -> ResponseType:
        try:
            with open(f"{filename}.json", "w") as file:
                dump(object, file)
            return ResponseType.success
        except BaseException as e:
            error(">>>>>>>>>>>>>>>>>>>>>>>> " + str(e))
            return ResponseType.error

    @staticmethod
    def updateCollections(endpoint: str) -> ResponseType:
        try:
            collection: dict = DevCMS.getCollections(endpoint)
            updatedCollection: list = list(
                map(
                    lambda x: {
                        "type": x.get("type"),
                        "id": x.get("id"),
                        "name": x.get("attributes").get("name"),
                    },
                    collection.get("data", []),
                )
            )
            return DevCMS.write({"updatedCollection": updatedCollection}, endpoint)
        except BaseException as e:
            error(">>>>>>>>>>>>>>>>>>>>>>>> " + str(e))
            return ResponseType.error

    @staticmethod
    def getCollections(endpoint: str) -> dict:
        info(f">>>>>>>>>>>>>>>>>>>>>>>> Fetching {endpoint.upper()} Collection")
        try:
            response: Response = get(f"{DevCMS.__CMSURL__}{endpoint}")
            return response.json()
        except BaseException as e:
            error(">>>>>>>>>>>>>>>>>>>>>>>> " + str(e))
            return {}
