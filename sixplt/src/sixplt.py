import matplotlib
import matplotlib.pyplot as plt
from subprocess import Popen, PIPE
import warnings

def is_ipython() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'TerminalInteractiveShell':
            return True  
        else:
            return False  
    except NameError:
        return False      

def show(*args, transparent=False, **kwargs):
    if is_ipython():
        print()

        try:
            p = Popen(["convert", 'png:-', 'sixel:-'], stdin=PIPE)
            plt.savefig(p.stdin, bbox_inches="tight", format='png', transparent=transparent) 
            p.stdin.close()
            p.wait()
            plt.close()
        except FileNotFoundError:
            warnings.warn("Unable to convert plot to sixel format: Imagemagick not found.")

    else:
        plt.show(*args, **kwargs)

