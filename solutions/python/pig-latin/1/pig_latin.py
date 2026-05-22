""""""
"""又放弃了🥹，反正我今天已经做了%60了，下次再来挑战。插个旗子5月12"""
"""兄弟不要怕这个顺序很重要哈哈哈哈哈哈，其实也可以一个一个试🤣"""
"""继续插旗子，现在是5月20号，已经试了百分之90了，还有一点就能跑通了。另外再跑通之后，一定要去看社区解决方法，还有就是可以看看有没有规则可以简化，我的想法是其实规则三和规则四就是一个变量替换，或许可以简化。"""
"""兄弟今天是5月21，我最后还是用了ai，我真的放弃了，我今天啥也没干，我好伤心😭，算了早点睡也是我干了事"""
#VOWEL = ("a","e","i","o","u")

def translate(text):
    """    
    if text.startswith(VOWEL) or text.startswith("xr") or text.startswith("yt"):
        return text + "ay"#这行代码是规则1，这行代码并没有问题，只是后面的顺序可能需要调换。
        
    if "qu" in text and all(c not in VOWEL for c in text[:text.find("qu")]):
        pos = text.find("qu") + 2
        return text[pos:] + text[:pos] + "ay"#规则三，这行代码目前不清楚，能跑，但是我并没有理解，并且可能需要调换顺序
    
    if "y" in text and all(char not in VOWEL for char in text[:text.find("y")]):
        y_pos = text.find("y")
        return text[y_pos:] + text[:y_pos] + "ay"#规则四，和规则三同样
     
    i = next((i for i, char in enumerate(text) if char.lower() in VOWEL), 0)
    return text[i:] + text[:i] + "ay"    #规则二，代码没有问题，大概不需要调换位置，没有if因为是一个elif条件。
    """#上面是我之前自己推出来的写法

    VOWEL = "aeiouAEIOU"
    words = text.split()
    result = []
    
    for word in words:
        # 1. 傻瓜式特例拦截：元音、xr、yt 开头，直接加 ay，最省心
        if word.startswith(tuple(VOWEL)) or word.startswith("xr") or word.startswith("yt"):
            result.append(word + "ay")
            
        # 2. 剩下的全是辅音开头的单词了，我们从左到右，一个字母一个字母地数
        else:
            pos = 0  # 记录切开的位置
            
            for i in range(len(word)):
                # 如果看到以 qu 开头或者中间有 qu (比如 squ...)
                if word[i:].startswith("qu"):
                    pos = i + 2  # 找到了！切分点在 qu 后面（比如 squ | are）
                    break
                # 如果看到了普通的元音，或者看到了不是第一个字母的 y
                elif word[i] in VOWEL or (word[i] == "y" and i > 0):
                    pos = i      # 找到了！切分点就在它前面（比如 str | ing）
                    break
            
            # 找到点之后，一刀切成两半，调换顺序拼上 "ay"
            result.append(word[pos:] + word[:pos] + "ay")
            
    return " ".join(result)
    #上面是ai的写法。
