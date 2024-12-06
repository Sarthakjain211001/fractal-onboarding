lambda_square_fun = lambda x : x*x
print(lambda_square_fun(5))

#map function using lambda function on a list
sample_list = [1,2,3,4,5]
res = map(lambda_square_fun, sample_list)
print(list(res))