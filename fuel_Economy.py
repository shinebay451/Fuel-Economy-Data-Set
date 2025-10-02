import pandas as pd



file = r"C:\Users\Shiny\OneDrive\Desktop\Honda Data sets\25data\20250814 MY25 ICE,EV,PHEV For DOE R2public.xlsx"

df = pd.read_excel(file)


##print(df.head())
##print(df.columns.tolist())

print("Rows:", df.shape[0], "Columns:", df.shape[1])

columns_GPM = ['Model Year', 'Mfr Name', 'City FE (Guide) - Conventional Fuel', 'Comb FE (Guide) - Conventional Fuel',
               'Hwy FE (Guide) - Conventional Fuel' ]

smaller_df = df[columns_GPM]

smaller_df = smaller_df.rename(columns={
    'Model Year': 'ModelYear',
    'Mfr Name': 'Mfr',
    'City FE (Guide) - Conventional Fuel': 'City FE',
    'Comb FE (Guide) - Conventional Fuel': 'Cob FE',
    'Hwy FE (Guide) - Conventional Fuel': 'Hwy FE'

})

smaller_df = smaller_df[smaller_df['Mfr'].str.contains('Honda', case=False, na=False)]


print(smaller_df.head(868))

smaller_df.to_csv("cleaned_honda_mpg.csv", index=False)
