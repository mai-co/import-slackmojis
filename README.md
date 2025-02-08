# import-slackmojis

This repository contains a script to import slackmojis to a local directory.

Once the slackmojis are downloaded, you can then bulk-upload them to a slack workspace by:

1. Downloading the chrome extension [Neutral Face Emoji Tools](https://chromewebstore.google.com/detail/neutral-face-emoji-tools/anchoacphlfbdomdlomnbbfhcmcdmjej)
2. Navigating to your slack admin page for emojis https://<workspace>.slack.com/customize/emoji
3. Dragging and dropping the downloaded emojis into the emoji upload area.

## Bulk downloading emojis

1. Find the URL of the slackmoji category you want to download. For example https://slackmojis.com/categories/25-blob-cats-emojis
2. Run the script `curl https://slackmojis.com/categories/25-blob-cats-emojis > slackmojis.html`
3. Run the script `grep -o 'https://emojis\.slackmojis\.com[^"]*' slackmojis.html > slackmoji_urls.csv`
4. Run the script `python download_slackmojis.py`
5. The emojis will be downloaded to `cwd/slackmojis`
