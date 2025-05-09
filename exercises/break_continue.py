"""
练习: break和continue语句

描述：
返回从1到n的所有非3的倍数的整数列表。

请补全下面的函数，使用continue语句跳过3的倍数。
"""


def skip_multiples_of_three(n):
    """
    返回从1到n的所有非3的倍数的整数列表

    参数:
    - n: 正整数上限

    返回:
    - 从1到n中所有不是3的倍数的整数列表
    """
    # 创建一个空列表来存储结果
    result = []
    # 请在下方编写代码
    for i in range(1, n + 1):
        # 如果是3的倍数，跳过
        if i % 3 == 0:
            continue
        # 否则，将其添加到结果列表中
        result.append(i)
    return result
    pass
