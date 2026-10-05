# abc_liecrew - 競技プログラミング解答集

[AtCoder](https://atcoder.jp/home)のABC（AtCoder Beginner Contest）を中心に、[Educational DP Contest](https://atcoder.jp/contests/dp?lang=ja)や[競プロ典型90問](https://atcoder.jp/contests/typical90)などで書いた自分の解答をまとめたリポジトリです。

- コンテスト・問題集ごとにディレクトリを分けて保存しています。
- PythonとC++の両方で解いています。
- 復習やコードの改善のため、今後も更新を続けます。

## ディレクトリ構成

```
abc_liecrew/
├── myans_py/                  # Pythonの解答
│   ├── ab/                    # ABC A・B問題
│   ├── c/                     # ABC C問題
│   ├── d/                     # ABC D問題
│   ├── e/                     # ABC E問題
│   ├── EducationalDP/         # Educational DP Contest
│   └── tenkei90/              # 競プロ典型90問
├── myans_cpp/                 # C++の解答
│   ├── a/                     # ABC A問題
│   ├── b/                     # ABC B問題
│   └── c/                     # ABC C問題
├── requirements.txt
└── README.md
```

### ファイル名のルール

| パターン | 例 | 説明 |
|---|---|---|
| `abc{コンテスト番号}{問題}.py` / `.cpp` | `abc310b.py` | 通常の解答 |
| `abc{コンテスト番号}{問題}_{解法}.py` | `abc240c_DP.py` | 使った解法を明記した解答 |

## 解答数

2026年10月時点の内訳です。

| ディレクトリ | 内容 | 解答数 |
|---|---|---:|
| `myans_py/ab` | ABC A・B問題 | 75 |
| `myans_py/c` | ABC C問題 | 258 |
| `myans_py/d` | ABC D問題 | 202 |
| `myans_py/e` | ABC E問題 | 25 |
| `myans_py/EducationalDP` | Educational DP Contest | 8 |
| `myans_py/tenkei90` | 競プロ典型90問 | 35 |
| `myans_cpp` | ABC A〜C問題（C++） | 3 |

## よく使う解法

ファイル名に付けた解法のうち、数の多いものを並べました。

| 解法 | ファイル名の例 |
|---|---|
| 二分探索 | `_bisect` |
| 幅優先探索・深さ優先探索 | `_BFS`、`_DFS`、`_01bfs` |
| 動的計画法 | `_DP` |
| bit全探索 | `_bit` |
| 優先度付きキュー・ダイクストラ法 | `_heapq`、`_dijkstra` |
| Union-Find | `_UF`、`_uf` |
| いもす法・しゃくとり法 | `_imos`、`_syaku` |

## 実行方法

標準入力から読み込み、標準出力に答えを出します。

```
python myans_py/ab/abc310b.py < input.txt
```

一部の解答は[ac-library-python](https://github.com/not522/ac-library-python)と[sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)を使います。実行する前に、次のコマンドでインストールしてください。

```
pip install -r requirements.txt
```

## リンク

- [AtCoder Problems](https://kenkoooo.com/atcoder/#/user/liecrew?userPageTab=AtCoder+Pie+Charts) - これまでに解いた問題の一覧
- [AtCoder NoviSteps](https://atcoder-novisteps.vercel.app/problems) - 難易度順の問題一覧（自分の解答状況は未反映）

[![Badge](https://cp-logo.vercel.app/atcoder/liecrew)](https://atcoder.jp/users/liecrew)
