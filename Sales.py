#===================================================================================================
# Project: Retail Sales analytics System
# Module: Data Cleaning
# Database: Oracle
#====================================================================================================

import pandas as pd
import oracledb
import re

#====================================================================================================
#Database Connection
#===================================================================================================
try:
  conn = oracledb.connect(
    user = "dharshini",
    password = "Oracle@123",
    host="localhost",
    port= 1521,
    service_name= "XEPDB1"
  )
  print("Oracle Database Connected Successfully")

except Exception as e:
  print("Connection Failed")
  print(e)
  exit()


#==================================================================================================
# Reading Sales Table
#==================================================================================================

query = """
SELECT * FROM SALES 
"""
sales_df = pd.read_sql(query,conn)
print("\nOriginal Sales Data:\n")
print(sales_df)

#==================================================================================================
# Checking Missing values
#==================================================================================================
print("\nNumber of Missing Values:\n")
print(sales_df.isnull().sum())

#===================================================================================================
# Removing duplicates
#===================================================================================================
print("\nRemoving Duplicate Records:")
sales_df = sales_df.drop_duplicates(subset=['PRODUCT_ID'])
print(sales_df)

#==================================================================================================
# Cleaning PRODUCT_ID
#==================================================================================================
missing_product_id = sales_df[sales_df['PRODUCT_ID'].isnull()]
print("\nThe Missing Product_ID:\n",missing_product_id)
sales_df['PRODUCT_ID']=sales_df['PRODUCT_ID'].fillna(5)
print("\n The Cleaned Product_ID:\n",sales_df)

#==================================================================================================
# Cleaning SALE_DATE
#==================================================================================================
missing_sale_date = sales_df[sales_df['SALE_DATE'].isnull()]
print("\nThe Missing Sale_date:\n",missing_sale_date)
sales_df['SALE_DATE']=sales_df["SALE_DATE"].fillna(pd.Timestamp.today().normalize()) 
print("\nThe Cleaned Sale Date:\n",sales_df)

#================================================================================================
# Cleaning Customer_ID
#===============================================================================================
sales_df['CUSTOMER_ID']=sales_df['CUSTOMER_ID'].replace(999,104)
print("\nThe Cleaned Customer ID:\n",sales_df)
#==================================================================================================
# Cleaning Quantity
#==================================================================================================

sales_df["QUANTITY"]=sales_df["QUANTITY"].fillna(1)
print("\n The Cleaned Quantity:\n",sales_df)

#=================================================================================================
# Cleaning Amount
#=================================================================================================
sales_df['TOTAL_AMOUNT'] = sales_df['TOTAL_AMOUNT'].abs()
print("\nThe Cleaned Amount:\n",sales_df)

#==================================================================================================
# The Full Cleaned Sales Table
#===================================================================================================
print("\n The Cleaned Data:\n")
print(sales_df)

#==================================================================================================
# Converting to CSV file
#==================================================================================================
sales_df.to_csv("Sales_Clean.csv",index=False)

#===================================================================================================
# Checking Data Types
#===================================================================================================
print("\nData Types:\n",sales_df.dtypes)
sales_df.info()
#=================================================================================================
# Close Connection
#=================================================================================================
conn.close()
print("\nOracle Connection Closed\n")



