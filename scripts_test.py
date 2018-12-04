import csv
from article_list_test import article_list_test
from pop_list import pop_list
from quality_list import quality_list
from tot_list import tot_list
from analyzer_man import list_sample_size, list_amount_pos, list_amount_neg, list_bigger_sample_size, list_total_amount_pos, list_total_amount_neg

# sample_size = 1
# amount_pos = 2
# amount_neg = 3

with open("my_csv_test.csv", "w", newline = "") as f:
    fieldnames = ["item_ID", "newspaper_type", "year", "sample_size", "amount_pos", "amount_neg", "N"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(article_list_test)):
        writer.writerow({"item_ID": article_list_test[i][8:-4], "newspaper_type": 0, "year": article_list_test[i][-8:-4], "sample_size": list_sample_size[i], "amount_pos": list_amount_pos[i], "amount_neg": list_amount_neg[i], "N": list_bigger_sample_size[i]})
    for i in range(len(pop_list)):
        writer.writerow({"item_ID": pop_list[i], "newspaper_type": 0, "year": pop_list[i][-4:], "sample_size": (list_sample_size[i] + list_sample_size[i+5]) , "amount_pos": (list_amount_pos[i] + list_amount_pos[i+5]), "amount_neg": (list_amount_neg[i] + list_amount_neg[i+5]), "N": "."})
    for i in range(len(quality_list)):
        writer.writerow({"item_ID": quality_list[i], "newspaper_type": 0, "year": quality_list[i][-4:], "sample_size": (list_sample_size[i+10] + list_sample_size[i+15]), "amount_pos": (list_amount_pos[i+10] + list_amount_pos[i+15]), "amount_neg": (list_amount_neg[i+10] + list_amount_neg[i+15]), "N": "."})
    for i in range(len(tot_list)):
        writer.writerow({"item_ID": tot_list[i], "newspaper_type": ".", "year": tot_list[i][-4:], "sample_size": (list_sample_size[i] + list_sample_size[i+5] + list_sample_size[i+10] + list_sample_size[i+15]), "amount_pos": (list_amount_pos[i] + list_amount_pos[i+5] + list_amount_pos[i+10] + list_amount_pos[i+15]), "amount_neg": (list_amount_neg[i] + list_amount_neg[i+5] + list_amount_neg[i+10] + list_amount_neg[i+15]), "N": "."  })



# voordat ik total amount pos en neg weghaalde
# with open("my_csv_test.csv", "w", newline = "") as f:
#     fieldnames = ["item_ID", "newspaper_type", "year", "sample_size", "amount_pos", "amount_neg", "total_amount_pos", "total_amount_neg", "N"]
#     writer = csv.DictWriter(f, fieldnames = fieldnames)
#     writer.writeheader()
#     for i in range(len(article_list_test)):
#         # print('eerste letter', article_list_test[i][8])
#         # if article_list_test[i][8] == "a" or "t":
#         #     newspaper_type = 0
#         # if article_list_test[i][8] == "n" or "v":
#         #     newspaper_type = 1
#         writer.writerow({"item_ID": article_list_test[i][8:-4], "newspaper_type": 0, "year": article_list_test[i][-8:-4], "sample_size": list_sample_size[i], "amount_pos": list_amount_pos[i], "amount_neg": list_amount_neg[i], "total_amount_pos": list_total_amount_pos[i], "total_amount_neg": list_total_amount_neg[i], "N": list_bigger_sample_size[i]})
#     for i in range(len(pop_list)):
#         writer.writerow({"item_ID": pop_list[i], "newspaper_type": 0, "year": pop_list[i][-4:], "sample_size": (list_sample_size[i] + list_sample_size[i+5]) , "amount_pos": (list_amount_pos[i] + list_amount_pos[i+5]), "amount_neg": (list_amount_neg[i] + list_amount_neg[i+5]), "total_amount_pos": (list_total_amount_pos[i] + list_total_amount_pos[i+5]), "total_amount_neg": list_total_amount_neg[i] + list_total_amount_neg[i+5], "N": "."})
#     for i in range(len(quality_list)):
#         writer.writerow({"item_ID": quality_list[i], "newspaper_type": 0, "year": quality_list[i][-4:], "sample_size": (list_sample_size[i+10] + list_sample_size[i+15]), "amount_pos": 20, "amount_neg": 30, "total_amount_pos": 40, "total_amount_neg": 50, "N": 60})
