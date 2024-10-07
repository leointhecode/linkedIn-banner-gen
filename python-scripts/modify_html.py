from bs4 import BeautifulSoup

def modify_html(name, line1, line2, line3):
    
    if name == '':
        name = "Leonardo Espinosa __"
    if line1 == '':
        line1 ='Graduate as Computational Systems Engineer'
    if line2 == '':
        line2 = 'specialized in QA for AI testing and TM.'
    if line3 == '':
        line3 = 'Big fan of Python and Lua ᕙ(⇀‸↼‶)ᕗ'

    with open('../html-source/banner.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    name_tag = soup.find('span', class_='name')
    name_tag.string = name

    line1_tag = soup.find('span', class_='line1')
    line1_tag.string = line1

    line2_tag = soup.find('span', class_='line2')
    line2_tag.string = line2

    line3_tag = soup.find('span', class_='line3')
    line3_tag.string = line3

    with open('../html-source/banner.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print("HTML file modified successfully!")


