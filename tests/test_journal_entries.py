import logging
from typing import List

from economic.journals import Journal
from economic.journal_entries import JournalEntry


def test_fetch_journal_entries(auth):
    journal_entries: List[JournalEntry] = []
    journals = Journal.all(auth)
    for journal in journals:
        _journal_entries = list(journal.get_journal_entries())
        journal_entries.extend(_journal_entries)
    logging.debug(journal_entries)
