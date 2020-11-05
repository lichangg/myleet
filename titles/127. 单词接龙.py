#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
from typing import List

# 无脑用递归, 直接超时, 因为有些分支虽然也能到终点,但是很远,用贪心
# class Solution:
#
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         self.c = []
#         self.recur(beginWord, endWord, wordList, 1) or 0
#         if self.c:
#             return min(self.c)
#         else:
#             return 0
#
#
#     def filter_func(self,word1, word2):
#
#         i = 0
#         count = 0
#         while i < len(word1):
#             if word1[i] != word2[i]:
#                 count += 1
#             i+=1
#         if count > 1:
#             return False
#         else:
#             return True
#     def recur(self, beginWord: str, endWord: str, wordList: List[str], step):
#         if beginWord == endWord:
#             self.c.append(step)
#         if endWord not in wordList:
#             return
#         li_word = [i for i in wordList if self.filter_func(beginWord, i)]
#         new_wordList = wordList[:]
#         new_wordList = list(set(new_wordList) - set(li_word))
#         for i in li_word:
#                 res = self.recur(i, endWord, new_wordList, step+1)
#                 if res:
#                     return res

# 贪心仍然超时
# class Solution:
#     def filter_func(self,word1, word2):
#
#         i = 0
#         count = 0
#         while i < len(word1):
#             if word1[i] != word2[i]:
#                 count += 1
#             i+=1
#         if count == 1:
#             return True
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         self.end = endWord
#         def check(begin, wordList, step, li_word):
#             if self.end not in wordList or step<0:
#                 return
#             if begin == self.end:
#                 return True
#             new_li_word = [i for i in wordList if self.filter_func(begin, i)]
#             new_wordList = wordList[:]
#             new_wordList = list(set(new_wordList) - set(li_word))
#             for b in new_li_word:
#                 res = check(b, new_wordList, step-1, li_word)
#                 if res:
#                     return res
#
#
#         for i in range(len(wordList)):
#             res = check(beginWord, wordList, i, [])
#             if res:
#                 return i+1
#         else:
#             return 0

# 别人的单向BFS, 耗时160ms
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)

        queue = collections.deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            cur, step = queue.popleft()
            if cur == endWord:
                return step

            for i in range(m):
                for j in range(26):
                    tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                    if tmp not in visited and tmp in st:
                        queue.append((tmp, step + 1))
                        visited.add(tmp)

        return 0

# 别人的双向BFS,耗时120
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)
        lvisited = set()
        rvisited = set()
        lqueue = collections.deque()
        rqueue = collections.deque()

        lqueue.append(beginWord)
        rqueue.append(endWord)

        lvisited.add(beginWord)
        rvisited.add(endWord)
        step = 0

        while lqueue and rqueue:
            if len(lqueue) > len(rqueue):
                lqueue, rqueue = rqueue, lqueue
                lvisited, rvisited = rvisited, lvisited
            step += 1
            for k in range(len(lqueue)):
                cur = lqueue.popleft()
                if cur in rvisited:
                    return step

                for i in range(m):
                    for j in range(26):
                        tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                        if tmp not in lvisited and tmp in st:
                            lqueue.append(tmp)
                            lvisited.add(tmp)

        return 0


a=Solution().ladderLength(
"cet",
"ism",
["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
)
print(a)