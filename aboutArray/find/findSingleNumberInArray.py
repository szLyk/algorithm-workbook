# 在一个数组中有两个数字出现的次数为奇数,其余的均为偶数 求两个奇数
one_array = [1, 2, 3, 2, 5, 4, 1, 4]
xor_num = 0
# 通过异或计算的性质 n * n =0 | n * 0 = n 将偶数项去除
for num in one_array:
    xor_num ^= num
# one_num=a^b 因为存在两个数 两数必不相等 a^b != 0 取a^b中 最右位不为0的数 用于分组
mid_num = xor_num & (-xor_num)  # 一个数取反相当于取反码再加补码 即+1 [0000 0011] -> [1111 1100] -> [1111 1101]
# 进行分组 因为偶数项会抵消 剩下的两数取一个
one_num = 0
two_num = 0

for num in one_array:
    if mid_num & num != 0:  # [1, 2, 2, 5, 4, 1, 4] 与 [1, 2, 3, 2, 4, 1, 4] | 与运算 n & n = n n * 0 = 0
        one_num ^= num
    else:
        two_num ^= num

print(one_num, two_num)
