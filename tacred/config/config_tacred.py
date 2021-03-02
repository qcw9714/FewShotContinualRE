import torch
import json

CONFIG= {
    'learning_rate': 0.001,
    'embedding_dim': 300,
    'hidden_size': 200,
    'batch_size': 50,
    'gradient_accumulation_steps':1,
    'num_clusters': 10,
    'epoch': 2,
    'random_seed': 100,
    'task_memory_size': 10,
    'loss_margin': 0.5,
    'sequence_times': 5,
    'lambda': 100,
    'num_cands': 10,
    'num_steps': 1,
    'num_constrain': 10,
    'data_per_constrain': 5,
    'lr_alignment_model': 0.0001,
    'epoch_alignment_model': 20,
    'checkpoint_path': 'checkpoint',
    'use_gpu': True,
    'relation_file': './data/tacred/relation_name.txt',
    'training_file': './data/tacred/train.txt',
    'test_file': './data/tacred/test.txt',
    'valid_file': './data/tacred/val.txt',
    'task_name': 'FewRel',
    'num_workers':4,
    'max_grad_norm':1
}

f = open("config_tacred_10.json", "w")
f.write(json.dumps(CONFIG))
f.close()

