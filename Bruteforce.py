#!/usr/bin/env python3
import zipfile, rarfile, tarfile, argparse, sys

def brute_zip(path, wordlist):
    with zipfile.ZipFile(path) as zf:
        for pw in open(wordlist):
            pw = pw.strip()
            try:
                zf.extractall(pwd=pw.encode('utf-8'))
                print(f"[ZIP] Password ditemukan: {pw}")
                return
            except:
                pass
    print("[ZIP] Tidak ditemukan password.")

def brute_rar(path, wordlist):
    rf = rarfile.RarFile(path)
    for pw in open(wordlist):
        pw = pw.strip()
        try:
            rf.extractall(pwd=pw)
            print(f"[RAR] Password ditemukan: {pw}")
            return
        except:
            pass
    print("[RAR] Tidak ditemukan password.")

def brute_tar(path, wordlist):
    print("[TAR] .tar.gz biasanya tidak dienkripsi dengan password.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="file .zip/.rar/.tar.gz")
    parser.add_argument("wordlist", help="path ke file wordlist (satu password tiap baris)")
    args = parser.parse_args()

    if args.archive.endswith(".zip"):
        brute_zip(args.archive, args.wordlist)
    elif args.archive.endswith(".rar"):
        brute_rar(args.archive, args.wordlist)
    elif args.archive.endswith((".tar.gz", ".tgz")):
        brute_tar(args.archive, args.wordlist)
    else:
        print("[!] Format file tidak didukung.")

if __name__ == "__main__":
    main()
