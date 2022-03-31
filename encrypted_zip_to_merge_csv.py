import os
import pyzipper
import pandas as pd

# collect all paths of zips or csvs from given folder
def get_file_paths(path, file_type='zip'):
    try:
        master_list=[]
        for root, dirs, files in os.walk(os.path.abspath(path)):
            for file in files:
                if file.endswith(file_type):
                    master_list.append(os.path.join(root, file))
        return master_list
    except Exception as e:
        print(e.args)
                
# extraction of encrypted zip data
def extract_encrypted_zip(zip_file, password='123456'):
    try:
        with pyzipper.AESZipFile(zip_file, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode(password))
    except Exception as e:
        print(e.args)

# combining all csv data files in given location
def merge_csv_files(csv_list):
    try:
        df = pd.concat(map(pd.read_csv, csv_list), ignore_index=True)
        return df
    except Exception as e:
#         print('from Merge files')
        print(e.args)
#         df = pd.DataFrame({"message": ["Error "]})
# remove duplicates and create master csv
def remove_duplicates(df, folder_name, col_no):
    try:
        print('\nSelected Column: ',df.columns[int(col_no)-1])
        df_clean = df.drop_duplicates(subset=df.columns[int(col_no)-1])
        df_clean.to_csv('final_data_{}.csv'.format(folder_name), index=False)
    except Exception as e:
        print(e.args)
    
    
# duplicate = df_clean[df_clean.duplicated()]


def main():
    path = input(r'Enter folder path: ')
    folder_name = path.split('\\')[-1]
    zip_list = get_file_paths(path, 'zip')
    for zip_file in zip_list:
        extract_encrypted_zip(zip_file, password='123456')
    csv_list = get_file_paths('.', 'csv')
    df = merge_csv_files(csv_list)
    print('--'*20)
    print({i+1: col for (i, col) in enumerate(list(df.columns))})
    print('--'*20)
    col_no = int(input('\nEnter Column number: '))
    remove_duplicates(df, folder_name, int(col_no))
    

if __name__ == '__main__':
    main()