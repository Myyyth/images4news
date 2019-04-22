import os

def get_keywords(path_to_news):
    import_data = '../mallet/bin/mallet import-dir --input ' + path_to_news + ' --output ../mallet_output/news.mallet' \
                                                                    ' --keep-sequence --remove-stopwords'
    #os.system(import_data)

    train_topics = '../mallet/bin/mallet train-topics --input ../mallet_output/news.mallet --num-topics 4 ' \
                   '--output-state ../mallet_output/topic-state.gz --output-doc-topics ../mallet_output/topic_composition.txt ' \
                   '--output-topic-keys ../mallet_output/topic-keys.txt --num-top-words 4'
    #os.system(train_topics)
    with open('mallet_output/topic-keys.txt', 'r') as f:
        topics = f.readlines()
    topics = [x.strip() for x in topics]
    result = []
    for topic in topics:
        result.append(' '.join(topic.split()[2:]))
    return result
