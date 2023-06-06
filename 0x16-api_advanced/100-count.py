posts:
            title = post['data']['title'].lower()
                        for word in title.split(' '):
                                                if word in word_list:
                                                                            found_list.append(word)
                                                                                    if aft is not None:
                                                                                                        count_words(subreddit, word_list, found_list, aft)
                                                                                    else:
                                                                                                        result = {}
                                                                                                                    for word in found_list:
                                                                                                                                            if word.lower() in result.keys():
                                                                                                                                                                        result[word.lower()] += 1
                                                                                                                                            else:
                                                                                                                                                                        result[word.lower()] = 1
                                                                                                                                                                                    for key, value in sorted(result.items(), key=lambda item: item[1],
                                                                                                                                                                                                                                                  reverse=True):
                                                                                                                                                                                                            print('{}: {}'.format(key, value))
                                                                                                                                                                                    else:
                                                                                                                                                                                                    return~
