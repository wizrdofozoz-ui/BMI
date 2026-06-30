import tkinter as tk
from tkinter import messagebox

def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "저체중", "#3498db"
    elif bmi < 23.0:
        return "정상", "#2ecc71"
    elif bmi < 25.0:
        return "과체중", "#f39c12"
    else:
        return "비만", "#e74c3c"

def on_calculate():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("입력 오류", "키와 몸무게는 0보다 커야 합니다.")
            return

        bmi = calculate_bmi(height, weight)
        category, color = get_bmi_category(bmi)

        label_bmi_value.config(text=f"{bmi}", fg=color)
        label_category_value.config(text=category, fg=color)
        frame_result.config(bg="#f0f0f0")

    except ValueError:
        messagebox.showerror("입력 오류", "숫자를 올바르게 입력해주세요.")

def on_reset():
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    label_bmi_value.config(text="-", fg="#333333")
    label_category_value.config(text="-", fg="#333333")

root = tk.Tk()
root.title("BMI 계산기")
root.geometry("400x480")
root.resizable(False, False)
root.configure(bg="#ffffff")

# 제목
tk.Label(root, text="BMI 계산기", font=("맑은 고딕", 20, "bold"),
         bg="#ffffff", fg="#2c3e50").pack(pady=(30, 20))

# 입력 프레임
frame_input = tk.Frame(root, bg="#ffffff")
frame_input.pack(pady=10, padx=40, fill="x")

tk.Label(frame_input, text="키 (cm)", font=("맑은 고딕", 11),
         bg="#ffffff", fg="#555555", anchor="w").grid(row=0, column=0, sticky="w", pady=5)
entry_height = tk.Entry(frame_input, font=("맑은 고딕", 12), width=20,
                        relief="solid", bd=1, justify="center")
entry_height.grid(row=0, column=1, padx=(10, 0), pady=5)

tk.Label(frame_input, text="몸무게 (kg)", font=("맑은 고딕", 11),
         bg="#ffffff", fg="#555555", anchor="w").grid(row=1, column=0, sticky="w", pady=5)
entry_weight = tk.Entry(frame_input, font=("맑은 고딕", 12), width=20,
                        relief="solid", bd=1, justify="center")
entry_weight.grid(row=1, column=1, padx=(10, 0), pady=5)

# 버튼
frame_btn = tk.Frame(root, bg="#ffffff")
frame_btn.pack(pady=20)

btn_calc = tk.Button(frame_btn, text="계산하기", font=("맑은 고딕", 11, "bold"),
                     bg="#2c3e50", fg="white", width=10, height=1,
                     relief="flat", cursor="hand2", command=on_calculate)
btn_calc.grid(row=0, column=0, padx=8)

btn_reset = tk.Button(frame_btn, text="초기화", font=("맑은 고딕", 11),
                      bg="#bdc3c7", fg="white", width=10, height=1,
                      relief="flat", cursor="hand2", command=on_reset)
btn_reset.grid(row=0, column=1, padx=8)

# 결과 프레임
frame_result = tk.Frame(root, bg="#f0f0f0", bd=0, relief="flat")
frame_result.pack(pady=10, padx=40, fill="x", ipady=15)

tk.Label(frame_result, text="BMI 수치", font=("맑은 고딕", 10),
         bg="#f0f0f0", fg="#888888").grid(row=0, column=0, padx=30, pady=(10, 2))
tk.Label(frame_result, text="판정", font=("맑은 고딕", 10),
         bg="#f0f0f0", fg="#888888").grid(row=0, column=1, padx=30, pady=(10, 2))

label_bmi_value = tk.Label(frame_result, text="-", font=("맑은 고딕", 22, "bold"),
                            bg="#f0f0f0", fg="#333333")
label_bmi_value.grid(row=1, column=0, padx=30, pady=(2, 10))

label_category_value = tk.Label(frame_result, text="-", font=("맑은 고딕", 22, "bold"),
                                 bg="#f0f0f0", fg="#333333")
label_category_value.grid(row=1, column=1, padx=30, pady=(2, 10))

# 기준 안내
guide_text = "[ BMI 판정 기준 ]\n저체중: 18.5 미만  |  정상: 18.5 ~ 22.9\n과체중: 23.0 ~ 24.9  |  비만: 25.0 이상"
tk.Label(root, text=guide_text, font=("맑은 고딕", 9),
         bg="#ffffff", fg="#aaaaaa", justify="center").pack(pady=(10, 0))

root.mainloop()
