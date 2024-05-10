import json
import matplotlib.pyplot as plt

# read txt and parse to list
with open('../../bags/node_edge_diff_15.txt', 'r') as f:
    for idx, line in enumerate(f, 1):
        data_dict = json.loads(line.strip())
        array = data_dict[list(data_dict.keys())[0]]
        exec(f"array{idx} = {array}")

# set font
from matplotlib.font_manager import FontProperties
font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')
font.set_size('16')

group_size_K = 10
x = range(0, len(array1) * group_size_K, group_size_K)

plt.plot(x, array1, label='25_edges', linewidth=1.5)
plt.plot(x, array2, label='50_edges', linewidth=1.5)
plt.plot(x, array3, label='75_edges', linewidth=1.5)
plt.plot(x, array4, label='100_edges', linewidth=1.5)

# plt.plot(x, array1, label='100_edges', linewidth=1.5)
# plt.plot(x, array2, label='200_edges', linewidth=1.5)
# plt.plot(x, array3, label='300_edges', linewidth=1.5)
# plt.plot(x, array4, label='400_edges', linewidth=1.5)

# plt.plot(x, array1, label='245_edges', linewidth=1.5)
# plt.plot(x, array2, label='490_edges', linewidth=1.5)
# plt.plot(x, array3, label='735_edges', linewidth=1.5)
# plt.plot(x, array4, label='980_edges', linewidth=1.5)

# plt.plot(x, array1, label='440_edges', linewidth=1.5)
# plt.plot(x, array2, label='880_edges', linewidth=1.5)
# plt.plot(x, array3, label='1320_edges', linewidth=1.5)
# plt.plot(x, array4, label='1760_edges', linewidth=1.5)

plt.legend(prop=font)
plt.xlabel('Iteration', fontproperties=font)
plt.ylabel('Absolute difference', fontproperties=font)
plt.title('Convergence (with 15 arguments) ', fontproperties=font)
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.show()