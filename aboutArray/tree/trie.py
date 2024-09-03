# 前缀树的基本概念
# 节点：
# 每个节点代表一个字符。
# 根节点通常为空节点，不包含任何字符。
# 每个节点可以有多个子节点，每个子节点对应一个不同的字符。
# 边：
# 每条边代表一个字符，连接两个节点。
# 从根节点到任意一个叶子节点的路径构成一个完整的字符串。
# 字符串存储：
# 一个字符串存储为从根节点到叶子节点的一条路径。
# 每个节点可以标记为字符串的结尾，表示该路径上的字符序列是一个完整的单词或字符串。
# 前缀树的特点
# 空间效率：
# 前缀树通过共享公共前缀来节省空间。例如，单词 "apple" 和 "app" 共享相同的前缀 "app"。
# 查询效率：
# 查询一个字符串是否存在的时间复杂度为 O(L)，其中 L 是字符串的长度。这是因为每个字符只需要一次访问即可确定路径。
# 插入和删除操作：
# 插入一个新的字符串只需要沿着字符路径创建新的节点。
# 删除一个字符串只需要移除对应的路径上的标记，如果路径上的节点没有其他子节点，则可以删除该节点。
# 前缀树的应用
# 自动补全：
# 在搜索引擎、输入法等应用中，前缀树可以用于快速检索与输入前缀匹配的建议。
# 拼写检查：
# 可以用于检查输入的单词是否存在于词典中。
# 字符串匹配：
# 用于模式匹配，例如在文本编辑器中搜索特定的单词或模式。
# IP 路由表：
# 在网络路由中，前缀树可以用于高效地查找最长前缀匹配。

class Node:
    def __init__(self, value):
        self.data = value
        self.nexts = [None] * 26
        self.pre = 0
        self.end = 0


def letter_to_order(letter):
    # 小写字母 'a' 的 ASCII 码是 97
    ascii_a = ord('a')
    # 计算字母相对于 'a' 的位置
    order = ord(letter) - ascii_a
    return order


class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert_trie(self, word):
        current_node = self.root
        for w in range(len(word)):
            index = letter_to_order(word[w])

            # 如果对应位置为空，创建新的节点
            if not current_node.nexts or current_node.nexts[index] is None:
                current_node.nexts[index] = Node(word[w])

            # 移动到下一个节点
            current_node = current_node.nexts[index]

            # 记录前缀信息
            current_node.pre += 1

            # 如果是单词最后一个字母，增加结束标记
            if w == len(word) - 1:
                current_node.end += 1


def search_word(trie, word):
    current_node = trie.root
    for w in range(len(word)):
        index = letter_to_order(word[w])
        if current_node.nexts[index] is None:
            return False
        else:
            current_node = current_node.nexts[index]

    # 检查单词结尾，确保这是一个完整的单词
    return current_node.end > 0


def starts_with(self, prefix: str):
    current_node = self.root
    for w in prefix:
        nexts = current_node.nexts
        index = letter_to_order(w)

        if not nexts[index]:
            return 0
        else:
            current_node = nexts[index]
    return current_node.pre


word = 'abcdef'
one_trie = Trie()
one_trie.insert_trie(word)
print(search_word(one_trie, word))
print(search_word(one_trie, "banana"))
one_trie.insert_trie(word)
print(starts_with(one_trie, "abcdef"))
