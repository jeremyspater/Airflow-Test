#v2 uses new R scripts (implement seg simulation / classification)
import airflow
from airflow.models import DAG
from airflow.operators.bash import BashOperator
import os
# Get current directory
#cwd = os.getcwd()
#cwd = cwd + '/airflow_home/scripts/'
#cwd = cwd + 'scripts/'
#cwd = '/Users/jeremyspater/Dropbox/duke/methods/airflow_seg/scripts/'
cwd = '/Users/jeremyspater/Dropbox/duke/methods/python for finance/github repository/airflow_updating_test/Airflow-Test/airflow/scripts/'
# Define the default arguments
args = {
    'owner': 'your_name',
    'start_date': airflow.utils.dates.days_ago(2),
}
# Instantiate the DAG passing the args as default_args
dag = DAG(
    dag_id='test_dag',
    default_args=args,
    schedule_interval=None
)
# Define the task:
A = BashOperator(
    task_id='add_data',
    bash_command=f'{cwd}run_r.sh {cwd}generate_data.R ',
    dag=dag,
    )
# A = BashOperator(
#     task_id='A_sim_neighs',
#     bash_command=f'{cwd}run_r.sh {cwd}23okt23_seg_sim.R ',
#     dag=dag,
#     )
# B = BashOperator(
#     task_id='B_KNN',
#     bash_command=f'{cwd}run_r.sh {cwd}24okt23_knn_calc.R ',
#     dag=dag,
#     )
# C = BashOperator(
#     task_id='C_moments',
#     bash_command=f'{cwd}run_r.sh {cwd}25okt23_moments.R ',
#     dag=dag,
#     )
# Plot = BashOperator(
#     task_id='Plot',
#     bash_command=f'{cwd}run_r.sh {cwd}26okt23_plot-neigh.R ',
#     dag=dag,
#     )
# D = BashOperator(
#     task_id='D_classn',
#     bash_command=f'{cwd}run_r.sh {cwd}25okt23_classn.R ',
#     dag=dag,
#     )
#command_line = 'Rscript -e "rmarkdown::render('+ "'" + f'{cwd}D_task.Rmd' + "')" + '"'
#D = BashOperator(
#    task_id='D_html_report',
#    bash_command=f'{command_line} ',
#    dag=dag,
#    )
# Define the task dependencies
#A >> B
A #>> [B, Plot]
#B >> C
#C >> D
#[B, C] >> D
