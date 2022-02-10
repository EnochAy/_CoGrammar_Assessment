class Solution:
       def groupAnagrams(self, strs):
      result = {} #Expected indented blockPylance,  unindent not expected Pylance
      for i in strs: #unexpected indentation
         x = "".join(sorted())
         if x in result:
            result[x].append(i)
         else:
            result[x] = [i]
      return list(result.values())
ob1 = Solution() #solution is not defined("Solution" is not definedPylancereportUndefinedVariable)
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
