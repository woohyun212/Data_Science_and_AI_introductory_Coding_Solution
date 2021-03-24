# print(bin(5), "&", bin(6), "=", bin(5 & 6))
# print(bin(5), "|", bin(6), "=", bin(5 | 6))
# print(bin(5), "^", bin(6), "=", bin(5 ^ 6))


def neat_bin(num1, num2):  # 깔끔한 bin
    num1_binary_length = len(format(num1, 'b'))  # 첫번째 입력받는 정수에 대한 이진수의 길이 저장
    num2_binary_length = len(format(num2, 'b'))  # 두번째 입력받는 정수에 대한 이진수의 길이 저장
    result_binary_length = len(format(num1 ^ num2, 'b'))  # 결과 값에 대한 2진수 길이 저장
    total_string = '0b'  # 최종으로 반환할 문자열 선언/ 접두사"0b" 설정
    if num1_binary_length >= num2_binary_length:  # 첫번째 이진수의 길이가 더길다면
        total_binary_length = num1_binary_length  # 최종길이로 첫번째 이진수의 길이로 설정
    else:  # 아니면
        total_binary_length = num2_binary_length  # 반대로 두번째 이진수의 길이로 설정
    for i in range(total_binary_length - result_binary_length):  # 최종 길이보다 결과 길이가 작은만큼
        total_string += "0"  # 반환할 문자열에 0 추가
    total_string += format(num1 ^ num2, 'b')  # 결과 문자열을 최종 문자열에 추가
    return total_string  # 최종 문자열 반환


print(bin(5), "^", bin(6), "=", neat_bin(5, 6))
