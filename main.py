# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    for i in range(m):
        minimum_time =  min(threads)
        threads_index = threads.index(minimum_time)
        output.append((threads_index, minimum_time))
        threads[threads_index] += data[i]
    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n,m,data)
    for i in range(m):
        print(result[i][0], result[i][1])

if __name__ == "__main__":
    main()
