
def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break

    return allocation, blocks


# Test Case 1: Normal allocation
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

allocation, remaining = first_fit(blocks.copy(), processes)

print("Test Case 1:", allocation)
print("Remaining:", remaining)


# Test Case 2: No suitable memory block
blocks = [50, 100, 150]
processes = [200]

allocation, remaining = first_fit(blocks.copy(), processes)

print("\nTest Case 2:", allocation)
print("Remaining:", remaining)


# Test Case 3: Exact memory match
blocks = [100, 200]
processes = [200]

allocation, remaining = first_fit(blocks.copy(), processes)

print("\nTest Case 3:", allocation)
print("Remaining:", remaining)
