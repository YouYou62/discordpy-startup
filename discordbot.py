import discord
import random

TOKEN = "ODAwMDI1OTAyNjM2NDY2MTg3.YAMILg.V1EVO3ch3ibvXNKcEpk4vX3hu-8"
client = discord.Client()

Buki_all = [
    "ボールドマーカー",
    "ボールドマーカーネオ",
    "ボールドマーカー7",
    "わかばシューター",
    "もみじシューター",
    "おちばシューター",
    "シャープマーカー",
    "シャープマーカーネオ",
    "プロモデラーMG(銀)",
    "プロモデラーRG(金)",
    "プロモデラーPG(銅)",
    "スプラシューター",
    "スプラシューターコラボ",
    "スプラシューターベッチュー",
    ".52ガロン",
    ".52ガロンデコ",
    ".52ガロンベッチュー",
    "N-ZAP85",
    "N-ZAP89",
    "N-ZAP83",
    "プライムシューター",
    "プライムシューターコラボ",
    "プライムシューターベッチュー",
    ".96ガロン",
    ".96ガロンデコ",
    "ジェットスイーパー",
    "ジェットスイーパーカスタム",
    "ノヴァブラスター",
    "ノヴァブラスターネオ",
    "ノヴァブラスターベッチュー",
    "ホットブラスター",
    "ホットブラスターカスタム",
    "ロングブラスター",
    "ロングブラスターカスタム",
    "ロングブラスターネクロ",
    "クラッシュブラスター",
    "クラッシュブラスターネオ",
    "ラピッドブラスター",
    "ラピッドブラスターデコ",
    "ラピッドブラスターベッチュー",
    "Rブラスターエリート",
    "Rブラスターエリートデコ",
    "L3リールガン",
    "L3リールガンD",
    "L3リールガンベッチュー",
    "H3リールガン",
    "H3リールガンD",
    "H3リールガンチェリー",
    "ボトルカイザー",
    "ボトルカイザーフォイル",
    "カーボンローラー",
    "カーボンローラーデコ",
    "スプラローラー",
    "スプラローラーコラボ",
    "スプラローラーベッチュー",
    "ダイナモローラー",
    "ダイナモローラーテスラ",
    "ダイナモローラーベッチュー",
    "ヴァリアブルローラー",
    "ヴァリアブルローラーフォイル",
    "パブロ",
    "パブロ・ヒュー",
    "パーマネント・パブロ",
    "ホクサイ",
    "ホクサイ・ヒュー",
    "ホクサイベッチュー",
    "スクイックリンα",
    "スクイックリンβ",
    "スクイックリンγ",
    "スプラチャージャー",
    "スプラチャージャーコラボ",
    "スプラチャージャーベッチュー",
    "スプラスコープ",
    "スプラスコープコラボ",
    "スプラスコープベッチュー",
    "リッター4K",
    "リッター4Kカスタム",
    "4Kスコープ",
    "4Kスコープカスタム",
    "14式竹筒銃・甲",
    "14式竹筒銃・乙",
    "14式竹筒銃・丙",
    "ソイチューバー",
    "ソイチューバーカスタム",
    "バケットスロッシャー",
    "バケットスロッシャーデコ",
    "バケットスロッシャーソーダ",
    "ヒッセン",
    "ヒッセン・ヒュー",
    "スクリュースロッシャー",
    "スクリュースロッシャーネオ",
    "スクリュースロッシャーベッチュー",
    "オーバーフロッシャー🛀",
    "オーバーフロッシャーデコ🛀",
    "エクスプロッシャー",
    "エクスプロッシャーカスタム",
    "スプラスピナー",
    "スプラスピナーコラボ",
    "スプラスピナーベッチュー",
    "バレルスピナー",
    "バレルスピナーデコ",
    "バレルスピナーリミックス",
    "ハイドラント",
    "ハイドラントカスタム",
    "クーゲルシュライバー",
    "クーゲルシュライバー・ヒュー",
    "ノーチラス47",
    "ノーチラス79",
    "スパッタリー",
    "スパッタリー・ヒュー",
    "スパッタリークリア",
    "スプラマニューバー",
    "スプラマニューバーコラボ",
    "スプラマニューバーベッチュー",
    "ケルビン525",
    "ケルビン525デコ",
    "ケルビン525ベッチュー",
    "デュアルスイーパー",
    "デュアルスイーパーカスタム",
    "クアッドホッパーブラック",
    "クアッドホッパーホワイト",
    "パラシェルター",
    "パラシェルターソレーラ",
    "キャンピングシェルター",
    "キャンピングシェルターソレーラ",
    "キャンピングシェルターカーモ",
    "スパイガジェット",
    "スパイガジェットソレーラ",
    "スパイガジェットベッチュー",
]

@client.event
async def on_ready():
    On_chat = "準備おっけーでし！"
    print(On_chat)
    print(discord.__version__)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == "!vc":

        if not message.author.voice.channel.voice_states.keys:
            await message.channel.send(message.author.userNAME + "さんはボイスチャンネルに誰もいないでし！")
            return

        else:

            userID = []
            userNAME = []

            #ユーザーIDの取得
            user_id = message.author.voice.channel.voice_states.keys()
            for users in user_id:
                print(users)
            userID += user_id
            print("ユーザーIDの取得完了")

            #ユーザーネームの取得
            ID_len = len(userID)
            i = 0
            while i < ID_len:
                ID = str(userID[int(i)])
                user = await client.fetch_user(ID)
                MESSAGE = user.name, user.discriminator, str(user)
                userNAME.insert(0, MESSAGE[0])
                i += 1
                
            #ブキルーレットのチャット
            i = 0
            while i < len(userNAME):
                r = random.randint(1, 129)
                await message.channel.send("**" + str(userNAME[i]) + "**さんは**__" + str(Buki_all[int(r)]) + "__**でし！")
                i += 1

    if message.content.startswith("!buki"):

        if message.content.endswith("1"):
            await message.channel.send()
        

    elif message.content == "end":
        print("コマンド名[end]")
        await message.channel.send("プログラムを終了したでし！")
        exit()

client.run(TOKEN)
