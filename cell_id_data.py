import pandas as pd
from sqlalchemy import create_engine

# Load the data from Excel files
cell_5308_df = pd.read_excel(r'C:\Users\hp\Documents\Assigments\5308.xls', sheet_name=None)
cell_5329_df = pd.read_excel(r'C:\Users\hp\Documents\Assigments\5329.xls', sheet_name=None)

# Access specific sheets if necessary
sheet_names_5308 = cell_5308_df.keys()  # List all sheet names
sheet_names_5329 = cell_5329_df.keys()

# Convert each sheet to CSV
for sheet_name in sheet_names_5308:
    df = cell_5308_df[sheet_name]
    df.to_csv(f'5308_{sheet_name}.csv', index=False)

for sheet_name in sheet_names_5329:
    df = cell_5329_df[sheet_name]
    df.to_csv(f'5329_{sheet_name}.csv', index=False)

# Create a MySQL database connection
engine = create_engine('mysql+mysqlconnector://root:Thiva@1999@localhost/cell_data_db')

# List of CSV files for each cell_id
files_5308 = [
    r'C:\Users\hp\5308_Cycle_67_3_5.csv',
    r'C:\Users\hp\5308_Detail_67_3_5.csv',
    r'C:\Users\hp\5308_DetailTemp_67_3_5.csv',
    r'C:\Users\hp\5308_DetailVol_67_3_5.csv',
    r'C:\Users\hp\5308_Info.csv',
    r'C:\Users\hp\5308_Statis_67_3_5.csv'
]

files_5329 = [
    r'C:\Users\hp\5329_Cycle_67_3_1.csv',
    r'C:\Users\hp\5329_Detail_67_3_1.csv',
    r'C:\Users\hp\5329_DetailTemp_67_3_1.csv',
    r'C:\Users\hp\5329_DetailVol_67_3_1.csv',
    r'C:\Users\hp\5329_Info.csv',
    r'C:\Users\hp\5329_Statis_67_3_1.csv'
]

# Load and append CSV files to the database
def load_files_to_db(files, engine):
    for file in files:
        try:
            df = pd.read_csv(file)
            df.to_sql('cell_data', con=engine, if_exists='append', index=False)
            print(f'Successfully loaded {file} into the database.')
        except FileNotFoundError:
            print(f'File {file} not found.')
        except Exception as e:
            print(f'An error occurred while loading {file}: {e}')

# Load files for each cell_id
load_files_to_db(files_5308, engine)
load_files_to_db(files_5329, engine)