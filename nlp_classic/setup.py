#!/usr/bin/env python

import nltk

print("Downloading NLTK data..")
nltk.download('punkt', download_dir='/home/bentoml/nltk_data')
nltk.download("wordnet", download_dir='/home/bentoml/nltk_data')
nltk.download('omw-1.4', download_dir='/home/bentoml/nltk_data')

### for yandex cloud deployment use without download_dir
# nltk.download('punkt')
# nltk.download("wordnet")
# nltk.download('omw-1.4')