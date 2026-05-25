import subprocess

target = input("Enter target to ping: ")

# Run ping command
result = subprocess.run(
    ["ping", "-c", "4", target],
    capture_output=True,
    text=True
)

# Print output
print(result.stdout)
