import subprocess

# Run the command to get the list of installed packages
result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)

# Get the output of the command
output = result.stdout

# Save the list of installed packages to a requirements.txt file
with open('requirements.txt', 'w') as file:
    file.write(output)

print("List of installed packages saved to 'requirements.txt'")
