from economic.auth import Authentication
from economic.journals import Journal


class EconomicApi:

    def __init__(self, app_id, token):
        self._auth = Authentication(app_id, token)

    def fetch_all_journal_entries(self):
        for journal in Journal.all(self._auth):
            yield from journal.get_journal_entries()
