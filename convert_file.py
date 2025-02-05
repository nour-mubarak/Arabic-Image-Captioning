import pandas as pd

# Read the text file (assuming it's tab or comma-separated)
df = pd.read_csv(
    "/home/nour/vision project/Arabic-Image-Captioning/Flickr8k_arabic_text.txt",
    delimiter="\t",
)  # Change delimiter if needed

# Save as CSV
df.to_csv("arabic_captions.csv", index=False)
