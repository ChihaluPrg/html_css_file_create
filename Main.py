import os
import tkinter as tk
from tkinter import filedialog

# Tkinterのrootウィンドウを非表示にする
root = tk.Tk()
root.withdraw()

# フォルダ選択ダイアログを表示して親ディレクトリを選択
parent_dir = filedialog.askdirectory(title="フォルダを選択してください")

# フォルダが選択されなかった場合
if not parent_dir:
    print("フォルダが選択されませんでした。")
    exit()

# 新しいサブフォルダの名前を指定
new_folder_name = input("作成する新しいフォルダの名前を入力してください: ")

# 新しいサブフォルダのパスを作成
dir_path = os.path.join(parent_dir, new_folder_name)

# フォルダが存在しない場合は作成する
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print(f"{dir_path} を作成しました。")
else:
    print(f"{dir_path} はすでに存在しています。")

# index.htmlを作成
html_content = """<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="shortcut icon" href="" type="image/x-icon" />
    <link rel="stylesheet" href="reset.css" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="container">

    </div>
  </body>
</html>"""

html_file_path = os.path.join(dir_path, 'index.html')
with open(html_file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)
    print(f"{html_file_path} を作成しました。")

# reset.cssを作成
reset_css_content = """
*,
*::before,
*::after {
  box-sizing: border-box;
}

body,
h1,
h2,
h3,
h4,
h5,
h6,
p,
figure,
blockquote,
dl,
dd {
  margin: 0;
  padding: 0;
}

ul, ol {
    list-style: none;
    margin: 0;
    padding: 0;
}
a {
    text-decoration: none;
}

img,
picture {
  max-width: 100%;
  display: block;
}

table {
    border-collapse: collapse;
    width: 100%;
}"""

reset_css_file_path = os.path.join(dir_path, 'reset.css')
with open(reset_css_file_path, 'w', encoding='utf-8') as file:
    file.write(reset_css_content)
    print(f"{reset_css_file_path} を作成しました。")

# style.cssを作成
style_css_content = """@charset "utf-8";

html {
  font-size: 62.5%;
}"""

style_css_file_path = os.path.join(dir_path, 'style.css')
with open(style_css_file_path, 'w', encoding='utf-8') as file:
    file.write(style_css_content)
    print(f"{style_css_file_path} を作成しました。")
