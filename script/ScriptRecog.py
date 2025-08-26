import os
from tqdm import tqdm
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model_dir = "alextomcat/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch"
file_dir = "/home/red/Documents/data/text/script.txt"
audio_save_dir = "/home/red/Documents/data"

model = AutoModel(
    model=model_dir,
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 60000},
    punc_model="ct-punc",
    device="cuda:0",  # device="mps",
    hub="hf",
)

audios = [a for a in os.listdir(audio_save_dir) if os.path.isfile(audio_save_dir + '/' + a)]

for audio in tqdm(audios):
    res = model.generate(
        # input=f"{model.model_path}/example/asr_example.wav",
        input=f"{audio_save_dir}/{audio}",
        cache={},
        language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech", "auto"
        use_itn=True,
        batch_size_s=6000,
        merge_vad=True,  #
        merge_length_s=15,
        disable_pbar=True,
        disable_update=True,
    )
    if res:
        text = rich_transcription_postprocess(res[0]["text"])
    with open(file_dir, mode="a") as audio:
        audio.write(text + "\n")
        audio.write("\n")
