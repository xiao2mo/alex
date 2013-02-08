#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import __init__

if __name__ == "__main__":
    import autopath
from SDS.components.asr.utterance import Utterance, UtteranceNBList, UtteranceConfusionNetwork

class TestUtteranceConfusionNetework(unittest.TestCase):
    """ Test using
            $ python -m unittest test_utterance
    """

    def test_conversion_of_confnet_into_nblist(self):

        A1, A2, A3 = 0.90, 0.05, 0.05
        B1, B2, B3 = 0.50, 0.35, 0.15
        C1, C2, C3 = 0.60, 0.30, 0.10

        correct_nblist = UtteranceNBList()
        correct_nblist.add(A1*B1*C1, Utterance("A1 B1 C1"))
        correct_nblist.add(A1*B2*C1, Utterance("A1 B2 C1"))
        correct_nblist.add(A1*B1*C2, Utterance("A1 B1 C2"))
        correct_nblist.add(A1*B2*C2, Utterance("A1 B2 C2"))
        correct_nblist.add(A1*B3*C1, Utterance("A1 B3 C1"))
        correct_nblist.add(A1*B1*C3, Utterance("A1 B1 C3"))
        correct_nblist.add(A1*B3*C2, Utterance("A1 B3 C2"))
        correct_nblist.add(A1*B2*C3, Utterance("A1 B2 C3"))
        correct_nblist.merge()
        correct_nblist.normalise()
        correct_nblist.sort()

        confnet = UtteranceConfusionNetwork()
        confnet.add([[A1, 'A1'], [A2, 'A2'], [A3, 'A3'],])
        confnet.add([[B1, 'B1'], [B2, 'B2'], [B3, 'B3'],])
        confnet.add([[C1, 'C1'], [C2, 'C2'], [C3, 'C3'],])
        confnet.merge()
        confnet.normalise()
        confnet.sort()

        gen_nblist = confnet.get_utterance_nblist(10)

        s = []
        s.append("")
        s.append("Confusion network:")
        s.append(str(confnet))
        s.append("")
        s.append("Generated nblist:")
        s.append(str(gen_nblist))
        s.append("")
        s.append("Correct nblist:")
        s.append(str(correct_nblist))
        s.append("")
        print '\n'.join(s)

        self.assertEqual(str(gen_nblist), str(correct_nblist))


if __name__ == '__main__':
    unittest.main()