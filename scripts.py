import csv
from article_list import article_list
from pop_list import pop_list
from quality_list import quality_list
from tot_list import tot_list
from analyzer_man import list_sample_size, list_amount_pos, list_amount_neg, list_bigger_sample_size, list_total_amount_pos, list_total_amount_neg, list_word_count

with open("my_results.csv", "w", newline = "") as f:
    fieldnames = ["item_ID", "newspaper_type", "year", "sample_size",
                    "amount_pos", "amount_neg", "N"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for i in range(len(article_list)):
        writer.writerow({"item_ID": article_list[i][8:-4], "newspaper_type": 0,
                        "year": article_list[i][-8:-4],
                        "sample_size": list_sample_size[i],
                        "amount_pos": list_amount_pos[i],
                        "amount_neg": list_amount_neg[i],
                        "N": list_bigger_sample_size[i]})

    for i in range(len(pop_list)):
        writer.writerow({"item_ID": pop_list[i], "newspaper_type": 0,
                        "year": pop_list[i][-4:],
                        "sample_size": (list_sample_size[i] + list_sample_size[i+21]),
                        "amount_pos": (list_amount_pos[i] + list_amount_pos[i+21]),
                        "amount_neg": (list_amount_neg[i] + list_amount_neg[i+21]),
                        "N": "."})

    for i in range(len(quality_list)):
        writer.writerow({"item_ID": quality_list[i],
                        "newspaper_type": 0, "year": quality_list[i][-4:],
                        "sample_size": (list_sample_size[i+42] + list_sample_size[i+63]),
                        "amount_pos": (list_amount_pos[i+42] + list_amount_pos[i+63]),
                        "amount_neg": (list_amount_neg[i+42] + list_amount_neg[i+63]),
                        "N": "."})

    for i in range(len(tot_list)):
        writer.writerow({"item_ID": tot_list[i],
                        "newspaper_type": ".", "year": tot_list[i][-4:],
                        "sample_size": (list_sample_size[i] + list_sample_size[i+21] +
                                        list_sample_size[i+42] + list_sample_size[i+63]),
                        "amount_pos": (list_amount_pos[i] + list_amount_pos[i+21] +
                                        list_amount_pos[i+42] + list_amount_pos[i+63]),
                        "amount_neg": (list_amount_neg[i] + list_amount_neg[i+21] +
                                        list_amount_neg[i+42] + list_amount_neg[i+63]),
                        "N": "."  })
