version_input = input().split(".")

new_version = str(int("".join(version_input)) + 1)

print(".".join(new_version))

