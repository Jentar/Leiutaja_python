f = open("Leiutaja.txt", "r")
first_line = f.readline().split()

albert = int(first_line[0]) + int(first_line[1]) * 10
biggest = albert

for line in f:
    line_split = line.split()
    result = int(line_split[0]) + int(line_split[1]) * 10
    if result > biggest:
        biggest = result

        
if biggest > albert:
    print(biggest - albert + 1)
else:
    print(0)
  
        
    

    


    









