import os
import math
import shutil

class Checker_MRG():
    
    '''Change in the input: Multiply all x_data, and y_data values by a positive constant k'''
    '''Posible outcome: 
    - intersection point (int_x, int_y) should also be sscaled by k
    - new intersection point > than original
    - new intersection point =
    - new intersection point <
    '''
    def mr_mul_scaled(td_int_x, td_int_y, ttd_int_x, ttd_int_y, const):
        
        try:
            
            expected_int_x = td_int_x * const
            expected_int_y = td_int_y * const
            diff_x = expected_int_x - ttd_int_x
            diff_y = expected_int_x - ttd_int_y
            
            if math.isclose(expected_int_x, ttd_int_x, rel_tol= 1e-5) and math.isclose(expected_int_y,ttd_int_y, rel_tol= 1e-5):
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR, 'NA', 'NA'
    
    def mr_mul_g(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
        
        try:
            
            if td_int_x < ttd_int_x and td_int_y < ttd_int_y:
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_mul_l(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
        
        try:
            
            if td_int_x > ttd_int_x and td_int_y > ttd_int_y:
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_mul_equal(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
        
        try:
            
            if math.isclose(td_int_x, ttd_int_x, rel_tol= 1e-4) and math.isclose(td_int_y,ttd_int_y, rel_tol= 1e-4):
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_exc_g(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
        
        try:
            
            if td_int_x < ttd_int_x and td_int_y < ttd_int_y:
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_exc_l(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
        
        try:
            
            if td_int_x > ttd_int_x and td_int_y > ttd_int_y:
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_exc_equal(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
        
        try:
            
            if math.isclose(td_int_x, ttd_int_x, rel_tol= 1e-2) and math.isclose(td_int_y,ttd_int_y, rel_tol= 1e-2):
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_ref_eq(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
            
        try:
            expected_int_x = td_int_x * (-1)
            expected_int_y = td_int_y * (-1)
            
            if math.isclose(expected_int_x, ttd_int_x, rel_tol= 1e-2) and math.isclose(expected_int_y,ttd_int_y, rel_tol= 1e-2):
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR
        
    def mr_dupli_eq_x(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
            
        try:

            if math.isclose(td_int_x, ttd_int_x, rel_tol= 1e-2):
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR

    def mr_dupli_eq_y(td_int_x, td_int_y, ttd_int_x, ttd_int_y):
            
        try:
            
            if math.isclose(td_int_y, ttd_int_y, rel_tol= 1e-2):
                MR = 'no-violated'
            else:
                MR = 'violated'
            
            return MR
        
        except:
            MR = 'error'
            
            return MR