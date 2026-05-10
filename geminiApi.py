from google import genai

client = genai.Client(api_key="AIzaSyBwWx268mGlcfFHTHzHLrAOHC3DdBFN9rE")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)

print(response.text)