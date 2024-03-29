def shap_to_lower(s):
    s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return s


def solution(m, musicinfos):
    answer = [0, '(None)']  # time_len, title
    m = shap_to_lower(m)
    for info in musicinfos:
        split_info = info.split(',')
        time_length = (int(split_info[1][:2]) - int(split_info[0][:2])) * 60 \
                      + int(split_info[1][-2:]) - int(split_info[0][-2:])
        title = split_info[2]
        part_notes = shap_to_lower(split_info[-1])
        full_notes = part_notes * (time_length // len(part_notes)) + part_notes[:time_length % len(part_notes)]
        if m in full_notes and time_length > answer[0]:
            answer = [time_length, title]
    return answer[-1]
