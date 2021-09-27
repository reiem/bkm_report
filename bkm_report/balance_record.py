from dataclasses import dataclass
from datetime import date
from logging import StringTemplateStyle
from typing import Generator, TypeVar

from economic.journal_entries import JournalEntry


def get_department_from_journal_entry(entry: JournalEntry):
    if 'departmental_distribution' in entry.valid_fields and \
            'departmentalDistributionNumber' in entry.departmental_distribution:
        return entry.departmental_distribution['departmentalDistributionNumber']
    return 0


def voucher_numner_from_entry(entry: JournalEntry):
    if 'voucher_number' in entry.valid_fields:
        return entry.voucher_number
    if 'voucher' in entry.valid_fields and 'voucherNumber' in entry.voucher:
        return entry.voucher['voucherNumber']
    return None


DEFAULT_DEBITOR_ACCOUNT = 5600


BalanceRecordType = TypeVar('BalanceRecordType', bound='BalanceRecord')


@dataclass
class BalanceRecord:
    org: str
    department_id: int
    account_number: int
    date: str
    origin_entry_type: str
    text: str
    amount: float
    voucher_number: int

    @classmethod
    def from_journal_entry(cls, org, entry: JournalEntry) -> Generator[BalanceRecordType, None, None]:
        if entry.entry_type == 'customerPayment':
            yield from cls.from_customer_payment(org, entry)
        elif entry.entry_type == 'financeVoucher':
            yield from cls.from_finance_voucher(org, entry)
        else:
            raise ValueError(f'Cannot translate journal entry of type `{entry.entry_type}` to instance of `BalanceRecord`')

    @classmethod
    def from_customer_payment(cls, org, entry: JournalEntry) -> Generator[BalanceRecordType, None, None]:
        assert entry.entry_type == 'customerPayment'
        yield cls(
            org=org,
            department_id=get_department_from_journal_entry(entry),
            account_number=DEFAULT_DEBITOR_ACCOUNT,
            date=entry.date,
            origin_entry_type=entry.entry_type,
            text=entry.text,
            amount=entry.amount,
            voucher_number=voucher_numner_from_entry(entry)
        )
        if hasattr(entry, 'contra_account'):
            yield cls(
                org=org,
                department_id=get_department_from_journal_entry(entry),
                account_number=entry.contra_account['accountNumber'],
                date=entry.date,
                origin_entry_type=entry.entry_type,
                text=entry.text,
                amount=-entry.amount,
                voucher_number=voucher_numner_from_entry(entry),
            )

    @classmethod
    def from_finance_voucher(cls, org, entry: JournalEntry) -> Generator[BalanceRecordType, None, None]:
        assert entry.entry_type == 'financeVoucher'
        yield cls(
            org=org,
            department_id=get_department_from_journal_entry(entry),
            account_number=DEFAULT_DEBITOR_ACCOUNT,
            date=entry.date,
            origin_entry_type=entry.entry_type,
            text=entry.text,
            amount=entry.amount,
            voucher_number=voucher_numner_from_entry(entry)
        )
        if 'contra_account' in entry.valid_fields:
            yield cls(
                org=org,
                department_id=get_department_from_journal_entry(entry),
                account_number=entry.contra_account['accountNumber'],
                date=entry.date,
                origin_entry_type=entry.entry_type,
                text=entry.text,
                amount=-entry.amount,
                voucher_number=voucher_numner_from_entry(entry),
            )