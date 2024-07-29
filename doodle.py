S = 'Python'
P = [S[ :i] for i in range (len(S)+1)]
printf(*(P+P[ ::-1]), sep = '\n')
