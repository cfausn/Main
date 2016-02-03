"""
Project: Unigrams
Task: Letter Frequencies (Part One)

This is a test program that students can use to verify that they are
able to compute the correct letter frequencies using the unigram file
'very_short.csv'.

Author: Sean Strout (sps@cs.rit.edu)
Language: Python 3
"""

import letterFreq   # letterFreq
import wordData     # readFile, totalOccurrences
import string       # ascii_lowercase

def testVeryShort():
    WORD_OCCURRENCES = {'airport' : 348996,
                        'request' : 2816909,
                        'wandered' : 451106}

    LETTER_FREQ = [0.03104758705050717,
                   0.0,
                   0.0,
                   0.03500991824543893,
                   0.2536276129665047,
                   0.0,
                   0.0,
                   0.0,
                   0.013542627927787708,
                   0.0,
                   0.0,
                   0.0,
                   0.0,
                   0.017504959122719464,
                   0.013542627927787708,
                   0.013542627927787708,
                   0.10930884736053291,
                   0.15389906233882777,
                   0.10930884736053291,
                   0.12285147528832062,
                   0.10930884736053291,
                   0.0,
                   0.017504959122719464,
                   0.0,
                   0.0,
                   0.0]

    print('Testing with very_short.csv...')
    words = wordData.readWordFile('very_short.csv')

    # test totalOccurrences
    for word in words:
        print('Total occurrences of', word + ':',
              'OK' if wordData.totalOccurrences(word, words) == WORD_OCCURRENCES[word] \
                else 'GOT: ' + str(wordData.totalOccurrences(word, words)) +
                     ', EXPECTED: ' + str(WORD_OCCURRENCES[word]))

    freqList = letterFreq.letterFreq(words)
    for ch, got, expected in zip(string.ascii_lowercase, freqList, LETTER_FREQ):
        print('Frequency of', ch + ':',
              'OK' if got == expected else 'GOT: ' + str(got) +
                    ', EXPECTED: ' + str(expected))

if __name__ == '__main__':
    testVeryShort()
