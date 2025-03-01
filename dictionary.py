existing_article=(
    "無頼勇騎"
)

race_to_article={
    "アーク・セラフィム":["霊騎"],
    "アース・ドラゴン":["緑神龍"],
    "アースイーター":["・クロウラー"],
    "アーマード・ドラゴン":["・ドラゴン"],
    "アーマード・ワイバーン":["・ワイパーン"],
    "アーマロイド":["神兵"],
    "アビスドラゴン":["邪[○]"],
    "アビスロイヤル":["悪[○]","深淵の"],
    "アポロニア・ドラゴン":["光神龍"],
    "アンノウン":["偽りの名","真実の名"],
    "イニシエート":["[○○]の使徒"],
    "イニシャルズX":["終断[禁断ギリシャ文字]"],
    "エッグ":["・エッグ"],
    "エメラルド・モンスター":["ネイチャー"],
    "エンジェル・コマンド":["[○○]の精霊"],
    "エンジェル・コマンド・ドラゴン":["[○○]の精霊龍"],
    "エンジェル・ドラゴン":["[○○]の精霊龍"],
    "オラクリオン":["神聖[「き」と読む漢字一文字]"],
    "オラクル・ドラゴン":["神聖龍"],
    "ガーディアン":["[○○]の守護者"],
    "ガイア・コマンド":["[○○]の大地"],
    "ガイアール・コマンド・ドラゴン":["熱血龍"],
    "キマイラ":["ギガ"],
    "グラディエーター":["宣凶師"],
    "グランド・デビル":["封魔"],
    "クリエイター":["[○○]神","世紀末"],
    "クリスタル・コマンド・ドラゴン":["龍素記号[アルファベット二文字]"],
    "クリスタル・ドラゴン":["龍素記号[アルファベット二文字]"],
    "グレートメカオー":["[○○]機装"],
    "ゲリラ・コマンド":["獣軍隊"],
    "ゴースト":["[○○]の影"],
    "コスモ・ウォーカー":["巡霊者"],
    "ゴッド":["[○○]神"],
    "コロコロイヤル":["深淵の[○○]"],
    "コロニー・ビートル":["シェル・[○○]"],
    "サイバー・ウイルス海":["[アルファベット一文字]・"],
    "サイバー・クラスター":["[○○]・クラスター"],
    "サイバー・コマンド":["サイバー・[アルファベット一文字]・"],
    "サイバー・ドラゴン":["蒼神龍"],
    "サイバー・ムーン":["ルナ・[○○]"],
    "サバキスト":["[○○]ノ裁徒"],
    "ジ・アンサー":["夢の[○○]"],
    "ジャイアント":["[○○]の超人"],
    "ジャイアント・スノーフェアリー":["[○○]の妖精"],
    "ジャイアント・ドラゴン":["龍樹"],
    "シャイン・モンスター":["ピュア"],
    "ジャスティス・ウイング":["[○○]の翼"],
    "ジャスティス・オーブ":["[○○]の玉"],
    "ジュラシック・コマンド・ドラゴン":["[○○]類", "[○○]目","[○○]類[○○]目"],
    "ジュラシック・ドラゴン":["[○○]類", "[○○]目"],
    "スノーフェアリー":["[○○]妖精"],
    "スノーフェアリー風":["雪精"],
    "スピリット・クォーツ・ドラゴン":["結晶龍"],
    "スプラッシュ・クイーン・ドラゴン":["海姫龍"],
    "セイント・ヘッド":["秘護精"],
    "ゼニス":["「[漢字一・二文字]」の頂"],
    "ゼロ・ドラゴン":["無量大龍"],
    "ソルトルーパー":["粛清者"],
    "ダーク・ナイトメア":["暗黒鎧"],
    "ダーク・モンスター":["ヤミノ"],
    "ティラノ・ドレイク":["[○○]・ドラグーン"],
    "デーモン・コマンド・ドラゴン":["悪魔龍"],
    "デーモン・ドラゴン":["[○○]の悪魔龍"],
    "デスパペット":["[○○]人形"],
    "デビルマスク":["[○○]怪人"],
    "デューンゲッコー":["[○○]・リザード"],
    "ドラグナー・ドラゴン":["龍覇龍"],
    "ドラゴンギルド":["龍[「そう」と読む漢字一文字]者"],
    "ドラゴン・ゾンビ":["黒神龍"],
    "ドリームメイト・ドラゴン":["森夢龍"],
    "ニトロ・ドラゴン":["[雨冠の漢字一文字]龍"],
    "ニート":["[○○]の[漢数字]男"],
    "バーサーカー":["[○○]の伝道師", "[○○]の伝道士"],
    "バーサーカー・ドラゴン":["聖板龍"],
    "パラサイトワーム":["[○○]虫"],
    "バルーン・マッシュルーム":["[○○]ダケ"],
    "パンドラボックス":["[○○]秘宝"],
    "ビーストフォーク號":["[○○]の面"],
    "ヒューマノイド爆":["爆[○○]"],
    "ファイアー・バード炎":["[○○]ッチ"],
    "ファイブ・オリジン・ドラゴン":["[○]龍神"],
    "ファンキー・ナイトメア・ドラゴン":["歓楽龍"],
    "フェザーノイド":["[○]風の"],
    "ブルー・モンスター":["シンカイ"],
    "フレイム・コマンド":["爆裂"],
    "フレイム・ビースト":["グレンオー"],
    "フレイム・モンスター":["グレンオー"],
    "ヘドリアン":["男"],
    "ホーリー・ドラゴン":["聖神龍"],
    "ホーン・ビースト":["[○○]する[○○]・ホーン"],
    "ポセイディア・ドラゴン":["蒼神龍"],
    "ボルケーノ・ドラゴン":["紅神龍"],
    "マジカル・モンスター":["[○○]の精獣"],
    "マジック・アースイーター":["[○○]・クロウラー"],
    "マジック・コマンド":["機術士", "奇天烈"],
    "マジック・サイバー・ムーン":["ルナ・[○○]"],
    "マジック・リキッド・ピープル":["AQ"],
    "魔導具":["堕魔"],
    "ミステリー・トーテム":["[○○]の化身"],
    "ミルクガール":["ベイB"],
    "ミルクボーイ":["ベイB"],
    "ムートピア":["貝獣"],
    "メガ・コマンド・ドラゴン":["メガ・[○○]・ドラゴン"],
    "メカ・デル・ステラ":["星姫械"],
    "メカ・デル・ソル":["光器"],
    "メガ・ドラゴン":["メガ・[○○]・ドラゴン"],
    "メカサンダー":["[○○]の求道者"],
    "メルト・ウォリアー":["[○○]・リザード"],
    "ライトブリンガー":["予言者"],
    "リヴァイアサン":["キング・[○○]"],
    "リキッド・ピープル":["アクア・[○○]"],
    "リキッド・ピープル閃":["アクア[○○]"],
    "リビング・デッド":["[○○]者"],
    "ルナーズ・サンガイザー":["超神羅"],
    "ルナティック":["羅月"],
    "ルナティック・エンペラー":["神羅"],
    "レインボー・ファントム":["聖騎士"],
    "ロスト・クルセイダー":["鎧亜の[○○]","[○]鎧亜","鎧亜[○○]"],
    "ロック・ビースト":["ザウルス", "ティラノス"],
    "ワールド・ドラゴン":["星龍"],
    "ワンダー・トリック":["式神"],
    "2016カレンダー":["月"]
}

