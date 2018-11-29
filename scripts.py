import csv
from article_list import article_list

sample_size = 200
amount_pos = 10
amount_neg = 20

with open("my_csv.csv", "w", newline = "") as f:
    fieldnames = ["article_ID", "sample_size", "amount_pos", "amount_neg"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(article_list)):
        writer.writerow({"article_ID": article_list[i][8:-4], "sample_size": sample_size, "amount_pos": amount_pos, "amount_neg": amount_neg})
