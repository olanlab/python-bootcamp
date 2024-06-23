import csv

def calCulateMean(gpas) : 
    return sum(gpas) / len(gpas)

def calCulateMedian(gpas) :
    sorted_list = sorted(gpas)
    n = len(sorted_list)
    if n % 2 == 0:
        median_value = (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        median_value = sorted_list[n//2]
    return median_value

def calCulateMode(gpas) : 
    mode = max  = 0
    gpasSet = set(gpas)
    
    for gpa in gpasSet :
        if max < gpas.count(gpa) :
            max = gpas.count(gpa)
            mode = gpa
    return mode

command = ''
fieldnames = ['id', 'name', 'sex', 'gpa']

while command != 'q':
    command = input("command ( q = exit, i = insert, d = delete, s = show, stat = statistic) = ")
    # i = insert
    if(command == 'i') :
        name = input("name : ")
        sex = input("sex : ")
        gpa = input("gpa : ")
        max = 0
        # FIND MAX ID
        with open('students-recorder.csv', 'r') as f:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for(i, row) in enumerate(reader):
                if (i > 0)  :
                    id = int(row['id'])
                    if (id > max) :
                        max = id
        # WRITE FILE APPEND MODE 
        with open('students-recorder.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow({'id': max + 1, 'name': name, 'sex': sex, 'gpa': gpa})
    # d = delete
    elif (command == 'd'):
        id = input('id : ')
        rows = []
        # READ FILE : GET OLD DATA
        with open('students-recorder.csv', 'r') as f:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for(i, row) in enumerate(reader):
                if (row['id'] == id) :
                    continue
                else :
                    rows.append(row)
        # WRITE FILE : WRITE NEW DATA
        with open('students-recorder.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(rows)
    # s = show, stat = statistic
    elif (command == 's' or command == 'stat'): 
        # READ FILE
        with open('students-recorder.csv', 'r') as f:
            reader = csv.DictReader(f, fieldnames=fieldnames)
            # SHOW
            if(command == 's'):
                for (i, row) in enumerate(reader):
                    print(f"{row['id']}\t{row['name']}\t{row['sex']}\t{row['gpa']}")
            # STAT
            elif(command == 'stat'):
                gpas = []
                for (i, row) in enumerate(reader):
                    if(i > 0):
                        gpas.append(float(row['gpa']))
                # mean
                mean = calCulateMean(gpas)
                # median
                median = calCulateMedian(gpas)
                # mode
                mode = calCulateMode(gpas)
                print(f"mean = {mean}, median = {median}, mode = {mode}")