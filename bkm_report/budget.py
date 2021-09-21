import logging
import os

import pandas as pd


def load_budget(filepath, faktor: float = 1_000):
    budget_records = []
    df = pd.read_excel(filepath).fillna(0)
    # df[df.drop(['Nr.', 'Navn'], axis=1).columns] *= faktor
    records = df.to_dict('records')
    yield from records


def load_all_budgets(dir_path):
    for filename in os.listdir(dir_path):
        if filename.endswith('.xlsx'):
            filepath = os.path.join(dir_path, filename)
            logging.info(f'Try to read budget from {filepath} ...')
            org, dep = org_dep_from_filename(filename)
            for record in load_budget(filepath):
                record['org'] = org
                record['dep'] = dep
                yield record


def org_dep_from_filename(filename):
    filename = filename.split('.')[0]  # throw away file extension
    return filename.split('-')
