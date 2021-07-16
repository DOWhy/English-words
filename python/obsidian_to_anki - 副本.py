# -*- coding: utf-8 

import markdown
import os
import re


if __name__ == "__main__":

    anki = []

    questionPath = 'C:\\Users\\john\\Downloads\\question.txt'

    path = 'C:\\Users\\john\\my_works\\English words\\'

    fileList = os.listdir(path)

    count = 0
    for file in fileList:

        count = count + 1
        print(count)

        if file.endswith('.md') and re.match(r'\d{14}', file):

            file1 = open(path + file, encoding='utf-8')
            content = file1.read()
            file1.close()

            content = content.replace('"', '""')
            content = content.replace("'", "''")
            content = content.replace('\n', '<br>')

            anki.append(file[0:14] + '\t' + file[15:-3] + '\t' + '"' + content + '"' + '\n')

    file2 = open(questionPath, 'w', encoding='utf-8')
    file2.writelines(anki)
    file2.close()


            





