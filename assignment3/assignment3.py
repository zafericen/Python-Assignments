import sys
def ANU(new_user):
    if new_user in dict_users:
        file2.write("ERROR: Wrong input type! for 'ANU'! -- This user already exists!!\n")
    else:
        dict_users[new_user] = []
        file2.write("User '{}' has been added to the social network successfully\n".format(new_user))


def DEU(e_user):
    try:
        dict_users.pop(e_user)
        for i3 in dict_users:
            if e_user in dict_users[i3]:
                dict_users[i3].remove(e_user)
    except KeyError:
        file2.write("ERROR: Wrong input type! for 'DEU'!--There is no user named '{}'!!\n".format(e_user))
    else:
        file2.write("User '{}' and his/her all relations have been deleted successfully\n".format(e_user))


def ANF(s_user, t_user):
    if s_user not in dict_users and t_user not in dict_users:
        file2.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' and '{}' found!\n".format(s_user,t_user))
    elif s_user not in dict_users:
        file2.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' found!!\n".format(s_user))
    elif t_user not in dict_users:
        file2.write("ERROR: Wrong input type! for 'ANF'! -- No user named '{}' found!!\n".format(t_user))
    elif s_user in dict_users[t_user]:
        file2.write("ERROR: A relation between '{}' and '{}' already exists!!\n".format(s_user,t_user))
    else:
        dict_users[s_user].append(t_user)
        dict_users[t_user].append(s_user)
        dict_users[s_user].sort()
        dict_users[t_user].sort()
        file2.write("Relation between '{}' and '{}' has been added successfully\n".format(s_user,t_user))


def DEF(s_user, t_user):

    if s_user not in dict_users and t_user not in dict_users:
        file2.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' and '{}' found!\n".format(s_user,t_user))
    elif s_user not in dict_users:
        file2.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' found!!\n".format(s_user))
    elif t_user not in dict_users:
        file2.write("ERROR: Wrong input type! for 'DEF'! -- No user named '{}' found!!\n".format(t_user))
    elif s_user not in dict_users[t_user]:
        file2.write("ERROR: No relation between '{}' and '{}' found!!\n".format(s_user,t_user))
    else:
        dict_users[s_user].remove(t_user)
        dict_users[t_user].remove(s_user)
        file2.write("Relation between '{}' and '{}' has been deleted successfully\n".format(s_user,t_user))


def CF(username):
    if username not in dict_users:
        file2.write("ERROR: Wrong input type! for 'CF'! -- No user named '{}' found!\n".format(username))
    else:
        file2.write("User '{}' has {} friends\n".format(username,len(dict_users[username])))


def FPF(username, max_distance):
    fpf_list = []
    if username not in dict_users:
        file2.write("ERROR: Wrong input type! for 'FPF'! -- No user named '{}' found!\n".format(username))
    else:
        if dict_users[username] == [""]:
            file2.write("ERROR: This user has 0 friend\n")
            return None
        elif max_distance not in [1, 2, 3]:
            file2.write("ERROR: Maximum Distance is out of range!!\n")
            return None
        elif max_distance == 1:
            fpf_list = dict_users[username]
            fpf_list.append(username)
        elif max_distance == 2:
            for i4 in dict_users[username]:
                fpf_list.append(i4)
                for i5 in dict_users[i4]:
                    fpf_list.append(i5)
        elif max_distance == 3:
            for i4 in dict_users[username]:
                fpf_list.append(i4)
                for i5 in dict_users[i4]:
                    fpf_list.append(i5)
                    for i6 in dict_users[i5]:
                        fpf_list.append(i6)
        fpf_set = set(fpf_list)
        fpf_set.remove(username)
        friends_string = "{"+str(sorted(fpf_set))[1:-1]+"}"
        file2.write("User '{}' has {} possible friends when maximum distance is {}\n".format(username,len(fpf_set),max_distance))
        file2.write("These possible friends: {}\n".format(friends_string))


def SF(username,m_d):
    md_list = []
    md_list_usable = []
    if username not in dict_users:
        file2.write("Error: Wrong input type! for 'SF'! -- No user named '{}' found!\n".format(username))
    elif m_d not in [2,3]:
        file2.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")
    else:
        for i in dict_users[username]:
            for i1 in dict_users[i]:
                md_list.append(i1)
        md_list.sort()
        md_set = set(md_list)
        md_set.remove(username)
        for i9 in md_set:
            if md_list.count(i9) >= m_d:
                md_list_usable.append([md_list.count(i9),i9])
        md_list_usable.sort(key=lambda x:(x[0],x[1]))
        file2.write("Suggestion List for '{}' (when MD is {}):\n".format(username,m_d))
        for i in md_list_usable:
            file2.write("'{}' has {} mutual friends with '{}'\n".format(username,i[0],i[1]))
        file2.write("The suggested friends for '{}': ".format(username))
        for i in md_list_usable:
            if i != md_list_usable[-1]:
                file2.write("'{}',".format(i[1]))
            else:
                file2.write("'{}'\n".format(i[1]))



with open(sys.argv[1], "r+",encoding="utf-8") as file:
    list_1 = file.readlines()
    list_usable = []
    for i in range(len(list_1)):
        list_usable.append(list_1[i].split(":"))
        list_usable[i][1] = list_usable[i][1].split(" ")
        if "" in list_usable[i][1]:    
            for i2 in range(list_usable[i][1].count("")):
                list_usable[i][1].remove("")
    for i in range(len(list_usable)):
        if "\n" not in list_usable[i][1] and "\n" not in list_usable[i][1][-1]:
            continue
        elif "\n" not in list_usable[i][1]:
            list_usable[i][1][-1] = list_usable[i][1][-1][0:-1]
        else:
            list_usable[i][1].remove("\n")
    

with open(sys.argv[2],"r",encoding="utf-8") as file3:
    list_2 = file3.readlines()
    list_commands = []
    for i in range(len(list_2)):
        list_commands.append(list_2[i].split(" "))
        if "" in list_commands[i]:
            for i2 in range(list_commands[i].count("")):
                list_commands[i].remove("")
    for i in range(len(list_commands)):
        if "\n" not in list_commands[i] and "\n" not in list_commands[i][-1]:
            continue
        elif "\n" not in list_commands[i]:
            list_commands[i][-1] = list_commands[i][-1][0:-1]
        else:
            list_commands[i].remove("\n")

dict_users = {}
for i1 in list_usable:
    dict_users[i1[0]] = i1[1]
friends = list(dict_users.values())
with open("output.txt","w",encoding="utf-8") as file2:
    for i in list_commands:
        if i[0] == "ANU":
            ANU(i[1])
        elif i[0] == "DEU":
            DEU(i[1])
        elif i[0] == "ANF":
            ANF(i[1], i[2])
        elif i[0] == "DEF":
            DEF(i[1], i[2])
        elif i[0] == "CF":
            CF(i[1])
        elif i[0] == "FPF":
            FPF(i[1], int(i[2]))
        elif i[0] == "SF":
            SF(i[1], int(i[2]))
