#!/usr/bin/env python3
"""
画像から日本語テキストを抽出するスクリプト
EasyOCRを使用して講義資料の画像からテキストを読み取ります
"""

import glob
import os
from pathlib import Path

import easyocr


def extract_text_from_images(image_dir="data", output_dir="out", lang=["ja", "en"]):
    """
    指定ディレクトリ内のPNG画像からテキストを抽出

    Args:
        image_dir: 画像ファイルがあるディレクトリ
        output_dir: 抽出したテキストを保存するディレクトリ
        lang: 認識する言語（デフォルト: 日本語と英語）
    """
    # 出力ディレクトリを作成
    Path(output_dir).mkdir(exist_ok=True)

    # EasyOCRリーダーの初期化
    print("EasyOCRを初期化中...")
    reader = easyocr.Reader(lang, gpu=False)

    # PNG画像のリストを取得
    image_pattern = os.path.join(image_dir, "*.png")
    image_files = sorted(glob.glob(image_pattern))

    if not image_files:
        print(f"警告: {image_pattern} に該当する画像が見つかりません")
        return

    print(f"{len(image_files)}個の画像を処理します\n")

    # 全テキストを統合したファイル
    combined_output = os.path.join(output_dir, "all_extracted_text.txt")

    with open(combined_output, "w", encoding="utf-8") as combined_file:
        for idx, image_path in enumerate(image_files, 1):
            image_name = os.path.basename(image_path)
            print(f"[{idx}/{len(image_files)}] {image_name} を処理中...")

            # テキスト抽出
            result = reader.readtext(image_path)

            # 個別のテキストファイル名
            base_name = os.path.splitext(image_name)[0]
            output_file = os.path.join(output_dir, f"{base_name}.txt")

            # 個別ファイルに保存
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"=== {image_name} ===\n\n")
                for detection in result:
                    text = detection[1]
                    confidence = detection[2]
                    f.write(f"{text}\n")
                f.write(f"\n検出されたテキスト数: {len(result)}\n")

            print(f"  → {output_file} に保存しました（{len(result)}個のテキスト検出）")

            # 統合ファイルにも追加
            combined_file.write(f"\n{'='*60}\n")
            combined_file.write(f"ファイル: {image_name}\n")
            combined_file.write(f"{'='*60}\n\n")
            for detection in result:
                text = detection[1]
                combined_file.write(f"{text}\n")
            combined_file.write("\n")

    print(f"\n完了！全テキストは {combined_output} にまとめられています。")


if __name__ == "__main__":
    extract_text_from_images()