multi_articles={
    "アーク・セラフィム":["霊騎"],
    "アースイーター":["戦攻"],
    "アース・ドラゴン":["無双","武装"],
    "アーマード・ドラゴン":["龍騎","竜騎","竜機","竜鬼"],
    "アーマード・アポロニア・ドラゴン":["光鎧龍"],
    "アーマード・ファイアー・バード":["翔鎧","凰翔"],
    "アーマード・ワイバーン":["雷炎"],
    "アーマロイド":["機動"],
    "アウトレイジ":["無法"],
    "アポロニア・ドラゴン":["龍聖"],
    "イニシエート":["聖者"],
    "イニシャルズX":["禁忌"],
    "エメラルド・モンスター":["森獣"],
    "エンジェル・コマンド":["聖霊","堕天"],
    "エンジェル・ドラゴン":["聖龍"],
    "オラクル":["神徒"],
    "ガーゴイル":["音像"],
    "ガーディアン":["護聖"],
    "ガイアール・コマンド・ドラゴン":["熱血"],
    "ガイア・コマンド":["大地"],
    "キカイヒーロー":["機士"],
    "キマイラ":["魔獣"],
    "グラディエーター":["賢者"],
    "グランセクト":["大地"],
    "グランド・デビル":["封魔"],
    "クリスタル・コマンド・ドラゴン":["水晶"],
    "グレートメカオー":["王機"],
    "ゲル・フィッシュ":["魚雷","電脳"],
    "ゴースト":["腐敗"],
    "コスモ・ウォーカー":["巡霊"],
    "コロニー・ビートル":["群蟲"],
    "サイバー・ウイルス":["猛菌"],
    "サイバー・コマンド":["大河"],
    "サイバーロード":["電磁"],
    "シノビ":["忍者"],
    "ジャイアント":["剛撃","無敵"],
    "ジャイアント・インセクト":["鎧冑"],
    "シャイン・モンスター":["聖獣"],
    "ジャスティス・ウイング":["天翼"],
    "ジュラシック・コマンド・ドラゴン":["古龍"],
    "スターライト・ツリー":["星樹"],
    "スノーフェアリー":["妖精"],
    "スピリット・クォーツ":["魂晶"],
    "スプラッシュ・クイーン":["麗姫"],
    "セイント・ヘッド":["秘精","護精"],
    "ゼノパーツ":["神機","魂具"],
    "ソルトルーパー":["神官"],
    "ダーク・ナイトメア":["悪夢"],
    "ダーク・モンスター":["黒獣"],
    "ダークロード":["恐皇","死爵"],
    "ツリーフォーク":["賢樹"],
    "ディープ・マリーン":["深塊"],
    "ティラノ・ドレイク":["闘竜","騎神"],
    "デーモン・コマンド":["悪魔","魔天"],
    "デーモン・コマンド・ドラゴン":["邪龍"],
    "デスパペット":["傀儡"],
    "デビルマスク":["奇面"],
    "デューンゲッコー":["月砂"],
    "ドラゴノイド":["剣兵"],
    "ドラゴン・ゾンビ":["神滅","真滅"],
    "ドラゴンの花嫁":["龍后"],
    "ドリームメイト":["幻獣"],
    "トリックス":["機生"],
    "ナイト":["天雷","氷河","邪眼","魔光","爆獣","蒼狼"],
    "パラサイトワーム":["妖蟲"],
    "パンドラボックス":["秘宝"],
    "ビークル・ビー":["甲蟲"],
    "ビーストフォーク":["無頼"],
    "ビーストフォーク號":[],
    "ビートジョッキー":["爆衆"],
    "ビッグマッスル":["山脈"],
    "ヒューマノイド":["勇騎"],
    "ヒューマノイド爆":[],
    "ファイアー・バード":["翔天","凰翔"],
    "ファンキー・ナイトメア":["悪魔"],
    "フェザーノイド":["熱風","疾風"],
    "ブレイブ・スピリット":["炎霊"],
    "フレイム・コマンド":["爆裂"],
    "フレイム・モンスター":["爆炎","火焔"],
    "ブレインジャッカー":["邪脚"],
    "ヘドリアン":["妖魔"],
    "ホーン・ビースト":["勇猛"],
    "ポセイディア・ドラゴン":["海王"],
    "ボルケーノ・ドラゴン":["旋竜"],
    "マーフォーク":["電影","海族"],
    "マフィ・ギャング":["闇影"],
    "ミステリー・トーテム":["霊樹"],
    "ムートピア":["海郷"],
    "メガ・コマンド・ドラゴン":["激龍"],
    "メカ・デル・ソル":["光姫"],
    "メタリカ":["輝晶"],
    "メルト・ウォリアー":["血風"],
    "ライトブリンガー":["黙示"],
    "リヴァイアサン":["海嶺"],
    "リキッド・ピープル":["電脳"],
    "レインボー・ファントム":["幻風"],
    "ロスト・クルセイダー":["鎧亜"],
    "ロック・ビースト":["霊峰"],
    "ワイルド・ベジーズ":["剛勇"]
}

