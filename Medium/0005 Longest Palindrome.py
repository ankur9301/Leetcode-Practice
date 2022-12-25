class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length=0
        output=s[0]
        for i in range(len(s)-1):
            pointer=1
            substring=s[i]
            left=0
            right=1
            while i-left>=0 and i+right<=(len(s)-1) and s[i-left]==s[i+right]:
                substring=s[i-left:i+right+1]
                if len(substring)>max_length:
                    output=substring
                max_length=max(max_length,len(substring))
                left+=1
                right+=1
                # i+=1
                if len(substring)>max_length:
                    output=substring
                max_length=max(max_length,len(substring))
                
            while (i-pointer)>=0 and (i+pointer)<=len(s)-1 and s[i-pointer]==s[i+pointer]:
                substring=s[i-pointer:i+pointer+1]
                pointer+=1
                if len(substring)>max_length:
                    output=substring
                max_length=max(max_length,len(substring))
        return output



    #     max_length=0
    
    # output=s[0]
    # for i in range(len(s)-1):
    #     pointer=1
    #     substring=s[i]
        
        
    #     while i>=0 and i+1<=(len(s)-1) and s[i]==s[i+1]:
    #         substring+=s[i+1]
    #         if len(substring)>max_length:
    #             output=substring
    #         max_length=max(max_length,len(substring))
    #         # substring=""
            
    #         i+=1
    #         if len(substring)>max_length:
    #             output=substring
    #         max_length=max(max_length,len(substring))
            
    #     while (i-pointer)>=0 and (i+1+pointer)<=len(s)-1 and s[i-pointer]==s[i+pointer+1]:
    #         substring=s[i-pointer:i+pointer+1+1]
    #         pointer+=1
    #     if len(substring)>max_length:
    #         output=substring
    #     max_length=max(max_length,len(substring))
    #     # substring=""
        
    #     i+=1
    #     if len(substring)>max_length:
    #         output=substring
    #     max_length=max(max_length,len(substring))
            
            
    #     while (i-pointer)>=0 and (i+pointer)<=len(s)-1 and s[i-pointer]==s[i+pointer]:
    #         substring=s[i-pointer:i+pointer+1]
    #         pointer+=1
    #         if len(substring)>max_length:
    #             output=substring
    #         max_length=max(max_length,len(substring))
    # return output




        # substring=s[0]
        # max_length=0
        # output=s[0]
        # for i in range(len(s)-1):
        #     pointer=1
        #     copyi = i
        #     substring=s[i]
        #     #foreven palindrome
        #     while i>=0 and i+1<len(s)-1 and s[i]==s[i+1]:
        #         substring+=s[i+1]
        #         while (i-pointer)>=0 and (i+1+pointer)<=len(s)-1 and s[i-pointer]==s[i+pointer+1]:
        #             substring=s[i-pointer:i+pointer+2]
        #             pointer+=1
        #         i+=1
        #         if len(substring)>max_length:
        #             output=substring
        #         max_length=max(max_length,len(substring))
        #         substring=""
                
        #     while (copyi-pointer)>=0 and (copyi+pointer)<=len(s)-1 and s[copyi-pointer]==s[copyi+pointer]:
        #         substring=s[copyi-pointer:copyi+pointer+1]
        #         pointer+=1
        #         if len(substring)>max_length:
        #             output=substring
        #         max_length=max(max_length,len(substring))
        # return output



             
            






        
        # max_length=1
        # end=len(s)-1
        # substring=s[0]
        # output=s[0]
        # for i in range(len(s)):
        #     for j in range(end,i,-1):
        #         substring=s[i:j+1]
        #         if substring[::-1]==substring and len(substring)>=len(s)-i-1 and len(substring)>len(output):
        #             return substring
        #         if substring[::-1]==substring and len(substring)>max_length:
        #             max_length=max(max_length,len(substring))
        #             output=substring
        # return output
