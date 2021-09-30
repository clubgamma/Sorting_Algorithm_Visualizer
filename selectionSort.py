import time

def selection_sort(A, drawData, timeTick):
  for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]
    drawData(A, ['green' if x == j or x == j+1 else 'red' for x in range(len(A))] )
    time.sleep(timeTick)
  drawData(A, ['green' for x in range(len(A))])