def output(dic, qn):
    result = dic[qn]
    avg = round(sum(result) / len(result), 2)
    print(f"{avg:.2f}")


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        #  The variable name will receive the first element of the split string, and the variable line will receive the
        #  rest of the elements as a list.
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    output(student_marks, query_name)
