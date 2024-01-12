from constants.directions import Direction
from utils.input_interpreter import InputInterperter
from errors.input_exceptions import InvalidCoordInputException, InvalidDirectionException, InvalidStrAxisException, InvalidNumericAxisException

import pytest

interpreter = InputInterperter()


@pytest.mark.parametrize("test_input", [
    f'{letter}{number}' for letter in 'ABCDEFGHIJ' for number in range(1, 11)
])
def test_valid_coord_inputs(test_input):
    result = interpreter.coord_to_tuple(test_input)
    assert isinstance(result, tuple)

    a, b = result

    assert 0 <= a <= 9
    assert 0 <= b <= 9


@pytest.mark.parametrize("test_input, input_exception_type", [
    ('', InvalidCoordInputException),  # Empty string
    ('A', InvalidCoordInputException),  # Single letter
    ('A12', InvalidNumericAxisException),  # 12 is not a valid number
    ('A0', InvalidNumericAxisException),  # 0 is not a valid number
    ('K1', InvalidStrAxisException),  # K is not a valid letter
    ('1', InvalidCoordInputException),  # 1 is not a valid letter
    ('0', InvalidCoordInputException),  # 0 is not a valid letter
    ('10', InvalidStrAxisException),  # 10 is not a valid letter
    ('JF', InvalidNumericAxisException),  # JF is not a valid number axis
])
def test_invalid_coord_inputs(test_input, input_exception_type):
    with pytest.raises(input_exception_type):
        interpreter.coord_to_tuple(test_input)


@pytest.mark.parametrize("test_input, expected_result", [
    ('up', Direction.UP),
    ('down', Direction.DOWN),
    ('left', Direction.LEFT),
    ('right', Direction.RIGHT),
    ('Up', Direction.UP),
    ('Down', Direction.DOWN),
    ('Left', Direction.LEFT),
    ('Right', Direction.RIGHT),
    ('uP', Direction.UP),
    ('dOwn', Direction.DOWN),
    ('lEft', Direction.LEFT),
    ('rIght', Direction.RIGHT),
    ('UP', Direction.UP),
    ('DOWN', Direction.DOWN),
    ('LEFT', Direction.LEFT),
    ('RIGHT', Direction.RIGHT),
])
def test_valid_direction_inputs(test_input, expected_result):
    result = interpreter.get_direction(test_input)
    assert result == expected_result


@pytest.mark.parametrize("test_input", [
    'u', 'd', 'l', 'r', 'uppp', 'downnn', 'lefttt', 'righttt', 'UPPP', 'DOWNNN', 'LEFTTT', 'RIGHTTT',
])
def test_invalid_direction_inputs(test_input):
    with pytest.raises(InvalidDirectionException):
        interpreter.get_direction(test_input)
