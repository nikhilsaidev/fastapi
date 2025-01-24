from multiprocessing import Process
import listener1
import listener2
import listener3
import listener4

if _name_ == "_main_":
    
    processes = [
        Process(target=listener1.run),
        Process(target=listener2.run),
        Process(target=listener3.run),
        Process(target=listener4.run),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
        

        
#DOCKER FILE

# FROM python:3.9-slim
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# CMD ["python", "master_script.py"]