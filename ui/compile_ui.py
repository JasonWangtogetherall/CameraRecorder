import glob
import ntpath
import os
import platform

_cur_dir = os.path.dirname(os.path.realpath(__file__))

RC_NAME = 'resources'


if __name__ == '__main__':

    for ui_file in glob.glob(os.path.join(_cur_dir, '*.ui')):
        name = ntpath.basename(ui_file).split('.')[0]
        py_file = os.path.join(_cur_dir, f'ui_{name}.py')
        os.system(f"pyside2-uic {ui_file} > {py_file}")
        # A bug in PySide2?
        if platform.system() == 'Linux':
            os.system(f"sed -i -- \"s/QString()/''/g\" {py_file}")

    os.system(f"pyside2-rcc -o {_cur_dir}/{RC_NAME}_rc.py {_cur_dir}/{RC_NAME}.qrc")

    # Fix the path issue of the RC file.
    for rc in glob.glob(os.path.join(_cur_dir, 'ui_*.py')):
        if platform.system() == 'Linux':
            os.system(f"sed -i -- \"s/import {RC_NAME}_rc/import ui.{RC_NAME}_rc/g\" {rc}")
        else:
            with open(rc, "r") as sources:
                lines = sources.readlines()
            with open(rc, "w") as sources:
                for line in lines:
                    sources.write(line.replace(f"import {RC_NAME}_rc", f"import ui.{RC_NAME}_rc"))
