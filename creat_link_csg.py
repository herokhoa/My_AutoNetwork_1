f = open('csg_list')

for line in f:
    bts = line.strip()
    file_intf = "csg" + line.strip()
    g = open(file_intf)
    i = 1
    for sline in g:
        aaa = sline.strip()
        words = aaa.split()
        i = len(words)
        j = i - 1
        dict = {}
        if i == 4:
            interface = words[0]
            status = words[1]
            protocol = words[2]
            type_pbts = words[3]
            bts_p =words[j]
            if status == "up" and protocol == "up":
                with open("file_t", "a") as file_object:
                    file_object.write(bts + " " + interface + " " + protocol + " " + type_pbts  + " " + bts_p + "\n")
                    file_object.close()

