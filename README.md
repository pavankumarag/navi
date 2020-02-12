# navi
Navi technologies coding problem

Demo at - https://drive.google.com/open?id=1FCPxOLBub6yy-K_ov37ORoJ3viUq8Y8z

There are two ways of deploying/run this work.

**1. As a stanalone application**

  a. Install xvfb
  
      mac - >https://www.xquartz.org/
      ubuntu -> sudo apt-get install xvfb xserver-xephyr vnc4server
      
  b. git clone the repo ( Note: add your vm ssh keys to your git account )
      git clone git@github.com:pavankumarag/navi.git
      
  c. Install requirements.txt
  
      ```cd Navi/Automation
      virtualenv navi
      source navi/bin/activate
      pip install -r requirements.txt```
      
   d. Install latest chrome driver 
      https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.16/
      
   e. Run the test using python's open source test runner(pytest)
   
      ```cd Navi/Automation
      pytest -sv --html=test_result.html tests/ui/test_director_films_diff_source.py```
      
   f. Observe the outputs generated -> report.json and test_result.html
   
**2. As a docker on any OS**

  a. Pull customised docker image(this comes with all environment details)
    docker pull pavankumarag/pytest-framework-internal:v1.0
    
  b.Clone the navi automation repo
    git clone git@github.com:pavankumarag/navi.git
    
  c.Create a docker container 
  
    docker run -tid -v /home/pavan.govindraj/navi:/navi --name navi pavankumarag/pytest-framework-internal:v1.0
    
  d.Execute testcase using the following steps
  
    ```docker exec -ti navi bash
    source pytest-env/bin/activate
    cd /navi/automation
    pytest -sv tests/ui/test_director_films_diff_source.py```
  
