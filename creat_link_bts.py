f = open('csg_list')

for line in f:
    bts = line.strip()
    file_intf = "csg" + line.strip()
    g = open(file_intf)
    for sline in g:
        i = 0
        k = 0
        if not(len(sline.strip()) == 0):
            aaa = sline.strip()
            words = aaa.split()
            i = len(words)
            k = i - 1
            csg_agg_str = words[0]
            bts_str = words[k]
            csg_agg_list = list(csg_agg_str)
            bts_list = list(bts_str)
            j = len(csg_agg_list)
            l = len(bts_list)
            if j > 7 and i > 7:
                 kq = csg_agg_list[0] + csg_agg_list[1] + csg_agg_list[2] + csg_agg_list[3] + csg_agg_list[4] + csg_agg_list[5]
                 if kq == "AGG-LA":
                     if i == 8:
                         descript = "TO_" + words[0] + "_PO_" + words[7] + "_TY_Noitinh/FO/TPCOMS" 
                         int_local = words[1]  + words[2]
                         with open("file_t", "a") as file_object:
                             file_object.write(bts + " " + int_local + " " + descript + "\n")
                             file_object.close()
                     if i == 9:
                         descript = "TO_" + words[0] + "_PO_" + words[7] + words[8] + "_TY_Noitinh/FO/TPCOMS"
                         int_local = words[1]  + words[2]
                         with open("file_t", "a") as file_object:
                             file_object.write(bts + " " + int_local + " " + descript + "\n")
                             file_object.close() 
                 if kq == "CSG-LA":
                     descript = "TO_" + words[0] + "_PO_" + words[8] + words[9] + "_TY_Noitinh/FO/TPCOMS" 
                     int_local = words[1]  + words[2]
                     with open("file_t", "a") as file_object:
                         file_object.write(bts + " " + int_local + " " + descript + "\n")
                         file_object.close()
