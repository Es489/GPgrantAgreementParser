import pandas as pd

f1 = open("main_info.txt", "a")
f2 = open("support.txt", "a")

tilda1 = pd.read_csv("tilda1.csv")
tilda2 = pd.read_csv("tilda2.csv")

for index, row in tilda1.iterrows():
    company = row["Org_Name"]
    t2_row = tilda2.iloc[index]

    np = int(row["of_placements"])
    roles = row["Job_Titiles_Start_Dates"]
    npeople = t2_row["How_many_employed"]
    website = row["Website"]
    description = row["Business_description"]
    wfchanges = t2_row["Workforce_changes"]
    funding = t2_row["KS_funding_alternative"]
    trade_unions = t2_row["Trade_Unions"]
    number = index+1
    similar_roles = t2_row["Recruitment_changes_past_6_months"]
    support = row["Employability_Support"]
    template = f"""
    {number}) {company} - {np} positions;

    {roles}

    {company} has {npeople}, thus it is sufficient to manage {np} positions;

    Website: {website}

    Short description: {description} 

    The changes to the workforce in the last 6 months: {wfchanges}
    What funding source would be used if Kickstart Scheme was unavailable: It would not be possible to fund these  roles without Kickstart, unless {funding};
    What recruitment was completed/started/paused in the last 6 months; how similar are/were the vacancies to the job placements: {similar_roles};
    Have you engaged any relevant trade unions; if so, what advice they’ve given you: {trade_unions}.

    """
    f1.write(template)
    f2.write(f"{company}: {support}\nAdditional employability support will be provided by Over-Deliver Ltd, a career consultancy firm.\n\n\n")
f1.close()
f2.close()
