#!/bin/bash

echo "[+] Unzipping $1"
unzip $1;
echo "[*] Unzipped $1";
python3 code1.py