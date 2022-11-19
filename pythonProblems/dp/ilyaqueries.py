

if __name__ == '__main__':
    query_string = input()
    num_queries = int(input())
    for eachquery in range(num_queries):
        s_f = input().split(" ")
        start = int(s_f[0])
        finish = int(s_f[1])
        count = 0
        for i in range(start - 1, finish - 1):
            if query_string[i] == query_string[i + 1]:
                count += 1
        print(count)
