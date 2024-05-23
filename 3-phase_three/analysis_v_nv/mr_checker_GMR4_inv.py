from mrg_checkers import *
import glob as gl
import json

'''
To Run example:

python3 mr_checker.py -n n -i '/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/Analysis/unmutated_new/Results_new_unmutated.json' -t '/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/Analysis/unmutated_new/Results_MRG1_inv_unmutated.json' -o 'gmr_inv_unmutated'

'''
if __name__ == '__main__':
    
    import click
    import os
    
    @click.command()
    @click.option('-n', '--dir', 'dir', help = '[y] if the path point to directory, [n] if the paths point tho individual files')
    @click.option('-i', '--root_path_td', 'root_path_td', help = 'Path to the json file with the outputs from the SUT excutions with the TD')
    @click.option('-t', '--root_path_ttd', 'root_path_ttd', help = 'Path to the json file with the outputs from the SUT excutions with the TTD')
    @click.option('-o', '--output', 'output', help = 'output name final file  with the violation status')
    
    def main(dir, root_path_td, root_path_ttd, output):
    
        with open('/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/Analysis/unmutated_new/test_data_MRG.json', 'r') as file:
            all_td_ttd = json.load(file)
            
        final_results = {}
        count = 0

        if(dir == 'n'):
            
            with open(root_path_td, 'r') as file:
                td = json.load(file)
    
            with open(root_path_ttd, 'r') as file:
                ttd = json.load(file)

            for key, value in td.items():
                
                try:
                    
                    vs_mrg_inv_g = Checker_MRG.mr_exc_g(td[key]['int_x'],td[key]['int_y'],ttd[key]['int_x'],ttd[key]['int_y'])
                    vs_mrg_inv_l =Checker_MRG.mr_exc_l(td[key]['int_x'],td[key]['int_y'],ttd[key]['int_x'],ttd[key]['int_y'])
                    vs_mrg_inv_e =Checker_MRG.mr_exc_equal(td[key]['int_x'],td[key]['int_y'],ttd[key]['int_x'],ttd[key]['int_y'])
                    final_file = {
                        key:{
                            'id': key,
                            'td_x': td[key]['input_xdat'],
                            'td_y': td[key]['input_ydat'],
                            'ttd_x': ttd[key]['input_xdat_trans'],
                            'ttd_y': ttd[key]['input_ydat_trans'],
                            'td_output_x': td[key]['output_xdat'],
                            'td_output_y': td[key]['output_ydat'],
                            'ttd_output_x' : ttd[key]['output_xdat'],
                            'ttd_output_y' : ttd[key]['output_ydat'],
                            'td_int_x' : td[key]['int_x'],
                            'td_int_y': td[key]['int_y'],
                            'ttd_int_x' : ttd[key]['int_x'],
                            'ttd_int_y': ttd[key]['int_y'],
                            'vs_gmr_inv_g': vs_mrg_inv_g,
                            'vs_gmr_inv_l': vs_mrg_inv_l,
                            'vs_gmr_inv_e': vs_mrg_inv_e,
                        }
                    }
                
                except:
                    final_file = {
                        key:{
                            'id': key,
                            'td_x': td[key]['input_xdat'],
                            'td_y': td[key]['input_ydat'],
                            'ttd_x': all_td_ttd[key]['ttd_xdat_MRG4_inv'],
                            'ttd_y': all_td_ttd[key]['ttd_xdat_MRG4_inv'],
                            'td_output_x': td[key]['output_xdat'],
                            'td_output_y': td[key]['output_ydat'],
                            'ttd_output_x' : 'NA',
                            'ttd_output_y' : 'NA',
                            'td_int_x' : td[key]['int_x'],
                            'td_int_y': td[key]['int_y'],
                            'ttd_int_x' : 'NA',
                            'ttd_int_y': 'NA',
                            'vs_gmr_inv_g': 'NA',
                            'vs_gmr_inv_l': 'NA',
                            'vs_gmr_inv_e': 'NA',
                        }
                    }
                
                final_results.update(final_file)
                count += 1
            output_name = output + '.json'
            with open(output_name, 'w') as json_file:
                json.dump(final_results, json_file, indent = 4 )
        
        if(dir == 'y'):
                
            paths = gl.glob(root_path_td)
            
            for root_path in paths:
                name_folder = root_path.split('/')[-1]
                
                new_root_path_td = os.path.join('/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/MutatedFiles/', name_folder)
                root_path_td_final = os.path.join(new_root_path_td, 'Results_' + name_folder +'.json')

                new_root_path_ttd = os.path.join('/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/not_crased_mutated_files_all_inputs', name_folder)
                root_path_ttd_final = os.path.join(new_root_path_ttd, 'Results_MRG4_inv_' + name_folder +'.json')
                save_path = os.path.join('/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/Analysis/analysis_step_3', name_folder)
                if os.path.exists(root_path_ttd_final) and os.path.exists(root_path_td_final):
                    
                    with open(root_path_td_final, 'r') as file:
                        td = json.load(file)
            
                    with open(root_path_ttd_final, 'r') as file:
                        ttd = json.load(file)
                        
                    for key, value in td.items():
                        
                        try:
                            vs_mrg_inv_g = Checker_MRG.mr_exc_g(td[key]['int_x'],td[key]['int_y'],ttd[key]['int_x'],ttd[key]['int_y'])
                            vs_mrg_inv_l =Checker_MRG.mr_exc_l(td[key]['int_x'],td[key]['int_y'],ttd[key]['int_x'],ttd[key]['int_y'])
                            vs_mrg_inv_e =Checker_MRG.mr_exc_equal(td[key]['int_x'],td[key]['int_y'],ttd[key]['int_x'],ttd[key]['int_y'])
                            final_file = {
                                key:{
                                    'id': key,
                                    'td_x': td[key]['input_xdat'],
                                    'td_y': td[key]['input_ydat'],
                                    'ttd_x': ttd[key]['input_xdat_trans'],
                                    'ttd_y': ttd[key]['input_ydat_trans'],
                                    'td_output_x': td[key]['output_xdat'],
                                    'td_output_y': td[key]['output_ydat'],
                                    'ttd_output_x' : ttd[key]['output_xdat'],
                                    'ttd_output_y' : ttd[key]['output_ydat'],
                                    'td_int_x' : td[key]['int_x'],
                                    'td_int_y': td[key]['int_y'],
                                    'ttd_int_x' : ttd[key]['int_x'],
                                    'ttd_int_y': ttd[key]['int_y'],
                                    'vs_gmr_inv_g': vs_mrg_inv_g,
                                    'vs_gmr_inv_l': vs_mrg_inv_l,
                                    'vs_gmr_inv_e': vs_mrg_inv_e,
                                }
                            }
                        
                        except:
                            final_file = {
                                key:{
                                    'id': key,
                                    'td_x': td[key]['input_xdat'],
                                    'td_y': td[key]['input_ydat'],
                                    'ttd_x': all_td_ttd[key]['ttd_xdat_MRG4_inv'],
                                    'ttd_y': all_td_ttd[key]['ttd_xdat_MRG4_inv'],
                                    'td_output_x': td[key]['output_xdat'],
                                    'td_output_y': td[key]['output_ydat'],
                                    'ttd_output_x' : 'NA',
                                    'ttd_output_y' : 'NA',
                                    'td_int_x' : td[key]['int_x'],
                                    'td_int_y': td[key]['int_y'],
                                    'ttd_int_x' : 'NA',
                                    'ttd_int_y': 'NA',
                                    'vs_gmr_inv_g': 'NA',
                                    'vs_gmr_inv_l': 'NA',
                                    'vs_gmr_inv_e': 'NA',
                                }
                            }
                            
                        final_results.update(final_file)
                        count += 1
                    
                    output_name = save_path + '/' + output + '.json'
                    with open(output_name, 'w') as json_file:
                        json.dump(final_results, json_file, indent = 4 )
                        
                else:
                    print('missed file: ', root_path_ttd_final)
main()
        