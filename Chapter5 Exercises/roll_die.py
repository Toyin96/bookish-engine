# coding: utf-8
import ipython --matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

rolls = [random.randrange(1, 7) for i in range(60000)]
values, frequencies = np.unique(rolls, return_counts=True)
sns.set_style('whitegrid')
title = f'Rolling a six-sided die {len(rolls):,} times'
axes = sns.barplot(x=values, y=frequencies, palette='dark')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequencies) * 1.10)
    
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency}\n{frequency / len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
    
