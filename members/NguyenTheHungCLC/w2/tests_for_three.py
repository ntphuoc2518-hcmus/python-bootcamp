# Giả sử hàm W1-3 nằm ở module rules của bạn hoặc của đồng đội
from members.NguyenTheHungCLC.w1.rules import can_register_thesis, missing


def test_can_register_thesis_eligible():
    assert can_register_thesis(credits=120, gpa=2.0) is True

def test_can_register_thesis_ineligible_credits():
    assert can_register_thesis(credits=119, gpa=3.0) is False

def test_can_register_thesis_ineligible_gpa():
    assert can_register_thesis(credits=130, gpa=1.9) is False

def test_missing_reasons_both():
    reasons = missing(credits=110, gpa=1.8)
    assert len(reasons) == 2

def test_missing_reasons_none():
    reasons = missing(credits=125, gpa=2.5)
    assert len(reasons) == 0
