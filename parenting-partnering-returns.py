def check_avail(list_activities, s_i, e_i, person):
    check_start_end = False
    if len(scheduling_list) == 0:
        scheduling_list.append("C")
        list_activities.append((s_i, e_i))
        return True
    else:
        for start, end in list_activities:
            if start < s_i < end or start < e_i < end:
                return False
            else:
                check_start_end = True
        if check_start_end or len(list_activities) == 0:
            if person == "C":
                scheduling_list.append(person)
                list_activities.append((s_i, e_i))
            else:
                scheduling_list.append(person)
                list_activities.append((s_i, e_i))
            return True


tc = int(input())
tmp_tc = tc
scheduling_list = []
cam_scheduling_list = []
jam_scheduling_list = []
m = 1
while tmp_tc > 0:
    n = int(input())  # activities
    tmp_n = n
    while tmp_n > 0:
        dur = [int(i) for i in input().split(" ")]
        start_i = dur[0]
        end_i = dur[1]
        check = check_avail(cam_scheduling_list, start_i, end_i, "C")
        if not check:
            check = check_avail(jam_scheduling_list, start_i, end_i, "J")
        tmp_n -= 1
    if len(scheduling_list) != n:
        print("Case #{}: {}".format(m, "IMPOSSIBLE"))
        print(scheduling_list)
    else:
        print("Case #{}: {}".format(m, ''.join(scheduling_list)))
    m += 1
    scheduling_list.clear()
    cam_scheduling_list.clear()
    jam_scheduling_list.clear()
    tmp_tc -= 1
