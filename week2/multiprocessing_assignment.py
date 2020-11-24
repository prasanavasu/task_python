from multiprocessing import Process, Array, Value


def square(mylist, res, sq_sum):
    for index, number in enumerate(mylist):
        res[index] = number ** 2

    sq_sum.value = sum(res)

    print(f"square value - {sq_sum.value}")


if __name__ == "__main__":
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    res = Array("i", 10)
    sq_sum = Value("i")

    pro1 = Process(target=square, args=(mylist, res, sq_sum))

    pro1.start()
    pro1.join()
