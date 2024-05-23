

import glob as gl
import subprocess
import time  # Import the time module

def run_dot_m_script(output, command, folder_name):
    start_time = time.time()  # Capture start time
    # Open the file for writing
    with open(output, "w") as outfile:
        # Execute the MATLAB command and redirect stdout and stderr to the file
        subprocess.run(command, stdout=outfile, stderr=subprocess.STDOUT)
    end_time = time.time()  # Capture end time
    execution_time = end_time - start_time  # Calculate execution time
    print('DONE with ', folder_name, '. Execution time: ', execution_time, ' seconds')

def get_folder_name(path):
    return path.split('/')[-1]

if __name__ == '__main__':
    import click
    import os
    
    @click.command()
    @click.option('-i', '--path_mutated_files', 'path_mutated_files', help = 'path to the files')
    @click.option('-m', '--dot_m_file_name', 'dot_m_file_name', help = 'name of the main .m file')
    
    def main(path_mutated_files, dot_m_file_name):
        
        files_path = gl.glob(path_mutated_files)
        
        # ready = ['Num84Line13Vers2', 'Num313Line25Vers4', 'Num433Line43Vers19', 'Num955Line115Vers10', 'Num1039Line117Vers13', 'Num608Line85Vers30', 'Num232Line16Vers38', 'Num1230Line139Vers15', 'Num46Line10Vers7', 'Num117Line13Vers35', 'Num606Line85Vers28', 'Num161Line15Vers5', 'Num336Line34Vers8', 'Num324Line33Vers3', 'Num878Line112Vers52', 'Num192Line15Vers36', 'Num446Line60Vers1', 'Num1283Line140Vers41', 'Num1095Line118Vers27', 'Num920Line114Vers25', 'Num943Line114Vers48', 'Num1297Line141Vers9', 'Num872Line112Vers46', 'Num774Line101Vers50', 'Num113Line13Vers31', 'Num404Line42Vers7', 'Num253Line20Vers4', 'Num667Line87Vers14', 'Num1343Line149Vers2', 'Num757Line101Vers33', 'Num456Line61Vers5', 'Num419Line43Vers5', 'Num1219Line139Vers4', 'Num1058Line117Vers32', 'Num1072Line118Vers4', 'Num1145Line122Vers27', 'Num508Line72Vers10', 'Num387Line41Vers31', 'Num108Line13Vers26', 'Num898Line114Vers3', 'Num1309Line144Vers8', 'Num165Line15Vers9', 'Num1052Line117Vers26', 'Num105Line13Vers23', 'Num179Line15Vers23', 'Num1334Line146Vers20', 'Num534Line83Vers2', 'Num292Line20Vers43', 'Num678Line88Vers8', 'Num305Line22Vers4', 'Num461Line61Vers10', 'Num474Line63Vers10', 'Num1304Line144Vers3', 'Num520Line82Vers3', 'Num867Line112Vers41', 'Num1102Line118Vers34', 'Num810Line104Vers11', 'Num452Line61Vers1', 'Num266Line20Vers17', 'Num1237Line139Vers22', 'Num248Line19Vers8', 'Num877Line112Vers51', 'Num407Line42Vers10', 'Num771Line101Vers47', 'Num1111Line119Vers1', 'Num944Line114Vers49', 'Num39Line9Vers13', 'Num880Line112Vers54', 'Num1293Line141Vers5', 'Num826Line104Vers27', 'Num971Line115Vers26', 'Num262Line20Vers13', 'Num510Line72Vers12', 'Num1155Line122Vers37', 'Num216Line16Vers22', 'Num91Line13Vers9', 'Num1036Line117Vers10', 'Num622Line86Vers4', 'Num202Line16Vers8', 'Num524Line82Vers7', 'Num747Line101Vers23', 'Num1329Line146Vers15', 'Num569Line84Vers17', 'Num875Line112Vers49', 'Num101Line13Vers19', 'Num580Line85Vers2', 'Num280Line20Vers31', 'Num930Line114Vers35', 'Num139Line14Vers20', 'Num764Line101Vers40', 'Num1055Line117Vers29', 'Num949Line115Vers4', 'Num614Line85Vers36', 'Num187Line15Vers31', 'Num144Line14Vers25', 'Num868Line112Vers42', 'Num1380Line152Vers4', 'Num1333Line146Vers19', 'Num220Line16Vers26', 'Num379Line41Vers23', 'Num42Line10Vers3', 'Num1078Line118Vers10', 'Num284Line20Vers35', 'Num1057Line117Vers31', 'Num828Line112Vers2', 'Num400Line42Vers3', 'Num472Line63Vers8', 'Num23Line8Vers10', 'Num610Line85Vers32', 'Num365Line41Vers9', 'Num140Line14Vers21', 'Num1076Line118Vers8', 'Num1056Line117Vers30', 'Num111Line13Vers29', 'Num1079Line118Vers11', 'Num1340Line147Vers1', 'Num58Line11Vers12', 'Num1251Line140Vers9', 'Num954Line115Vers9', 'Num765Line101Vers41', 'Num437Line51Vers1', 'Num1310Line144Vers9', 'Num78Line11Vers32', 'Num682Line88Vers12', 'Num674Line88Vers4', 'Num1332Line146Vers18', 'Num869Line112Vers43', 'Num831Line112Vers5', 'Num153Line14Vers34', 'Num910Line114Vers15', 'Num1054Line117Vers28', 'Num1037Line117Vers11', 'Num1240Line139Vers25', 'Num807Line104Vers8', 'Num1154Line122Vers36', 'Num226Line16Vers32', 'Num276Line20Vers27', 'Num281Line20Vers32', 'Num181Line15Vers25', 'Num554Line84Vers2', 'Num649Line86Vers31', 'Num874Line112Vers48', 'Num1328Line146Vers14', 'Num443Line52Vers4', 'Num647Line86Vers29', 'Num145Line14Vers26', 'Num427Line43Vers13', 'Num67Line11Vers21', 'Num22Line8Vers9', 'Num385Line41Vers29', 'Num545Line83Vers13', 'Num770Line101Vers46', 'Num285Line20Vers36', 'Num272Line20Vers23', 'Num876Line112Vers50', 'Num593Line85Vers15', 'Num548Line83Vers16', 'Num485Line63Vers21', 'Num820Line104Vers21', 'Num633Line86Vers15', 'Num141Line14Vers22', 'Num488Line63Vers24', 'Num574Line84Vers22', 'Num157Line15Vers1', 'Num881Line112Vers55', 'Num725Line101Vers1', 'Num490Line63Vers26', 'Num343Line37Vers1', 'Num728Line101Vers4', 'Num1335Line146Vers21', 'Num866Line112Vers40', 'Num422Line43Vers8', 'Num460Line61Vers9', 'Num502Line72Vers4', 'Num756Line101Vers32', 'Num1354Line150Vers2', 'Num1053Line117Vers27', 'Num717Line92Vers7', 'Num798Line103Vers8', 'Num1161Line130Vers5']
        path_mr_checker_gmr1 = '/Users/alduck/Documents/Github/mt_industrial_usecase/SpecialIssue_PROFES/MutationAnalisys/Analysis/analysis_v_nv/mr_checker_GMR1_mul.py'
        ready = []
        for path in files_path:
        
            folder_name = get_folder_name(path)
            print('***** Procesing:', folder_name)
        
            if folder_name in ready:
                print(f"{folder_name} is ready" )

            else:
                
                output = path + '/' + folder_name + 'MRG1_checker.txt'

                command = [ "python3",
                        path_mr_checker_gmr1,
                        "-n",
                        "-nodesktop",
                        "-r",]
                
                m = path + '/' + dot_m_file_name
                
                path_dot_m = "try, run(" + "'" + m + "'); catch ME, fprintf(2, 'Error encountered: %s\\n', getReport(ME)); end; exit;"
                
                command.append(path_dot_m)
                
                run_dot_m_script(output=output, command=command, folder_name=folder_name)
                print('*****')

main()
