import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

expend_dict = {
               'project_0': 1e3,
               'project_1': 1e4,
               'project_2': 1e5,
               'project_3': 1e6
}

def  expenditure_chart(expenditures_dict, nested_pie=True, *args, **kwargs):
    if nested_pie: fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    else: fig, ax = plt.subplots(subplot_kw=dict(polar=True))

    size = 0.3

    # Normalize all obligations to 2pi, then take fraction of expenditures/
    # obligations to get the portion of the circle they should fill
    norm_hr_expenditures = list()
    norm_actual_expenditures = list()
    for project_name in expenditures_dict.keys():
        project_dict = expenditures_dict[project_name]
        obligation = expenditures_dict[project_name]['obligation']
        for hr_expenditure in expenditure_dict[project_name]['hr_expenditure']:
            norm_hr = hr_expenditures/obligation * 2 * np.pi
            norm_hr_expenditures.append(norm_hr)
        for actual_expenditure in expenditures_dict[project_name]:
            norm_actual = actual_expenditure/obligation * 2 * np.pi
            norm_actual_expenditures.append(norm_actual)



    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(len(obligations))*4)
    inner_colors = cmap(np.array([1,2,5,6,9,10))

    i = 0
    for idx in len(expenditures_dict.keys()):
       ax.bar =
    for obligation in obligations:
        ax.bar(bottom=1-size, height=size,
               color=outer_colors[i], edgecolor='w',
               linewidth=1, align="edge")
        ax.text(ax.patches.get_x() + ax.patches.get_width() / 2,
                ax.patches.get_height() + 5, obligation[0], ha='center',
                va='bottom')
    for hr_expend in norm_hr_expenditures:
        ax.bar(bottom=1-2*size, height=size, color=)






    return