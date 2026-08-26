import os
from google import genai

# ステップ1で設定したSecretから安全にAPIキーを読み込む
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# 自動実行のテスト用プロンプト
prompt = "今日はどんな日ですか？エンジニアに向けた今日の一言応援メッセージを1文で書いてください。"

response = client.models.generate_content(
    model="gemini-2.5-flash",  # または現在利用可能なモデル名
    contents=prompt
)

print("=== Geminiからの自動配信メッセージ ===")
print(response.text)