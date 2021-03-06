
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

if __name__ == "__main__":
    print(sum_timestamps(['1:02:01', '40:01:05', '10:57:30']))
