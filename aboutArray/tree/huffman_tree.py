# 哈夫曼树的特点
# 带权路径长度最小：哈夫曼树的构造保证了编码的平均长度最小，从而实现了最优编码。
# 无损压缩：哈夫曼树编码是一种无损压缩算法，压缩后数据可以无误解码。
# 前缀编码：每个字符的编码都是前缀码，即任意一个字符的编码都不是其他字符编码的前缀。
# 哈夫曼树的构建步骤
# 统计每个字符的频率：从输入的文本中统计出每个字符出现的频率或权重。
#
# 初始化：把每个字符看作一个节点，并将其频率作为该节点的权值，生成一个优先队列（通常是最小堆）。
#
# 构建哈夫曼树：
#
# 从优先队列中取出权值最小的两个节点，将它们合并为一个新节点（新节点的权值为两个节点权值之和）。
# 将合并后的新节点重新加入优先队列。
# 重复上述过程，直到队列中只剩下一个节点，这个节点就是哈夫曼树的根节点。
# 生成编码：从根节点开始，通过左子节点表示为 0，右子节点表示为 1，直到叶子节点为止，这样每个字符就可以通过一串 0 和 1 的比特表示出来。

import heapq
from collections import defaultdict


class Node:
    def __init__(self, freq, char=None):
        self.char = char  # 节点存储的字符
        self.freq = freq  # 节点的频率
        self.left = None  # 左子树
        self.right = None  # 右子树

    # 为了让堆可以进行节点比较，我们定义比较函数
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_map):
    # 构建优先队列 (最小堆)
    heap = [Node(freq, char) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    # 构建哈弗曼树
    while len(heap) > 1:
        # 取出频率最小的两个节点
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # 合并这两个节点
        merged = Node(left.freq + right.freq)
        merged.left = left
        merged.right = right

        # 将合并后的节点重新放入堆中
        heapq.heappush(heap, merged)

    # 返回哈弗曼树的根节点
    return heap[0]


def encode_huffman_tree(root, code_dict={}, path=""):
    # 递归地生成每个字符的哈弗曼编码
    if root is None:
        return

    # 如果是叶子节点，则记录该字符的编码
    if root.char is not None:
        code_dict[root.char] = path

    encode_huffman_tree(root.left, code_dict, path + "0")
    encode_huffman_tree(root.right, code_dict, path + "1")

    return code_dict


def huffman_encoding(data):
    # 统计每个字符出现的频率
    freq_map = defaultdict(int)
    for char in data:
        freq_map[char] += 1

    # 构建哈弗曼树
    root = build_huffman_tree(freq_map)

    # 生成哈弗曼编码
    huffman_code = encode_huffman_tree(root)

    # 输出编码后的字符串
    encoded_data = "".join([huffman_code[char] for char in data])

    return encoded_data, huffman_code


def huffman_decoding(encoded_data, huffman_code):
    # 创建字符->编码的映射
    code_to_char = {code: char for char, code in huffman_code.items()}

    decoded_data = ""
    current_code = ""

    # 遍历编码后的数据，逐步匹配编码到字符
    for bit in encoded_data:
        current_code += bit
        if current_code in code_to_char:
            decoded_data += code_to_char[current_code]
            current_code = ""

    return decoded_data


# 测试哈弗曼编码和解码
if __name__ == "__main__":
    data = "huffman tree example"

    print("原始数据: ", data)

    # 编码
    encoded_data, huffman_code = huffman_encoding(data)
    print("哈弗曼编码后的数据: ", encoded_data)
    print("哈弗曼编码表: ", huffman_code)

    # 解码
    decoded_data = huffman_decoding(encoded_data, huffman_code)
    print("解码后的数据: ", decoded_data)
