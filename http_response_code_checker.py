#!/usr/bin/env python

import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import click
from tqdm import tqdm

def get_response_code_and_write_excel(data, file_path_to_save): 
    """_summary_

    Args:
        data (_type_): _description_
        file_path_to_save (_type_): _description_
    """

    # Create a session for re-use to speed up individual requests
    session = requests.Session()

    i = 0

    # Loop through each row, requesting the individual URL and receiving a response code
    for server, path, method in tqdm(zip(data["Server"], data["Path"], data["Method"]), total=len(data)): 
        try: 
            response = session.request(method, server+path)
            data.at[i, "Response"] = response.status_code
        except requests.exceptions.RequestException as e: 
            data.at[i, "Response"] = f"{str(e)}"
        i += 1
    
    # Write dataframe to Excel file
    data.to_excel(file_path_to_save, index = False)

def read_excel(file): 
    """_summary_

    Args:
        file (_type_): _description_
    """
    # Read excel file into dataframe and return it
    return pd.read_excel(file)

def main(): 
    """_summary_
    """
    root = tk.Tk()
    root.withdraw()

    # Prompt user for file input
    if click.confirm("Please select what Excel to read from", default=True): 
        # Get Excel file containing URLs and methods to check
        file_path_to_read = filedialog.askopenfilename(filetypes=[("Excel files"), "*.xlsx"])
    else: 
        print("Exiting")
        exit()
    
    # Prompt user for file output
    if click.confirm("Please select where to save output to", default=True): 
        #Get file to save results to
        file_path_to_save = filedialog.asksaveasfilename(filetypes=[("Excel files", "*.xlsx")])
    else: 
        print("Exiting")
        exit()

    # Send file to be read into dataframe
    data = read_excel(file_path_to_read)

    # Add column
    data["Response"] = ""

    # Call function to check URLs and write to new Excel file
    get_response_code_and_write_excel(data, file_path_to_save)

if __name__ == "__main__": 
    main()