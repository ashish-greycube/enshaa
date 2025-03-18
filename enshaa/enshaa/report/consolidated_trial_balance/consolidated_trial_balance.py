# Copyright (c) 2025, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from erpnext.accounts.report.trial_balance.trial_balance import execute as tb_execute
from frappe.utils import cint
import pandas as pd

amount_columns = [
    "debit",
    "credit",
    "opening_debit",
    "opening_credit",
    "closing_debit",
    "closing_credit",
]


def execute(filters=None):

    is_group = frappe.db.get_value("Company", filters.get("company"), "is_group")
    if not cint(is_group):
        columns, data = tb_execute(filters)
        return columns, data

    # execute Trial Balance for each company and sum values
    #
    # Note: all companies must have same rows (accounts)
    #
    columns, consolidated_data = tb_execute(filters)

    for d in frappe.db.get_list(
        "Company",
        filters={
            "parent_company": filters.get("company"),
        },
        pluck="name",
    ):
        filters["company"] = d
        columns, data = tb_execute(filters)
        if len(consolidated_data) == 1:
            consolidated_data = data
            continue

        for idx in range(len(consolidated_data)):
            account_name = consolidated_data[idx].get("account_name")
            if not account_name:
                continue
            for item in filter(lambda x: x.get("account_name") == account_name, data):
                for col in amount_columns:
                    if item.get(col):
                        consolidated_data[idx][col] = consolidated_data[idx].get(
                            col
                        ) + item.get(col)

    return columns, consolidated_data


# def get_consolidated(filters):

#     columns, consolidated_data, index = [], [], []
#     for d in frappe.db.get_list(
#         "Company",
#         filters={
#             "parent_company": filters.get("company"),
#         },
#         pluck="name",
#     ):
#         filters["company"] = d
#         columns, data = tb_execute(filters)
#         consolidated_data.append(data)
#         consolidated_data.append(data)
#         index = index or [x.get("account_name") for x in data]

#     frames = [pd.DataFrame(d) for d in consolidated_data]
#     df = pd.concat(frames)
#     df = df.fillna("")

#     totals = (
#         df.groupby(["account", "account_name", "has_value", "currency", "indent",])[
#             [
#                 "debit",
#                 "credit",
#                 "opening_debit",
#                 "opening_credit",
#                 "closing_debit",
#                 "closing_credit",
#             ]
#         ]
#         .sum()
#         .reset_index()
#     )
#     totals.set_axis(index)
#     print(index)
#     # print(totals.to_dict("records"))

#     # print("\n" * 5, consolidated_data)
#     return columns, totals.to_dict("records")