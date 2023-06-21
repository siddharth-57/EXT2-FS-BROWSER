import subprocess

# Run a command and capture its output
def output(a,b,c):
    if len(c) > 1:
        c1 = c[0]
        c2 = c[1:]
        result = subprocess.run(['sudo', './project', a, b, c1, c2], stdout=subprocess.PIPE)
    else:     
        result = subprocess.run(['sudo', './project', a, b, c], stdout=subprocess.PIPE)
    # Decode the output as a string
    output = result.stdout.decode('utf-8')
    return output
