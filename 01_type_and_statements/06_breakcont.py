studen_name = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

# breaking out of the for loop
for name in studen_name:
    if name == "Mark":
        print("Found him!" + name)
        break
    print("Currently testing " + name)

print("")
print('')

# continue
for name in studen_name:
    if name == "Bort":
        continue
        print("Found him!" + name)       
    print("Currently testing " + name)