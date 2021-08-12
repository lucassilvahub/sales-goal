import pandas as pd

# Solution step-by-step
# Open the 6 excel files
# For each file: check if there is any value greater than R$55,000 (Sales column).
# If there is any value greater than R$55,000 -> Send an sms (Name, Month and sales amount).

# Technologies used: Python, openpyxl, pandas and twilio

list_months = ["January", "February", "March", "April", "May", "June"]

for month in list_months:
    sales_table = pd.read_excel(f"./Excel spreadsheets/{month}.xlsx")
    if (sales_table['Sales'] > 55000).any():
        seller = sales_table.loc[sales_table['Sales'] > 55000, "Seller"]
        sales = sales_table.loc[sales_table['Sales'] > 55000, "Sales"]
        print(
            f"The seller {seller} reached the target of R$55000 in {month}, with R${sales} in sales")