ignore_rules={
    "ディスタス":["Dis","[複合種族冠詞] [固有名]-[ササゲールで軽減されるコスト数]"],
    "鬼札王国":["[○○+妖怪関連の漢字二文字]","「[○○]の鬼」"],
    "チームウェイブ":["#[文章] #[文章]"],
    "オラクル":["[○○]の[階級]"],
    "ドラグナー":["龍覇"],
    "イメン団":["[漢数字]面"],
    "ハムカツ団":["[○○]の[アラビア数字]号","[漢数字]つ星"],
    "ダママ団":["[漢数字]族"],
    "ドレミ団":["タイム[アラビア数字]"],
    "テック団":["【問[アラビア数字]】"],
}

reigai_articles={
    "封魔妖魔":["封魔妖"],
    "":[""],
    "":[""]
}

evolution_articles={
    "鬼レクスターズ":["〈[○○].鬼〉","-鬼MAX"],
    "レクスターズ":["〈[○○].Star〉","-MAX"],
    "アーク・セラフィム":["聖帝"],
    "アース・ドラゴン":["超神龍"],
    "アポロニア・ドラゴン":["超神龍"],
    "ドラゴン・ゾンビ":["超神龍"],
    "ポセイディア・ドラゴン":["超神龍"],
    "アースイーター":["戦攻"],
    "アーマード・ドラゴン":["超竜"],
}