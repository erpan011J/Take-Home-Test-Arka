def remove_duplicates(input_list):
    seen = set() # Use set to achive time complexity O(1)
    output_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    return output_list