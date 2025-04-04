# This file will use subprocess module to check disk usage

import subprocess
cp = subprocess.run(["df", "-h"], capture_output=True, text=True)
print(cp.stdout)

