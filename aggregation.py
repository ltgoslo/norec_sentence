import json
import os

def aggregate_sentence(sentence):
    opinions = sentence["opinions"]
    if len(opinions) == 0:
        label = 'Neutral'
    elif len(set([op['Polarity'] for op in opinions])) == 1:
        label = opinions[0]['Polarity']
    else:
        label = 'Mixed'
    return label

def aggregate_dataset(infile, outfile, labels=["Positive", "Negative"]):
    binary_data = []
    with open(infile) as o:
        finegrained_data = json.load(o)

    for sentence in finegrained_data:
        label = aggregate_sentence(sentence)
        if label in labels:
            new_sent = {}
            new_sent["sent_id"] = sentence["sent_id"]
            new_sent["text"] = sentence["text"]
            new_sent["label"] = label
            binary_data.append(new_sent)

    with open(outfile, "w") as out:
        json.dump(binary_data, out)

if __name__ == "__main__":


    input_dir = '../OLD/norec_fine/'
    output_dir = "./"

    for split in ["train", "dev", "test"]:
        infile = os.path.join(input_dir, "{}.json".format(split))
        binary = os.path.join(output_dir, "binary", "{}.json".format(split))
        threeway = os.path.join(output_dir, "3class", "{}.json".format(split))
        aggregate_dataset(infile, binary, labels=["Positive", "Negative"])
        aggregate_dataset(infile, threeway, labels=["Positive", "Negative", "Neutral"])
