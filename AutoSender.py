import requests, json, time
from colorfull import init; init()

Send_List = []

def LoadList():
    with open("File.txt", "r") as send_list:
        for send in send_list:
            Send_List.append(send.strip())

def Send_Message(Token, ChannelID, Message, Time: int):
    for List in Send_List:
        r = requests.post(f"https://discord.com/api/v8/channels/{ChannelID}/messages", headers={"Authorization": Token, "Content-Type": "application/json"}, data=json.dumps({"content": List})).json()
        LastedMessageId = r["id"]
        LastedChannelId = r["channel_id"]
        time.sleep(int(Time))
        requests.delete(f"https://discord.com/api/v8/channels/{LastedChannelId}/messages/{LastedMessageId}", headers={"Authorization": Token, "Content-Type": "application/json"})

LoadList()
Send_Message("Token Here", "Channel ID Here", "Message Here", 1)
