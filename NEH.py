import numpy as np # type: ignore

# Global variable for machines
machines = [
    [6, 8, 3],  # Job 1
    [5, 1, 3],  # Job 2
    [2, 4, 9]   # Job 3
]

# Function to calculate the Makespan
def fitnessFlowShop(sequence):
    numJobs = len(sequence)
    numMachines = len(machines[0])
    completionTime = np.zeros((numJobs, numMachines), dtype=int)
    makespan = 0

    for i, job in enumerate(sequence):
        job_index = job - 1  
        for m in range(numMachines):
            prevMachineTime = completionTime[i][m-1] if m > 0 else 0
            prevJobTime = completionTime[i-1][m] if i > 0 else 0
            completionTime[i][m] = max(prevMachineTime, prevJobTime) + machines[job_index][m]

    makespan = completionTime[numJobs - 1][numMachines - 1]
    return makespan


sequence = [1, 3, 2]
makespan = fitnessFlowShop(sequence)
print(f"Makespan for the sequence {sequence}: {makespan}")