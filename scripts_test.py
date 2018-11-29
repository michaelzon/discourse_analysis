import csv
from article_list_test import article_list_test
from analyzer_man import list_sample_size, list_amount_pos, list_amount_neg, list_bigger_sample_size, list_total_amount_pos, list_total_amount_neg
# sample_size = 1
# amount_pos = 2
# amount_neg = 3

with open("my_csv_test.csv", "w", newline = "") as f:
    fieldnames = ["article_ID", "sample_size", "amount_pos", "amount_neg", "total_amount_pos", "total_amount_neg", "N"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(article_list_test)):
        writer.writerow({"article_ID": article_list_test[i][8:-4], "sample_size": list_sample_size[i], "amount_pos": list_amount_pos[i], "amount_neg": list_amount_neg[i], "total_amount_pos": list_total_amount_pos[i], "total_amount_neg": list_total_amount_neg[i], "N": list_bigger_sample_size[i]})
