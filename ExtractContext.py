import json

from support_001 import generate


def extractcontext(context,question):
    P1 = f"""内容:{context}
从上面内容中找出问题:({question}) 的答案 一百个字以内
答案:"""
    rating = "0"
    mistake = 0
    Answer=generate(P1)
    while len(Answer)<6:
        mistake+=1
        print("error\nreloop")
        Answer=generate(P1)
        if mistake==3:
            return ""
    data_dict = {
        "instruction": P1,
        "input": "",
        "output": Answer,
    }

    json_str = json.dumps(data_dict, ensure_ascii=False)
    with open("tool_data.txt", "a", encoding="utf-8") as f:
        f.write(json_str + "\n")
    return Answer