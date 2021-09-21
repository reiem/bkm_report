import pytest

from economic.journal_entries import JournalEntry


@pytest.fixture
def customer_payment(auth):
    return JournalEntry(auth, {
        'customer': {
            'customerNumber': 92,
            'self': 'https://restapi.e-conomic.com/customers/92'
        },
        'customerInvoice': 481,
        'text': 'Husleje januar',
        'journal': {
            'journalNumber': 1,
            'self': 'https://restapi.e-conomic.com/journals-experimental/1'
        },
        'amount': -2300.0,
        'contraAccount': {
            'accountNumber': 6750,
            'self': 'https://restapi.e-conomic.com/accounts/6750'
        },
        'currency': {
            'code': 'DKK',
            'self': 'https://restapi.e-conomic.com/currencies/DKK'
        },
        'date': '2021-01-04',
        'exchangeRate': 100.0,
        'entryType': 'customerPayment',
        'voucher': {
            'accountingYear': {
                'year': '2021',
                'self': 'https://restapi.e-conomic.com/accounting-years/2021'
            },
            'voucherNumber': 19,
            'attachment': 'https://restapi.e-conomic.com/journals-experimental/1/vouchers/2021-19/attachment',
            'self': 'https://restapi.e-conomic.com/journals-experimental/1/vouchers/2021-19'
        },
        'departmentalDistribution': {
            'departmentalDistributionNumber': 120,
            'distributionType': 'department',
            'self': 'https://restapi.e-conomic.com/departmental-distributions/departments/120'
        },
        'amountDefaultCurrency': -2300.0,
        'remainder': -2300.0,
        'remainderDefaultCurrency': -2300.0,
        'journalEntryNumber': 3,
        'metaData': {
            'delete': {
                'description': 'Delete this entry.',
                'href': 'https://restapi.e-conomic.com/journals-experimental/1/entries/3',
                'httpMethod': 'delete'
            }
        },
        'self': 'https://restapi.e-conomic.com/journals-experimental/1/entries/3'
    })
