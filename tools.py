
from dotenv import load_dotenv
# 加载 .env 文件中的环境变量
load_dotenv()

import os
import json

# ============================================================
# 北交大校园知识库（每条都标注来源，查得到才答）
# 原则：不确定的信息，宁可回答“去官方核实”，也不要编。
# 信息来源：北交大信息中心 ic.bjtu.edu.cn、图书馆 lib.bjtu.edu.cn、
#          北交大官方微信《新生攻略！带你玩转交大》、迎新系统通知等。
# ============================================================
CAMPUS_KB = [
    {
        "keywords": ["一卡通", "校园卡", "饭卡", "挂失", "补卡", "补办", "充值", "圈存", "完美校园", "卡密码"],
        "answer": (
            "【校园一卡通】\n"
            "用途：食堂/超市消费、淋浴、开水、图书借阅、校医院、门禁、网费、机房上机、成绩打印等。\n"
            "充值：用“完美校园”App/小程序，或在自助终端圈存转账（先绑定学校发的中国银行卡）；"
            "充值后要到食堂POS机刷一次或在自助终端点“异常领款”，钱才真正到卡。\n"
            "挂失：自助补卡机 / 完美校园 / 学活一站式服务大厅人工挂失；解挂需本人带证件+卡到大厅信息中心2号窗口。\n"
            "初始密码：身份证号后6位（X用0代替）。\n"
            "人工服务：学生活动中心一层一站式服务大厅1-4号柜台，周一至周五 8:00-11:30、14:00-17:00；电话 51688446/51688476。\n"
            "来源：信息中心 ic.bjtu.edu.cn《校园一卡通使用指南》（2022年12月整理，营业时间可能调整）"
        ),
    },
    {
        "keywords": ["食堂", "餐厅", "吃饭", "学活", "明湖", "清真", "学一", "学二", "学三", "学四", "东区餐厅", "嘉园"],
        "answer": (
            "【主校区主要食堂】\n"
            "· 学活一层 学二餐厅（基本伙）：07:00-09:00 / 11:00-13:00 / 17:00-19:00\n"
            "· 学活一层西北侧 西式快餐：10:00-21:00\n"
            "· 学活二层 学三餐厅（各地风味）：07:00-14:00 / 17:00-21:00\n"
            "· 学活三层 清真餐厅：07:00-09:00 / 11:00-13:00 / 17:00-19:00\n"
            "· 明湖一层 学一餐厅（基本伙）；明湖二层 东快餐厅；明湖三层 明湖餐厅\n"
            "· 嘉园东侧 学四餐厅、学四风味餐厅\n"
            "东校区还有东区餐厅等；学苑区有学苑美食厅等。\n"
            "来源：北交大官方微信《新生攻略！带你玩转交大》（2023版，节假日营业时间可能变，以现场为准）"
        ),
    },
    {
        "keywords": ["浴室", "澡堂", "洗澡", "公共浴室", "淋浴"],
        "answer": (
            "公共浴室大致开放时间：主校区 15:00-23:30；学苑区 16:00-24:00；东校区 17:00-23:30。\n"
            "来源：北交大官方微信《新生攻略！带你玩转交大》（2023版，不同宿舍楼可能有差异，以现场为准）"
        ),
    },
    {
        "keywords": ["图书馆", "自习室", "借书", "阅览室", "开馆"],
        "answer": (
            "【主区图书馆】\n"
            "· 三层图书外借库、四层阅览室：周一至周日 8:00-22:00\n"
            "· 五层自习室：周一至周日 7:00-22:00（需网上预约）\n"
            "· 二层书架周边也有自习座位\n"
            "【东校区馆】周一至周日 8:00-22:00\n"
            "人工服务（办证、咨询）：周一至周五 8:00-12:00、14:00-17:30。\n"
            "来源：北交大图书馆 lib.bjtu.edu.cn 与官方微信新生攻略，具体以图书馆当天公告为准"
        ),
    },
    {
        "keywords": ["选课", "教务", "查成绩", "课表", "门户", "mis", "教学支撑平台"],
        "answer": (
            "选课/查课表/查成绩：登录北京交通大学信息门户 https://mis.bjtu.edu.cn，"
            "点“教务系统”进入“教学支撑平台”。每学期选课一般分“正选”和开学初“退补选”。\n"
            "来源：学校选课通知"
        ),
    },
    {
        "keywords": ["vpn", "校园网", "上网", "无线", "wifi", "网络", "邮箱"],
        "answer": (
            "校外访问校内资源：https://vpn.bjtu.edu.cn（客户端+OTP动态口令）；"
            "访问图书馆数字资源可用 libvpn.bjtu.edu.cn（全代理）。\n"
            "网络/一卡通/邮箱等问题指南集中在 ic.bjtu.edu.cn。\n"
            "来源：信息中心《北京交通大学VPN使用指南》"
        ),
    },
    {
        "keywords": ["官网", "网站", "网址", "迎新", "welcome", "公众号", "信息门户", "办事大厅"],
        "answer": (
            "常用官方入口：\n"
            "· 学校官网 www.bjtu.edu.cn\n"
            "· 信息门户（选课/教务/办事）mis.bjtu.edu.cn\n"
            "· 迎新系统 welcome.bjtu.edu.cn\n"
            "· 网络/一卡通 ic.bjtu.edu.cn\n"
            "· 图书馆 lib.bjtu.edu.cn\n"
            "· VPN vpn.bjtu.edu.cn\n"
            "官方公众号：北京交通大学。"
        ),
    },
    {
        "keywords": ["奖学金", "国家奖学金", "励志奖学金", "助学金", "评优"],
        "answer": (
            "本科生国家奖学金：8000元/人/年，由中央政府出资，一般每年9-10月按学校通知评选；"
            "名额、条件以当年通知和《学生手册》为准。另有国家励志奖学金、助学金、校级学习优秀奖学金等。\n"
            "来源：信息公开网《北京交通大学本科生国家奖学金实施细则》（2024年9月1日起施行）"
        ),
    },
    {
        "keywords": ["宿舍", "门禁", "熄灯", "断电", "住宿", "公寓", "床位", "入住"],
        "answer": (
            "宿舍门禁/熄灯/断电我没有查到学校官方统一规定，网上说法互相矛盾。\n"
            "以你所在宿舍楼值班室通知、《学生手册》和后勤通知为准，不确定直接问楼管阿姨。"
        ),
    },
    {
        "keywords": ["校车", "班车", "接站", "摆渡"],
        "answer": (
            "日常班车：目前没查到学校官方公开的固定时刻表；"
            "新生报到当天学校在北京站/北京西站/北京朝阳站设有接站校车。\n"
            "来源：《北交大2026级新生报到须知》；日常通勤关注后勤通知"
        ),
    },
]


