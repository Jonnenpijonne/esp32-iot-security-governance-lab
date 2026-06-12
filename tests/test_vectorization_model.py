from models.vectorization_model import FeatureInput, distance, vectorize


def test_vectorize_returns_expected_dimension():
    vector = vectorize(
        FeatureInput(
            battery_percent=90,
            temperature_c=21.5,
            humidity_percent=45.0,
            network_enabled=False,
            telemetry_enabled=False,
            ota_enabled=False,
            persistent_storage_enabled=False,
        )
    )
    assert vector.version == "feature-vector-v1"
    assert len(vector.values) == 7


def test_vector_values_are_normalized():
    vector = vectorize(
        FeatureInput(
            battery_percent=100,
            temperature_c=60.0,
            humidity_percent=100.0,
            network_enabled=True,
            telemetry_enabled=True,
            ota_enabled=True,
            persistent_storage_enabled=True,
        )
    )
    assert all(0.0 <= value <= 1.0 for value in vector.values)


def test_distance_between_same_vector_is_zero():
    first = vectorize(
        FeatureInput(90, 21.5, 45.0, False, False, False, False)
    )
    second = vectorize(
        FeatureInput(90, 21.5, 45.0, False, False, False, False)
    )
    assert distance(first, second) == 0.0
