import pandas as pd
import re

# Load CSV with column names
df = pd.read_csv("arabic_captions.csv", header=None, names=["image", "caption"])

print(df.head())
print(df.columns)


# Function to clean Arabic text
def clean_arabic_text(text):
    if not isinstance(text, str):  # Ensure text is a string
        text = str(text) if text is not None else ""

    text = re.sub(r"[ـ]", "", text)  # Remove elongation
    text = re.sub(r"\s+", " ", text).strip()  # Normalize spaces
    return text


# Apply cleaning function
df["caption"] = df["caption"].apply(clean_arabic_text)

# Save cleaned data
df.to_csv("cleaned_arabic_captions.csv", index=False)

print("Cleaning completed and saved to cleaned_arabic_captions.csv")
