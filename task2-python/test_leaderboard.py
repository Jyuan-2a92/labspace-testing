import pytest
from leaderboard import Leaderboard


def test_add_player():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert len(lb) == 1


def test_add_player_with_initial_score():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    assert lb.get_top_n(1) == [("Alice", 500)]

    with pytest.raises(ValueError):
        lb.add_player("Alibe", initial_score=-1)
    with pytest.raises(ValueError):
        lb.add_player("Alice", initial_score=500)


def test_record_match_updates_scores():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    lb.record_match("Alice", "Bob")
    assert lb.get_top_n(2) == [("Alice", 110), ("Bob", 90)]

    with pytest.raises(KeyError):
        lb.record_match("a","b")
    with pytest.raises(KeyError):
        lb.record_match("Alice", "b")
    with pytest.raises(ValueError):
        lb.record_match("Alice", "Bob", -10)


def test_get_rank():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.add_player("Carol", 200)
    assert lb.get_rank("Alice") == 1
    assert lb.get_rank("Carol") == 2
    assert lb.get_rank("Bob") == 3

    with pytest.raises(KeyError):
        lb.get_rank("a")

def test_get_top():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    with pytest.raises(ValueError):
        lb.get_top_n(-1)

def test_get_percentile():
    lb = Leaderboard()
    lb.add_player("Alice", 300)

    with pytest.raises(KeyError):
        lb.get_percentile("c")
    assert lb.get_percentile("Alice") == 100.0

    lb.add_player("Bob", 100)
    assert lb.get_percentile("Bob") == 0

def test_apply_bonus():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    with pytest.raises(KeyError):
        lb.apply_bonus("c",1.1)
    with pytest.raises(ValueError):
        lb.apply_bonus("Alice", -1.1)
    lb.add_player("b", 301)
    lb.apply_bonus("Alice", 2)
    assert lb.get_top_n(1) == [("Alice", 600)]

def test_get_win_rate():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.record_match("Alice", "Bob")
    with pytest.raises(KeyError):
        lb.get_win_rate("c")
    assert lb.get_win_rate("Alice") == 1.0

def test_reset():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    assert lb.__len__ != 0
    lb.reset()
    with pytest.raises(KeyError):
        lb.get_percentile("Alice")
