import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def resolve(input):
    print(BASE_DIR)
    f = open("%s/problems/input3" % BASE_DIR, "w")
    f.write(input)
    f.close()
    os.system("%s/problems/problem3 < %s/problems/input3 > %s/problems/output3" % (BASE_DIR, BASE_DIR, BASE_DIR))
    f = open("%s/problems/output3" % BASE_DIR, "r")
    output = f.read()
    f.close()
    return "\n%s" % output
