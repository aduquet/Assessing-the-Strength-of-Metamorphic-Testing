import random
import numpy as np
import json

class InputGenerator():
    
    def __init__(self):
        self.mainDF = {}
        self.auxList = []
        
    # def generate_random_numbers(self, num_integers, num_floats, int_range, float_range):
    #     """
    #     Generate a list of random integers and floats.

    #     :param num_integers: Number of random integers to generate
    #     :param num_floats: Number of random floats to generate
    #     :param int_range: Tuple of (min, max) for integer range
    #     :param float_range: Tuple of (min, max) for float range
    #     :return: List of random integers and floats
    #     """
    def generate_random_numbers(self):
        
        num_range = (0, 10)
        num_floats = np.random.uniform(low=0, high=9, size=1).astype(int).item()
        num_int = np.random.uniform(low=0, high=9, size=1).astype(int).item()
        # size = num_int + num_floats
        
        random_integers_x = [random.randint(*num_range) for _ in range(num_int)]
        random_floats_x = [round(random.uniform(*num_range), 1) for _ in range(num_floats)]
        
        random_integers_y = [random.randint(*num_range) for _ in range(num_int)]
        random_floats_y = [round(random.uniform(*num_range), 1) for _ in range(num_floats)]

        xdat = random_integers_x + random_floats_x
        ydat = random_integers_y + random_floats_y
        
        random.shuffle(xdat)
        random.shuffle(ydat)

        return xdat, ydat
    
    def save_json(self, df, output, savePath):

        df.to_json(savePath + '/' + output + '.json', indent=4, orient="records")        
        json_str = df.to_json(orient='records')
        records = json.loads(json_str)
        
        # Create a new dictionary with the 'id' as the key
        formatted_records = {record['id']: record for record in records}

        # Convert the dictionary back to a JSON string
        formatted_json_str = json.dumps(formatted_records, indent=4)

        # Save the JSON string to a file
        output_file = savePath + '/' + output + '.json'
        with open(output_file, 'w') as file:
            file.write(formatted_json_str)


    def save_csv(self, df, output, savePath):
        df.to_csv(savePath + '/' + output + '.csv')
    


