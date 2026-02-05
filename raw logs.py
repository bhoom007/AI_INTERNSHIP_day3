raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users=set(raw_logs)
print(unique_users)
if "ID05" in raw_logs:
  print(True)
  print("The length of the original list=",len(raw_logs)) 
  print("The length of the list without duplicates",len(unique_users))   


