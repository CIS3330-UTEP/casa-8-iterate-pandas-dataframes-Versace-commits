#import pandas
import pandas as pd

# method iterrows
#define a ditionary containing big mac data
data = {'Name': ['Argentina', 'Australia', 'Brazil', 'Canada'],
        'Date': [2000-4-1, 2007-6-1, 2013-7-1, 2023-7-1],
        'Iso_a3': ['Arg', 'Aus', 'Bra', 'Can'],
        'Currency_code': ['Ars', 'Aud', 'Brl', 'Cad']}

# convert dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Date', 'Iso_a3', 'Currency_code'])

print("Given DataFrame :\n", df)

print("\nIterating over rows using iterrows() method:\n")




for index, row in df.iterrows():
    print(row["Name"], row["Date"], row["Iso_a3"], row["Currency_Code"])




# import pandas
# apply method
import pandas as pd

# define a dictionary containing big mac data
data = {'Name': ['Argentina', 'Australia', 'Brazil', 'Canada'],
        'Date': [2000-4-1, 2007-6-1, 2013-7-1, 2023-7-1],
        'Iso_a3': ['Arg', 'Aus', 'Bra', 'Can'],
        'Currency_code': ['Ars', 'Aud', 'Brl', 'Cad']}

# convert dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Date', 'Iso_a3', 'Currency_code'])

print("Given DataFrame :\n", df)

print("\nIterating over rows using apply function:\n")

# iterate through each row and concatenate 
print(df.apply(lambda row: row["Name"] + row["Date"] + row["Iso_a3"] + row["Currency_Code"]), axis=1)
