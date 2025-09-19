'''
다음 소스 코드는 40명의 학생에게 50~100점 사이의 점수(50이상 100 이하)를 무작위로 할당한 딕셔너리 scores를 제공한다.
각 문제의 정답을 제시하기 위한 소스 코드를 작성하고 결과를 입력하시오.
'''

import random

scores = dict()
for i in range(10, 50):
    scores['S' + str(i)] = random.randrange(50, 100+1)
print(scores)

#40평의 학생의 평균 점수를 구하시오
avg = sum(scores.values())/ len(scores)
print(avg)

# 최고 점수 찾기
max_score = max(scores.values())

# 최고 점수를 가진 학생들만 필터링
candidates = [student for student, score in scores.items() if score == max_score]

# 학번이 가장 빠른 학생 (문자열 비교 시 S11 < S12 < ...)
best_student = min(candidates)

print("최고 득점 학생:", best_student)
print("점수:", max_score)