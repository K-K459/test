import os
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# プロンプト設定
prompt = "今日はどんな日ですか？エンジニアに向けた今日の一言応援メッセージを1文で書いてください。"

# 最新モデルを指定
response = client.models.generate_content(
    model="gemini-3.6-flash",  # または現在利用可能なモデル名
    contents=prompt
)

print("=== Geminiからの自動配信メッセージ ===")
print(response.text)