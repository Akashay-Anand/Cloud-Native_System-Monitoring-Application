import psutil
from flask import Flask

app = Flask(__name__) # [Note 1]

@app.route('/') # root addres '/'
def index():
    cpu_utlize = psutil.cpu_percent() # returns the current state of cpu 
    mem_utlize = psutil.virtual_memory().percent # returns the current state of virtual memory
    Message = None
    if cpu_percent > 90 or mem_percent > 90 :
        Message = "Your system resultsare at risk ; please optemiz it before it crashes"
    if cpu_percent > 75 or mem_percent > 75 :
        Message = "High CPU or Memory utilization detected. please modify your settings"
    return f"CPU Utilization: {cpu_percent} and Memory utilization: {mem_percent}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# --------------------------------
#[Note 1]: __name__ is a built-in Python variable that represents the name of the current module or file
# When a Python file is executed directly, __name__ is set to '__main__'. When the file is imported as a module, __name__ is set to the module's name.

# 