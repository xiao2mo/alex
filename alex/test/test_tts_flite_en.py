#!/usr/bin/env python
# -*- coding: utf-8 -*-

import __init__

import alex.utils.cache as cache
import alex.utils.audio as audio

from alex.components.tts.flite import FliteTTS

if __name__ == '__main__':
    print "Testing Flite TTS"
    print "=" * 120
    print

    text = 'Hello. Thank you for calling. '
    voice = 'kal'
    sample_rate = 16000

    print "Synthesize text:", text
    print "Voice:          ", voice
    print "Sample rate:    ", sample_rate
    print

    cfg = {
        'Audio': {
            'sample_rate': sample_rate
        },
        'TTS': {
        'Flite': {
            'debug': False,
            'voice': 'kal'
        }
        }
    }

    tts = FliteTTS(cfg)

    print 'calling TTS'
    wav = tts.synthesize(text)

    print 'saving the TTS audio in ./tmp/flite_tts.wav'
    audio.save_wav(cfg, './tmp/flite_tts.wav', wav)

    print 'playing audio'
    audio.play(cfg, wav)