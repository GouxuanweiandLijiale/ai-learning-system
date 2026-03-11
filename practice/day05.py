#classwork01
#作业1：最基础函数
# 定义函数 introduce(name)，返回一句话：
# "我是{name}，今天在学习Python函数。"
# 要求：
# 定义函数
# 调用两次，传不同名字
# 用 print() 打印结果
# 示例输出：
# 我是小李，今天在学习Python函数。
# 我是AI学习者，今天在学习Python函数。

def introduce(name):
    message = "hello," + name + ",today I am learning Python function."
    return message
print(introduce("小李"))
print(introduce("AI学习者"))
# 作业2：默认参数函数
# 定义函数 check_goal(minutes, goal=50)。
# 要求：
# 如果 minutes >= goal，返回：
# "达标：学习了XX分钟"
# 否则返回：
# "未达标：还差XX分钟"
# 至少测试 3 次：
# 一次默认 goal
# 一次不达标
# 一次手动传 goal
def check_goal(minutes,goal=50):
    if minutes >= goal:
        return f"ok:you studied for {minutes} minutes"
    else:
        return f"未达标：还差{goal - minutes}分钟"
print(check_goal(60))
print(check_goal(40))
print(check_goal(65,goal=70))
# 作业3：多返回值
# 定义函数 calc_scores(scores)，接收一个列表，比如：
# [80, 90, 70]
# 返回：
# 总分
# 科目数
# 平均分
# 要求：
# 写出函数
# 正确接收三个返回值
# 用 f-string 打印结果
# 示例输出：
# 共3科，总分240，平均80.0
def calc_scores(scores):
    total = sum(r["scores"] for r in scores)
    count = len(scores)
    average = total / count
    return total, count, average
samples = [
    {"scores" : 60 },
    {"scores" : 67 },
    {"scores" : 68 }
]
total, count, average = calc_scores(samples)
print(f"all {count} subjects,total {total} points, average {average} points") 
# 作业4：封装字典
# 定义函数 build_book(title, author, pages, note="无")，返回一个字典。
# 要求：
# 返回的字典包含：
# title
# author
# pages
# note
# 调用一次生成一本书的信息
# 用 for k, v in book.items() 打印出来
def build_book(title,author,pages,notes="无"):
    return{
        "title":title,
        "author":author,
        "pages":pages,
        "notes":notes
    }
book = build_book("python_teaching","XuanweiGou","100","good book")
for k,v in book.items():
    print(f"{k}:{v}")                      
# 作业5：综合题
# 定义一个函数 make_study_record(date, minutes, topic, feeling="还行")，返回一条学习记录字典。
# 然后：
# 调用 3 次，创建 3 条记录
# 把它们放进一个列表
# 遍历输出
# 格式示例：
def make_study_record(date,minutes,topic,feeling="ok"):
    return{
        "date":date,
        "minutes":minutes,
        "topic":topic,
        "feeling":feeling
    }
records = [
    make_study_record("2026-06-01",60,"Python函数","good"),
    make_study_record("2026-06-02",45,"Python数据结构"),
    make_study_record("2026-06-03",30,"Python面向对象","not bad")
]
for record in records:
    print(f"date:{record['date']},minute:{record['minutes']},topic:{record['topic']},feeling:{record['feeling']}")

# 最优版本：
# # 作业1
# def introduce(name):
#     return f"我是{name}，今天在学习Python函数。"

# print(introduce("小李"))
# print(introduce("AI学习者"))


# # 作业2
# def check_goal(minutes, goal=50):
#     if minutes >= goal:
#         return f"达标：学习了{minutes}分钟"
#     else:
#         return f"未达标：还差{goal - minutes}分钟"

# print(check_goal(60))
# print(check_goal(40))
# print(check_goal(65, goal=70))


# # 作业3
# def calc_scores(scores):
#     total = sum(scores)
#     count = len(scores)
#     average = total / count
#     return total, count, average

# scores = [60, 67, 68]
# total, count, average = calc_scores(scores)
# print(f"共{count}科，总分{total}，平均{average:.1f}")


# # 作业4
# def build_book(title, author, pages, note="无"):
#     return {
#         "title": title,
#         "author": author,
#         "pages": pages,
#         "note": note
#     }

# book = build_book("python_teaching", "XuanweiGou", 100, "good book")
# for k, v in book.items():
#     print(f"{k}: {v}")


# # 作业5
# def make_study_record(date, minutes, topic, feeling="还行"):
#     return {
#         "date": date,
#         "minutes": minutes,
#         "topic": topic,
#         "feeling": feeling
#     }

# records = [
#     make_study_record("2026-06-01", 60, "Python函数", "good"),
#     make_study_record("2026-06-02", 45, "Python数据结构"),
#     make_study_record("2026-06-03", 30, "Python面向对象", "not bad")
# ]

# for record in records:
#     print(f"{record['date']} {record['minutes']}分钟 {record['topic']} {record['feeling']}")







