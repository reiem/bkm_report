import logging
import os
from typing import Iterable

from _pytest.fixtures import SubRequest

from bkm_report.budget import load_all_budgets, load_budget


def test_load_budget(request: SubRequest):
    budget = load_budget('tests/assets/BKM-0.xlsx')
    assert isinstance(budget, Iterable)
    for entry in budget:
        assert isinstance(entry, dict)
        assert 'Nr.' in entry
        assert 'Navn' in entry
        assert '01/2021' in entry
        assert '02/2021' in entry
        assert '03/2021' in entry
        assert '04/2021' in entry
        assert '05/2021' in entry
        assert '05/2021' in entry
        assert '06/2021' in entry
        assert '07/2021' in entry
        assert '08/2021' in entry
        assert '09/2021' in entry
        assert '10/2021' in entry
        assert '11/2021' in entry
        assert '12/2021' in entry


def test_load_from_directory():
    budget_records = load_all_budgets(os.path.join('tests', 'assets'))
    assert isinstance(budget_records, Iterable)
    for entry in budget_records:
        assert 'Nr.' in entry
        assert 'Navn' in entry
        assert '01/2021' in entry
        assert '02/2021' in entry
        assert '03/2021' in entry
        assert '04/2021' in entry
        assert '05/2021' in entry
        assert '05/2021' in entry
        assert '06/2021' in entry
        assert '07/2021' in entry
        assert '08/2021' in entry
        assert '09/2021' in entry
        assert '10/2021' in entry
        assert '11/2021' in entry
        assert '12/2021' in entry
        assert 'org' in entry
        assert 'dep' in entry
