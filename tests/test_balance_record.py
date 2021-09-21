import logging
from economic.journal_entries import JournalEntry
from bkm_report.balance_record import BalanceRecord


def test_can_make_record_from_customer_payment(customer_payment: JournalEntry):
    records = list(BalanceRecord.from_customer_payment('BKM', customer_payment))
    assert len(records) == 1
    record = records[0]
    assert hasattr(record, 'org')
    assert record.org == 'BKM'
    assert hasattr(record, 'department_id')
    assert hasattr(record, 'account_number')
    assert hasattr(record, 'date')
    assert hasattr(record, 'voucher_number')
    assert hasattr(record, 'origin_entry_type')
    assert hasattr(record, 'text')
    assert hasattr(record, 'amount')
    logging.info(record)
