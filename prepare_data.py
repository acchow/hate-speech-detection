import json 
import config

if __name__ == "__main__": 
    data = []
    PATH = config.path
    with open(PATH + 'train.jsonl') as f:
        data = [ json.loads(line) for line in f ] 

    no_hate = []
    no_hate_ocr = {}
    hate = []
    hate_ocr = {}

    for meme in data: 
        # create ocr file
        f_name = meme['img'].split("/")[1]
        with open(PATH + f_name + '.ocr', "w") as f_ocr: 
            f_ocr.write(meme['text'])

        #split hate/nohate
        if meme['label'] == 0: 
            no_hate.append(f_name)
        else: 
            hate.append(f_name)

    train_hate = hate[:int(len(hate) * 0.8)]
    train_no_hate = no_hate[:int(len(no_hate) * 0.8)]
    valid_hate = hate[int(len(hate) * 0.8):]
    valid_no_hate = no_hate[int(len(no_hate) * 0.8):]

    with open(PATH + "hate_train.txt", "w") as f: 
        for hate in train_hate: 
            f.write(hate + '\n')

    with open(PATH + "nohate_train.txt", "w") as f: 
        for no_hate in train_no_hate: 
            f.write(no_hate + '\n')

    with open(PATH + "hate_valid.txt", "w") as f: 
        for hate in valid_hate: 
            f.write(hate + '\n')

    with open(PATH + "nohate_valid.txt", "w") as f: 
        for no_hate in valid_no_hate: 
            f.write(no_hate + '\n')
    
    print('Training:', len(train_hate), 'hate memes', len(train_no_hate), 'no hate')
    print('Validation:', len(valid_hate), 'hate memes', len(valid_no_hate), 'no hate')
    print('done')