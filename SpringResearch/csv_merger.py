import os
def combined_csv(path: str):
    """Function created to take in a path to a folder with a lot of .csv files,
    and it merges the files on a common column. Credit to
    https://raredogmarketing.com/resources/combining-multiple-csv-files-into-one-file-using-python-step-by-step-guide
    for a majority of this function.

    Args:
        path (str): The folder path
    """
    folder_path = path

    all_files = os.listdir(folder_path)

    # Filter out non-CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]

    # Create a list to hold the dataframes
    df_list = []
    print(csv_files)

    for csv in csv_files:
        file_path = os.path.join(folder_path, csv)
        try:
            # Try reading the file using default UTF-8 encoding
            df = pd.read_csv(file_path)
            df_list.append(df)
        except UnicodeDecodeError:
            try:
                # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df_list.append(df)
            except Exception as e:
                print(f"Could not read file {csv} because of error: {e}")
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")

    # Concatenate all data into one DataFrame    
    from functools import reduce
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Neighborhood'],
                                            how='outer'),df_list)
    # Save the final result to a new CSV file
    df_merged.to_csv(os.path.join(folder_path, 'combined_file.csv'), index=False)
