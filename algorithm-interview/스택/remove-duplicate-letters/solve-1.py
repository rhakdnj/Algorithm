class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # sorted by set
        # if s = '', do not go through the for statement
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''


if __name__ == "__main__":
    solution = Solution()
    s = "bcabc"
    print(solution.removeDuplicateLetters(s))


'''
input : bcabc

0번째 재귀함수
s = bcabc     
1번째 for문 sorted(set(s)) : ['a', 'b', 'c']
char = a
suffix = abc
set(s) = {'b', 'c', 'a'}
set(suffix) = {'b', 'c', 'a'}

1번째 재귀함수
s = bc
1번째 for문 sorted(set(s)) : ['b', 'c']
char = b
suffix = bc
set(s) = {'b', 'c'}
set(suffix) = {'b', 'c'}

2번째 재귀함수
s = c
1번째 for문 sorted(set(s)) : ['c']
char = c
suffix = c
set(s) = {'c'}
set(suffix) = {'c'}

3번째 재귀함수
s =
answer : abc
'''

'''

input : cbacdcbc

0번째 재귀함수
s = cbacdcbc
1번째 for문 sorted(set(s)) : ['a', 'b', 'c', 'd']
char = a
suffix = acdcbc
set(s) = {'b', 'c', 'd', 'a'}
set(suffix) = {'b', 'c', 'd', 'a'}

1번째 재귀함수
s = cdcbc
1번째 for문 sorted(set(s)) : ['b', 'c', 'd']
char = b
suffix = bc
set(s) = {'b', 'c', 'd'}
set(suffix) = {'b', 'c'}

2번째 for문 sorted(set(s)) : ['b', 'c', 'd']
char = c
suffix = cdcbc
set(s) = {'b', 'c', 'd'}
set(suffix) = {'b', 'c', 'd'}

2번째 재귀함수
s = db
1번째 for문 sorted(set(s)) : ['b', 'd']
char = b
suffix = b
set(s) = {'b', 'd'}
set(suffix) = {'b'}
2번째 for문 sorted(set(s)) : ['b', 'd']
char = d
suffix = db
set(s) = {'b', 'd'}
set(suffix) = {'b', 'd'}

3번째 재귀함수
s = b
1번째 for문 sorted(set(s)) : ['b']
char = b
suffix = b
set(s) = {'b'}
set(suffix) = {'b'}

4번째 재귀함수
s =
answer : acdb

'''



