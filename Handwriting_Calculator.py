import tkinter as tk
import io
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import json
from latex2sympy2 import latex2sympy, latex2latex

class Handwriting_Calculater:

    def convert_to_calculate_functions(self, latex_expression):
        # Mathpix Api 식 LaTeX를 계산용 LaTex로 변환을 위한 함수
        trig_functions = {
            '\operatorname { sin }': '\sin',  
            '\operatorname { cos }': '\cos',
            '\operatorname { tan }': '\tan',
            '\operatorname { csc }': '\csc',
            '\operatorname { sec }': '\sec',
            '\operatorname { cot }': '\cot',
            '\operatorname { ln }': '\ln',
            '\operatorname { log }': '\log',
            '\operatorname { lim }': '\lim',
        }

        for func in trig_functions:
            if func in latex_expression:
                latex_expression = latex_expression.replace(func, trig_functions[func])
        return latex_expression
    
    def __init__(self, root):
        self.root = root
        self.root.title("Handwriting Calculater")
        # 지우개 버튼
        self.eraser_button=tk.Button(root, text="지우개", command=self.use_eraser)
        self.eraser_button.place(x=250, y=10)
        # 볼펜 버튼
        self.pen_button=tk.Button(root, text="볼펜", command=self.use_pen)
        self.pen_button.place(x=320, y=10)

        self.tool=1

        # 이미지 불러오기 버튼
        self.load_image_button = tk.Button(root, text="이미지 불러오기", command=self.load_image)
        self.load_image_button.place(x=10, y=10)  # Canvas의 왼쪽 위에 배치

        # 이미지 저장 버튼
        self.save_image_button = tk.Button(root, text="이미지 저장", command=self.save_image)
        self.save_image_button.place(x=140, y=10)  # Canvas의 왼쪽 위에 배치

        # 그림판 초기화 버튼
        self.clear_canvas_button = tk.Button(root, text="그림판 초기화", command=self.clear_canvas)
        self.clear_canvas_button.place(x=560, y=10)

        # 그림판 추가
        self.canvas = tk.Canvas(root, bg="white", width=650, height=600)
        self.canvas.place(x=10, y=50)

        # 키보드 입력 위젯 생성
        self.keyboard_input_label = tk.Label(self.root, text="LATEX 수식 입력:")
        self.keyboard_input_label.place(x=10, y=700)

        self.keyboard_input = tk.Entry(self.root)
        self.keyboard_input.place(x=120, y=700, width=200)

        # 키보드 입력 계산 버튼
        self.calculate_keyboard_button = tk.Button(self.root, text="계산", command=self.calculate_keyboard_input)
        self.calculate_keyboard_button.place(x=350, y=695)

        # 결과 텍스트 영역
        self.keyboard_result_label = tk.Label(self.root, text="")
        self.keyboard_result_label.place(x=10, y=750)

        # 마우스 이벤트 바인딩
        self.canvas.bind("<B1-Motion>", self.draw)

        # 이미지 표시 영역
        self.image_label = tk.Label(root)
        self.image_label.place(x=700, y=50)

        # 이미지에서 추출한 LaTeX 결과 표시
        self.image_latex_label = tk.Label(root, text="")
        self.image_latex_label.place(x=700, y=570)

        # 이미지 계산 버튼
        self.calculate_button = tk.Button(root, text="계산", command=self.calculate)
        self.calculate_button.place(x=1150, y=10)

        # 이미지 계산 결과 텍스트 영역
        self.result_label = tk.Label(root, text="")
        self.result_label.place(x=700, y=620)

    def calculate_keyboard_input(self):
        try:
            # 키보드로부터 수식 입력 받기
            expression = self.keyboard_input.get()

            # 입력된 수식 계산
            latex_expression = latex2latex(expression)
            converted_expression = self.convert_trig_functions(latex_expression)
            result = latex2sympy(converted_expression).evalf()

            # 결과 텍스트로 표시
            self.keyboard_result_label.config(text=f"계산 결과: {result}")
        except Exception as e:
            # 예외가 발생하면 에러 메시지 표시
            self.keyboard_result_label.config(text=f"에러: {str(e)}")

    def use_eraser(self):
        self.tool=0

    def use_pen(self):
        self.tool=1
        
    def draw(self, event):
        x, y = event.x, event.y
        if self.tool==0:
            self.canvas.create_oval(x, y, x+20, y+20, fill="white", outline="white", width=2)
        else:
            self.canvas.create_oval(x, y, x+2, y+2, fill="black", width=2)

    def clear_canvas(self):
        # 그림판 초기화
        self.canvas.delete("all")

    def load_image(self):
        # 파일 선택 다이얼로그를 열어 이미지 파일 선택
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png*")])

        # 선택한 이미지를 표시
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.image.resize((600, 500), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

            # 선택한 이미지 파일 경로 저장
            self.image_path = file_path

            # 이미지를 LaTeX로 변환하여 표시
            image_data = open(self.image_path, "rb").read()
            image_latex = self.convert_trig_functions(self.image_to_latex(image_data))
            self.image_latex_label.config(text=f"LaTeX: {image_latex}")

    def calculate(self):
        try:
            # 이미지를 LaTeX로 변환
            image_data = open(self.image_path, "rb").read()
            image_latex = self.image_to_latex(image_data)

            # 이미지 LaTeX를 계산
            result = (latex2sympy(latex2latex(self.convert_trig_functions(image_latex)))).evalf()
    
            # 결과를 텍스트로 표시
            self.result_label.config(text=f"계산 결과: {result}")
        except Exception as e:
            # 예외가 발생하면 에러 메시지 표시
            self.result_label.config(text=f"{str(e)}")

    def image_to_latex(self, image_data):
        # MathPix API를 사용하여 이미지 파일을 LaTeX로 변환
        r = requests.post("https://api.mathpix.com/v3/latex",
                          files={"file": image_data},
                          headers={
                              "app_id": "dongjun_4e3b60_281b35",
                              "app_key": "0388bed1e99fae114ac60d16f77db34190cbc0344359696489b66febdd88bb19"
                          })

        latex = json.loads(r.text)['latex']
        return latex

    def save_image(self):
    # Canvas에서 그린 그림을 이미지로 저장
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            try:
            # Canvas에서 이미지로 변환
                image = self.canvas.postscript(colormode='color')
                img = Image.open(io.BytesIO(image.encode('utf-8')))
            
            # PNG 파일로 저장
                img.save(file_path, "png")
                messagebox.showinfo("저장 완료", "이미지가 성공적으로 저장되었습니다.")
            except Exception as e:
                messagebox.showerror("오류", f"이미지 저장 중 오류가 발생했습니다: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    app = Handwriting_Calculater(root)
    root.mainloop()
