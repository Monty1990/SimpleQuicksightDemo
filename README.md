# QuickSight
This is a demo with Quicksight ML insight

# Kaggle data
The data in this demo is from kaggle.
https://www.kaggle.com/

# Required data type
Date or Timestamp is necessary data type to process ML insight.

# Instructions
1. Using the aws account, create QuickSight Enterprise account
<img width="600" alt="quicksight-register" src="https://user-images.githubusercontent.com/48192505/68187836-ad7f3e80-ffe2-11e9-92cb-a056d2761325.PNG">

2. Create a data set. You can use different data sources like direct upload, S3, Athena... For this demo, i use direct upload
<img width="600" alt="create-data-set" src="https://user-images.githubusercontent.com/48192505/69515213-d020c980-0f88-11ea-91fe-59722a97d528.PNG">

3. Edit settings and prepare data
<img width="450" alt="edit-settings-and-prepare-data" src="https://user-images.githubusercontent.com/48192505/69515392-72d94800-0f89-11ea-850d-04281d084d31.PNG">

4. If you do not need filter, save and visualize
<img width="600" alt="visualize" src="https://user-images.githubusercontent.com/48192505/69515543-dc595680-0f89-11ea-87fe-511b544b06af.PNG">

5. Click add and select add insight, use AutoGraph or Line chart, choose Date for X axis and Total(Sum) for Value

- **Date or Timestamp is necessary data type to process ML insight.**
<img width="600" alt="insight" src="https://user-images.githubusercontent.com/48192505/69517580-23e2e100-0f90-11ea-95c7-6c77d591cabf.PNG">

- **It is also can show forecast by text.**
<img width="600" alt="text_forecasting" src="https://user-images.githubusercontent.com/48192505/69522270-f00db880-0f9b-11ea-982e-605ca9c7d97e.PNG">

6. Click the top right button of insight, select add forecast
<img width="600" alt="add_forecast" src="https://user-images.githubusercontent.com/48192505/69519392-e46ac380-0f94-11ea-807b-c84ca27a2347.PNG">

7. Enter the periods forward, set the percentage of prediction interval and apply
<img width="600" alt="forecast" src="https://user-images.githubusercontent.com/48192505/69519431-f9475700-0f94-11ea-8228-420529c5c65c.PNG">

8. Click add insight and select anomaly detection
<img width="600" alt="add_anomaly_detection" src="https://user-images.githubusercontent.com/48192505/69519693-a15d2000-0f95-11ea-8d58-e5fe759a83fc.PNG">

9. Choose the field of time, value and categories and click get started
<img width="600" alt="add_value_anomaly_detection" src="https://user-images.githubusercontent.com/48192505/69520295-39a7d480-0f97-11ea-9dff-6c7fac214f6b.PNG">

10. Tick Analyze all combinations of these categories, set the Schedule and save
    - **Amazon QuickSight runs anomaly detection on the following combinations hierarchically: A, AB, ABC. If you choose this option, Amazon QuickSight analyzes all combinations: A, AB, ABC, BC, AC.If your data isn't hierarchical, make sure to enable this option.**
<img width="600" alt="set_anomaly_detection" src="https://user-images.githubusercontent.com/48192505/69520507-dd918000-0f97-11ea-80c1-492e09968586.PNG">

11. Click run nows and wait for few minutes, 
