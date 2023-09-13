import json

from support_001 import generate


def generatequerycontext(question):
    P1 = f"""
问题:{question}  
将问题:({question}) 重写为互联网搜索，要求精炼，十个字以内
重写后的搜索:"""
    Answer= generate(P1)
    data_dict = {
        "instruction": P1,
        "input": "",
        "output": Answer,
    }
    Answer=Answer.replace("\"","")
    json_str = json.dumps(data_dict, ensure_ascii=False)
    with open("tool_data.txt", "a", encoding="utf-8") as f:
        f.write(json_str + "\n")
    return Answer