import subprocess

result = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, encoding="utf-8")

if result.returncode == 0:
    print(result.stdout)


result = subprocess.run(["w"], stdout=subprocess.PIPE, encoding="utf-8")

lines = result.stdout.split("\n")
line = result.stdout.readline()
print(line)