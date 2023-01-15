import sys
import subprocess

# Get parameter
if len(sys.argv) != 2:
    print('Usage: python3 run.py <function-name>')
    sys.exit(1)

target_function = sys.argv[1]

# Build
build_command = 'faas-cli build -f stack.yml --shrinkwrap'
result = subprocess.run(build_command, shell=True, capture_output=True)
if result.returncode == 0:
    print(result.stdout.decode())
else:
    print(result.stderr.decode())

# Run
run_command = ['python3', './build/' + target_function + '/index.py']
p = subprocess.Popen(run_command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,
                     universal_newlines=True)
                     
while p.poll() == None:
	out = p.stdout.readline()
	print(out, end='')