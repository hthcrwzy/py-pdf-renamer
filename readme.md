# py-pdf-renamer

A simple renamer for PDF Files.

## Usage

https://github.com/hthcrwzy/py-pdf-renamer/assets/119731650/b45812d8-9bac-4a69-bf93-d17a6ac8f0d8

```console
$ python3 main.py -h
usage: py-pdf-renamer [-h] [-r] targets [targets ...]

renames pdf file(s) to the first line of text in the pdf file. if a directory is specified, all PDF file names in that directory are replaced.

positional arguments:
  targets          target pdf file(s) or directory(directories)

options:
  -h, --help       show this help message and exit
  -r, --recursive  rename recursively. valid only if directories are specified.
```

## Dependencies

| dependency     | version    |
| :------------- | :--------- |
| `Python`       | `3.11.6`   |
| `pdfminer.six` | `20221105` |

👉 For more details, see [requirements.txt](requirements.txt).

## Installation

1. clone this repository
2. run `python3 -m pip -r requirements.txt`
3. run `. .venv/bin/activate`
4. run `python3 main.py`

## License

👉 This project is under the MIT License, see [LICENSE.txt](LICENSE.txt) for more details.
