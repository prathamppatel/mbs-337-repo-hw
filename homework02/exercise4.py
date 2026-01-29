expression_data = {'Gene1': {'control': [10.5, 11.2, 10.8], 'treatment': [25.3, 24.7, 26.1]}, 
                   'Gene2': {'control': [8.2, 8.5, 8.0], 'treatment': [12.1, 11.8, 12.5]}, 
                   'Gene3': {'control': [15.0, 14.8, 15.2], 'treatment': [18.5, 18.2, 18.8]}}

print(expression_data)

for gene in expression_data: 
    print(gene)
    control_val = expression_data[gene]['control']
    mean_control = sum(control_val)/3
    print(f'control mean = {mean_control}')
    treatment_val = expression_data[gene]['treatment']
    mean_treat = sum(treatment_val)/3
    print(f'treatment mean = {mean_treat}')
    fold_change = mean_treat/mean_control
    print(f'fold change = {fold_change}')
    if fold_change > 2.0 or fold_change < .5:
        print(f'{gene} shows significant changes!')

