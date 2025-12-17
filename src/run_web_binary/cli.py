import os
import subprocess
import sys
import tempfile
import urllib.request

def main() -> None:
    with tempfile.NamedTemporaryFile(delete=False) as f:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            while chunk := resp.read(8192):
                f.write(chunk)
        f.flush()

    os.chmod(f.name, 0o755)
    result = subprocess.run([f.name] + sys.argv[2:], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()

