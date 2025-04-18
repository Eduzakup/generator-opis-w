from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Klucz z ENV
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/generate-description", methods=["POST"])
def generate_description():
    data = request.json
    prompt = f"""
Wygeneruj unikalny, profesjonalny opis produktu zoptymalizowany pod SEO, używając HTML i języka polskiego.

Produkt: {data.get("productName")}
Kategoria: {data.get("productCategory")}
Opis: {data.get("productDescription")}
Cechy: {data.get("productFeatures")}
Słowa kluczowe SEO: {data.get("seoKeywords")}
Dodatkowe informacje: {data.get("additionalContent")}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        content = response.choices[0].message["content"]
        return jsonify({"description": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)