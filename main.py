import function
import streamlit as st

def input_contents():
    select_races=st.selectbox(label="種族数を選択",options=("1","2","3","4","6以上"))
    races=[]
    if select_races=="1":
        races.append(st.text_input("種族を入力"))
    elif select_races=="6以上":
        return function.otoko(),[""],False
    else:
        races.append(st.text_input("種族1つめを入力"))
    if select_races=="2":
        races.append(st.text_input("種族2つめを入力"))
    if select_races=="3":
        races.append(st.text_input("種族2つめを入力"))
        races.append(st.text_input("種族3つめを入力"))
    if select_races=="4":
        races.append(st.text_input("種族2つめを入力"))
        races.append(st.text_input("種族3つめを入力"))
        races.append(st.text_input("種族4つめを入力"))
    civils=st.multiselect(label="文明を選択",options=("火","自然","水","光","闇","ゼロ"))
    civils.sort() #['ゼロ', '光', '水', '火', '自然', '闇']
    evolution=st.checkbox("進化クリーチャー")
    return races,civils,evolution

def main():
    function.message()
    races,civils,evolution=input_contents()
    if races==["男"]:
        article=races
    else:
        article=function.generate_article(races,civils,evolution)
    if st.button("冠詞を確認！"):
        for a in article:
            st.write(a)

if __name__=="__main__":
    main()