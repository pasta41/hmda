import pandas as pd

def clean_split(path, output_path):
    _, name = path.split("/")
    df = pd.read_csv(path)

    
    # delete columns with alpha data
    del df['respondent_id'] # save elsewhere 
    del df['agency_name']
    del df['agency_abbr']
    del df['loan_type_name']
    del df['property_type_name']
    del df['loan_purpose_name']
    del df['owner_occupancy_name']
    del df['preapproval_name']
    del df['action_taken_name']
    del df['msamd_name']
    del df['state_name']
    del df['county_name']
    del df['applicant_ethnicity_name']
    del df['co_applicant_ethnicity_name']
    del df['applicant_race_name_1']
    del df['applicant_race_name_2']
    del df['applicant_race_name_3']
    del df['applicant_race_name_4']
    del df['applicant_race_name_5']
    del df['co_applicant_race_name_1']
    del df['co_applicant_race_name_2']
    del df['co_applicant_race_name_3']
    del df['co_applicant_race_name_4']
    del df['co_applicant_race_name_5']
    del df['applicant_sex_name']
    del df['co_applicant_sex_name']
    del df['purchaser_type_name']
    del df['denial_reason_name_1']
    del df['denial_reason_name_2']
    del df['denial_reason_name_3']
    del df['hoepa_status_name']
    del df['lien_status_name']
    del df['edit_status_name']
    del df['application_date_indicator'] # a 2004 date indicator
    
    # delete proxies
    del df['lien_status'] # also a proxy
    del df['hoepa_status'] # only for originated loans, so proxy
    
    # some missing state info; delete those since we need that to subdivide
    # some missing state info; remove those rows
    df = df.dropna(subset=['state_abbr', 'state_code'])
    df.to_csv("{op}{n}_clean.csv".format(op=output_path, n=name))


def filter_ny(path, output_path):
    _, name_plus = path.split("/")
    name, _ = name_plus.split(".")

    df = pd.read_csv(path)
    df_ny = df[df['state_abbr'] == 'NY']
    df_ny.to_csv("{op}{n}_ny.csv".format(op=output_path, n=name))


def split_out_target_and_protected(path, output_root):
    df = pd.read_csv(path)

    target_df = df[['action_taken',
                    'denial_reason_1', 
                    'denial_reason_2', 
                    'denial_reason_3']]

    del df['denial_reason_1']
    del df['denial_reason_2']
    del df['denial_reason_3']
    del df['action_taken']

    g_df = df[['applicant_ethnicity',
               'applicant_race_1',
               'applicant_race_2',
               'applicant_race_3',
               'applicant_race_4',
               'applicant_race_5',
               'applicant_sex',
               'co_applicant_ethnicity',
               'co_applicant_race_1', 
               'co_applicant_race_2', 
               'co_applicant_race_3', 
               'co_applicant_race_4', 
               'co_applicant_race_5',
               'co_applicant_sex']]

    del df['applicant_ethnicity']
    del df['applicant_race_1']
    del df['applicant_race_2']
    del df['applicant_race_3']
    del df['applicant_race_4']
    del df['applicant_race_5']
    del df['co_applicant_ethnicity']
    del df['co_applicant_race_1']
    del df['co_applicant_race_2']
    del df['co_applicant_race_3']
    del df['co_applicant_race_4']
    del df['co_applicant_race_5']
    del df['applicant_sex']
    del df['co_applicant_sex']

    df.to_csv("{o}_features_ny.csv")
    target_df.to_csv("{o}_target_ny.csv")
    g_df.to_csv("{o}_protected.csv")