# open and read file
# f = open("De_Volkskrant_2017_1.TXT", "r")
#
# print(f.name)
#
# f.close()

# simaler, but you can do coding within the blok, close automatically(contextmanager)
# with open ("volkskrant_sample.txt", "r") as f:
#     fContents = f.readlines()
#     print(fContents, end=" ")

# index = 0
# with open ("volkskrant_sample.txt", "r") as f:
#     for line in f:
#         index += 1
#         print(index, line, end="")

# with open ("volkskrant_sample.txt", "r") as f:

    # sizeToRead = 10
    # fContents = f.read(sizeToRead)
    #
    # while len(fContents) > 0:
    #     print(fContents, end=)
    #     fContents = f.read(sizeToRead)



# with open ("volkskrant_sample.txt", "r") as f:
#
#     # sizeToRead = 301
#
#     fContents = f.readlines()
#     print("1111111111")
#     print(fContents, end=" ")
#
#     f.seek(34)
#
#     fContents = f.readlines()
#     print("222222222222")
#     print(fContents, end=" ")
#
#     print('\n')


with open("test2.txt", "w") as f:
    f.write("testje")
