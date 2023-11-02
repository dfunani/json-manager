from models.base import ResponseType
from models.base import DevCMS
from os import listdir, remove
from pytest import raises


def test_responsetype():
    assert ResponseType.error.value == 0
    assert ResponseType.success.value == 1


def test_write():
    dummy_data = {"name": "test", "surname": "test"}
    assert DevCMS.write(dummy_data, "dummy_data") == ResponseType.success
    assert "dummy_data.json" in listdir()
    remove("dummy_data.json")


def test_no_write():
    dummy_data = {"name": "test", "surname": "test"}
    assert DevCMS.write(dummy_data, "dummy_data*/?") == ResponseType.error


def test_getCollection():
    assert isinstance(DevCMS.getCollections("category"), dict)
    assert "data" in DevCMS.getCollections("category")
    assert "jsonapi" in DevCMS.getCollections("category")


def test_updateCollections():
    assert DevCMS.updateCollections("category") == ResponseType.success
    assert "category.json" in listdir()
    remove("category.json")
