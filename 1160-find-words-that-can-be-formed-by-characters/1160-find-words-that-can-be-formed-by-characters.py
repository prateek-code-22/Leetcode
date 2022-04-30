class Solution:
    def countCharacters(self, words: List[str], char: str) -> int:
        ans = 0
        char_dic = {}
        
        for i in range(len(char)):
            if char[i] not in char_dic:
                char_dic[char[i]] = 1
            else:
                char_dic[char[i]] +=1
        
        for word in words:
            word_dic = {}
            count = 0 
            for i in range(len(word)):   
                if word[i] not in word_dic:
                    word_dic[word[i]] = 1
                else:
                    word_dic[word[i]] +=1
            
            for i in range(len(word)):
                if char_dic.get(word[i]) != None:
                    if word_dic.get(word[i]) <= char_dic.get(word[i]):
                        count += 1
                else:
                    count += 0 
            
            #print(char_dic, word_dic,count)
            if count == len(word):
                ans += len(word)
                
        return ans