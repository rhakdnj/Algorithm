'''
멜로디 -> 음악을 찾음
한 음악을 반복해서 재생할 때도 있고, 네오가 기억하고 있는 멜로디는 음 끝과 처음부분이 이어서 재생된 멜로디일수
rotate queue

음악을 중간에 끊을 경우 ->
원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 네오가 들은 곡이 아닐수도 있다

각 음은 1분에 1개씩 재생

음악은 반드시 처음부터 재생
음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생
음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생

반환 조건
조건이 일치하는 음악이 여러 개일 때
라디오에서 재생된 시간이 제일 긴 음악 제목을 반환

재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환.

조건이 일치하는 음악이 없을 때에는 “(None)”을 반환

'''


def replace_special(m):
    return m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f') \
        .replace('G#', 'g').replace('A#', 'a')


def solution(m, musicinfos):
    answer = []
    cnt = 0
    m = replace_special(m)

    for musicinfo in musicinfos:
        result = ''
        start, end, name, music = musicinfo.split(',')
        music = replace_special(music)
        s_hour, s_minute = start.split(':')
        s_time = 60 * int(s_hour) + int(s_minute)
        e_hour, e_minute = end.split(':')
        e_time = 60 * int(e_hour) + int(e_minute)
        play_time = e_time - s_time
        div, mod = divmod(play_time, len(music))
        result = div * music + music[:mod]
        print(result)
        if m in result:
            answer.append((name, play_time, cnt))
            cnt += 1

    print(answer)
    if cnt > 1:
        return sorted(answer, key=lambda x: (-x[1], x[2]))[0][0]
    elif cnt == 0:
        return '(None)'
    else:
        return answer[0][0]
