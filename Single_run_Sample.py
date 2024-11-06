# -*- coding: gbk -*-
import start
import sixtyfour_gua_map
import requests
import tkinter as tk
from tkinter import messagebox
import sys  # ���� sys ģ��
has_run = False

def process_question():
    global has_run
    if not has_run:
    # ��ȡ������Ϣ
        bengua = start.bengua
        benguaxiang = sixtyfour_gua_map.sixtyfour_hexagrams.get(bengua)
        bianguaxiang = ""
        if start.shifoubiangua == 1:
            biangua = start.biangua
            bianguaxiang = sixtyfour_gua_map.sixtyfour_hexagrams.get(biangua)

        # ��ӡ����
        def draw_lines_and_text(canvas):
            z = 20
            canvas.create_text(95, 20, text="����", font=("Microsoft YaHei", 20), fill="black")
            for i in range(6):
                z += 20
                if bengua[i] == '1':
                    canvas.create_line(50, z, 140, z, fill="black", width=5)
                else:
                    canvas.create_line(50, z, 80, z, fill="black", width=5)
                    canvas.create_line(110, z, 140, z, fill="black", width=5)
            if start.shifoubiangua == 1:
                z = 20
                canvas.create_text(205, 20, text="����", font=("Microsoft YaHei", 20), fill="black")
                for i in range(6):
                    z += 20
                    if biangua[i] == '1':
                        canvas.create_line(160, z, 250, z, fill="black", width=5)
                    else:
                        canvas.create_line(160, z, 190, z, fill="black", width=5)
                        canvas.create_line(220, z, 250, z, fill="black", width=5)
        question = entry.get()  # ��ȡ������е��ı�
        # ���������Ӵ���������߼�
        # �滻���±���Ϊ���ʵ��ֵ
        personal_access_token = "pat_8Of828MmaEjzl22MkEBpZU61DwFCb4IMF5F36MCxZ3RqChNt06MiRfVO28Nvl552"
        bot_id = "7386918888384397331"
        your_query = f"{question} ����{benguaxiang} ����{bianguaxiang}"

        # ��������ͷ
        headers = {
            'Authorization': f'Bearer {personal_access_token}',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Host': 'api.coze.cn',
            'Connection': 'keep-alive'
        }

        # ����������
        payload = {
            "conversation_id": "123",
            "bot_id": bot_id,
            "user": "CustomizedString123",
            "query": your_query,
            "stream": False
        }

        # ����POST����
        response = requests.post('https://api.coze.cn/open_api/v2/chat', headers=headers, json=payload)

        # ��ӡ��Ӧ״̬�����Ӧ����
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
            processed_result = '����ʧ�ܣ�״̬�룺', response.status_code
        desired_output = processed_result[:processed_result.index('{', 1)]
        canvas.create_text(canvas_width // 2, (canvas_height // 2)+100, text=desired_output, font=("Microsoft YaHei", 10), fill="black",
                           width=canvas_width - 20)
        has_run = True
    else:
        # ��ʾ��ʾ��Ϣ
        messagebox.showinfo("��ʾ", "���������г���")
        # �رճ���
        root.quit()
        sys.exit()  # ��ֹ����

# ����������
root = tk.Tk()
root.title("��س����")


# ��ӱ�ǩ
label = tk.Label(root, text="�������������⣺")
label.pack(pady=10)
# ����س����¼�
def on_enter_pressed(event):
    process_question()
# ��������
entry = tk.Entry(root, width=50, justify='center')
entry.pack(pady=10)
entry.bind("<Return>", on_enter_pressed)

# ��Ӵ���ť
process_button = tk.Button(root, text="����", command=process_question)
process_button.pack(pady=10)

# ������ѭ��
root.mainloop()
