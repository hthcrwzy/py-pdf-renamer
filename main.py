"""
MIT License

Copyright © 2023 hthcrwzy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import argparse
import glob
import os
import re
from pathlib import Path

from pdfminer.high_level import extract_text

EXTENSION_PDF = ".pdf"

def main():
    parser = argparse.ArgumentParser(
        prog="py-pdf-renamer",
        description="renames pdf file(s) to the first line of text in the pdf file. if a directory is specified, all PDF file names in that directory are replaced.",
    )
    parser.add_argument(
        "targets",
        nargs="+",
        help="target pdf file(s) or directory(directories)"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="rename recursively. valid only if directories are specified.",
        required=False,
    )
    args = parser.parse_args()
    targets = args.targets
    r = args.recursive

    for target in targets:
        target = Path(target)
        if Path.is_file(target):
            rename(target)
        elif Path.is_dir(target):
            rename_in_dir(target, r)
        else:
            print(f"{target}: no such file or directory")

def rename_in_dir(dir: Path, r=False):
    if r:
        rename_in_dir_recursively(dir)
    else:
        rename_in_dir_non_recursively(dir)

def rename_in_dir_non_recursively(dir: Path):
    for pdf in glob.glob(f"{dir}/*{EXTENSION_PDF}"):
        rename(pdf)

def rename_in_dir_recursively(dir: Path):
    for root, _, files in os.walk(top=dir):
        for file in files:
            if not file.lower().endswith(EXTENSION_PDF):
                continue

            pdf = os.path.join(root, file)
            rename(pdf)

def rename(pdf):
    dir_name, old_file_name = os.path.split(pdf)

    # 新ファイル名を作る
    # 空白などは_に、ヌル文字は消す
    base = get_first_line(pdf).replace(" ", "_").replace("　", "_").replace("\t", "_").replace("\x00", "").strip()
    # 無効な記号は-に置換
    base = re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '-', base)
    new_file_name = base + EXTENSION_PDF
  
    if old_file_name == new_file_name:
        print(f"rename: skipped: '{pdf}'")
        return
    new_pdf = os.path.join(dir_name, new_file_name)
    os.rename(pdf, new_pdf)
    print(f"renamed: '{pdf}' -> '{new_pdf}'")

def get_first_line(pdf_file):
    # 一行目を抽出
    text = extract_text(pdf_file)
    lines = text.splitlines()
    return lines[0]

if __name__ == "__main__":
    main()
