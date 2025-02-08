import os
import requests
from pathlib import Path
from urllib.parse import urlparse


def download_emojis(csv_file):
    # Create directory if it doesn't exist
    output_dir = os.path.expanduser("~/slackmojis")
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Read URLs from file
    with open(csv_file, "r") as f:
        urls = f.readlines()

    # Download each emoji
    for url in urls:
        url = url.strip()
        if not url:
            continue

        # Extract filename from URL
        filename = os.path.basename(urlparse(url).path)
        # Remove the timestamp query parameter
        filename = filename.split("?")[0]

        # Full path for saving
        save_path = os.path.join(output_dir, filename)

        try:
            # Download the file
            response = requests.get(url, stream=True)
            response.raise_for_status()

            # Save to file
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"Downloaded: {filename}")

        except Exception as e:
            print(f"Error downloading {filename}: {str(e)}")


if __name__ == "__main__":
    download_emojis("slackmoji_urls.csv")
