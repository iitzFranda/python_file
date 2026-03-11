"""
快速测试 GPT 调用是否成功
"""
import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ 错误: 未找到 OPENAI_API_KEY 环境变量")
    print("\n请按以下步骤设置:")
    print("1. 创建 .env 文件: OPENAI_API_KEY=your-api-key-here")
    print("2. 或设置系统环境变量")
    exit(1)

client = OpenAI(api_key=api_key)

try:
    print("正在测试 GPT API 连接...")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "你好，请简短回答：1+1=?"}
        ],
        max_tokens=100
    )
    
    print("✅ 连接成功！")
    print(f"\nGPT 回复: {response.choices[0].message.content}")
    print(f"\n使用费用信息:")
    print(f"  - 输入 tokens: {response.usage.prompt_tokens}")
    print(f"  - 输出 tokens: {response.usage.completion_tokens}")
    print(f"  - 总共 tokens: {response.usage.total_tokens}")
    
except Exception as e:
    print(f"❌ 出错了: {e}")
    print("\n可能的原因:")
    print("  1. API 密钥无效或已过期")
    print("  2. 账户没有额度")
    print("  3. 网络连接问题")
