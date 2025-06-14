import subprocess
import sys

result = subprocess.run(["python", "evaluate.py"], capture_output=True, text=True)
print(result.stdout)

for line in result.stdout.splitlines():
    if "Accuracy:" in line:
        acc = float(line.strip().split()[-1])
        if acc < 0.80:
            print("Model accuracy below threshold.")
            sys.exit(1)
        else:
            print("Model accuracy acceptable.")
            sys.exit(0)
