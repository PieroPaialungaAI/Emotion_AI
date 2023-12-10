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
    
    def build_environment(self): #Creating the environment (folders)
        print('Building the environment paths...\n') 
        environment_path = self.environment_path+'/'+DEFAULT_ENVIRONMENT_PATH #This is where you will store your folder
        emotions_paths = [environment_path+'/'+e+'_data' for e in EMOTIONS] #In your folder, you will create a subfolder per emotion
        create_folder(environment_path) #Create the main folder 
        [create_folder(emotion_path) for emotion_path in emotions_paths] #Create the subfolders
        all_paths = [environment_path] + emotions_paths #Creating the dictionary values (just to store it as a variable)
        path_names = ['Environment']+EMOTIONS #Creating the dictionary keys (just to store it as a variable)
        path_dict = {path_names[i]:all_paths[i] for i in range(len(path_names))} #Creating the dictionary
        return path_dict



    def sentence_generator(self,environment):
        client = OpenAI(api_key=self.open_ai_key) #This is the code to talk with the OpenAI
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a creative writer and you are writing a funny story for kids."}, #You tell OpenAI to be a story writer
                {"role": "user", "content": "What is a text that transmit %s?"%(self.emotion)}, #Give them a hint of the emotions
                {"role": "assistant", "content": EMOTION_DICT[self.emotion]}, #Selecting the emotions that we give them as an hint
                {"role": "user", "content": "Give me %i more sentences like the example, split by '\n'. "%(self.num_sentences)} #Give me X more examples...
              ]
            )
        text = response.choices[0].message.content #This is what you use to extract the text 
        create_result_log(environment[self.emotion],text) #Add the text to the folder of the environment
        return text
    
