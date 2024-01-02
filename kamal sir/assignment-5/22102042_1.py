
with open('result.txt', 'w') as content:
    content.write("Moumita, 22102242, 3.80\n")
    content.write("Ashraful, 22102201, pass\n")
    content.write("Naeem, 22102224, pass\n")
    content.write("ULA, 22102238, 3.90\n")
    content.write("Ruma, 22102023, 3.80\n")
    content.write("Hridi, 22102013, 4.00\n")
    content.write("Shazid, 22102206, 4.00\n")
    content.write("Hamidul, 22102037, pass\n")
    content.write("Fahad, 22102028, pass\n")

with open('result.txt', 'r') as content:
    for line in content:
        name, roll, gpa = line.strip().split(', ')
        print(f"Name: {name}, Roll: {roll}, GPA: {gpa}")
        
    content.close()
