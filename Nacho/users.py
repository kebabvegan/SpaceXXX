
users_al = {}

def add_user(pseudo, ip):
    users_al[pseudo] = ip

def listOf_users():
    listof = []
    for pseudo_users in users_al.keys():
        listof.append(pseudo_users)
    return listOf_users()

def user_islogged(ip):
    for pseudo_users in users_al.keys():
        if users_al[users_al] == ip:
            return True
    return False

def getIP(ip):
    for ip_users in users_al.keys():
        if users_al[users_al] == ip:
            return ip_users
