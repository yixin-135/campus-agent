# campus-agent · ReAct 校园助手

一个基于 **ReAct 架构** + **DeepSeek API** 的命令行智能体：能通过「思考 → 行动 → 观察」循环，自主调用工具完成校园信息查询、待办管理等任务。

## ✨ 功能

- **校园信息查询**：问"图书馆几点关门"，Agent 自动调用 `Search` 工具检索并回答
- **待办添加**：说"帮我添加一条待办"，Agent 调用 `AddTodo` 工具写入 `todo.json`
- **自主决策**：Agent 判断何时该调工具、何时该结束回答（`Finish`）

## 🛠 技术栈

- Python 3.12
- DeepSeek API（`deepseek-chat`）
- ReAct 架构（Reason + Act 循环）
- JSON 文件持久化

## 🚀 快速开始

```bash
# 1. 克隆
git clone https://github.com/yixin-135/campus-agent.git
cd campus-agent

# 2. 配置 API Key（创建 .env 文件）
# LLM_API_KEY=你的DeepSeek Key
# LLM_MODEL_ID=deepseek-chat
# LLM_BASE_URL=https://api.deepseek.com
# LLM_TIMEOUT=60

# 3. 安装依赖
pip install openai python-dotenv

# 4. 运行
python agent.py
```

## 🧠 运行原理

Agent 遵循 ReAct 循环：

```
Thought（思考）→ Action（调用工具）→ Observation（观察结果）→ 再思考 → ... → Finish（回答）
```

- `llm_client.py`：封装 DeepSeek API 调用
- `tools.py`：工具注册与执行（校园信息查询 / 待办）
- `agent.py`：ReAct 主循环 + 输出解析

## 📁 目录结构

```
campus-agent/
├── agent.py          # ReAct 主循环
├── tools.py          # 工具定义（Search / AddTodo）
├── llm_client.py     # LLM 客户端封装
├── .gitignore        # 忽略 .env 等敏感文件
└── README.md
```

## 📷 运行效果

用户说「帮我添加一条待办：周五前交软工作业」，Agent 自主完成 思考 → 调用工具 → 确认 的完整流程：

```
工具 'Search' 已注册。
工具 'AddTodo' 已注册。

--- 第 1 步 ---
🧠 正在调用 deepseek-chat 模型...
✅ 大语言模型响应成功:
Thought: 用户要求添加一条待办事项，内容明确为"周五前交软工作业"。这不需要搜索外部信息，直接使用AddTodo工具即可。

Action: AddTodo[周五前交软工作业]
🤔 思考: 用户要求添加一条待办事项，内容明确为"周五前交软工作业"。这不需要搜索外部信息，直接使用AddTodo工具即可。
🎬 行动: AddTodo[周五前交软工作业]
👀 观察: 已添加待办：周五前交软工作业，当前共 2 条

--- 第 2 步 ---
🧠 正在调用 deepseek-chat 模型...
✅ 大语言模型响应成功:
Thought: 工具已成功执行，待办事项已添加。现在我可以向用户确认操作已完成。
Action: Finish[已成功添加待办事项：周五前交软工作业。当前共有2条待办事项。]
🤔 思考: 工具已成功执行，待办事项已添加。现在我可以向用户确认操作已完成。
🎉 最终答案: 已成功添加待办事项：周五前交软工作业。当前共有2条待办事项。
```

