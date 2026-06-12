from models.interference_observation_model import InterferenceObservation, evaluate_interference


def test_interference_normal():
    observation = InterferenceObservation(
        observation_id="SYNTH-OBS-001",
        repeated_disconnects=False,
        unstable_power_observed=False,
        unexpected_device_seen=False,
        enclosure_opened=False,
        temperature_outside_band=False,
        manual_note_present=True,
    )
    result = evaluate_interference(observation)
    assert result.status == "NORMAL"
    assert result.score == 0


def test_interference_watch():
    observation = InterferenceObservation(
        observation_id="SYNTH-OBS-002",
        repeated_disconnects=True,
        unstable_power_observed=False,
        unexpected_device_seen=False,
        enclosure_opened=False,
        temperature_outside_band=False,
        manual_note_present=True,
    )
    result = evaluate_interference(observation)
    assert result.status == "WATCH"
    assert result.score == 20


def test_interference_escalate():
    observation = InterferenceObservation(
        observation_id="SYNTH-OBS-003",
        repeated_disconnects=True,
        unstable_power_observed=True,
        unexpected_device_seen=True,
        enclosure_opened=False,
        temperature_outside_band=False,
        manual_note_present=True,
    )
    result = evaluate_interference(observation)
    assert result.status == "ESCALATE"
    assert result.score == 60
