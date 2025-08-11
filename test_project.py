import project

def test_average_speed():
    # Test a valid calculation
    assert project.average_speed('1:12.909', 3.337) == 164.71
    # Test with invalid input (should return None)
    assert project.average_speed('not a time', 3.337) is None

def test_is_valid_choice():
    # Test valid choices
    assert project.is_valid_choice('Monaco', project.CIRCUITS) == True
    assert project.is_valid_choice('Aggressive', project.STRATEGIES) == True

    # Test invalid choices
    assert project.is_valid_choice('Barcelona', project.CIRCUITS) == False
    assert project.is_valid_choice('Hello', project.STRATEGIES) == False