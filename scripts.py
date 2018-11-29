import csv
from article_list import article_list
from analyzer_man import list_sample_size, list_amount_pos, list_amount_neg, list_bigger_sample_size, list_total_amount_pos, list_total_amount_neg

with open("my_results.csv", "w", newline = "") as f:
    fieldnames = ["article_ID", "sample_size", "amount_pos", "amount_neg", "total_amount_pos", "total_amount_neg", "N"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(article_list)):
        writer.writerow({"article_ID": article_list[i][8:-4], "sample_size": list_sample_size[i], "amount_pos": list_amount_pos[i], "amount_neg": list_amount_neg[i], "total_amount_pos": list_total_amount_pos[i], "total_amount_neg": list_total_amount_neg[i], "N": list_bigger_sample_size[i]})
