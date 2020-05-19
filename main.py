import pandas as pd
import glob

wsl_path = '/mnt/c/Users/jprhe/Dropbox/Codes/Projects/protein-analysis/Data/*'
linux_path = '/home/rheinheimer/Dropbox/Codes/Projects/protein-analysis/Data/*'
windows_path = 'C:/Users/jprhe/Dropbox/Codes/Projects/protein-analysis/Data/*'

files = glob.glob(wsl_path)

for file in files:
    data = pd.read_excel(
        file
    )

    data.columns = [
        'first_column',
        'second_column',
        'third_column',
        'fourth_column',
        'fifth_column',
        'sixth_column',
        'seventh_column',
        'eighth_column',
        'nineth_column',
        'tenth_column',
        'eleventh_column',
        'tewelfth_column',
        'thirteenth_column'
    ]

    data.query(
        expr='first_column != "A0A"',
        inplace=True
    )

    data.query(
        expr='second_columm != 0',
        inplace=True
    )

    data.query(
        expr='data.third_column != Homo sapiens',
        inplace=True
    )

    print(data)
