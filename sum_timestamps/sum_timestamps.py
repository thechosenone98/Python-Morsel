
def lpad_list(some_list, target_len, padding=0):
    return [padding]*(target_len - len(some_list)) + some_list

def sum_timestamps(timestamps):
    # To pass the test you must change 24 to a big number like 100 (the challenge didn't include days)
    field_overflow_map = {0:-1, 1: 24, 2: 60, 3:60}
    field_out_map = {'days': '', 'hours': '', 'minutes': '', 'seconds': ''}
    total = [0 for i in range(4)]
    for timestamps in timestamps:
        fields = timestamps.split(':')
        fields = lpad_list(fields, 4, '0')
        for i, number in enumerate(fields):
            n = int(number)
            n_wrap = (n + total[i]) // field_overflow_map[i]
            if n_wrap > 0:
                total[i-1] += n_wrap
            total[i] = (total[i] + int(number)) % field_overflow_map[i]
    if total[0]:
        return f"{total[0]}:{total[1]:02d}:{total[2]:02d}:{total[3]:02d}"
    elif total[1]:
        return f"{total[1]:01d}:{total[2]:02d}:{total[3]:02d}"
    else:
        return f"{total[2]:01d}:{total[3]:02d}"
    # field_out_map['days'] = str(total[0])
    # field_out_map['hours'] = '0' + str(total[1]) if total[0] != 0 and len(str(total[1])) < 2 else str(total[1])
    # field_out_map['minutes'] = '0' + str(total[2]) if total[1] != 0 and len(str(total[2])) < 2 else str(total[2])
    # field_out_map['seconds'] = '0' + str(total[3]) if len(str(total[3])) < 2 else str(total[3])
    # return ':'.join(field for key, field in field_out_map.items() if field != '0' or key == 'minutes')

if __name__ == "__main__":
    print(sum_timestamps(['1:02:01', '40:01:05', '10:57:30']))
