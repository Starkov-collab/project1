import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(not_16_digets_card):
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000792289606362") == "7000 79** **** 6362"
    assert get_mask_card_number("70007922896063") == not_16_digets_card
    assert get_mask_card_number("700079228960631212") == not_16_digets_card


def test_get_mask_card_number(not_isdigit_card) :
    assert get_mask_card_number("7000792FS289606361") == not_isdigit_card


def test_get_mask_account(not_20_digets_account):
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("73654108430135875") == not_20_digets_account
    assert get_mask_account("73654108430135874305122") == not_20_digets_account


def test_get_mask_account(not_isdigit_account):
    assert get_mask_account("7000792FS289606361") == not_isdigit_account












