#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:43:43 2023

@author: pieropaialunga
"""

from .constants import * 
from .emotionai import * 

if __name__=='__main__':
    round_of_emotions = 3 #This multiplies the number of times you want to generate emotions (e.g. 3 -> 50x3 = 150 sentences)
    for _ in range(round_of_emotions):
        for picked_emotion in EMOTIONS: #Generate sentences for every emotion
            print('Processing Emotion AI for emotion %s' %(picked_emotion)) #Just a print statement
            emotion_generator = AIEmotionGenerator(emotion=picked_emotion,openaikey = OPEN_AI_API_KEY) #Calling the class of Emotion Generator 
            environment = emotion_generator.build_environment() #Build your folder to store the files
            text_for_emotion = emotion_generator.sentence_generator(environment=environment) #Generate sentences in those environment
            #print(text_for_emotion) #You can print the text you're saving in the files if you want...
