def mac_cruncher(milled_key_length, milled_key_depth, milled_key_mac):
    if (milled_key_depth + milled_key_mac + milled_key_length) < 4:
        return "don't mess with me, this doesn't look like a valid key schema"
    if milled_key_length == 1:
        return milled_key_depth
    max_key_space = milled_key_depth ** milled_key_length

    print("length: " + str(milled_key_length) + " height/depth: " + str(milled_key_depth) +
          " max_key_space " + str(max_key_space) +
          " MAC " + str(milled_key_mac))

    work_mac = milled_key_mac + 1  # mac 4 allows 6,2
    if work_mac >= milled_key_depth:
        return max_key_space

    else:
        potential_transforms = 0
        depth_range = range(0, milled_key_depth)
        fresh_set = set()
        for j in depth_range:
            for x in depth_range:
                if abs(j - x) <= milled_key_mac:
                    fresh_set.add((j, x))
                    potential_transforms += 1

        for i in range(1, milled_key_length):
            #print("length position: " + str(i))
            if i > 1:
                current_set = fresh_set
                fresh_set = set()
                for q in current_set:
                    for x in depth_range:
                        if abs(q[-1] - x) <= milled_key_mac:
                            working_lad = list(q)
                            working_lad.append(x)
                            working_lad = tuple(working_lad)
                            fresh_set.add(working_lad)
        #print("valid positions " + str(potential_transforms))
        print(', '.join(str(s) for s in sorted(fresh_set)))
        return len(fresh_set)


# print(mac_cruncher(3,4,1))
print(mac_cruncher(5, 6, 4))
# 
# assert mac_cruncher(2,6,6) == 36
# assert mac_cruncher(2,6,5) == 36
# assert mac_cruncher(2,6,4) == 34
# assert mac_cruncher(2,6,3) == 30
# assert mac_cruncher(2,4,2) == 14
# assert mac_cruncher(3,3,1) == 17
# assert mac_cruncher(3,4,2) == 50
# assert mac_cruncher(3,4,1) == 26
