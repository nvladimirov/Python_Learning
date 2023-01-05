# # d1 = {'dict1': 1, 'dictionary2': 2}
# # d2 = {'dict3': 3, 'dictionary4': 4}
# # s = sum(d1.values())
# # print(s)
# import pandas
#
# d1 = {"Name": ["Pankaj", "Lisa"], "ID": [1, 2]}
# d2 = {"Name": "David", "ID": 3}
# merged_dict = {**d1, **d2}
# print(merged_dict)
#
# d1 = {"Name": ["Pankaj", "Lisa"], "ID": [1, 2]}
# d2 = {"Name": "David", "ID": 3}
#
# df1 = pandas.DataFrame(d1, index={1, 2})
# df2 = pandas.DataFrame(d2, index={3})
#
# print('********\n', df1)
# print('********\n', df2)
#
# df3 = pandas.concat([df1, df2])
#
# print('********\n', df3)

# Initialize dictionaries
# test_dict1 = {'gfg': 'a', 'is': 'b', 'best': 'c'}
# test_dict2 = {'gfg': 'd', 'is': 'e', 'best': 'f'}
#
# # printing original dictionaries
# print("The original dictionary 1 : " + str(test_dict1))
# print("The original dictionary 2 : " + str(test_dict2))
#
# # Using dictionary comprehension + keys()
# # Concatenate Dictionary string values
# res = {key: test_dict1[key] + test_dict2.get(key, '') for key in test_dict1.keys()}
#
# # printing result
# print("The string concatenation of dictionary is : " + str(res))

# d1 = {"a": 1, "b": 2, "c": 3}
# a = d1["a"]
# b = d1["b"]
# c = d1["c"]
# print(a, b, c, sep="")


# class Dict1:
#     dict1 = {"a": 1, "b": 2, "c": 3}
#
#     def __init__(self, a: int, b: int, c: int, dict1):
#         self.a = a
#         self.b = b
#         self.c = c
#         Dict1.dict1 = dict1
#
#
# ab = Dict1.dict1["a"]
# bb = Dict1.dict1["b"]
# cb = Dict1.dict1["c"]
# print("Сумма значений словаря: {}".format(sum(Dict1.dict1.values())))
# print("Сложение строк: ", ab, bb, cb, sep="")

class Dict1:
    dict1 = {"q": 1, "w": 2, "e": 3}
    dict2 = {"r": 44, "t": 55, "y": 66}
    dict3 = {"u": 777, "i": 888, "o": 999}

    def __init__(self, dict1, dict2, dict3):
        self.dict3 = dict3
        self.dict2 = dict2
        self.dict1 = dict1

    @staticmethod
    def sum():
        Dict1.merged_dict = Dict1.dict1 | Dict1.dict2 | Dict1.dict3
        return print("Сумма значений словаря: {}".format(sum(Dict1.merged_dict.values())))

    @staticmethod
    def concat():
        q = Dict1.dict1["q"]
        w = Dict1.dict1["w"]
        e = Dict1.dict1["e"]
        r = Dict1.dict2["r"]
        t = Dict1.dict2["t"]
        y = Dict1.dict2["y"]
        u = Dict1.dict3["u"]
        i = Dict1.dict3["i"]
        o = Dict1.dict3["o"]
        return print("Сложение строк: ", q, w, e, r, t, y, u, i, o, sep="")


Dict1.sum()
Dict1.concat()
