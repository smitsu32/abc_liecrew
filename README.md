# abc_liecrew　- 競技プログラミング回答リポジトリ

このリポジトリは、競技プログラミングサイト[AtCoder](https://atcoder.jp/home) の「ABC（AtCoder Beginner Contest）」を中心に、[Educational DP Contest](https://atcoder.jp/contests/dp?lang=ja)や[競プロ典型90問](https://atcoder.jp/contests/typical90)などの過去の自分の回答を整理・管理するためのものです。

- 各コンテスト・問題集ごとにディレクトリを分けて回答を保存しています。
- Python・C++の両方で実装しています。
- コードの見直しや復習、精度向上のために継続的に更新していきます。

## ファイル構成

```
abc_liecrew/
├── myans_py/                  # Python解答ファイル
│   ├── ab/                    # ABC A・B問題
│   ├── c/                     # ABC C問題
│   ├── d/                     # ABC D問題
│   ├── e/                     # ABC E問題
│   ├── EducationalDP/         # EducationalDPコンテスト
│   └── tenkei90/              # 競プロ典型90問
├── myans_cpp/                  # C++解答ファイル
│   ├── a/                     # ABC A問題
│   ├── b/                     # ABC B問題
│   └── c/                     # ABC C問題
├── requirements.txt
└── README.md
```

### ファイル命名規則

| パターン | 例 | 説明 |
|---|---|---|
| `abc{番号}{難易度}.py` / `.cpp` | `abc310b.py` | 基本解答 |
| `abc{番号}{難易度}_{手法}.py` | `abc240c_DP.py` | 手法を明記した解答 |

## リンク

- [Atcoder Library](https://kenkoooo.com/atcoder/#/user/liecrew?userPageTab=AtCoder+Pie+Charts) - 今までに解いた問題一覧
- [Atcoder NoviSteps](https://atcoder-novisteps.vercel.app/problems) - 難易度でソートされた問題一覧(反映なし)

[![Badge](https://cp-logo.vercel.app/atcoder/liecrew)](https://atcoder.jp/users/liecrew)
