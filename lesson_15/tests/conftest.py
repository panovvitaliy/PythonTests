import pytest
from lesson_15.car import Car


@pytest.fixture
def get_brand():
    return 'Toyota'


@pytest.fixture
def get_model():
    return 'Camry 3.5'


@pytest.fixture
def car_instance(get_brand, get_model):
    return Car(get_brand, get_model, 100)
