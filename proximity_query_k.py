import Position
import Term


def load_data(GIRL, FRIEND, POS_G1, POS_G2, POS_G3, POS_F1, POS_F2):
    for i in [1, 7, 20, 72]:
        POS_G1.append(i)
    GIRL.append(1, POS_G1)

    for i in [2, 50, 86]:
        POS_G2.append(i)
    GIRL.append(2, POS_G2)

    for i in [8, 131, 252]:
        POS_G3.append(i)
    GIRL.append(3, POS_G3)

    for i in [3, 70, 99]:
        POS_F1.append(i)
    FRIEND.append(2, POS_F1)

    for i in [19, 81, 132]:
        POS_F2.append(i)
    FRIEND.append(3, POS_F2)


# p1, p2是TermLinkList结构的倒排记录表, k是两个词项的位置在k以内
def positional_intersect(p1, p2, k):
    result = []  # 最终的搜索结果, 以(文档id, 词项1的位置, 词项2的位置)
    p1 = p1.head()  # 取出头节点
    p2 = p2.head()
    while p1 is not None and p2 is not None:  # 当p1, 和 p2 都没有达到最尾部时
        if p1.docID == p2.docID:  # 如果两个词项出现在同一个文档中
            l = []  # 临时变量, 用来存储计算过程中满足位置距离的位置对信息
            pp1 = p1.position.head()
            pp2 = p2.position.head()
            while pp1 is not None:  # 先固定pp1的位置, 循环移动pp2的位置进行检查
                while pp2 is not None:
                    if abs(pp1.pos - pp2.pos) <= k:  # 如果pp1和pp2的距离小于k, 则满足要求
                        l.append(pp2.pos)  # 添加到临时变量
                    elif pp2.pos > pp1.pos:  # 如果pp2当前的位置相对pp1已经超过给定的范围(构不成短语要求), 则停止移动pp2, 后续后把pp1再往前移动一个位置
                        break
                    pp2 = pp2.next  # pp2向后移一个位置
                while l and abs(l[0] - pp1.pos) > k:  # 当每次移动一次pp1时, l里面会存储上一次计算所得的pp2的一些位置,
                    # 这里要过滤那些相对于当前pp1最新位置, 那些不再满足要求的pp2的位置
                    del l[0]
                for p in l:
                    result.append((p1.docID, pp1.pos, p))  # 把最终的结果加入到结果集中
                pp1 = pp1.next  # pp1向前移动一个位置, 重复上次逻辑计算
            p1 = p1.next
            p2 = p2.next
        elif p1.docID < p2.docID:
            p1 = p1.next
        else:
            p2 = p2.next
    return result


if __name__ == '__main__':
    GIRL = Term.TermLinkList()
    FRIEND = Term.TermLinkList()
    POS_G1 = Position.PosLinkList()
    POS_G2 = Position.PosLinkList()
    POS_G3 = Position.PosLinkList()
    POS_F1 = Position.PosLinkList()
    POS_F2 = Position.PosLinkList()

    load_data(GIRL, FRIEND, POS_G1, POS_G2, POS_G3, POS_F1, POS_F2)

    print(positional_intersect(GIRL, FRIEND, 1))
    # 结果是一个元组列表，每个元组代表一个匹配记录，格式为[(文档ID, 词项1位置, 词项2位置), ...]
