#!/usr/bin/env python
# coding: utf-8

# # <span style="color:blue"> Breast cancer stage report exploration</span>.

# ### Data Analyst: Omosona Alfred
# 
# ### Data Source: kaggle
# ### License: the license permits me to modify and share findings from this dataset

# Tableau.Dashboard: https://public.tableau.com/views/DataExplorationBreastCancerstagereport/Dashboard2?:language=en-US&publish=yes&:display_count=n&:origin=viz_share_link
# 
# Exploration questions;
# 
# These are the questions I answered with the dataset
# 
# 1. Exploration of Differentiation and survival month
# 2. Correlation of Tumor size, survival month and status
# 3. which of the stages has higher survival rate
# 4. which combination of the different classification has higher no of dead persons and lowest number of surviving months

# ### Brief explanation of terms
# 
# In the TNM system
# 
# ##### The T 
# refers to the size and extent of the main tumor. The main tumor is usually called the primary tumor.
# 
# ##### The N 
# refers to the number of nearby lymph nodes that have cancer.
# 
# ##### The M 
# refers to whether the cancer has metastasized. This means that the cancer has spread from the primary tumor to other parts of the body.
# 
# ##### T1, T2, T3, T4: 
# Refers to the size and/or extent of the main tumor. The higher the number after the T, the larger the tumor or the more it has grown into nearby tissues.
# 
# ##### N1, N2, N3:
# Refers to the number and location of lymph nodes that contain cancer. The higher the number after the N, the more lymph nodes that contain cancer.
# 
# ##### A stage
# In situ—Abnormal cells are present but have not spread to nearby tissue.
# 
# Localized—Cancer is limited to the place where it started, with no sign that it has spread.
# 
# Regional—Cancer has spread to nearby lymph nodes, tissues, or organs.
# 
# Distant—Cancer has spread to distant parts of the body.
# 
# 
# 
# #### 6th stage
# 
# ##### Stage 0: 
# Stage zero (0) describes disease that is only in the ducts of the breast tissue and has not spread to the surrounding tissue of the breast. It is also called non-invasive or in situ cancer
# 
# ##### Stage IA: 
# The tumor is small, invasive, and has not spread to the lymph nodes
# 
# ##### Stage IB: 
# Cancer has spread to the lymph nodes and the cancer in the lymph node is larger than 0.2 mm but less than 2 mm in size. There is either no evidence of a tumor in the breast or the tumor in the breast is 20 mm or smaller
# 
# ##### Stage IIA: 
# Any 1 of these conditions:
# There is no evidence of a tumor in the breast, but the cancer has spread to 1 to 3 axillary lymph nodes. It has not spread to distant parts of the body
# The tumor is 20 mm or smaller and has spread to 1 to 3 axillary lymph nodes 
# The tumor is larger than 20 mm but not larger than 50 mm and has not spread to the axillary lymph nodes 
# 
# ##### Stage IIB: 
# Either of these conditions:
# The tumor is larger than 20 mm but not larger than 50 mm and has spread to 1 to 3 axillary lymph nodes 
# The tumor is larger than 50 mm but has not spread to the axillary lymph nodes (T3, N0, M0).
# 
# ##### Stage IIIA: 
# The tumor of any size has spread to 4 to 9 axillary lymph nodes or to internal mammary lymph nodes. It has not spread to other parts of the body. Stage IIIA may also be a tumor larger than 50 mm that has spread to 1 to 3 axillary lymph nodes.
# 
# ##### Stage IIIB: 
# The tumor has spread to the chest wall or caused swelling or ulceration of the breast, or it is diagnosed as inflammatory breast cancer. It may or may not have spread to up to 9 axillary or internal mammary lymph nodes. It has not spread to other parts of the body.
# 
# ##### Stage IIIC:
# A tumor of any size that has spread to 10 or more axillary lymph nodes, the internal mammary lymph nodes, and/or the lymph nodes under the collarbone. It has not spread to other parts of the body.
# 
# ##### Stage IV (metastatic): 
# The tumor can be any size and has spread to other organs, such as the bones, lungs, brain, liver, distant lymph nodes, or chest wall (any T, any N, M1). Metastatic cancer found when the cancer is first diagnosed occurs about 6% of the time.

# In[1]:


import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt


# In[2]:


get_ipython().system('pip install matplotlib')


# In[3]:


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


# In[4]:


cursor.execute("SELECT tumor_size, survival_months FROM bcs_report")
data = cursor.fetchall()


# In[5]:


tumor_size = [d[0] for d in data]
survival_months = [d[1] for d in data]


# In[26]:





# In[6]:


conn = sqlite3.connect('mydatabase.db')


# In[7]:


get_ipython().system('pip install ipython-sql')


# In[8]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[9]:


