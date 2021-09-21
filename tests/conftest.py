from fixtures.auth import auth
from fixtures.journal_entry import customer_payment


def pytest_addoption(parser):
    parser.addoption('--app-id', action='store')
    parser.addoption('--bkm-token', action='store')
