#QBB2022 - Day 5 - Lunch Exercises Submission
Exercise 1
2.
cut -d , -f 5,6 aau1043_dnm.csv | grep father | cut -d , -f 1 | sort | uniq -c >Father_mut.txt
cut -d , -f 5,6 aau1043_dnm.csv | grep mother | cut -d , -f 1 | sort | uniq -c >mother_mut.txt
join -1 2 -2 2 Father_mut.txt mother_mut.txt > par_of_org.txt
3.
tr ',' ' ' < aau1043_parental_age.csv > aau1043_parental_age.txt
sort aau1043_parental_age.txt > par_age_sort.txt
join par_of_org.txt par_age_sort.txt > data.txt

Exercise 2
Mother Model
Significant: yes
Size of relationship: 0.6026
Father Model
Significant: yes
Size of relationship: 0.4571

There is a significant diference between the number of mutations from the mother and father.

For a father aged 50.5, you would expect 7.017 mutations.