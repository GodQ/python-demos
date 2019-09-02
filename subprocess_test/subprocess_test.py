from subprocess import Popen, PIPE, STDOUT

def run(command):
    process = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if line:
            yield line
        if process.poll()!=None:
            break


if __name__ == "__main__":
    for path in run("for i in $(seq 1 3); do echo $i; sleep 1; done"):
        print(path)
