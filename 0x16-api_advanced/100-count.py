t, word_list, hot_list, after)


def print_results(word_list, hot_list):
        '''Prints'''
            count = {}
                for word in word_list:
                            count[word] = 0
                                for title in hot_list:
                                            for word in word_list:
                                                            count[word] = count[word] +\
                                                                             len(re.findall(r'(?:^| ){}(?:$| )'.format(word), title, re.I))

                                                                count = {k: v for k, v in count.items() if v > 0}
                                                                    words = sorted(list(count.keys()))
                                                                        for word in sorted(words,
                                                                                                                  reverse=True, key=lambda k: count[k]):
                                                                                    print("{}: {}".format(word, count[word]))~
