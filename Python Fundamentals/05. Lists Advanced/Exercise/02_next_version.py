version = [int(num) for num in input().split(".")]
if version[2] < 9:
    version[2] += 1
else:
    version[2] = 0
    if version[1] < 9:
        version[1] += 1
    else:
        version[1] = 0
        version[0] += 1
version = [str(num) for num in version]
print(".".join(version))
#print(f"{version[0]}.{version[1]}.{version[2]}")