def search(query: str) -> str:
    """校园信息查询工具：只查上面有来源的知识库，不联网。"""
    query = query.strip()
    if not query:
        return "请输入要查询的内容，例如：校园卡怎么挂失？图书馆几点关门？"
    matched = []
    for entry in CAMPUS_KB:
        if any(keyword in query for keyword in entry["keywords"]):
            matched.append(entry["answer"])
    if matched:
        result = []
        for answer in matched:
            if answer not in result:
                result.append(answer)
        return "\n\n".join(result)
    return (
        f"我的知识库里还没有「{query}」的可靠资料。\n"
        "可以先试着问：校园卡、食堂、浴室、图书馆、自习、选课、VPN、奖学金、宿舍、校车。\n"
        "更权威的信息请关注“北京交通大学”官方公众号或访问 www.bjtu.edu.cn。"
    )

DATA_FILE = "todo.json"

def add_todo(task: str) -> str:
    """添加一条待办事项。"""
    todos = []   # ① 先建一个空列表

    # ② 如果 todo.json 存在，就把它读出来
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            todos = json.load(f)   # ← 空1：把文件内容读成列表（json 的"读"）

    # ③ 把新任务加进列表
    todos.append(task)      # ← 空2：往列表里加东西用什么方法？

    # ④ 写回文件
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)              # ← 空3：把 todos 写进文件（json 的"写"）

    return f"已添加待办：{task}，当前共 {len(todos)} 条"

class ToolExecutor:
    """
    一个工具执行器，负责管理和执行工具。
    """
    def __init__(self):
        self.tools: dict = {}

    def registerTool(self, name: str, description: str, func):
        """
        向工具箱中注册一个新工具。
        """
        if name in self.tools:
            print(f"警告：工具 '{name}' 已存在，将被覆盖。")

        self.tools[name] = {"description": description, "func": func}
        print(f"工具 '{name}' 已注册。")

    def getTool(self, name: str):
        """
        根据名称获取一个工具的执行函数。
        """
        return self.tools.get(name, {}).get("func")

    def getAvailableTools(self) -> str:
        """
        获取所有可用工具的格式化描述字符串。
        """
        return "\n".join([
            f"- {name}: {info['description']}"
            for name, info in self.tools.items()
        ])


# --- 工具初始化与使用示例 ---
if __name__ == '__main__':
    # 1. 初始化工具执行器
    toolExecutor = ToolExecutor()

    # 2. 注册我们的校园查询工具
    search_description = "北交大校园信息查询工具：只查内置的、带来源的校园知识库。问校园卡、食堂、浴室、图书馆、选课、VPN、奖学金、宿舍等校园问题时使用。"
    toolExecutor.registerTool("Search", search_description, search)

    # 3. 打印可用的工具
    print("\n--- 可用的工具 ---")
    print(toolExecutor.getAvailableTools())

    # 4. 模拟一次 Action 调用
    print("\n--- 执行 Action: Search['图书馆几点关门'] ---")
    tool_name = "Search"
    tool_input = "图书馆几点关门"

    tool_function = toolExecutor.getTool(tool_name)
    if tool_function:
        observation = tool_function(tool_input)
        print("--- 观察 (Observation) ---")
        print(observation)
    else:
        print(f"错误：未找到名为 '{tool_name}' 的工具。")
