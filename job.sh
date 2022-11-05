#!/bin/bash
#
#SBATCH --job-name=ciw_gan_2word
#SBATCH --account=fc_bsclab
#
#SBATCH --partition=savio3_gpu
#SBATCH --ntasks=1
#SBATCH --qos=v100_gpu3_normal
#SBATCH --gres=gpu:V100:1
#SBATCH --cpus-per-task=4
#
#
#SBATCH --output=./envelope.out
#SBATCH --error=./envelope.err
# Wall clock limit:
#SBATCH --time=72:00:00
#
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=azhou314@berkeley.edu
## Command(s) to run (example):
module load ml/tensorflow/1.12.0-py36
nohup python backup.py ./2_word_concat/train_dir 60 &
python train_ciwgan.py train ./2_word_concat/train_dir/ --data_dir ./2_word_concat/generated_data/ --data_slice_len 32768 --num_categ 6 --data_first_slice --data_fast_wav --data_pad_end 