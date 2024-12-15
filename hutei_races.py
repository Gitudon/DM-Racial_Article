from dictionary import *

def initials(races:list,civils:list):
    if len(races)==1:
        return ["禁断[禁断文字のアルファベット一文字]"]
    if "ヒューマノイド爆" in races:
        return ["爆G"]
    if "デーモン・コマンド・ドラゴン" in races:
        return ["Mの悪魔龍"]
    if "ソニック・コマンド" in races:
        if civils==["火"]:
            return ["轟音"]
        elif civils==["水"]:
            return ["改速"]
    return ["特定の冠詞がありません"]

def master_initials(civils:list):
    if civils==["火"]:
        return ["D2G"]
    if civils==["自然"]:
        return ["D2B","D2Y"]
    if civils==["水"]:
        return ["D2W","D2W2","D2S"]
    if civils==["光"]:
        return ["D2P","D2J","D2J2"]
    if civils==["闇"]:
        return ["D2K","D2K2"]
    if civils==["火","闇"]:
        return ["D2M","D2M2","D2V","D2-V","D2V2"]
    return ["特定の冠詞がありません"]

def kikaihero(civils:list):
    if civils==["水"]:
        return ["コマンダー・"]
    if civils==["光"]:
        return ["キャプテン・"]
    return ["特定の冠詞がありません"]

def king_command_dragon(races:list):
    if len(races)==1:
        return ["王龍"]
    if "アンノウン" in races:
        return ["偽りの王","真実の王"]
    return ["特定の冠詞がありません"]

def god_nova(races:list):
    articles=[]
    if len(races)==2:
        for r in races:
            if r!="ゴッド・ノヴァ":
                if r in multi_articles:
                    arg=multi_articles[r][0]
                    if arg=="神滅":
                        arg="真滅"
                    articles.append(arg+"右神")
                    articles.append(arg+"左神")
        return articles
    articles.append("[○○]右神")
    articles.append("[○○]左神")
    return articles

def god_nova_OMG(races:list):
    articles=["極限[○○]神"]
    if len(races)==2:
        for r in races:
            if r!="ゴッド・ノヴァOMG":
                if r in multi_articles:
                    arg=multi_articles[r][0]
                    if arg=="神滅":
                        arg="真滅"
                    articles.append(arg+"右神")
                    articles.append(arg+"左神")
        return articles
    articles.append("[○○]右神")
    articles.append("[○○]左神")
    return articles

def shinobi(civils:list):
    if civils==["火"]:
        return ["不知火","不死火","轟火","裏斬隠"]
    if civils==["自然"]:
        return ["土隠","旋風"]
    if civils==["水"]:
        return ["斬隠","裏斬隠"]
    if civils==["光"]:
        return ["光牙","裏斬隠"]
    if civils==["闇"]:
        return ["威牙","裏斬隠"]
    if civils==["火","自然"]:
        return ["裏斬隠"]
    if civils==["水","自然"] or civils==["光","水","自然"]:
        return ["怒流牙"]
    return ["特定の冠詞がありません"]

def shinryakusha(races:list,civils:list,evolution:bool):
    if civils==["光"]:
        if "エンジェル・コマンド" in races:
            if evolution:
                return ["超[漢数字]極"]
            return ["[漢数字]極"]
        return ["三界","侵略者"]
    if civils==["水"]:
        if evolution:
            return ["超奇天烈"]
        if "グレートメカオー" in races:
            return ["ガチャンコ"]
        if "アースイーター" in races:
            return ["海帝"]
        return ["奇天烈","宇宙","侵略者"]
    if civils==["闇"]:
        if evolution:
            return ["超不死"]
        if "ファンキー・ナイトメア" in races:
            return ["ニャンコ"]
        return ["復讐","不死","侵略者"]
    if civils==["火"]:
        if evolution:
            return ["超音速","超轟速"]
        return ["音速","轟速","侵略者"]
    if civils==["自然"]:
        if evolution:
            if "ミステリー・トーテム" in races:
                return ["超幻影"]
            return ["超獣軍隊"]
        if "ミステリー・トーテム" in races:
            return ["幻影"]
        return ["獣軍隊","原始","侵略者"]
    if "トリニティ・コマンド" in races:
        return ["天災"]
    return ["侵略者"]

def s_class_shinryakusha(races:list):
    if "ゲリラ・コマンド" in races:
        return ["S級原始"]
    if "マジック・コマンド" in races:
        return ["S級宇宙"]
    if "ソニック・コマンド" in races:
        return ["S級不死"]
    if "トリニティ・コマンド" in races:
        return ["S級天災"]
    return ["S級"]

def sonic_command(civils:list):
    if civils==["火"]:
        return ["暴走"]
    return ["[○]速"]

def chokaju(races:list,civils:list):
    if "デーモン・コマンド" in races:
        return ["[文明の冠詞]の夜","[文明の冠詞]神官"]
    return ["ハイパー・","[文明の応じた言葉]月"]

def dispecter(civils:list):
    if civils==["光","火","闇"]:
        return ["連結","連結王"]
    if civils==["光","水","火"]:
        return ["混成","混成王"]
    if civils==["光","自然","闇"]:
        return ["接続","接続王","魔縛","魔縛王"]
    if civils==["水","火","自然"]:
        return ["電融","電融王"]
    if civils==["水","自然","闇"]:
        return ["縫合","縫合王"]
    if civils==["光", "水", "火", "自然", "闇"]:
        return ["合成","合成王"]
    return ["冠詞が特定できません"]

def gransect(races:list):
    if "不死樹王国" in races:
        return ["ライマー・"]
    return ["特定の冠詞がありません"]

def giant_dragon(races:list):
    if "不死樹王国" in races:
        return ["龍樹"]
    return ["特定の冠詞がありません"]

def akumidan(races:list):
    if "イニシャルズ" in races:
        return ["第[アラビア数字]種"]
    if "革命軍" in races:
        return ["第[漢数字]種"]
    return ["特定の冠詞がありません"]

def alien(races:list,civils:list):
    if "メカ・デル・ソル" in races:
        if civils==["光"]:
            return ["光姫ガガ"]