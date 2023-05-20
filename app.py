import psutil
from flask import Flask, render_template

app = Flask(__name__) # [Note 1]

@app.route('/') # root addres '/'
def index():
    cpu_utlize = psutil.cpu_percent() # returns the current state of cpu 
    mem_utlize = psutil.virtual_memory().percent # returns the current state of virtual memory
    message = None
    if cpu_utlize > 90 or mem_utlize > 90 :
        message = "Your system resultsare at risk ; please optemiz it before it crashes"
    if cpu_utlize > 75 or mem_utlize > 75 :
        message = "High CPU or Memory utilization detected. please modify your settings"
    return render_template("index.html", cpu_data=cpu_utlize, mem_data=mem_utlize, message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# --------------------------------
#[Note 1]: __name__ is a built-in Python variable that represents the name of the current module or file
# When a Python file is executed directly, __name__ is set to '__main__'. When the file is imported as a module, __name__ is set to the module's name.

# 