from app import main
from models.base import ResponseType
from os import listdir, remove


def test_category():
    assert main(["-c"]) == ResponseType.success
    assert "category.json" in listdir()
    remove("category.json")


def test_countries():
    assert main(["-C"]) == ResponseType.success
    assert "countries.json" in listdir()
    remove("countries.json")


def test_languages():
    assert main(["-l"]) == ResponseType.success
    assert "languages.json" in listdir()
    remove("languages.json")


def test_all():
    assert main(["-a"]) == ResponseType.success
    assert "languages.json" in listdir()
    assert "countries.json" in listdir()
    assert "category.json" in listdir()
    remove("languages.json")
    remove("countries.json")
    remove("category.json")


def test_multiple_flags():
    assert main(["-c", "-C", "-l"]) == ResponseType.success

    assert "category.json" in listdir()
    assert "countries.json" in listdir()
    assert "languages.json" in listdir()

    remove("languages.json")
    remove("countries.json")
    remove("category.json")
