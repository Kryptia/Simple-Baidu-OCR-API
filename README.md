# Simple Baidu OCR API

A simple usage of Baidu OCR API.

## Requirements

requirements.txt

    certifi==2019.3.9
    chardet==3.0.4
    idna==2.8
    requests==2.21.0
    urllib3==1.24.1

## Usage

1. Install all the requirements. (`pip install -r requirements.txt`)
2. Rename `account.conf.sample` to `account.conf`, and change `'ak'` and `'sk'` to your own.
3. Simply Type `python main.py <path-to-picture-file>`.
4. The ocr text will be displayed on both console and `ocr_result.txt` file.