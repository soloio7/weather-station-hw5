def compute_stats(data_list, key):
    values = [entry[key] for entry in data_list]
    avg = sum(values) / len(values)
    return {
        "min": min(values),
        "max": max(values),
        "average": round(avg, 2)
    }