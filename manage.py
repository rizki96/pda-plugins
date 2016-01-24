import sys
import importlib
import subprocess
import shlex


if __name__ == '__main__':
    args = sys.argv

    if args[1] == 'standalone':
        if args[2] != None:
            cmd = "python -m %s.main" % args[2]
            cmd_args = shlex.split(cmd)

            subprocess.call(cmd_args)
