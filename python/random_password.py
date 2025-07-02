import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    """
    length (int) : 비밀번호의 길이
    use_uppercase (bool) : 대문자 사용 여부
    use_lowercase (bool) : 소문자 사용 여부
    use_digits (bool) : 숫자 사용 여부
    use_special_chars (bool) :특수 문자 사용 여부
    
    return:
        str: 생성된 비밀번호 또는 오류 메시지
    """
    # string 모듈에서 string.ascii_ 로 시작하는 것들은 영문자 알파벳 관련 상수
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    # 특수문자에서는 ' " \ | 를 포함하면 안되는 곳이 있을 수도 있으니 이를 제외하도록..
    if use_special_chars:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/"
    if not characters:
        return "최소 하나의 문자 유형을 선택해야 합니다."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def yes_no_input(prompt):
    """
    'y' 와 'n'이 입력될 때까지 사용자 입력을 요청하게하는 헬퍼 함수
    """
    while True:
        response = input(prompt).lower()
        if response in ['y', 'n']:
            return response =='y'
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")

def create_password():
    print("안전한 비밀번호를 생성해 봅시다!")
    
    while True :
        try:
            password_length = int(input("원하시는 비밀번호의 길이를 입력해 주세요 (예: 8): "))
            if password_length < 8 :
                print("비밀번호 길이는 8 이상이어야 합니다. 다시 입력해 주세요")
                continue
            break
        except ValueError:
            print("유효한 숫자를 입력해 주세요.")
    use_uppercase = yes_no_input("대문자를 포함할까요? (y/n): ")
    use_lowercase = yes_no_input("소문자를 포함할까요? (y/n): ")
    use_digits = yes_no_input("숫자를 포함할까요? (y/n): ")
    use_special_chars = yes_no_input("특수 문자를 포함할까요? (y/n): ")
    
    password = generate_password(password_length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    print(f"생성된 비밀번호: {password}")
    
if __name__ == "__main__":
    create_password()