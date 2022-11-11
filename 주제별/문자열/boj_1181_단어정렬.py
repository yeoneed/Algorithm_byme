import sys
def read_ints(): return sys.stdin.readline().strip()
def read_int(): return read_ints()[0]


def compare(word_lst):  # 일단 길이로 정렬, 같은 길이는 알파벳 순으로 그 부분만 또 정렬
    result = []
    same_len = []
    temp = sorted([(k, v)
                   for k, v in word_lst], key=lambda x: x[1])
    # v를 기준으로 정렬
    border_word = temp[0][0]
    border_len = temp[0][1]  # 가장 짧은 단어 길이를 기준값으로!

    for i in range(len(temp)-1):
        if border_len == temp[i][1]:
            if border_word > temp[i][0]:
                result.remove(border_word)
                result.append(temp[i][0])
                result.append(border_word)
                border_word =


def main():
    t = int(read_int())  # 문자열 몇 줄 들어오는지 입력
    word_lst = []

    for i in range(t):
        word = read_ints()
        word_lst.append(word, len(word))

    # print(word_lst)
    compare(word_lst)


if __name__ == "__main__":
    main()
