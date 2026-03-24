import torch  # PyTorchのインポート
import torchvision.models as models  # torchvisionの事前訓練済みモデルを使用するためのインポート
import torchvision.transforms as transforms  # 画像の前処理用モジュールのインポート
from PIL import Image  # 画像処理ライブラリPILのインポート
import torch.nn as nn  # ニューラルネットワークモジュールのインポート


NUM_CANDIDATES = 1  # 上位2つの予測結果を表示する設定
NUM_CLASSES = 3  # 分類したいクラス数

# 画像の前処理（リサイズ、テンソルへの変換、正規化）の設定
transform = transforms.Compose(
    [
        transforms.Resize([224, 224]),  # 画像を224x224にリサイズ
        transforms.ToTensor(),  # 画像をテンソルに変換
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),  # 画像の正規化
    ]
)

# ViTモデルのロード
model = models.vit_b_16(weights="DEFAULT")

# 全ての層のパラメータを訓練不可に
for param in model.parameters():
    param.requires_grad = False

# 最後の全結合層をNUM_CLASSES分類用に変更
num_ftrs = model.heads[0].in_features
model.heads[0] = nn.Linear(num_ftrs, NUM_CLASSES)

model.load_state_dict(torch.load("WeightSave/weights_vit.pth"))  # 学習済みの重みをロード
model.eval()  # モデルを評価モードに設定

# クラス名の定義
class_names = ["割引商品", "廃棄商品", "通常商品"]  


def predict(image):
    # 画像はすでにPillow Imageオブジェクトとして渡される
    tensor_image = transform(image).unsqueeze(0)  # 画像をテンソルに変換し、バッチ次元を追加
    outputs = model(tensor_image)  # モデルに画像を入力し、出力を取得
    probabilities = torch.nn.functional.softmax(outputs, dim=1)  # 出力をソフトマックス関数で確率に変換
    top_prob, top_classes = torch.topk(
        probabilities, NUM_CANDIDATES
    )  # 上位の確率とクラスのインデックスを取得
    top_prob_percent = [
        round(prob.item() * 100, 2) for prob in top_prob[0]
    ]  # 確率をパーセンテージに変換
    predictions = [
        (class_names[class_idx], prob)
        for class_idx, prob in zip(top_classes[0], top_prob_percent)
    ]
    results = []
    for class_name, prob in predictions:  # クラス名と確率を文字列に変換
        results.append(f"{class_name} : {prob:.2f}%")
    return results  # 予測結果のリストを返す



# デバッグ用のmain関数
if __name__ == "__main__":
    image_path = "./精度検証/割引商品/carrot_dis.jpg"  # テストする画像のパスを指定
    predictions = predict(image_path)  # 画像を予測する関数を呼び出す
    for p in predictions:  # 予測結果を表示
        print(p)
