from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = """
game player character level skill attack defense magic sword shield
warrior mage archer knight paladin ranger assassin monk wizard priest
quest dungeon boss monster enemy battle victory defeat reward experience
item weapon armor potion gold treasure map village castle dragon
team strategy strength speed agility intelligence stamina power ability
"""

def 문제1():
    wc = WordCloud(
        background_color='black',
        width=1000,
        height=500,
        max_words=50
    ).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def 문제2():
    colormaps = ['plasma', 'inferno', 'cool']
    plt.figure(figsize=(15, 5))
    for i, cmap in enumerate(colormaps):
        wc = WordCloud(
          colormap=cmap
        ).generate(text)
        plt.subplot(1, 3, i + 1)
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.title(cmap)
    plt.tight_layout()
    plt.show()

def 문제3():
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
        # TODO: 배경 흰색
    ).generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('wordCloud_1.png',dpi=150)
    plt.show()
def plt_없이_wordCloud_이미지저장하기():
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white'
        # TODO: 배경 흰색
    ).generate(text)
    wc.to_file("wc_file.png")
plt_없이_wordCloud_이미지저장하기()