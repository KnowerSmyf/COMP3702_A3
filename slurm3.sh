#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:1
#SBATCH --partition=vgpu
#SBATCH --job-name="CartV1" 
#SBATCH --mail-user=s4745275@student.uq.edu.au
#SBATCH --mail-type=ALL
#SBATCH -e test_err.txt
#SBATCH -o test_out_5.txt

source /home/Student/s4745275/miniconda/bin/activate /home/Student/s4745275/miniconda
python dqn_gym.py --env CartPole-v1 --config_file config/dqn.yaml --network single-hidden --seed 1 --lr 5e-5