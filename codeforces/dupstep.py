lyrics = input()

new = lyrics.replace('WUB', ' ')


l = new.split()

result = ''


for i in l:
    result+=i+' '

print(result)
