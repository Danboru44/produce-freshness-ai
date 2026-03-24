# 青果商品 鮮度判定AI

スーパーの青果商品を撮影するだけで  
**「通常商品・割引商品・廃棄商品」を自動分類するAI**です。

実際の店舗データを用いて独自モデルを構築し、  
試験導入を通じて業務改善を実現しました。

---

## 結果

| 項目 | 内容 |
|------|------|
| テスト精度 | 93.3% |
| 使用モデル | Vision Transformer（ViT-B/16）+ 転移学習 |
| 学習データ | 150枚（独自収集・店長監修）+ データ拡張 |
| 分類クラス | 通常商品 / 割引商品 / 廃棄商品 |
| 学習エポック数 | 15 |

---

## ファイル構成
```
/
├── training-vit.ipynb   # 学習・評価の全プロセス
├── inferenceViT.py      # 学習済みモデルによる推論
├── WeightSave/          # 学習済み重みファイル（非公開）
│   └── README.md
├── requirements.txt     # 必要ライブラリ
└── README.md
```

---

## 各ファイルの説明

**training-vit.ipynb**  
データの前処理・拡張から、ViTモデルの構築・学習・評価まで  
一連のプロセスを記載しています。

**inferenceViT.py**  
学習済みモデルを使って画像を入力すると  
分類結果と確率を返す推論スクリプトです。

---

## 使用技術

- Python 3.9
- PyTorch
- torchvision
- Vision Transformer（ViT-B/16）
- Pillow

---

## セットアップ
```bash
# リポジトリをクローン
git clone https://github.com/Danboru44/produce-freshness-ai.git
cd [repository-name]

# ライブラリをインストール
pip install -r requirements.txt
```

### 推論を実行する場合

training-vit.ipynbを実行すると、`weights_vit.pth` として重みがロードされます。
`WeightSave/` に配置してから実行します。


### 学習を実行する場合

`training-vit.ipynb` をJupyter Notebookで開いて実行します。

---

## 詳細記事

技術的な背景・設計思想・振り返りはQiitaに記載しています。  
[[画像認識を使用した青果食品の鮮度判定AIアプリ]]([https://qiita.com/Neo_44/items/13cb9f5e7e66958fda68])

---

## 注意事項

- 学習データは店舗の許可を得て独自収集したものです
- プライバシー保護のため実データは非公開としています
- 学習済み重みファイル（`weights_vit.pth`）は容量のため非公開です
