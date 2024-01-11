import pandas as pd

df_data = {"Name": ["Praveen", "Pratik", "Yashwanth"], "Height": ["5'11", "5'10", "5'11"],"Qualifications": ["Engineering", "Medicine", "Law"]}

new_df = pd.DataFrame(df_data)
print(new_df)
print()
address_data = ["Hyderabad", "Qatar", "Mumbai"]
new_df["Address"] = address_data
print(new_df)