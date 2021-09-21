import logging

from economic.journals import Journal
from bkm_report.economic_api import EconomicApi


def test_economic_journal_entries(request):
    ec_bkm = EconomicApi(
        request.config.option.app_id,
        request.config.option.bkm_token
    )

    for journal_entry in ec_bkm.fetch_all_journal_entries():
        logging.debug(journal_entry)
