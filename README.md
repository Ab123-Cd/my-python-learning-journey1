# my-python-learning-journey1
记录我从「Hello World」到「小项目」的所有脚印 

1. 项目简介  
本仓库用于归档本学期编写的 Python 练习与实验，既是代码备份，也是个人作品集。
目前包含 2 个我最满意的脚本：  
- `movie_recommender.py` – 基于协同过滤的简易电影推荐系统（CLI 版）  
- `data_visualizer.py` – 使用 pandas + matplotlib 对 COVID-19 公开数据做可视化分析  

2. 运行环境  
- Python ≥ 3.9  
- 依赖列表：`requirements.txt` 已备好，一键安装即可  

3. 快速开始  
```bash
# 克隆仓库
git clone https://github.com/你的用户名/My-Python-Learning-Journey.git
cd My-Python-Learning-Journey
# 创建并激活虚拟环境（可选）
python -m venv venv
source venv/bin/activate  # Windows 用 venv\Scripts\activate
# 安装依赖
pip install -r requirements.txt
# 运行电影推荐
python movie_recommender.py --user 15 --topk 5
# 运行数据可视化
python data_visualizer.py --source covid19.csv --plot-type line
```

4. 代码说明  
4.1 movie_recommender.py  
- 使用 `surprise` 库实现 SVD 协同过滤  
- 数据集：`ml-100k`（已放 `data/` 目录，100 KB 级，GitHub 可直接托管）  
- 输出：给定用户 ID，返回 Top-N 推荐电影及预测评分  
4.2 data_visualizer.py  
- 读取 CSV → 数据清洗 → 绘图三步走  
- 支持折线/柱状/散点三种图形，通过 CLI 参数切换  
- 结果自动保存到 `output/` 目录，高清 PNG & PDF 双格式  

5. 目录结构  
My-Python-Learning-Journey/
├─ README.md
├─ requirements.txt
├─ movie_recommender.py
├─ data_visualizer.py
├─ data/
│  ├─ ml-100k/
│  └─ covid19.csv
└─ output/          # 运行后自动生成

6. 更新日志  
日期	说明	
2025-11-20	初版上传，含 2 个核心脚本	
2025-11-22	补充 `requirements.txt` 与文档	

7. 学习心得与规划  
7.1 本次任务带来的启发  
1. 浏览他人高 Star Python 项目让我第一次体会到「好仓库 = 好 README + 好目录 + 好 commit 记录」。  
2. 用 issue 与 project 板做需求管理，比本地写 TXT 更高效。  
3. 公开代码天然带“代码审查”属性，促使我把变量命名、函数注释写到“能见人”的水平。  

7.2 未来利用计划  
- 每学完一章《Fluent Python》就开一个 branch，合并时写 summary，形成“知识快照”。  
- 把 LeetCode 周赛题解放到 `leetcode/` 目录，用 GitHub Actions 自动跑单测，绿色 √ 提升成就感。  
