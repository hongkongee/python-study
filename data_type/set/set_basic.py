'''
* 집합 (set)
- 집합은 여러 값들의 모임이며, 저장 순서가 보장되지 않고
 중복값의 저장을 허용하지 않습니다.

- 집합은 사전과 마찬가지로 {}로 표현하지만, key:value
쌍이 아닌, 데이터가 하나씩 들어간다는 점이 사전과는 다릅니다.

- set()함수는 공집합을 만들기도 하며, 다른 컬렉션 자료형을
집합 형태로 변환할 수도 있습니다.

# []-list(), tuple(), {}-dict(), set()
'''

names = {'홍길동', '김철수', '박영희', '고길동', '홍길동'}
print(type(names))
print(names)

for x in names:
    if x == '김철수':
        print(x)
        break

# 내장함수 set()
s = set()
print(type(s))
print(s)


s1 = 'programming'
print(set(s1))
print(list(s1))
print(tuple(s1))

'''
- 집합은 변경 가능한 자료형이어서 언제든지 데이터를 편집할 수 있습니다

- 집합에 요소를 추가할 때는 add() 메서드를 사용하고 제거할 때는 remove()를 사용합니다.
'''

print('-' * 40)

asia = {'korea', 'china', 'japan'}
print(asia)
asia.add('thailand')
asia.add('china')
asia.remove('japan')
print(asia)

# 집합의 결합은 update() 메서드를 사용합니다. (덧셈 연산 x)
asia2 = {'sigapore', 'indonesia', 'korea'}
# print(asia + asia2) (x)

asia.update(asia2)
print(asia)

'''
* 집합의 연산
1. 합집합(|): 두 집합의 전체 요소들의 모음 (중복 제거)
2. 교집합(&): 두 집합의 중복을 배제한 공통 요소들의 모음.
3. 차집합(-): 왼쪽 집합에서 오른쪽 집합 요소를 제거
4. 배타적 차집합(^): 합집합 - 교집합
5. 부분집합 (<=): 왼쪽 집합이 오른쪽 집합의 부분집합인지를 검사.
'''


A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}

print('교집합:', A & B)
print('합집합:', A | B)
print('차집합(A-B):', A - B)
print('차집합(B-A):', B - A)
print('배타적 차집합:', A ^ B)

C = {4, 8, 12}
print(C <= A)
print(C <= B)