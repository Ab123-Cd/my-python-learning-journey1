def avg_score(stu_list):
    # 存储每位同学的平均分
    avg_list = []
    # 遍历每位同学的信息
    for student in stu_list:
        # 提取姓名
        name = student[0]
        # 提取三门课程成绩（切片获取索引1到末尾的元素）
        scores = student[1:]
        # 计算平均分（保留1位小数）
        average = round(sum(scores) / len(scores), 1)
        avg_list.append(average)
        # 打印每位同学的平均分
        print(f"{name} 的平均分是 {average}")
    
    # 计算并返回全班总平均分（保留1位小数）
    total_avg = round(sum(avg_list) / len(avg_list), 1)
    return total_avg

# 主程序
if __name__ == "__main__":
    # 示例成绩列表
    scores = [
        ["Alice", 85, 92, 78],
        ["Bob", 79, 95, 83],
        ["Carol", 92, 89, 94],
        ["Dave", 78, 67, 88],
        ["Eve", 96, 90, 91]
    ]
    # 调用函数并获取总平均分
    total_average = avg_score(scores)
    # 输出全班总平均分
    print(f"全班总平均分是 {total_average}")
