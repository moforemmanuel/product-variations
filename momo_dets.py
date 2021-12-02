import re

fr_message = "Vous avez recu 50 FCFA de Emmanuel Nkwenti Mofor (237682999310) le 2021-11-30 22:12:38. Transaction Id: 3284332252.Reference: . Nouveau solde:92 FCFA. Envoie un MoMo de 5000F minimum et tente de gagner 1 TERRAIN chaque jour."
eng_message = "You just received FCFA 10000 from MFS AFRICA LIMITED (ECOBANK) at 2021-12-02 18:04:05. Transaction ID: 3291745108. Reference: Tranfert international New account balance: FCFA 10024. Send a MoMo of at least 5000F and try to win a piece of LAND each day."

#english
sender = re.search("(?<=from )(.*)(?=. Transaction)", eng_message).group().split(" at ")
sender_detail =  sender[0]
sender_name = re.search("(.*)(?= ())", sender_detail).group()
#sender_site = re.search("\(([^)]+)\)", "(uojsdfkb)").group()
sender_site = re.search("(?<= \()(.*)(?=\))", sender_detail).group()
sender_datetime = sender[1].split()
sender_date = sender_datetime[0]
sender_time = sender_datetime[1]
"""
print(sender)
print(sender_detail)
"""

print(sender_name)
print(sender_site)
print(sender_date)
print(sender_time)


reference = re.search("(?<=Reference: )(.*)(?= New account balance:)", eng_message).group()
print(reference)

amt_received = re.search("(?<=received FCFA )(\d*)(?= from)", eng_message).group()
print(amt_received)

acc_balance = re.search("(?<=New account balance: FCFA )(\d*)",eng_message).group()
print(acc_balance)
