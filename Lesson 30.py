# -------------------------------------------------------------------

# import random
# import time
# import matplotlib.pyplot as plt
# from matplotlib import animation

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         yield arr, i, min_idx

# def visualize_sort(arr):
#     fig, ax = plt.subplots()
#     bar_rects = ax.bar(range(len(arr)), arr, align="edge")
#     ax.set_xlim(0, len(arr))
#     ax.set_ylim(0, int(max(arr) * 1.1))
#     text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

#     iteration = [0]

#     def update(data):
#         arr, i, min_idx = data
#         for rect, val in zip(bar_rects, arr):
#             rect.set_height(val)
#             rect.set_color('blue')
#         bar_rects[i].set_color('red')
#         bar_rects[min_idx].set_color('yellow')
#         iteration[0] += 1
#         text.set_text(f"Iteration: {iteration[0]}")
#         return (*bar_rects, text)

#     generator = selection_sort(arr.copy())
#     anim = animation.FuncAnimation(fig, update, frames=generator, blit=True, repeat=False)
#     plt.show()

# if __name__ == "__main__":
#     arr = random.sample(range(1, 50), 10)
#     visualize_sort(arr)


# pip install matplotlib

# -------------------------------------------------------------------

# slot1 = [[5, 17], [20, 27], [45, 60], [82, 93]]
# slot2 = [[1, 12], [22, 30], [35, 47], [52, 81], [83, 88], [92, 100]]
# duration = 8

# def all_meetings(a, b, dur):
#     i = j = 0
#     results = []

#     while i < len(a) and j < len(b):
#         start = max(a[i][0], b[j][0])
#         end   = min(a[i][1], b[j][1])

#         if end - start >= dur:
#             results.append([start, start + dur])

#         if a[i][1] < b[j][1]:
#             i += 1
#         else:
#             j += 1

#     return results

# print(all_meetings(slot1, slot2, duration))

# -------------------------------------------------------------------

# def collect_water(heights):
#     n = len(heights)
#     if n == 0:
#         return 0

#     left, right = 0, n - 1
#     left_max = right_max = 0
#     water = 0

#     while left < right:
#         if heights[left] < heights[right]:
#             if heights[left] >= left_max:
#                 left_max = heights[left]
#             else:
#                 water += left_max - heights[left]
#             left += 1
#         else:
#             if heights[right] >= right_max:
#                 right_max = heights[right]
#             else:
#                 water += right_max - heights[right]
#             right -= 1

#     return water

# heights = [3, 0, 4, 7, 0, 6, 1, 5, 6]

# S = collect_water(heights)
# print("Ведро S =", S)



