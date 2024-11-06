# -*- coding: gbk -*-
import start
import sixtyfour_gua_map
import requests
import tkinter as tk
from tkinter import messagebox
import sys  # 导入 sys 模块
has_run = False

def process_question():
    global has_run
    if not has_run:
    # 获取卦象信息
        bengua = start.bengua
        benguaxiang = sixtyfour_gua_map.sixtyfour_hexagrams.get(bengua)
        bianguaxiang = ""
        if start.shifoubiangua == 1:
            biangua = start.biangua
            bianguaxiang = sixtyfour_gua_map.sixtyfour_hexagrams.get(biangua)

        # 打印卦象
        def draw_lines_and_text(canvas):
            z = 20
            canvas.create_text(95, 20, text="本卦", font=("Microsoft YaHei", 20), fill="black")
            for i in range(6):
                z += 20
                if bengua[i] == '1':
                    canvas.create_line(50, z, 140, z, fill="black", width=5)
                else:
                    canvas.create_line(50, z, 80, z, fill="black", width=5)
                    canvas.create_line(110, z, 140, z, fill="black", width=5)
            if start.shifoubiangua == 1:
                z = 20
                canvas.create_text(205, 20, text="变卦", font=("Microsoft YaHei", 20), fill="black")
                for i in range(6):
                    z += 20
                    if biangua[i] == '1':
                        canvas.create_line(160, z, 250, z, fill="black", width=5)
                    else:
                        canvas.create_line(160, z, 190, z, fill="black", width=5)
                        canvas.create_line(220, z, 250, z, fill="black", width=5)
        question = entry.get()  # 获取输入框中的文本
        # 这里可以添加处理问题的逻辑
        # 替换以下变量为你的实际值
        personal_access_token = "pat_8Of828MmaEjzl22MkEBpZU61DwFCb4IMF5F36MCxZ3RqChNt06MiRfVO28Nvl552"
        bot_id = "7386918888384397331"
        your_query = f"{question} 本卦{benguaxiang} 变卦{bianguaxiang}"

        # 构造请求头
        headers = {
            'Authorization': f'Bearer {personal_access_token}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': 'api.coze.cn',
            'Connection': 'keep-alive'
        }

        # 构造请求体
        payload = {
            "conversation_id": "123",
            "bot_id": bot_id,
            "user": "CustomizedString123",
            "query": your_query,
            "stream": False
        }

        # 发送POST请求
        response = requests.post('https://api.coze.cn/open_api/v2/chat', headers=headers, json=payload)

        # 打印响应状态码和响应内容
        if response.ok:
            response.data = response.json()
            processed_result = ""
            canvas_width = 300
            canvas_height = 400
            canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
            canvas.pack(pady=20)
            draw_lines_and_text(canvas)
            for message in response.data['messages']:
                processed_result += f"{message['content']}\n"
        else:
            processed_result = '请求失败，状态码：', response.status_code
        desired_output = processed_result[:processed_result.index('{', 1)]
        canvas.create_text(canvas_width // 2, (canvas_height // 2)+100, text=desired_output, font=("Microsoft YaHei", 10), fill="black",
                           width=canvas_width - 20)
        has_run = True
    else:
        # 显示提示信息
        messagebox.showinfo("提示", "请重新运行程序")
        # 关闭程序
        root.quit()
        sys.exit()  # 终止程序

# 创建主窗口
root = tk.Tk()
root.title("六爻算卦")


# 添加标签
label = tk.Label(root, text="请输入您的问题：")
label.pack(pady=10)
# 处理回车键事件
def on_enter_pressed(event):
    process_question()
# 添加输入框
entry = tk.Entry(root, width=50, justify='center')
entry.pack(pady=10)
entry.bind("<Return>", on_enter_pressed)

# 添加处理按钮
process_button = tk.Button(root, text="起卦", command=process_question)
process_button.pack(pady=10)

# 运行主循环
root.mainloop()
