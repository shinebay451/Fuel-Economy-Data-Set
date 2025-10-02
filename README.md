# Fuel-Economy-Data-Set

**Firstly save your data sheet**
`file = r"C:\Users\Shiny\OneDrive\Desktop\Honda Data sets\25data\20250814 MY25 ICE,EV,PHEV For DOE R2public.xlsx"`

## Now read data and load it into the DataFrame.

`df = pd.read_excel(file)`
This tell's you how much rows and columns the data contain. shape[0] is rows and shape[1] is columns.
`print("Rows:", df.shape[0], "Columns:", df.shape[1])`
![image](https://github.com/user-attachments/assets/d8186ab1-d279-44a2-a9ad-e47e4181c1e1)
## Next step Choose the columns you wish to work with.
`columns_GPM = ['Model Year', 'Mfr Name', 'City FE (Guide) - Conventional Fuel', 'Comb FE (Guide) - Conventional Fuel',
               'Hwy FE (Guide) - Conventional Fuel' ]`

and store it inside a new dataframe that is little bit smaller you know what it's way smaller.

`smaller_df = df[columns_GPM]`
![image](https://github.com/user-attachments/assets/2dbd3fa2-fdc0-4d85-a9bb-99a208d4b48f)


## now change the Name for quality of life sake.

`smaller_df = smaller_df.rename(columns={
    'Model Year': 'ModelYear',
    'Mfr Name': 'Mfr',
    'City FE (Guide) - Conventional Fuel': 'City FE',
    'Comb FE (Guide) - Conventional Fuel': 'Cob FE',
    'Hwy FE (Guide) - Conventional Fuel': 'Hwy FE'

