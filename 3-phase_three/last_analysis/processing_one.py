import pandas as pd
import glob as gl
import json

main_df = pd.read_csv('~/Documents/Github/INFSOF_Paper/3-phase_three/last_analysis/a4.csv', index_col=0)

df_mutants_survived_all_td = main_df[(main_df['is_output_x_equal_true'] == 195) &
    (main_df['is_output_y_equal_true'] == 195) &
    (main_df['is_int_x_equal_true'] == 195) &
    (main_df['is_int_y_equal_true'] == 195)].reset_index()

df_mutants_killed_all_td = main_df[(main_df['is_output_x_equal_false'] == 195) &
    (main_df['is_output_y_equal_false'] == 195) &
    (main_df['is_int_x_equal_false'] == 195) &
    (main_df['is_int_y_equal_false'] == 195)].reset_index()

ids = list(df_mutants_survived_all_td['mutant_ID']) + list(df_mutants_killed_all_td['mutant_ID'])

df_mutants_mix_td = main_df.copy()

for index, row in df_mutants_mix_td.iterrows():
    
    if row['mutant_ID'] in ids:
        df_mutants_mix_td = df_mutants_mix_td.drop([index])

df_mutants_mix_td = df_mutants_mix_td.reset_index()

df_mutants_survived_all_td.to_csv('mutants_survived_all_td.csv')
df_mutants_killed_all_td.to_csv('df_mutants_killed_all_td.csv')
df_mutants_mix_td.to_csv('df_mutants_mix_td.csv')