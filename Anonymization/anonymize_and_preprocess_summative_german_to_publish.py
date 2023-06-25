# -*- coding: utf-8 -*-
"""
Anonymize the first part of the summative assessment data of the German translation
of the ASA questionnaire.

Note that this is only the first part of the data we will collect, as we
aim for 120 responses per questionnaire part.

We collected data from people who have German as their first language and from
people who do not. All people have German as their primary language according
to their Prolific profiles though.

Date: 2023-06-22
Author: Nele Albers
"""

import copy
import pandas as pd
import pyreadstat  # for writing .sav-files


def anonymize(df_q, df_p, id_extension):
    """
    Anonymize the Qualtrics and Prolific data.
    Creates a new random ID called "rand_id".

    Parameters
    ----------
    df_q : dataframe
        Qualtrics data.
    df_p : dataframe
        Prolific data.
    id_extension : string
        Extension to add to new random IDs.

    Returns
    -------
    df_q : dataframe
        Anonymized Qualtrics data.
    df_p : dataframe
        Anonymized Prolific data.

    """

    # Only use Qualtrics data of people who passed in Prolific
    df_q = df_q[df_q["PROLIFIC_PID"].isin(df_p["Participant id"].to_list())]
    df_q = df_q.reset_index(drop=True)

    # Remove columns from Qualtrics data that we cannot publish or do not need
    df_q = df_q.drop(["StartDate", "EndDate", "Status", "Progress", 
                      "Duration (in seconds)", "RecordedDate", "ResponseId", 
                      "DistributionChannel", "UserLanguage",
                      "PIV_E_G_Fluency", "SESSION_ID",
                      "STUDY_ID", "Consent2", "PROL_ID_C",
                      "TIME_VID_INTRO_First Click", "TIME_VID_INTRO_Last Click",
                      "TIME_VID_INTRO_Page Submit", "TIME_VID_INTRO_Click Count",
                      "randomflag"], 
                     axis = 1)

    # Ceate random ID
    prolific_ids_sorted = sorted(df_q["PROLIFIC_PID"].to_list())
    df_q["rand_id"] = ["P" + str(prolific_ids_sorted.index(df_q.iloc[i]["PROLIFIC_PID"]) + 1) + id_extension for i in range(len(df_q))]
    df_p["rand_id"] = ["P" + str(prolific_ids_sorted.index(df_p.iloc[i]["Participant id"]) + 1) + id_extension for i in range(len(df_p))]

    # Drop original ID columns
    df_q = df_q.drop(["PROLIFIC_PID"], axis = 1)
    df_p = df_p.drop(["Participant id"], axis = 1)

    return df_q, df_p


if __name__ == "__main__":

    extension = "v1_2023_06_22"

    #### Second half of the questionnaire

    # Load the data files we need
    df_q_2 = pd.read_csv("U:/asaquestionnairegermandutch/Qualtrics_Exports/Summative/Final_ASA_German_Summative_Second_Half_v1_2023_06_22.csv")
    df_p_m_german = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_second_half_male_first-language-german_v0_2023_06_20.xlsx")
    df_p_m_notgerman = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_second_half_male_first-language-not-german_v1_2023_06_22.xlsx")
    df_p_f_german = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_second_half_female_non_binary_first-language-german_v1_2023_06_22.xlsx")
    df_p_f_notgerman = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_second_half_female_non_binary_first-language-not-german_v1_2023_06_22.xlsx")

    # Add first language column
    df_p_m_german["First_Language_German"] = [1 for i in range(len(df_p_m_german))]
    df_p_f_german["First_Language_German"] = [1 for i in range(len(df_p_f_german))]
    df_p_m_notgerman["First_Language_German"] = [0 for i in range(len(df_p_m_notgerman))]
    df_p_f_notgerman["First_Language_German"] = [0 for i in range(len(df_p_f_notgerman))]

    # Merge Prolific data
    df_p_2 = pd.concat([df_p_m_german, df_p_f_german, df_p_m_notgerman,
                      df_p_f_notgerman])

    # One participant messaged us that they meant to respond with "yes" to the 
    # recommended data question instead of "no". So want to change this.
    # Since data is numeric, "1" means "no" and "2" means "yes"
    # We replaced the PROLIFIC_PID by "xxxxx" in this code for publication, 
    # since we need to anonymize everything.
    df_q_2.iloc[df_q_2.index[df_q_2['PROLIFIC_PID'] == "xxxxx"].tolist()[0], 
                df_q_2.columns.get_loc("Use_Data")] = "2"

    # Anonymize
    # We need the not-anonymized Qualtrics data still for processing the first half 
    # data, so making a copy before anonymizing.
    df_q_2_anonym = copy.deepcopy(df_q_2)
    df_q_2_anonym, df_p_2 = anonymize(df_q_2_anonym, df_p_2, "_S_SH")

    # Save anonymized dataframes
    df_p_2.to_csv("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_second_half_" + extension + "_anonym.csv",
                  index=False)
    pyreadstat.write_sav(df_q_2_anonym, 
                         "U:/asaquestionnairegermandutch/Qualtrics_Exports/Summative/Final_ASA_German_Summative_Second_Half_" + extension + "_anonym.sav")


    #### First half of the questionnaire

    # Load the data files we need
    df_q_1 = pd.read_csv("U:/asaquestionnairegermandutch/Qualtrics_Exports/Summative/Final_ASA_German_Summative_First_Half_v1_2023_06_22.csv")
    df_p_m_german_1 = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_first_half_male_first-language-german_1_v1_2023_06_22.xlsx")
    df_p_m_german_2 = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_first_half_male_first-language-german_2_v1_2023_06_22.xlsx")
    df_p_m_notgerman = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_first_half_male_first-language-not-german_v1_2023_06_22.xlsx")
    df_p_f_notgerman = pd.read_excel("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_first_half_female_nonbinary_first-language-not-german_v1_2023_06_22.xlsx")

    # Add first language column
    df_p_m_german_1["First_Language_German"] = [1 for i in range(len(df_p_m_german_1))]
    df_p_m_german_2["First_Language_German"] = [1 for i in range(len(df_p_m_german_2))]
    df_p_m_notgerman["First_Language_German"] = [0 for i in range(len(df_p_m_notgerman))]
    df_p_f_notgerman["First_Language_German"] = [0 for i in range(len(df_p_f_notgerman))]

    # Merge Prolific data
    df_p_1 = pd.concat([df_p_m_german_1, df_p_m_german_2, df_p_m_notgerman,
                      df_p_f_notgerman])

    # Some people accidentally did the first half also after already having taken
    # the second half. So remove these people from the first half data.
    df_p_1 = df_p_1[~df_p_1["Participant id"].isin(df_q_2["PROL_ID_C"].to_list())]

    # Anonymize
    df_q_1, df_p_1 = anonymize(df_q_1, df_p_1, "_S_FH")

    # Save anonymized dataframes
    df_p_1.to_csv("U:/asaquestionnairegermandutch/Prolific_Exports/Summative/prolific_export_final_eval_german_first_half_" + extension + "_anonym.csv",
                  index=False)
    pyreadstat.write_sav(df_q_1, 
                         "U:/asaquestionnairegermandutch/Qualtrics_Exports/Summative/Final_ASA_German_Summative_First_Half_" + extension + "_anonym.sav")
