import re

text="""私は昨日____と____をした。"""

def f():
    global text
    answer=re.findall("__.*?__,text)
    while len(answer)>0:
        n=input"文字を入力してください："
        if n in answer:
            text.replace("____",answer)
            print(text)
        else:
            return

    print(text+"終了です。")

f()