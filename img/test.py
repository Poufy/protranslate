strs = ["we","say",":","yes"]
sizes = [0]
joined_strs = ""
    # [0, 4, 4, 4, 3]
    # neetcodeloveyou
for word in strs:
    sizes.append(len(word))
    joined_strs = joined_strs + word
        
print(joined_strs)

for i in range(len(sizes) - 1):
    strs.append(joined_strs[sizes[i]: sizes[i] + sizes[i+1]])
    sizes[i+1] = sizes[i] + sizes[i+1]

print(strs)
print(len(strs))
print(joined_strs)
