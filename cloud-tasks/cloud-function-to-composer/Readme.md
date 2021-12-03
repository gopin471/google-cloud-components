This folder contains the code/configs that are to demonstrate how you can use the cloud task to control the rate and retry between cloud functions and composer's airflow.

**Problem statement:**
    <br>Assume that you have a workflow written as Airflow DAG and trigger it based on cloud storage file arrival event. We will be using cloud functions to call the airflow dag manually. In case of receiving more files at a same time within milli seconds intervals, airflow api server may not respond for all the api calls. Hence there are chances to miss the trigger.

**Proposed solution:**
<br> To solve the above issue we can introduce cloud tasks componet for limiting the rate and automatic retrying.