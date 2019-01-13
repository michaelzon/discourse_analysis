import csv
from article_list_icb import article_list_icb
from analyzer_man_icb import list_sample_size, list_amount_pos, list_amount_neg

with open("my_icb_results.csv", "w", newline = "") as f:
    fieldnames = ["item_ID", "sample_size", "amount_pos", "amount_neg"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(article_list_icb)):
        writer.writerow({"item_ID": article_list_icb[i], "sample_size": list_sample_size[i], "amount_pos": list_amount_pos[i], "amount_neg": list_amount_neg[i]})
