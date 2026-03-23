const uploadBox = document.getElementById("uploadBox");
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const uploadIcon = document.getElementById("uploadIcon");

// ドラッグオーバー時の処理
uploadBox.addEventListener("dragover", (e) => {
  e.preventDefault(); // デフォルトの処理を防ぐ（ファイルのオープンを防止）
  uploadBox.style.backgroundColor = "#f0f0f0"; // 視覚的なフィードバックを提供
});

// ドラッグアウト時の処理
uploadBox.addEventListener("dragleave", () => {
  uploadBox.style.backgroundColor = ""; // 背景色を元に戻す
});

// ドロップ時の処理
uploadBox.addEventListener("drop", (e) => {
  e.preventDefault();
  uploadBox.style.backgroundColor = ""; // 背景色をリセット

  // ドロップされたファイルを取得
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith("image/")) {
    previewImage(file); // 画像のプレビュー表示
    imageInput.files = e.dataTransfer.files; // input要素にファイルをセット
  }
});

// アップロードボックスをクリックしたときの処理
uploadBox.addEventListener("click", () => {
  imageInput.click(); // input要素をクリックしてファイル選択をトリガー
});

// ファイル選択時の処理
imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (file && file.type.startsWith("image/")) {
    previewImage(file); // 画像のプレビュー表示
  }
});

// プレビュー画像を表示する関数
function previewImage(file) {
  const reader = new FileReader();
  reader.onload = (e) => {
    uploadIcon.style.display = "none"; // カメラアイコンを非表示
    preview.src = e.target.result; // プレビューに画像をセット
    preview.style.display = "block"; // プレビューを表示
  };
  reader.readAsDataURL(file); // ファイルをData URLとして読み込む
}

// フォーム送信時の処理
document.getElementById("imageForm").addEventListener("submit", function (e) {
  // ここでフォーム送信をそのまま進める
  // 特別な処理が必要な場合はここに追加できます
});

// 使い方説明の表示・非表示
document.getElementById("toggleButton").addEventListener("click", function () {
  const usageText = document.getElementById("usageText");
  if (usageText.style.display === "none" || usageText.style.display === "") {
    usageText.style.display = "block";
    this.textContent = "使い方説明を非表示";
  } else {
    usageText.style.display = "none";
    this.textContent = "使い方説明を表示";
  }
});
