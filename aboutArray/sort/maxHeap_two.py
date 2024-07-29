# 测试
# 大根堆 数组未知

# 每输入一个数 最后结果是一个大根堆

def input_value():
    some_array = []
    while True:
        try:
            number = (input("请输入数字: "))
            if number.__eq__('quit'):
                break
            else:
                some_array.append(int(number))
        except ValueError:
            print("输入类型错误，退出~~")
            break


def is_odd(number):
    return number % 2 != 0


#  left_child = index * 2 + 1
#  right_child = index * 2 + 2
#  parent_index = (left_child - 1) / 2 || parent_index = (left_child - 2) / 2
def heap_max(some_array, index):
    largest = index
