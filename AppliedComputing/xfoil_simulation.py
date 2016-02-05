from AppliedComputing.Bezier import Bezier
import os


# xfoil path on mac os x
xfoil_path = '/Applications/Xfoil.app/Contents/Resources/xfoil'
# dont really need this as python works from within this folder
directory_path = '/AppliedComputing'
# running xfoil from python
run_xfoil_command = xfoil_path + 'XfoilP4 < AppliedComputing/commands.in'


def run_command():
    """

    :return: runs xfoil command
    """
    os.system(run_xfoil_command)

