import Trie

if __name__ == '__main__':
    trie_forward = Trie.Trie()
    trie_reverse = Trie.Trie()

    # 构建字典树数据
    list_forward = ["procent", "prodecent", "progress", "peach", "percent", "absent"]
    list_reverse = []
    for w in list_forward:
        list_reverse.append(w[::-1])

    trie_forward.insert_many(list_forward)
    trie_reverse.insert_many(list_reverse)

    # 这里以pro*cent为例
    prefix = "pro"  # 前缀
    suffix = "cent"  # 后缀

    list1 = trie_forward.prefix_match(prefix)
    list2 = []
    tmp = trie_reverse.prefix_match(suffix[::-1])
    for w in tmp:
        list2.append(w[::-1])

    # 返回前后缀匹配的交集
    result = [w for w in list1 if w in list2]
    print(result)
