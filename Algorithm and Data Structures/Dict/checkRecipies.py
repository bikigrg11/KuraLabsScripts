def findAllRecipes(recipes, ingredients, supplies):

    # recipe = dict()

    # traverse through each recipies and add them to the dictionary
    # for i in range(len(recipes)):
    #     recipe[recipes[i]] = ingredients[i]
    output = []
    
    for i in range(len(ingredients)):
        flag = 0
        for eachIng in ingredients[i]:
            if eachIng in supplies or eachIng in output:
                pass
            else:
                flag = 1
        if flag == 0:
            output.append(recipes[i])

    # print(recipe)
    print(output)






# check the output with the below inputs
recipes = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
ingredients = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
supplies = ["wi","otr","wbjr","fzr","xgp"]

# call the function with the below inputs
print(findAllRecipes(recipes,ingredients,supplies))