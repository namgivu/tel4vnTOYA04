"""read file myfile.txt"""
from pathlib import Path

SH = Path(__file__).parent

# f_path = f'{THIS_FILE_DIR}/myfile.txt'
# f_path =      f'{THIS_DIR}/myfile.txt'
# f_path =            f'{SH}/myfile.txt'  # SH aka SCRIPT_HOME
f_path   =               SH /'myfile.txt'  # SH aka SCRIPT_HOME

s = f_path.read_text()
print(s)
