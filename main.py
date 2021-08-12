import pandas as pd

# Solution step-by-step
# Open the 6 excel files
# For each file: check if there is any value greater than R$55,000 (Sales column).
# If there is any value greater than R$55,000 -> Send an sms (Name, Month and sales amount).

# Technologies used: Python, openpyxl, pandas and twilio

list_months = ["January", "February", "March", "April", "May", "June"]

sales_table = pd.read_excel("./Excel spreadsheets/January.xlsx")

print(sales_table)