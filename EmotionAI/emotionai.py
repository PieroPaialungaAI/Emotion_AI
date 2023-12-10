from openai import OpenAI
from .constants import * 
from os import getcwd
from .util import *

class AIEmotionGenerator():
    
    def __init__(self,emotion, num_sentences = NUM_SENTENCES, environment_path = None, openaikey= OPEN_AI_API_KEY):
        self.emotion = emotion
        self.num_sentences = num_sentences
        if environment_path == None:
            self.environment_path = getcwd()
        self.open_ai_key = openaikey
    
    def build_environment(self):
        print('Building the environment paths...\n')
        environment_path = self.environment_path+'/'+DEFAULT_ENVIRONMENT_PATH
        emotions_paths = [environment_path+'/'+e+'_data' for e in EMOTIONS]
        create_folder(environment_path)
        [create_folder(emotion_path) for emotion_path in emotions_paths]
        all_paths = [environment_path] + emotions_paths
        path_names = ['Environment']+EMOTIONS
        path_dict = {path_names[i]:all_paths[i] for i in range(len(path_names))}
        return path_dict



    def sentence_generator(self,environment):
        client = OpenAI(api_key=self.open_ai_key)       
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a creative writer and you are writing a funny story for kids."},
                {"role": "user", "content": "What is a text that transmit %s?"%(self.emotion)},
                {"role": "assistant", "content": EMOTION_DICT[self.emotion]},
                {"role": "user", "content": "Give me %i more sentences like the example, split by '\n'. "%(self.num_sentences)}
              ]
            )
        text = response.choices[0].message.content
        create_result_log(environment[self.emotion],text)
        return text
    
