import matplotlib
import matplotlib.pyplot as plt


from subprocess import Popen, PIPE

def is_ipython() -> bool:
    try:
        shell = get_ipython().__class__.__name__
        print(shell)
        if shell == 'ZMQInteractiveShell':
            return False   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return True  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


plt.plot([1, 2, 3])
if is_ipython():
    print()

    p = Popen(["convert", 'png:-', 'sixel:-'], stdin=PIPE)
    plt.savefig(p.stdin, bbox_inches="tight", format='png', transparent=True) 
    p.stdin.close()
    p.wait()
else:
    plt.show()

