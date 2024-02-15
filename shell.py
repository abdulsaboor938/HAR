import os
# install pipreqs
os.system('pip install pipreqs')

# create requirements.txt
os.system('pipreqs .')

# install requirements
os.system('pip install -r requirements.txt')

# run the main function
os.system("python3 '1. data-extract.py'")