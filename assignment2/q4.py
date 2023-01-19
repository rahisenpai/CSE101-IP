import random
l = ['abuse', 'adult', 'agent', 'anger', 'beach', 'birth', 'block', 'board', 'brain', 'bread', 'break', 'brown', 'buyer', 'cause', 'chain', 'chair', 'chest', 'chief', 'child', 'china', 'claim', 'coast', 'court', 'cover', 'cream', 'crime', 'crowd', 'crown', 'dance', 'death', 'depth', 'doubt', 'draft', 'dream', 'drink', 'drive', 'earth', 'entry', 'faith', 'fault', 'field', 'fight', 'final', 'focus', 'force', 'frame', 'frank', 'front', 'fruit', 'grant', 'group', 'guide', 'heart', 'henry', 'horse', 'hotel', 'house', 'image', 'index', 'input', 'jones', 'judge', 'knife', 'layer', 'lewis', 'light', 'lunch', 'major', 'march', 'match', 'metal', 'model', 'money', 'month', 'mouth', 'music', 'night', 'noise', 'north', 'novel', 'nurse', 'other', 'owner', 'panel', 'party', 'phase', 'phone', 'pilot', 'pitch', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'price', 'pride', 'prize', 'radio', 'range', 'ratio', 'reply', 'right', 'round', 'route', 'rugby', 'scale', 'scope', 'score', 'shape', 'share', 'shift', 'shirt', 'shock', 'sight', 'simon', 'smile', 'smith', 'smoke', 'sound', 'south', 'space', 'spite', 'sport', 'squad', 'stage', 'steam', 'stock', 'stone', 'store', 'study', 'style', 'sugar', 'table', 'thing', 'touch', 'tower', 'track', 'trade', 'train', 'trend', 'trial', 'uncle', 'unity', 'value', 'video', 'voice', 'waste', 'watch', 'water', 'while', 'white', 'whole', 'woman', 'world', 'youth']
word = l[random.randint(0,156)]
print(word)

c,y = 1,[]
while(c<=6):
    x=input('\nenter your guess: ').lower()
    if x==word:
        print('\nyou win')
        break
    for i in word:
        if i in x:
            y.append(i)
    z=''
    for i in range(5):
        if x[i]==word[i]:
            z+=x[i]
        else:
            z+='-'
    print(z)
    print('other characters present:',end=' ')
    for i in y:
        if i not in z:
            print(i,end=' ')
    print('\nNumber of tries left:',6-c)
    y.clear()
    c+=1
else:
    print("\nyou couldn't guess, the word was",word)