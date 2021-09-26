import sys
import os
import copy

CWD = os.getcwd()
PATH_TO_INPUTS = "/../inputs/"
PATH_TO_OUTPUTS="/../outputs/"
FILE_NAME="FIX.09-Jan-2018.log"
OUT_FILE_NAME=FILE_NAME[:-4] + ".out"
DICT = {"55": "STOCK CODE",
        "14": "TRANS QTY",
        "6": "TRANS PX",
        "54": "TRANS SIDE",
        "1": "ACCOUNT",
        "11": "BUYER REF-ID",
        "37": "SELLER REF-ID",
        "60": "TRANS TIME"}
NEW_DICT = {"STOCK CODE": "",
            "TRANS QTY": "",
            "TRANS PX": "",
            "TRANS SIDE": "",
            "ACCOUNT": "",
            "BUYER REF-ID": "",
            "SELLER REF-ID": "",
            "TRANS TIME": ""}

def write_csv_headers():
    csv_headers = ""
    for key in NEW_DICT:
        csv_headers += key + ","
    csv_headers = csv_headers[:-1]
    print(csv_headers)
    f = open(CWD + PATH_TO_OUTPUTS + OUT_FILE_NAME, "w")
    f.write(csv_headers + "\n")
    f.close()

def write_csv(dict):
    #print(dict)
    csv_line = ""
    for key in dict:
        csv_line += dict[key] + ","
    csv_line = csv_line[:-1]
    if csv_line != ",,,,,,,":
        print(csv_line)
        f = open(CWD + PATH_TO_OUTPUTS + OUT_FILE_NAME, "a")
        f.write(csv_line + "\n")
        f.close()

if __name__ == "__main__":
    write_csv_headers()
    f = open(CWD + PATH_TO_INPUTS + FILE_NAME, "r")
    lines = f.readlines()
    # data processing
    for line in lines:
        columns = line.rstrip().split("|")
        new_dict = NEW_DICT.copy()
        for column in columns:
            if column == "": continue
            column = column.split("=")
            key = column[0]
            val = column[1]
            if key in DICT:
                new_dict[DICT[key]] = val
        write_csv(new_dict)

