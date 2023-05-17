import torch
path='/home/hun99/self-supervised-speech-recognition/outputs/2023-05-16/20-47-03/checkpoints/checkpoint_best.pt'
ckpt=torch.load(path)
print(load_state_dict(ckpt))
# print(model['cfg'])
