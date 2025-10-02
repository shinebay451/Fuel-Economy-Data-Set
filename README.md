# Fuel-Economy-Data-Set

**Firstly save your data sheet**
`file = r"C:\Users\Shiny\OneDrive\Desktop\Honda Data sets\25data\20250814 MY25 ICE,EV,PHEV For DOE R2public.xlsx"`

## Now read data and load it into the DataFrame.

`df = pd.read_excel(file)`
This tell's you how much rows and columns the data contain. shape[0] is rows and shape[1] is columns.
`print("Rows:", df.shape[0], "Columns:", df.shape[1])`
![Alt text](<img width="208" height="20" alt="image" src="https://github.com/user-attachments/assets/c7093066-49ae-4dbc-83d5-379a6c4e8942" />)
## Next step Choose the columns you wish to work with.
`columns_GPM = ['Model Year', 'Mfr Name', 'City FE (Guide) - Conventional Fuel', 'Comb FE (Guide) - Conventional Fuel',
               'Hwy FE (Guide) - Conventional Fuel' ]`
and store it inside a new dataframe that is little bit smaller you know what it's way smaller.
`smaller_df = df[columns_GPM]`

