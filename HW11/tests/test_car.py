class TestCar:

    def test_initialization(self, car_instance):
        assert car_instance.miles_limit == 100
        assert not car_instance._Car__is_engine_started

    def test_car_brand(self, car_instance, get_brand):
        assert car_instance._Car__brand == get_brand

    def test_car_model(self, car_instance, get_model):
        assert car_instance._Car__model == get_model

    def test_start_engine(self, car_instance):
        result = car_instance.start_engine()
        assert result == "Engine started."
        assert car_instance._Car__is_engine_started

    def test_start_engine_twice(self, car_instance):
        car_instance.start_engine()
        result = car_instance.start_engine()
        assert result == "Engine is already running."

    def test_stop_engine(self, car_instance):
        car_instance.start_engine()
        result = car_instance.stop_engine()
        assert result == "Engine stopped."
        assert not car_instance._Car__is_engine_started

    def test_stop_engine_when_already_off(self, car_instance):
        result = car_instance.stop_engine()
        assert result == "Engine is already off."

    def test_drive_when_engine_off(self, car_instance):
        result = car_instance.drive(50)
        assert result == "Cannot drive. Engine is off."
        assert car_instance.miles_limit == 100

    def test_drive_within_limit(self, car_instance):
        car_instance.start_engine()
        result = car_instance.drive(50)
        assert result == "Driving 50 miles."
        assert car_instance.miles_limit == 50

    def test_drive_exceeding_limit(self, car_instance):
        car_instance.start_engine()
        result = car_instance.drive(150)
        assert result == "The miles limit has been exceeded"
        assert car_instance.miles_limit == 100

    def test_drive_twice(self, car_instance):
        car_instance.start_engine()
        car_instance.drive(50)
        car_instance.stop_engine()

        car_instance.start_engine()
        result = car_instance.drive(50)
        assert result == "Driving 50 miles."
        assert car_instance.miles_limit == 0
