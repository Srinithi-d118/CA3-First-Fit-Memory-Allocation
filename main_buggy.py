def first_fit_buggy(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] < processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    print("\n--- Buggy First Fit Memory Allocation ---")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"Process {i + 1} ({processes[i]} KB) allocated to Block {allocation[i] + 1}")
        else:
            print(f"Process {i + 1} ({processes[i]} KB) Not Allocated")

    print("\nRemaining Block Sizes:", blocks)


blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

first_fit_buggy(blocks.copy(), processes)