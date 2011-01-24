# http://docs.python.org/release/2.6.5/library/subprocess.html
import subprocess

script_to_execute = 'print_time.py'

# make a Popen instance (which starts running the script).

print '===== output from the process is hidden'
process = subprocess.Popen(['python', script_to_execute],
                            # tell Popen to capture standard out for us
                            stdout=subprocess.PIPE)

# block until the process exits
process.wait()
print '^^^^^'

# get the output
output = process.stdout.read()

print '===== we now have a string with the output to use for whatever we like'
print output
print '^^^^^'
