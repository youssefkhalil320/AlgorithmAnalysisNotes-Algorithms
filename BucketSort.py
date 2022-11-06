def bucket_sort(input_list):
    max_value = max(input_list)
    size = max_value/len(input_list)

    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        buckets_list[z].sort()
            
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output
    
print(bucket_sort([79,13,16,64,39,20,89,53,71,42]))    