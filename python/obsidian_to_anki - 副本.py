# -*- coding: utf-8 

import markdown
import os
import re


# 将 markdown 转换为 HTML，并且写入到 某个 文件中
def markdown2htmlAndWrite2question(anki, path): # 参数是数组

    content1 = "".join(anki) # 将列表变成一个字符串
    content1 = content1.replace('@%```', '@%\n```')
    content1 = content1.replace('<br>```', '<br>\n```')

    # file7 = open("C:\\Users\\john\\Downloads\\bbbba.txt", 'w', encoding='utf-8')
    # file7.write(content1)
    # file7.close()


    # extensions 参考： https://python-markdown.github.io/extensions/
    html = markdown.markdown(content1, extensions=['fenced_code', 'codehilite', 'tables', 'nl2br', 'extra', 'abbr', 'def_list', 'footnotes', 'md_in_html', 'admonition', 'legacy_attrs', 'legacy_em', 'meta', 'sane_lists', 'smarty', 'toc',  'pymdownx.highlight', 'pymdownx.inlinehilite', 'pymdownx.tasklist', 'pymdownx.caret', 'sane_lists', 'mdx_truly_sane_lists']) # 'wikilinks', 这个是将 [[]] 转换为内部链接的。  'pymdownx.arithmatex', markdown 中的 latex 转换为 HTML

    # file6 = open("C:\\Users\\john\\Downloads\\aaaab.txt", 'w', encoding='utf-8')
    # file6.write(html)
    # file6.close()

    # 转换文件中的标签。虽然文件中标签的格式是：“#xxx”，但是python依然会将它识别为一级标题，转换成“<h1>”标签的形式，所以这里将<h1>标签进行转换
    taglist = re.findall(r'<h1.*>.*</h1>', html)
    if taglist != []:
        j = 0
        for j in range(len(taglist)):
            if re.search(r'<h1.*>(.*)</h1>', html):
                tag = re.search(r'<h1.*>(.*)</h1>', html).group(1)
                html = re.sub(r'<h1.*>' + tag + '</h1>', '#' + tag, html)

    html = html.replace('<br />\n', '@@%%')
    html = html.replace('\n', '<br />')
    html = html.replace('&lt;br&gt;', '')
    html = html.replace('@@%%', '<br />')
    html = html.replace('@%@%', '\n')
    html = html.replace("@%", "\t")
    html = html.replace('<p>', "")
    html = html.replace('</p>', '')

    file2 = open(path, 'w', encoding='utf-8')
    file2.write(html)
    file2.close()


if __name__ == "__main__":

    # anki = [] # 用来存放那些即将导入anki的 问答题
    anki = ["aa@%", "bb@%", "cc@%@%"]


    questionPath = 'C:\\Users\\john\\Downloads\\question.txt'


    path = 'c:\\Users\\john\\Documents\\English words\\'

    fileList = os.listdir(path)

    count = 0
    for file in fileList:

        count = count + 1
        print(count)

        if file.endswith('.md') and re.match(r'\d{14}', file):

            file1 = open(path + file, encoding='utf-8')
            conlist = file1.readlines()
            file1.close()


            aid = ''
            question = ''
            answer = ''

            i = 0
            for i in range(len(conlist)):
                if conlist[i] == '\n':
                    answer = answer + '<br>'
                elif conlist[i].startswith('Q：'): # 如果文件内容某行以 Q：开头，这个属于问题的一部分
                    question = conlist[i][2:-1]
                else:
                    answer = answer + conlist[i]


            aid = re.match(r'(\d{14})', file).group(1)
            question = file[15:-3] + '<br>' + question


            anki.append(aid + '@%') # @% 作为字段之间的分割
            anki.append(question + "@%")
            anki.append(answer + '@%@%') # @%@% 作为卡片之间的分割
            answer = ""
            
    
    
    markdown2htmlAndWrite2question(anki, questionPath)





