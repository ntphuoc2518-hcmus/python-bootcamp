# Test someone else's code

def test_summary_rounds_median_to_two_decimals(load):
    g = load("w1", "grades")
    assert g.summary([1.111, 2.222])["median"] == 1.67

def test_summary_rounds_mean_to_two_decimals(load):
    g = load("w1", "grades")
    assert g.summary([1.111, 2.222])["mean"] == 1.67

# Test when all scores are equal.
def test_summary_all_scores_equal(load):
    g = load("w1", "grades")
    assert g.summary([7, 7, 7]) == {
        "min": 7,
        "max": 7,
        "mean": 7,
        "median": 7,
    }

# Test summary with integer and decimal scores.
def test_summary_mixed_scores(load):
    g = load("w1", "grades")
    assert g.summary([5, 6.5, 8]) == {
        "min": 5,
        "max": 8,
        "mean": 6.5,
        "median": 6.5,
    }

# Test summary when all scores are zero.
def test_summary_zero_scores(load):
    g = load("w1", "grades")
    assert g.summary([0, 0, 0]) == {
        "min": 0,
        "max": 0,
        "mean": 0,
        "median": 0,
    }