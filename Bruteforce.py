#!/usr/bin/env python3
import zipfile
import argparse
import time
from tqdm import tqdm
import sys

def try_password(zip_file, password):
    try:
        first_file = zip_file.namelist()[0]
        zip_file.read(first_file, pwd=password.encode())
        return True
    except:
        return False

def bruteforce_zip(zip_path, wordlist_path):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid ZIP file")
        return
    
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist:
            passwords = wordlist.readlines()
    except FileNotFoundError:
        print(f"Error: Wordlist file {wordlist_path} not found")
        return
    
    print(f"\n[*] Starting ZIP password bruteforce")
    print(f"[*] ZIP file: {zip_path}")
    print(f"[*] Wordlist: {wordlist_path}")
    print(f"[*] Total passwords to try: {len(passwords)}")
    print("\n[*] Starting bruteforce...\n")
    
    start_time = time.time()
    
    for password in tqdm(passwords, desc="Trying passwords"):
        password = password.strip()
        if try_password(zip_file, password):
            end_time = time.time()
            print(f"\n[+] Password found: {password}")
            print(f"[+] Time elapsed: {end_time - start_time:.2f} seconds")
            zip_file.extractall(pwd=password.encode())
            print(f"[+] Contents extracted successfully!")
            return password
    
    end_time = time.time()
    print(f"\n[-] Password not found in wordlist")
    print(f"[*] Time elapsed: {end_time - start_time:.2f} seconds")
    return None

def main():
    parser = argparse.ArgumentParser(description='ZIP Password Bruteforcer')
    parser.add_argument('zip_file', help='Path to the ZIP file')
    parser.add_argument('wordlist', help='Path to the wordlist file')
    
    args = parser.parse_args()
    
    bruteforce_zip(args.zip_file, args.wordlist)

if _name_ == "_main_":
    main()
