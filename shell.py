import os
# ----------------- 0. Install required packages -----------------
os.system('pip install requests')
os.system('pip install pandas')
os.system('pip install numpy')
os.system('pip install zipfile')
os.system('pip install warnings')
os.system('pip install requests')
os.system('pip install matplotlib')
os.system('pip install scikit-learn')
os.system('pip install seaborn')
os.system('pip install scipy')
os.system('pip install statsmodels')
os.system('pip install torch')
os.system('pip install torchvision')
os.system('pip install torchsummary')


os.system('clear')

# ----------------- 1. data-extract.py -----------------
# run the main function
# wait for user input to continue
os.system('clear')
input("All installations complete, Press and key to begin Magic...")
os.system("python3 '1. data-extract.py'")
os.system('python3 "2. data-preprocessing.py"')