import json
import csv


def converter(csv_file, model_name, json_file):
    res = []
    with open(csv_file, encoding="utf-8") as csvf:
        for row in csv.DictReader(csvf):
            to_add = {"model": model_name, "pk": int(row["Id"]) if "Id" in row else row["id"]}
            if "Id" in row:
                del row["Id"]
            else:
                del row["id"]
            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "price" in row:
                row["price"] = int(row["price"])
            to_add["fields"] = row
            res.append(to_add)

    with open(json_file, "w", encoding="utf-8") as jsf:
        jsf.write(json.dumps(res, ensure_ascii=False, ))
    return res


converter(csv_file="category.csv", model_name="ads.category", json_file="category.json")
converter(csv_file="ad.csv", model_name="ads.ad", json_file="ad.json")
converter(csv_file="location.csv", model_name="ads.location", json_file="location.json")
converter(csv_file="user.csv", model_name="ads.user", json_file="user.json")