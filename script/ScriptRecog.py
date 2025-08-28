import os
from tqdm import tqdm
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
from VarMap import MODEL_DIRECTORY, AUDIO_SAVE_ADDRESS, SCRIPT_SAVE_ADDRESS

model = AutoModel(
    model=MODEL_DIRECTORY,
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 60000},
    punc_model="ct-punc",
    device="cuda:0",  # device="mps",
    hub="hf",
)

audios = [a for a in os.listdir(AUDIO_SAVE_ADDRESS) if os.path.isfile(AUDIO_SAVE_ADDRESS + '/' + a)]

for audio in tqdm(audios):
    res = model.generate(
        input=f"{AUDIO_SAVE_ADDRESS}/{audio}",
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
    with open(SCRIPT_SAVE_ADDRESS, mode="a") as audio:
        audio.write(text + "\n")
        audio.write("\n")
