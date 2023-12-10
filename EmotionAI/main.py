#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:43:43 2023

@author: pieropaialunga
"""

from .constants import * 
from .emotionai import * 

if __name__=='__main__':
    round_of_emotions = 3
    for number_of_simulation in range(round_of_emotions):
        for picked_emotion in EMOTIONS:
            print('Processing Emotion AI for emotion %s' %(picked_emotion))
            emotion_generator = AIEmotionGenerator(emotion=picked_emotion,openaikey = OPEN_AI_API_KEY)
            environment = emotion_generator.build_environment()
            text_for_emotion = emotion_generator.sentence_generator(environment=environment)
            print(text_for_emotion)