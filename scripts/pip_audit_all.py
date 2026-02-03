import subprocess
import sys

REQS = [
    "backend/requirements.txt",
    "frontend/requirements.txt",
]

def run(cmd):
    print(">", " ".join(cmd))
    return subprocess.call(cmd)

def main():
    rc = 0
    for req in REQS:
        r = run(["pip-audit", "-r", req])
        rc = rc or r
    sys.exit(rc)

if __name__ == "__main__":
    main()
