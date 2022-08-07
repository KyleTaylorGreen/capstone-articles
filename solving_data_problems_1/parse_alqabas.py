import pandas as pd
import regex as re

if __name__ == '__main__':

    # opens the source text file to be parsed
    source = 'Alqabas'
    with open(f'{source}.txt', 'r') as lines:

        # set data to the text file's contents, split each entry to a list
        data = lines.read()
        data = re.split(f'<{source}>|</{source}>', data)
        
        # holds each entry of article data to be made into a DataFrame
        article_list = []

        for i, article in enumerate(data):
            # disregard all failed searches and empty lists
            if article is not None and article != ['']:
                # append dictionary to article list, grab info from each tag
                try:
                    article_list.append({
                            'id': re.search('<ID>(.|\n)*<\/ID>', article).group()[4:-5],
                            'url': re.search('<URL>(.|\n)*<\/URL>', article).group()[5:-6],
                            'headline': re.search('<Headline>(.|\n)*<\/Headline>', article).group()[10:-11],
                            'dateline': re.search('<Dateline>(.|\n)*<\/Dateline>', article).group()[10:-11],
                            'text': re.search('<Text>(.|\n)*<\/Text>', article).group()[6:-7]
                    })
                except:
                    continue

        # write resulting DataFrame to csv
        df = pd.DataFrame(article_list)
        df.to_csv(f'{source}.csv', index=False)
        # sanity check
        print(df.head())
        print(df.shape)