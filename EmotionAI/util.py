import os
from .constants import * 

def create_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        # Create the folder if it doesn't exist
        os.makedirs(folder_path)
        print(f"Environment '{folder_path}' created.")
    else:
        print(f"Environment '{folder_path}' already exists.")
        


def create_result_log(emotion_path,text_to_write):
    emotion = (emotion_path.split('/')[-1]).split('_')[0]
    print(emotion)
    files = [f for f in os.listdir(emotion_path) if os.path.isfile(os.path.join(emotion_path, f))]
    if len(files)!=0:
        num_file = len(files)
    else:
        num_file = 0
    file_path = emotion_path+'/log_%s_%s.txt'%(emotion,str(num_file))
    with open(file_path, 'w') as file:
         # Write content to the file
         file.write(text_to_write)
    print(f"File '{file_path}' created.")
    
    
def build_environment_path(root_path):
    environment_path = root_path+'/'+DEFAULT_ENVIRONMENT_PATH
    emotions_paths = [environment_path+'/'+e+'_data' for e in EMOTIONS]
    all_paths = [environment_path] + emotions_paths
    path_names = ['Environment']+EMOTIONS
    path_dict = {path_names[i]:all_paths[i] for i in range(len(path_names))}
    return path_dict