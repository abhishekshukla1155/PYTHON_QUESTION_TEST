list1 = ["python", "fun", "java", "ai", "data analysis", "practice", "patience", "go"]
lam = lambda x: len(x) > 5
result = filter(lam, list1)
print(list(result))