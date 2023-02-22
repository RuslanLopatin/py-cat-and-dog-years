
from app.main import get_human_age


def test_get_human_age() -> None:
    assert get_human_age(0, 0) == [0, 0]

    assert get_human_age(14, 14) == [0, 0]

    assert get_human_age(15, 15) == [1, 1]

    assert get_human_age(23, 23) == [1, 1]

    assert get_human_age(24, 24) == [2, 2]

    assert get_human_age(27, 27) == [2, 2]

    assert get_human_age(28, 20) == [3, 2]

    assert get_human_age(100, 100) == [21, 17]

    assert get_human_age(-5, 0) == [0, 0]

    assert get_human_age(0, 0) == [0, 0]

    assert get_human_age(100000, 0) == [2129, 0]

    assert get_human_age(100000, 1) == [2130, 1]

    try:
        get_human_age(2.5, 5)
    except TypeError as e:
        assert str(e) == "Animal age should be an integer"

    try:
        get_human_age("cat", "dog")
    except TypeError as e:
        assert str(e) == "Animal age should be an integer"

    try:
        get_human_age(5, "dog")
    except TypeError as e:
        assert str(e) == "Animal age should be an integer"
