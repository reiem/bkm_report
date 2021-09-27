
from bkm_report.balance_record import BalanceRecord
from typing import Iterable, List, Optional


class Balance:

    def __init__(self, records: Optional[Iterable[BalanceRecord]]):
        self._records = list(records)
        self._grouped_records = {}
        for r in self._records:
            if r.org not in self._grouped_records:
                self._grouped_records[r.org] = {}
            if r.account_number not in self._grouped_records[r.org]:
                self._grouped_records[r.org][r.account_number] = []
            self._grouped_records[r.org][r.account_number].append(r)

    @property
    def zero_check(self):
        return round(sum(r.amount for r in self._records), 2)
