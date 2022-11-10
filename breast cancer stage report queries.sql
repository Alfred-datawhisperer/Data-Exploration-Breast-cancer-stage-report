select * from breast_cancer;

select count(*) from breast_cancer;

 select differentiate, survival_months from breast_cancer
 group by differentiate 
 order by survival_months desc;
 
 select differentiate, concat('had',' ' ,sum(survival_months), ' ','survival months in total') as survival_rate from breast_cancer
 group by differentiate
 order by survival_rate ;
 

select 
(avg(tumor_size * survival_months) - avg(tumor_size) * avg(survival_months)) /
(sqrt(avg(tumor_size * tumor_size)- avg(tumor_size) * avg(tumor_size)) * sqrt(avg(survival_months * survival_months)- avg(survival_months) * avg(survival_months))) AS CORRELATION
from breast_cancer;

select 
(count(*)*sum(tumor_size * survival_months) - sum(tumor_size) * sum(survival_months)) /
(sqrt(count(*)*sum(tumor_size * tumor_size)- sum(tumor_size) * sum(tumor_size)) 
* sqrt(count(*)*sum(survival_months * survival_months)- sum(survival_months) * sum(survival_months))) AS 'Correlation between tumor size and survival months'
from breast_cancer;

select 
(count(*)*sum(Status * survival_months) - sum(status) * sum(survival_months)) /
(sqrt(count(*)*sum(status * status)- sum(status) * sum(status)) 
* sqrt(count(*)*sum(survival_months * survival_months)- sum(survival_months) * sum(survival_months))) AS 'Correlation between tumor size and survival months'

select 
 6th_stage,survival_months from breast_cancer
 group by 6th_stage
 order by survival_months desc;
 
 select 
 T_Stage
 ,survival_months from breast_cancer
 group by T_Stage
 order by survival_months desc;
 
 select 
   N_stage,survival_months from breast_cancer
 group by   N_stage
 order by survival_months desc;

select N_stage , status,Survival_Months , count(*) as mortality_num  from breast_cancer 
where status='dead'
group by N_stage,status
order by MORTALITY_NUM DESC;

select T_stage , status ,Survival_Months, count(*) as mortality_num  from breast_cancer 
where status='dead'
group by T_stage,status
order by MORTALITY_NUM DESC;
 
 select 6TH_stage , status ,Survival_Months, count(*) as mortality_num  from breast_cancer 
where status='dead'
group by 6TH_stage,status
order by MORTALITY_NUM DESC;

select a_stage , status ,Survival_Months, count(*) as mortality_num  from breast_cancer 
where status='dead'
group by  a_stage,status
order by MORTALITY_NUM DESC;

 select T_stage ,N_Stage, 6th_Stage, status ,A_Stage,Survival_Months,count(*) as mortality_num  from breast_cancer 
where status='dead'
group by T_stage,N_Stage,6th_Stage, status,a_stage
order by MORTALITY_NUM DESC
limit 10;

select  marital_status,sum(Survival_Months) as sum_of_survival_months from breast_cancer
group by Marital_Status
order by sum_of_survival_months desc;

 
 
 