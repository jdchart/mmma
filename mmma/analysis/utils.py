import subprocess
import os
import uuid
import shutil
import scipy

def flucoma_subprocess(process_name : str, src : str, result_names : list, params : dict = {}):
    """Run a flucoma subprocess."""
    
    subprocess_list = [f"fluid-{process_name}", "-source", src]

    result_dests = []
    for item in result_names:
        file_name = os.path.join(os.getcwd(), "flucoma_process_temp", f"{str(uuid.uuid4())}_{item}.wav")
        result_dests.append(file_name)
        subprocess_list.append(f"-{item}")
        subprocess_list.append(file_name)
    os.makedirs(os.path.join(os.getcwd(), "flucoma_process_temp"))
    
    try:
        subprocess.run(subprocess_list)
        results = []
        for item in result_dests:
            results.append(_wav_to_np(item))
        if os.path.isdir(os.path.join(os.getcwd(), "flucoma_process_temp")):
            shutil.rmtree(os.path.join(os.getcwd(), "flucoma_process_temp"))
        return [results[i] for i in range(len(results))]
    except:
        if os.path.isdir(os.path.join(os.getcwd(), "flucoma_process_temp")):
            shutil.rmtree(os.path.join(os.getcwd(), "flucoma_process_temp"))

def _wav_to_np(path):
    """Convert the contents of a wav file to a numpy array."""
    try:
        rate, data = scipy.io.wavfile.read(path)
        return data
    except:
        print(f'Could not read: {path}')




#test_file = "/Users/jacob/Documents/Repos/mmma/test-corpora/audios/senita-8ch.wav"
#anal = flucoma_subprocess("mfcc", test_file, ["features"])
#print(anal)