get_ipython().run_line_magic('sql', 'sqlite:///mydatabase.db')


# In[12]:


df = pd.read_csv('C:/Users/FUTECH COMPUTER/Desktop/bcs_report.csv')


# In[13]:


df.to_sql('bcs_report',con=conn, if_exists='append',index=False)


# _Take a look at the dataset

# In[46]:


get_ipython().run_line_magic('sql', 'select * from bcs_report;')


# In[8]:


get_ipython().run_line_magic('sql', 'select count(*) from bcs_report;')


# _firstly we will look at the relationship between differentiation and survival month

# In[19]:


get_ipython().run_cell_magic('sql', '', 'select differentiate, survival_months from bcs_report\n group by differentiate \n order by survival_months desc;')


# Which of the differentiation has the most survival month

# In[16]:


get_ipython().run_cell_magic('sql', '  ', "SELECT differentiate,\n'had ' || SUM(survival_months) || ' survival months in total' as survival_rate\nFROM bcs_report \nGROUP BY differentiate \nORDER BY SUM(survival_months)desc;")


# In[ ]:





# In[28]:


plt.scatter(tumor_size, survival_months)
plt.xlabel('Tumor size')
plt.ylabel('Survival months')
plt.title('Tumor size vs Survival months')


# In[28]:


get_ipython().run_cell_magic('sql', '', 'select [6th_stage], survival_months from bcs_report\ngroup by [6th_stage]\norder by survival_months desc;')


# In[80]:


get_ipython().run_cell_magic('sql', '', ' select \n TRIM("T_Stage")\n ,survival_months from bcs_report\n group by TRIM("T_Stage")\n order by survival_months desc;')


# In[75]:


get_ipython().run_cell_magic('sql', '', 'ALTER TABLE bcs_report RENAME COLUMN T_Stage TO Tstage;')


# In[55]:


get_ipython().run_cell_magic('sql', 'select ', ' N_Stage\n ,survival_months, STATUS from bcs_report\ngroup by N_stage\norder  by survival_months desc;')


# In[35]:


get_ipython().run_cell_magic('sql', '', 'select \n   N_stage,survival_months from bcs_report\n group by   N_stage\n order by survival_months desc;')


# In[64]:


get_ipython().run_cell_magic('sql', '', 'select\nN_stage , status,Survival_Months, count(*) as mortality_num from bcs_report \n\ngroup by N_stage,status\n\norder by mortality_num DESC;')


# In[92]:


get_ipython().run_cell_magic('sql', '', "select 'T_stage' , status ,Survival_Months, count(*) as mortality_num  from bcs_report \n\ngroup by 'T_stage',status\norder by MORTALITY_NUM DESC;")


# In[83]:


get_ipython().run_cell_magic('sql', '', 'select [6TH_stage] , status ,Survival_Months, count(*) as mortality_num  from bcs_report \n\ngroup by [6TH_stage],status\norder by MORTALITY_NUM DESC;')


# In[71]:


get_ipython().run_cell_magic('sql', '', 'select a_stage , status ,Survival_Months, count(*) as mortality_num  from bcs_report\ngroup by  a_stage,status\norder by MORTALITY_NUM DESC;')


# In[90]:


get_ipython().run_cell_magic('sql', '', "select 'T_stage' ,N_Stage, [6th_Stage], status ,A_Stage,Survival_Months,count(*) as mortality_num  from bcs_report \ngroup by 'T_stage',N_Stage,[6th_Stage], status,a_stage\norder by MORTALITY_NUM DESC\nlimit 10;")


# In[73]:


get_ipython().run_cell_magic('sql', '', 'select  Marital_status,sum(Survival_Months) as sum_of_survival_months from bcs_report\ngroup by Marital_Status\norder by sum_of_survival_months desc;')


# In[18]:


get_ipython().run_line_magic('sql', 'drop table bcs_report')


# # Observation
# 
# •	At first glance it's obvious the 6th stage progression correlates with survival month.
# 
# •	The survival of people with breast cancer is highly dependent on the tumor size, the number and location of the             Cancerous lymph node, how metastasized the tumor is.
# 
# •	There is no correlation between tumor size and survival month.
# 
# •	The advanced the stage the less likely the survival. This agrees very well with early detection thereby saving lives       from cancer death.
# 
# •	Race is a factor to be considered because the data records shows a high amount of white folk with breast cancer             compared to other races (others and black) i.e the whites are more prone to breast cancer.
# 
# •	We may not readily conclude if marital status is truly as impacting on survival. Which of the marital status has higher     percentage of survivors per total patients in each class and if the percentage difference is definitive enough to prove     the need for a family function around the patient to improve quality of life, it seems so, although there is need for       further studies to be caried out in this regard.
# 

# In[ ]:




