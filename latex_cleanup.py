'''Deletes all unnecessary LaTex auxilliary files in every subfolder of the target directory. Adapted from a Python 2.x script Latex-Cleanup by Jeffrey Kennan (available on GitHub).'''

import os

def latex_cleanup(path):
    print("---------CLEANING LATEX---------")

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.abspath(file)
            filename, file_extension = os.path.splitext(file)
            if file_extension in ['.aux', '.fdb_latexmk', '.fls', '.gz', '.log', '.out', '.toc']:
                os.remove(str(root) + "\\" + str(filename) + str(file_extension))

    print("----------CLEANUP COMPLETED----------")




if __name__ == "__main__":
    print("Enter a full disk filepath to cleanup latex")
    path = input()
    latex_cleanup(path)