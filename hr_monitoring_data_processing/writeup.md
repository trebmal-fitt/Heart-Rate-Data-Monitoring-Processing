## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

There could be a sensor failure or malfunction, some kind of data transmission error or interruption, or some kind of user/human or environmental error that caused the missing value(s). Additionally, there could be some kind of data entry error that resulted in the missing value(s).

The risk of filtering the values out is that doing so could lead to skewed analysis due to the missing data, less representation of the data, and loss of context that could provide more insight into the data. This would affect information such as data trends and could lead to informational bias. Additionally, filtering the values out could lead to missed opportunities for improvement as by filtering out the data, one cannot identify an opportunity to improve things such as device reliability and design, data transmission, and user compliance where the device could be improved in some way, or the data transmission method could be improved, or the user could be instructed on how to use the device better and more reliably.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

Sleep occurs in phase 0. Analyzing the visualization and descriptive statistics that I've calculated, the maximum heart rate during phase 0 is lower than the maximum heart rate of the other phases. The graph illustrates that the maximum heart rate is lower in phase 0 than in the other phases, and the calculations indicate this as well. The maximum heart rate is lowest at 93.0 during phase 0, compared to 99.0 for phase 3, 110.0 for phase 1, and 117.0 for phase 2. 

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

Exercise occurs during phase 2, because the maximum heart rate is highest compared to the maximum heart rate of all other phases.

The maximum heart rate during phase 2 is 117.0, which is highest in comparison to the maximum heart rates of phase 0 at 93.0, phase 1 at 110.0, and phase 3 at 99.0. It is possible that exercise occurs in Phase 1 as well, since the maximum heart rate is 110.0 and it is higher than phases 0 and 3, though not as high as, but fairly close to, the maximum heart rate during phase 2.

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

The average heart rate at phase 3 is relatively lower than the average heart rate of the other phases at 60.65, but the standard deviation is higher at 11. The standard deviation for phase 2 is 13.38 which is slightly higher than the standard deviation of phase 3, but the average heart rate during phase 2 is 85.18 which is one of the higher average heart rates of the phases, which the average heart rate during phase 3 is relatively lower than all of the other phases. This trend indicates that awake activity is likely occuring during phase 3.
