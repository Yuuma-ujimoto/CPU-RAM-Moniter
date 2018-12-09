import psutil
import matplotlib.pyplot as pl

mem = psutil.virtual_memory().percent
print("memory use",mem)


cpu = psutil.cpu_percent(interval=1)
print("CPU use",cpu)



data = [cpu,mem]
data2= [100-cpu,100-mem]


name =["CPU Use"+str(cpu),"RAM Use"+str(mem)+"%"]

pl.title("CPU & RAM use graph")

pl.tick_params(labelsize=14)
pl.bar(name,data,color="red",width=0.4)
pl.bar(name,data2,bottom=data,color="black",width=0.4)

pl.show()