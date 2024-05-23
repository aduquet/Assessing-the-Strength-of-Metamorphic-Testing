import os
import time
import click
import pathlib
import pandas as pd
import shortuuid
from input_generator import InputGenerator

@click.command()
@click.option('-t', '--t_end', 't_end')
@click.option('-o', '--output', 'output', help='Output file name')

def main(t_end, output):
    generator = InputGenerator()
    
    mainPath = str(pathlib.Path().absolute()) + '/inputs'
    try:
        os.mkdir(mainPath)
    except:
        pass

    t_end = time.time() + float(t_end)
    while time.time() < t_end:
        xdat, ydat = generator.generate_random_numbers()
        
        id = shortuuid.uuid(name=str(xdat + ydat ))

        mainDF = {
            'id': id,
            'td_xdat': xdat,
            'td_ydat': ydat,
            'size': len(xdat)}
        
        generator.auxList.append(mainDF)
    
    df = pd.DataFrame(generator.auxList)

    generator.save_json(df, output, mainPath)
    generator.save_csv(df, output, mainPath)

if __name__ == '__main__':
    main()
