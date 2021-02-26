import requests

ID = input("Enter the person's Discord ID ")

r = requests.get(f"https://verify.eryn.io/api/user/{ID}")
try:
    rbxname = r.json().pop("robloxUsername")
    rbxid = r.json().pop("robloxId")
    print(f"ROBLOX Info for {ID} \n Username: {rbxname} \n ID = {rbxid} \n")
except:
    print(f"Error, cannot fetch an account, this user may not have connected their ROBLOX account to their Discord. \n")

end = input("Press enter to exit.. ")