"""
Project: Unigrams
Task: Word Frequencies (Part Two)

This is a test program that students can use to verify that they are
able to compute the correct word frequencies, using the
unigram file, 'very_short.csv'.

Author: Sean Strout (sps@cs.rit.edu)
Language: Python 3
"""

__author__ = 'sps'

import wordData     # readWordFile, WordCount
import wordFreq     # wordFrequencies

def testVeryShort():
    """
    Test function for 'words_that_start_with_q.csv'.
    :return: None
    :rtype: NoneType
    """

    # Expected results from the q words
    MOST_FREQ_WORD = wordData.WordCount('request', 2816909)
    SECOND_MOST_FREQ_WORD = wordData.WordCount('wandered', 451106)
    LEAST_FREQ_WORD = wordData.WordCount('airport', 348996)

    # read in the words
    print('Testing with very_short.csv...')
    words = wordData.readWordFile('very_short.csv')

    # get the frequency of WordCount objects
    freqList = wordFreq.wordFrequencies(words)

    # test most frequent, second most frequent, and least frequent word
    print('Most frequent word: ',
          'OK' if freqList[0].word == MOST_FREQ_WORD.word and
                  freqList[0].count == MOST_FREQ_WORD.count
               else 'GOT: '+ str(freqList[0]) +
                    ', EXPECTED: ' + str(MOST_FREQ_WORD))

    print('Second most frequent word: ',
          'OK' if freqList[1].word == SECOND_MOST_FREQ_WORD.word and
                  freqList[1].count == SECOND_MOST_FREQ_WORD.count
               else 'GOT: '+ str(freqList[1]) +
                    ', EXPECTED: ' + str(SECOND_MOST_FREQ_WORD))

    print('Least frequent word: ',
          'OK' if freqList[2].word == LEAST_FREQ_WORD.word and
                  freqList[2].count == LEAST_FREQ_WORD.count
               else 'GOT: '+ str(freqList[2]) +
                    ', EXPECTED: ' + str(LEAST_FREQ_WORD))

if __name__ == '__main__':
    testVeryShort()