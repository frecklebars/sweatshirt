#what even is there to comment here just makes my job easier when copy pasting from genius
songlist = open("songlist.txt", "r", encoding="utf-8")
nice = open("nice.txt", "w+", encoding="utf-8")

a = songlist.readlines()
i = 0
for line in a:
    if not i % 2 == 0:
        nice.write("\"" + line.replace("\n", "") + "\",\n")
    i = i + 1
        
songlist.close()
nice.close()
