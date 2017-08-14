def create_counting_list(count_to_number):
    lister = []
    count = 0
    if count_to_number >= 0:
        while count < count_to_number:
            count += 1
            lister.append(count)
        return lister
    return 'cannot be negative'
