# my-python-learning-journey1 
# My Python Learning Journey

这是一个记录我Python学习历程的仓库，包含了我学习过程中编写的一些有趣和实用的Python程序。

## 项目介绍

### 1. 学生成绩分析系统 (student_score_analyzer.py)
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
这个程序能够计算多名学生的各科平均分，并统计班级总平均分。

**功能特点：**
- 计算每位学生的平均分（保留1位小数）
- 统计班级总平均分
- 支持灵活的学生数据输入

**运行方法：**

python student_score_analyzer.py
代码说明：

使用列表存储学生信息（姓名+各科成绩）

通过切片操作提取成绩数据

使用round()函数控制小数位数

模块化的函数设计，便于维护和扩展

2. 快餐点餐系统 (fast_food_ordering_system.py)
# 定义商品价格字典
price = {"汉堡": 15, "薯条": 8, "可乐": 6, "鸡翅": 12}
# 初始化用于记录的字典和集合
order_count = {}  # 记录每种商品的总份数
ordered_items = set()  # 记录点过的所有商品（去重）
while True:
    # 获取用户输入
    item = input("请输入商品名称（输入“结账”结束）：")
    
    # 判断是否结账
    if item == "结账":
        break
    
    # 检查商品是否存在
    if item not in price:
        print("本店暂无此商品，请重新选择！")
        continue
    
    # 获取商品份数（确保输入合法）
    while True:
        try:
            count = int(input(f"请输入{item}的份数："))
            if count <= 0:
                print("份数必须为正数，请重新输入！")
                continue
            break
        except ValueError:
            print("请输入有效的数字！")
    
    # 更新订单记录
    if item in order_count:
        order_count[item] += count
    else:
        order_count[item] = count
    ordered_items.add(item)

# 计算总价
total = 0
for item, count in order_count.items():
    total += price[item] * count

# 格式化输出订单信息
order_str = []
for item in ordered_items:
    order_str.append(f"{item}×{order_count[item]}")
print(f"您点了：{' '.join(order_str)}")
print(f"共计 {total} 元，谢谢光临！")
这是一个模拟快餐店点餐的系统，支持商品选择、数量输入和自动结账。

功能特点：

商品菜单管理

输入验证和错误处理

自动计算总价

友好的用户界面

运行方法：
python fast_food_ordering_system.py
代码说明：

使用字典存储商品价格信息

使用集合记录已点商品（去重）

完善的异常处理机制

循环输入直到用户选择结账

环境要求
Python 3.6+

无需额外依赖包

如何运行
克隆本仓库到本地：

git clone https://github.com/你的用户名/My-Python-Learning-Journey.git
进入项目目录：

cd My-Python-Learning-Journey
运行任意一个程序：

python student_score_analyzer.py
或
python fast_food_ordering_system.py

学习心得与规划
浏览GitHub项目的启发
通过浏览GitHub上其他Python项目，我获得了以下启发：

项目结构规范化：优秀的项目都有清晰的文件结构和组织方式

文档的重要性：详细的README文档让项目更易于理解和使用

代码质量：规范的命名、注释和模块化设计让代码更易维护

版本控制：合理的commit记录和分支管理有助于项目追踪

完成本次任务的收获
在完成本次任务的过程中，我学会了：

如何使用Git进行版本控制

如何创建和管理GitHub仓库

如何编写专业的项目文档

如何展示个人编程项目
