from bkm_report.balance import Balance
import logging
from economic.journals import Journal
from conf import DEFAULT_DEBITOR_ACCOUNT
from economic.journal_entries import JournalEntry
from bkm_report.balance_record import BalanceRecord


def test_can_make_record_from_customer_payment(customer_payment: JournalEntry):
    records = list(BalanceRecord.from_customer_payment('BKM', customer_payment))
    assert len(records) == 2
    record = records[0]
    assert hasattr(record, 'org')
    assert record.org == 'BKM'
    assert hasattr(record, 'department_id')
    assert record.department_id == customer_payment.departmental_distribution['departmentalDistributionNumber']
    assert hasattr(record, 'account_number')
    assert record.account_number == DEFAULT_DEBITOR_ACCOUNT
    assert hasattr(record, 'date')
    assert record.date == customer_payment.date
    assert hasattr(record, 'voucher_number')
    assert record.voucher_number == customer_payment.voucher['voucherNumber']
    assert hasattr(record, 'origin_entry_type')
    assert record.origin_entry_type == customer_payment.entry_type
    assert hasattr(record, 'text')
    assert record.text == customer_payment.text
    assert hasattr(record, 'amount')
    assert record.amount == customer_payment.amount

    record = records[1]
    assert hasattr(record, 'org')
    assert record.org == 'BKM'
    assert hasattr(record, 'department_id')
    assert record.department_id == customer_payment.departmental_distribution['departmentalDistributionNumber']
    assert hasattr(record, 'account_number')
    assert record.account_number == customer_payment.contra_account['accountNumber']
    assert hasattr(record, 'date')
    assert record.date == customer_payment.date
    assert hasattr(record, 'voucher_number')
    assert record.voucher_number == customer_payment.voucher['voucherNumber']
    assert hasattr(record, 'origin_entry_type')
    assert record.origin_entry_type == customer_payment.entry_type
    assert hasattr(record, 'text')
    assert record.text == customer_payment.text
    assert hasattr(record, 'amount')
    assert record.amount == -customer_payment.amount


def record_generator(auth):
    for journal in Journal.all(auth):
        for entry in journal.get_journal_entries():
            yield from BalanceRecord.from_journal_entry('BKM', entry)


def test_can_make_records_from_fetched_journal_entries(auth):
    for record in record_generator(auth):
        assert hasattr(record, 'org')
        assert hasattr(record, 'department_id')
        assert hasattr(record, 'account_number')
        assert hasattr(record, 'date')
        assert hasattr(record, 'voucher_number')
        assert hasattr(record, 'origin_entry_type')
        assert hasattr(record, 'text')
        assert hasattr(record, 'amount')
        logging.info(record)


def test_can_make_balance_from_fetched_journal_entries(auth):
    balance = Balance(record_generator(auth))
    assert balance.zero_check == 0
