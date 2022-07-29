# This code take a sentense , then match words and return as most matched words

def matchingWord(sentense1, sentense2):
    words1 = sentense1.split(" ")
    words2 = sentense2.split(" ")
    score = 0

    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    sentenses = ['python is good', 'This is good', 'python is not python snake']
    query = input('Enter your sentense\n')
    scores = [matchingWord(query, sentense) for sentense in sentenses]
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentenses) , reverse=True)]

    for score, mainSentense in sortedSentScore:
        print(f"{mainSentense} score with {score}")
        