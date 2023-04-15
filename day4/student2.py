# 클래스
#변수 이름 만들때 앞에 self 붙임
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("수업을 들어요")


s1 = Student("김하나", 1)
print(f'{s1.name}학생은 {s1.grade}학년입니다.')

s2 = Student("이둘", 2)
print(f'{s2.name} 학생은 {s2.grade}학년입니다.')
s2.learn()

kim = Student("김지수", 3)
print(f'{kim.name} 학생은 {kim.grade}학년입니다.')
kim.learn()