class Solution:
       def groupAnagrams(self, strs):
      result = {} #  Expected indented block Pylance,  Unindent not expected Pylance
      for i in strs: #Unexpected indentation Pylance
         x = "".join(sorted())
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution() #Solution is not defined Pylance("Solution" is not definedPylancereportUndefinedVariable)
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
