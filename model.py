import google.generativeai as genai
genai.configure(api_key="AIzaSyA0P_xCDrRhfWnvCjTlRLKqctwJ7TypGKs")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
