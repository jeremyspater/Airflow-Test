#Read existing data file; add an entry; save the file

#A = data.frame('Date' = Sys.time(), 'Value' = rnorm(1))
#write.csv(A, file = '/Users/jeremyspater/Dropbox/duke/methods/python for finance/github repository/airflow_updating_test/Airflow-Test/airflow_test_data.csv',
#  row.names=FALSE) #this prevents 'X' columns from getting added on the left

rm(list=ls())

A = read.csv(file = '/Users/jeremyspater/Dropbox/duke/methods/python for finance/github repository/airflow_updating_test/Airflow-Test/airflow_test_data.csv')

A[nrow(A)+1, 'Date'] = as.character(Sys.time())
A[nrow(A), 'Value'] = rnorm(1)

write.csv(A, file = '/Users/jeremyspater/Dropbox/duke/methods/python for finance/github repository/airflow_updating_test/Airflow-Test/airflow_test_data.csv',
            row.names=FALSE) #this prevents 'X' columns from getting added on the left
