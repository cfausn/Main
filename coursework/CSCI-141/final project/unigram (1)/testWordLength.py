"""
Project: Unigrams
Task: Average Word Length (Part Three)

This is a test program that students can use to verify that they are
able to compute the correct word lengths using the unigram file
'very_short.csv'.

Author: Sean Strout (sps@cs.rit.edu)
Language: Python 3
"""

__author__ = 'sps'

import wordData     # readWordFile
import wordLength   # occurrencesInAYear, averageWordLength,
                    # averageWordLengthYears

def testVeryShort():
    """
    Test function for 'very_short.csv'.
    :return: None
    :rtype: NoneType
    """

    # expected results
    AIRPORT_2007 = 175702
    REQUEST_2004 = 0
    AVG_WORD_LENGTH_2007 = 7.110627395031065
    AVG_WORD_LENGTH_2004 = 0
    AVG_WORD_LENGTHS_2005_2008 = [
         7.1147602294958,       # 2005
         7.114548770228398,     # 2006
         7.110627395031065,     # 2007
         7.150069236398865      # 2008
    ]

    print('Testing with very_short.csv...')
    words = wordData.readWordFile('very_short.csv')

    # test occurrencesInAYear
    occurrences = wordLength.occurrencesInYear('airport', 2007, words)
    print('Occurrences of "airport" in 2007:',
          'OK' if occurrences == AIRPORT_2007
               else 'GOT: ' +  str(occurrences) +
                    ', EXPECTED: ' + str(AIRPORT_2007))

    occurrences = wordLength.occurrencesInYear('request', 2004, words)
    print('Occurrences of "request" in 2004:',
          'OK' if occurrences == REQUEST_2004
               else 'GOT: ' +  str(occurrences) +
                    ', EXPECTED: ' + str(REQUEST_2004))

    # test averageWordLength
    length = wordLength.averageWordLength(2007, words)
    print('Average word length in 2007:',
          'OK' if length == AVG_WORD_LENGTH_2007
               else 'GOT: ' + str(length) +
                    ', EXPECTED: ' + str(AVG_WORD_LENGTH_2007))

    length = wordLength.averageWordLength(2004, words)
    print('Average word length in 2004:',
          'OK' if length == AVG_WORD_LENGTH_2004
               else 'GOT: ' + str(length) +
                    ', EXPECTED: ' + str(AVG_WORD_LENGTH_2004))

    # averageWordLengthYears
    lengthsList = wordLength.averageWordLengthYears(2005, 2008, words)
    yearList = list(range(2005, 2009))
    for year, got, expected in zip(yearList, lengthsList,
        AVG_WORD_LENGTHS_2005_2008):
        print('Average word length for', str(year) + ':',
              'OK' if got == expected else
                   'GOT:' + str(got) +
                   ', EXPECTED: ' + str(expected))

if __name__ == '__main__':
    testVeryShort()