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
