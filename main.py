from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import jieba 
import jieba.analyse
topk = 10


def main():
    with open('chinese_text.txt') as f:
        content = f.read()
    
    with open('stop_words.txt') as g:
        stop_words = g.read().splitlines()

    myword = jieba.lcut(content)
    nWord = " ".join(myword)

    wc = WordCloud(font_path = 'Microsoftblack.ttf', stopwords=stop_words, background_color="white", width=800, height=600)
    # 这里字体是微软雅黑，但是字体文件被我重命名了，便于识别
    wc.generate(nWord)

    img = wc.to_image()
    plt.imshow(img, interpolation='bilinear')
    plt.axis("off") # 不需要坐标轴
    plt.show() # 利用matplotliib显示图片

    img.save('WordCloud.jpg') #  保存图片
    
    #关键词方法一
    tags = jieba.analyse.extract_tags(content,topK = topk)
    print(f"前 {topk} 个关键词为 {tags} ")

    # 关键词方法二
    filtered_word = [word for word in myword if len(word.strip()) > 1]
    print(f"有效词语:{filtered_word}") # 得到有效词语
    counter = Counter(filtered_word) # 统计有效词语的词频
    print(f"有效词语得词频为{counter}")

main()
