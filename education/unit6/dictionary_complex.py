users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
print(users["Tom"])     # { phone": "+971478745", "email": "supertom@gmail.com }


key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")


users2 = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    }
}
 
tom_skype = users2["Tom"].get("skype", "Undefined")
print(tom_skype)    # Undefined    