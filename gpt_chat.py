"""
OpenAI GPT 聊天程序
使用前需要安装: pip install openai
使用前需要设置环境变量或创建 .env 文件
"""

import os
from openai import OpenAI

# 从环境变量读取 API 密钥
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ 错误: 未找到 OPENAI_API_KEY 环境变量")
    print("\n请按以下步骤设置:")
    print("1. 创建 .env 文件:")
    print("   OPENAI_API_KEY=your-api-key-here")
    print("2. 或设置系统环境变量")
    exit(1)

# 初始化客户端
client = OpenAI(api_key=api_key)

def chat_with_gpt(user_message):
    """
    调用 GPT 进行单次聊天
    
    Args:
        user_message: 用户输入的消息
    
    Returns:
        GPT 的回复
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 或使用 "gpt-4o" 等其他模型
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=0.7,  # 控制回复的创意程度 (0-2)
        max_tokens=500    # 最大回复长度
    )
    
    return response.choices[0].message.content


def interactive_chat():
    """
    交互式聊天模式
    输入 'exit' 或 'quit' 退出
    """
    print("=" * 50)
    print("欢迎使用 GPT 聊天程序")
    print("输入您的问题，或输入 'exit' 退出")
    print("=" * 50)
    
    while True:
        user_input = input("\n您: ").strip()
        
        if user_input.lower() in ['exit', 'quit', '退出']:
            print("谢谢使用！再见！")
            break
        
        if not user_input:
            print("请输入有效内容")
            continue
        
        print("\nGPT 正在思考...")
        try:
            response = chat_with_gpt(user_input)
            print(f"\nGPT: {response}")
        except Exception as e:
            print(f"出错了: {e}")


def batch_process(questions: list):
    """
    批量处理多个问题
    
    Args:
        questions: 问题列表
    
    Returns:
        包含问题和回答的列表
    """
    results = []
    for i, question in enumerate(questions, 1):
        print(f"处理第 {i}/{len(questions)} 个问题...")
        try:
            answer = chat_with_gpt(question)
            results.append({
                "question": question,
                "answer": answer
            })
        except Exception as e:
            print(f"处理问题 '{question}' 时出错: {e}")
    
    return results


if __name__ == "__main__":
    # 方式 1: 交互式聊天
    interactive_chat()
    
    # 方式 2: 单个问题（取消注释使用）
    # response = chat_with_gpt("你好，你是谁？")
    # print(response)
    
    # 方式 3: 批量处理（取消注释使用）
    # questions = ["什么是机器学习？", "Python 如何调用 API？"]
    # results = batch_process(questions)
    # for r in results:
    #     print(f"Q: {r['question']}\nA: {r['answer']}\n")
