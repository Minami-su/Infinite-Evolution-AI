from duckduckgo_search import DDGS

from langchainmodule import similar_context
def remove_duplicate_lines(text):
    lines = text.split('\n')
    unique_lines = list(set(lines))
    cleaned_text = '\n'.join(unique_lines)
    return cleaned_text

def internet_research(input):
    #Answer=GenerateQueryContext(input)
    context=""
    search_results = DDGS().text(input, safesearch='off', timelimit='y')
    for result in search_results:
        if len(result["body"])>100:
            context += result["body"]+"\n"
    cleaned_context = remove_duplicate_lines(context)
    print(cleaned_context)
    print('情報を抽出①する...')
    if len(cleaned_context)>1:
        result=similar_context(input,cleaned_context)
    else:
        result=""
    print('情情報を抽出①完了')
    return result