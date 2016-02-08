from AppliedComputing.Bezier import Bezier
import os


# xfoil path on mac os x
xfoil_path = '/Users/Boateng/Desktop/xfoil/bin/xfoil'
# dont really need this as python works from within this folder
directory_path = '/AppliedComputing'
# running xfoil from python
run_xfoil_command = xfoil_path + ' < /Users/Boateng/Documents/uni_python/AppliedComputing/commands.in'


def run_command():
    """

    :return: runs xfoil command
    """
    os.system(run_xfoil_command)

def run_xfoil(file_path, x_foil_path):
    pass

if __name__ == '__main__':
    run_command()