import pandas as pd

def load_data():
    df_system_access = pd.read_csv('../data/system_access.csv')
    df_employees = pd.read_csv('../data/employees.csv')
    return df_system_access, df_employees

def combine_data(df_system_access, df_employees):
    df_employees.rename(columns={'employee_number':'id'}, inplace = True)
    df_employees.set_index('id', inplace =True)
    df_system_access.set_index('id', inplace =True)
    df = df_system_access.join(df_employees, how='outer')  
    return df
