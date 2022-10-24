learnerGrades = open("/Users/bikigurung/Desktop/KuraLabScripts/diagnostic6/grades.txt", "r")
passPeople = open("/Users/bikigurung/Desktop/KuraLabScripts/diagnostic6/pass.txt","w")
failPeople = open("/Users/bikigurung/Desktop/KuraLabScripts/diagnostic6/fail.txt","w")

 
for line in learnerGrades:
    line_split = line.split()
    if line_split[2] == 'fail':
        failPeople.write(line_split[0]+"\n")
    else:
        passPeople.write(line_split[0]+"\n")

failPeople.close()
passPeople.close()
learnerGrades.close()