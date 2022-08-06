# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(qualifying_loans_list, csvpath):
        # Creating new file called "qualifying_loans.csv" in the data directory
    qualifying_loans_csv_path = Path(csvpath)

    # Write same header as "daily_rate_sheet.csv"
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    
    # Open "qualifying_loans.csv" with csv module in a write mode
    with open(qualifying_loans_csv_path,'w', newline='') as csv_translated_into_python_readable_data:

        # Create csvwriter
        csvwriter = csv.writer(csv_translated_into_python_readable_data)

        # With csvwriter created before, write header first
        csvwriter.writerow(header)

        # "qualifying_loans" is a list with multiple lists
        # Must use "for" loop to write each list independently
        for each_loan_information in qualifying_loans_list:
            csvwriter.writerow(each_loan_information)