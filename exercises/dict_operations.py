"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""


def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作

    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数

    返回:
    - 根据操作返回不同结果
    """
    match operation:
        case "add":
            # 添加学生成绩
            students_dict[args[0]] = args[1]
            return students_dict
        case "remove":
            # 删除学生成绩
            if args[0] in students_dict:
                del students_dict[args[0]]
            return students_dict
        case "update":
            # 更新学生成绩
            if args[0] in students_dict:
                students_dict[args[0]] = args[1]
            return students_dict
        case "get":
            # 查询学生成绩
            return students_dict.get(args[0], None)
        case _:
            return students_dict
    # 请在下方编写代码
    pass
