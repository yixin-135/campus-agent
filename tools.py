from dotenv import load_dotenv
# 加载 .env 文件中的环境变量
load_dotenv()

import os
from typing import Dict, Any
import json

def search(query: str) -> str:
    """校园信息查询工具。"""
    campus_info = {
        "图书馆": "图书馆08:00-22:00开放，共5层，自习座位1200个",
        "食堂": "学一食堂06:30-20:30，学二食堂06:30-21:00",
    }
    for key, value in campus_info.items():
        if key in query:
            return f"查询到：{value}"
    return f"未找到关于「{query}」的校园信息"

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

from typing import Dict, Any

class ToolExecutor:
    """
    一个工具执行器，负责管理和执行工具。
    """
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}

    def registerTool(self, name: str, description: str, func: callable):
        """
        向工具箱中注册一个新工具。
        """
        if name in self.tools:
            print(f"警告：工具 '{name}' 已存在，将被覆盖。")
        
        self.tools[name] = {"description": description, "func": func}
        print(f"工具 '{name}' 已注册。")

    def getTool(self, name: str) -> callable:
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

    # 2. 注册我们的实战搜索工具
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolExecutor.registerTool("Search", search_description, search)
    
    # 3. 打印可用的工具
    print("\n--- 可用的工具 ---")
    print(toolExecutor.getAvailableTools())

    # 4. 智能体的Action调用，这次我们问一个实时性的问题
    print("\n--- 执行 Action: Search['英伟达最新的GPU型号是什么'] ---")
    tool_name = "Search"
    tool_input = "英伟达最新的GPU型号是什么"

    tool_function = toolExecutor.getTool(tool_name)
    if tool_function:
        observation = tool_function(tool_input)
        print("--- 观察 (Observation) ---")
        print(observation)
    else:
        print(f"错误：未找到名为 '{tool_name}' 的工具。")

