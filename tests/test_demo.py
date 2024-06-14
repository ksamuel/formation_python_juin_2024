import json

import pytest
from mockito import mock

from mon_package.ma_lib import count, get_dog_pic, get_words, requests


@pytest.fixture
def toto():
    print("Executé avant le test")
    yield "Passé au test"
    print("Executé après le test")


def test_get_words(toto):
    print(toto)
    result = get_words("Ceci est un texte!")
    expected_result = ["ceci", "est", "un", "texte"]
    assert result == expected_result

    result = get_words(" Ceci est Un , texte!")
    expected_result = ["ceci", "est", "un", "texte"]
    assert result == expected_result


def test_count(toto):
    assert count(["ceci", "est", "un", "texte"]) == {
        "ceci": 1,
        "est": 1,
        "un": 1,
        "texte": 1,
    }

    assert count(["a", "a", "aaa", "a"]) == {
        "a": 3,
        "aaa": 1,
    }


def test_get_dog_pic(when):
    data = {
        "message": "https://images.dog.ceo/breeds/schnauzer-giant/n02097130_864.jpg",
        "status": "success",
    }

    when(requests).get("https://dog.ceo/api/breeds/image/random").thenReturn(
        mock({"status_code": 200, "content": json.dumps(data), "json": lambda: data})
    )

    assert get_dog_pic() == {
        "message": "https://images.dog.ceo/breeds/schnauzer-giant/n02097130_864.jpg",
        "status": "success",
    }
