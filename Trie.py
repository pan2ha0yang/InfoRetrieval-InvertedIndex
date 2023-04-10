class TrieNode(object):
    def __init__(self):
        self.children = {}  # 记录当前结点的子结点
        self.is_leaf = False  # 当前结点是否表示一个单词


class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.count = 0  # 单词树中单词的总量

    def insert(self, word):
        curr = self.root
        for c in word:
            if not curr.children.get(c, None):
                new_node = TrieNode()
                curr.children[c] = new_node
            curr = curr.children[c]
        curr.is_leaf = True
        self.count += 1
        return

    def insert_many(self, words):
        for word in words:
            self.insert(word)
        return

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_leaf

    def prefix_match(self, prefix):
        # 以字符串为路径找到最后一个字符在字典中的节点
        curr = self.root
        for c in prefix:
            try:
                curr = curr.children[c]
            # 路径不存在字典中，则直接返回原词
            except:
                # 搜索单词如果不存在字典树的路径中，我们直接返回这个单词
                return "'" + str(prefix) + "'" + " Not Exist!"

        # 递归遍历字典树
        def get_complete_words(pre, node):
            word_list = []
            # 叶节点退出递归，返回完整字符串
            if node.is_leaf:
                word_list.append(pre)
                return word_list
            # 通过字典树的每个分支对之前的字符串进行补充
            for c in list(node.children):
                word_list.extend(get_complete_words(pre + str(c), node.children[c]))
            # 返回最终结果
            return word_list

        return get_complete_words(prefix, curr)
