#입출력문 연습-plint() input()
#주석-변역X#-한줄 주석
#여러줄 주석''' '''   """ """
''' 
print("hello world")
print("김건영")
massage="안녕하세요 저는 인평자동차고등학교 AI 1학년 2반 김건영입니다."
print(massage*10)

#변수와 자료형
a=4
b=2.5
c="hello"
d=5672
print("a변수에 입력된 값은",a,"입니다.")
a=54
print("a변수에 입력된 값은",a,"입니다.")

print(type(a))
print(type(b))
print(type(c))
print(type(d))

#입력문-input()
name=input("이름을 입력해주세요: ")
#print("입력하신 이름은",name,"입니다.")
age=input("나이를 입력해주세요: ")
print("내이름은",name+"이고","나이는",age+"살입니다")
'''
#두 수의 덧셈(키보드로부터 수를 입력받기)
#키보드로부터 입력받으면 모두문자로 취급
#형 변환 => 캐스트 연산 cast
a=int(input("첫 번째 값을 입력하세요: ")) #캐스트 연산 [문자->정수]
b=int(input("두 번째 값을 입력하세요: "))  #str->int
c=a*b
print(c)


























