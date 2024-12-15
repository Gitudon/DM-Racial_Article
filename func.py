import streamlit as st
from dictionary import *
from hutei_races import *

def otoko():
    return ["男"]

def message():
    st.title("種族冠詞確認")
    st.write("入力した種族から冠詞を生成します。")

def hutei(races:list,civils:list,evolution:bool):
    return []

def evolution_article(races:list):
    if "鬼レクスターズ" in races:
        return evolution_articles["鬼レクスターズ"]
    if "レクスターズ" in races:
        return evolution_articles["レクスターズ"]
    for r in races:
        if r in evolution_articles:
            return evolution_articles[r]
    return []

def explore_cards(article:str):
    cards=[]
    # APIを用いてカードを取得することができたらいいな
    return cards

def generate_article(races:list,civils:list,evolution:bool):
    article=hutei(races,civils,evolution)
    if article!=[]:
        return article
    for race in races:
        if race in ignore_rules:
            return ignore_rules[race]
    if evolution:
        article = evolution_article(races)
        if article!=[]:
            return article
    num_of_races=len(races)
    if num_of_races==1:
        if races[0] not in race_to_article:
            article=["特定の冠詞がありません"]
        else:
            data=race_to_article[races[0]]
            for d in data:
                article.append(d)
    else:
        if num_of_races==2:
            if races[0] not in multi_articles:
                article.append("特定の冠詞がありません")
            else:
                data=multi_articles[races[0]]
                for d in data:
                    article.append(d)
                if races[1] not in multi_articles:
                    article=["特定の冠詞がありません"]
                else:
                    data=multi_articles[races[1]]
                    tmp=[]
                    for d in data:
                        for a in article:
                            tmp.append(a+d)
                            tmp.append(d+a)
                    article=[]
                    for t in tmp:
                        if t in existing_article:
                            article.append(t)
                    for i in range(len(article)):
                        if article[i] in reigai_articles:
                            article[i]=reigai_articles[article[i]]
    return article