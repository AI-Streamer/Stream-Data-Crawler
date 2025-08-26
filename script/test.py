import os
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess

model_dir = "FunAudioLLM/SenseVoiceSmall"

model = AutoModel(
    model=model_dir,
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 60000},
    punc_model="ct-punc",
    device="cuda:0",  # device="mps",
    hub="hf",
)


res = model.generate(
    # input=f"{model.model_path}/example/asr_example.wav",
    input="/Users/dongyueqi/Desktop/25th Ave NE 1.m4a",
    cache={},
    language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech", "auto"
    use_itn=True,
    batch_size_s=6000,
    merge_vad=True,  #
    merge_length_s=15,
)
text = rich_transcription_postprocess(res[0]["text"])
print(text)
