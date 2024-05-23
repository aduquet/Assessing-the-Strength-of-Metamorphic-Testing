import pandas as pd
import glob as gl
import json
from utils import Utils

path_survived_mutants_all_td = '/Users/alduck/Documents/Github/INFSOF_Paper/3-phase_three/survived_mutants_all_td'
path_killed_mutants_all_td = '/Users/alduck/Documents/Github/INFSOF_Paper/3-phase_three/killed_mutants_all_td'
path_mixed_killed_td = '/Users/alduck/Documents/Github/INFSOF_Paper/3-phase_three/mixed_killed_td'

df_survived_mutants = pd.read_csv('/Users/alduck/Documents/Github/INFSOF_Paper/3-phase_three/last_analysis/df_mutants_survived_all_td.csv', index_col=0)
ids_survived_mutants = list(df_survived_mutants['mutant_ID'])

df_killed_mutants = pd.read_csv('/Users/alduck/Documents/Github/INFSOF_Paper/3-phase_three/last_analysis/df_mutants_killed_all_td.csv', index_col=0)
ids_killed_mutants = list(df_killed_mutants['mutant_ID'])

df_mixed_mutants = pd.read_csv('/Users/alduck/Documents/Github/INFSOF_Paper/3-phase_three/last_analysis/df_mutants_mix_td.csv', index_col=0)
ids_mixed_mutants = list(df_mixed_mutants['mutant_ID'])

logs_generated_paths = gl.glob('/Users/alduck/Documents/Github/INFSOF_Paper/2-phase_two/Logs_generated/*')


count_s = 0
count_k = 0
count_m = 0

for paths in logs_generated_paths:
    
    folder_name = paths.split('/')[-1]
    
    if folder_name in ids_survived_mutants:
        count_s += 1
        print('survided ', folder_name , ' count_s-> ', count_s)
        new_path = Utils.create_directories(folder_name=folder_name, base_directory= path_survived_mutants_all_td)
        Utils.copy_direct_to_directories(paths,new_path) 
    
    if folder_name in ids_killed_mutants:
        count_k += 1
        print('Killed ->', folder_name , ' count_k-> ', count_k)
        new_path = Utils.create_directories(folder_name=folder_name, base_directory= path_killed_mutants_all_td)
        Utils.copy_direct_to_directories(paths,new_path) 
        
    if folder_name in ids_mixed_mutants:
        count_m += 1
        print('mix ->', folder_name , ' count_m-> ', count_m)
        new_path = Utils.create_directories(folder_name=folder_name, base_directory= path_mixed_killed_td)
        Utils.copy_direct_to_directories(paths,new_path) 
        
        
    
        

    print(folder_name)
    
# new_path = Utils.create_directories(folder_name='Num8Line7Vers8', base_directory= path_killed_mutants_all_td)
# Utils.copy_direct_to_directories('/Users/alduck/Documents/Github/INFSOF_Paper/2-phase_two/Logs_generated/Num8Line7Vers8',new_path) 